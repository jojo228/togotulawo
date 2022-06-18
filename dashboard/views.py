from django.shortcuts import redirect, render
from main.models.article import Article
from dashboard.forms import ProfilForm, ArticleForm
from main.models.paiement import Payment
from main.models.user_article import UserArticle

def home_page(request):

    return render(request, template_name = "index.html")


def sale(request):
    
    order = Payment.objects.filter(article__auteur = request.user.auteur, )
    art = Article.objects.filter(auteur = request.user.auteur)
    
    return render(request , 'ventes.html', locals())



def author_profil(request):

   user = request.user.auteur
   form = ProfilForm(instance=user)

   if request.method == 'POST':
        form = ProfilForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()

   context = {'form': form}

   return render(request, 'profil.html', context)



def article_read(request , slug):
    context = {}
    try:
        article_obj = Article.objects.filter(slug = slug).first()
        context['article_obj'] =  article_obj
    except Exception as e:
        print(e)
    return render(request , 'article_detail.html' , context)


def article_list(request):
    context = {}
    
    try:
        article = Article.objects.filter(auteur=request.user.auteur, is_draft=False)
        context['article'] =  article
    except Exception as e: 
        print(e)
    
    print(context)
    return render(request , 'publications.html' ,context)


def article_create(request):
    
    context = {'form' : ArticleForm}
    try:
        if request.method == 'POST':
            form = ArticleForm(request.POST, request.FILES)
            
            if form.is_valid():
                article = form.save(commit=False)
                article.auteur = request.user.auteur
                article.save()
            return redirect('/dashboard/liste-article/')
    
    except Exception as e :
        print(e)
    
    return render(request , 'publier.html' , context)


def article_draft(request):

    context = {}
    
    try:
        article = Article.objects.filter(auteur=request.user.auteur, is_draft=True)
        context['article'] =  article
    except Exception as e: 
        print(e)
    
    print(context)
    return render(request , 'brouillons.html', context)



def article_update(request , slug):
    context = {}
    try:
        
        article = Article.objects.get(slug = slug)
       
        if article.user != request.user:
            return redirect('/')
        
        initial_dict = {'contenu': article.contenu}
        form = ArticleForm(initial = initial_dict)
        if request.method == 'POST':
            form = ArticleForm(request.POST)
            print(request.FILES)
            image = request.FILES['image']
            title = request.POST.get('title')
            subtitle = request.POST.get('subtitle')
            domaine = request.POST.get('domaine')
            user = request.user
            
            if form.is_valid():
                contenu = form.cleaned_data['contenu']
            
            article_obj = Article.objects.create(
                user = user , title = title,
                subtitle = subtitle, domaine = domaine,
                contenu = contenu, image = image
            )
        
        
        context['article_obj'] = article_obj
        context['form'] = form
    except Exception as e :
        print(e)

    return render(request , 'article_update.html' , context)


def article_delete(request , id):
    try:
        article = Article.objects.get(id = id)
        
        if article.auteur == request.user.auteur:
            article.delete()
        
    except Exception as e :
        print(e)

    return redirect('/liste-article/')