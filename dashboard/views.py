from django.shortcuts import redirect, render
from main.models.article import Article
from dashboard.forms import ProfilForm, ArticleForm
from main.models.paiement import Payment
from main.models.user_article import UserArticle
from django.contrib.auth.decorators import login_required



@login_required(login_url='/account/login')
def home_page(request):

    return render(request, template_name = "index.html")



@login_required(login_url='/account/login')
def sale(request):
    
    order = Payment.objects.filter(article__auteur = request.user.auteur, )
    art = Article.objects.filter(auteur = request.user.auteur)
    
    return render(request , 'ventes.html', locals())


@login_required(login_url='/account/login')
def author_profil(request):

   user = request.user.auteur
   form = ProfilForm(instance=user)

   if request.method == 'POST':
        form = ProfilForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()

   context = {'form': form}

   return render(request, 'profil.html', context)


@login_required(login_url='/account/login')
def article_read(request , slug):
    context = {}
    try:
        article_obj = Article.objects.filter(slug = slug).first()
        context['article_obj'] =  article_obj
    except Exception as e:
        print(e)
    return render(request , 'article_detail.html' , context)



@login_required(login_url='/account/login')
def article_list(request):
    context = {}
    
    try:
        article = Article.objects.filter(auteur=request.user.auteur, is_draft=False)
        context['article'] =  article
    except Exception as e: 
        print(e)
    
    print(context)
    return render(request , 'publications.html' ,context)


@login_required(login_url='/account/login')
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


@login_required(login_url='/account/login')
def article_draft(request):

    context = {}
    
    try:
        article = Article.objects.filter(auteur=request.user.auteur, is_draft=True)
        context['article'] =  article
    except Exception as e: 
        print(e)
    
    print(context)
    return render(request , 'brouillons.html', context)


@login_required(login_url='/account/login')
def article_update(request , slug):
    context = {}
    try:
        
        article = Article.objects.get(slug = slug)
       
        if article.auteur != request.user.auteur:
            return redirect('/')
        
        form = ArticleForm(instance=article)
        if request.method == 'POST':
            form = ArticleForm(request.POST, request.FILES, instance=article)
           
            if form.is_valid():
                form.save()
        
        context['article'] = article
        context['form'] = form
    except Exception as e :
        print(e)

    return render(request , 'article_update.html' , context)


@login_required(login_url='/account/login')
def article_delete(request , id):
    try:
        article = Article.objects.get(id = id)
        
        if article.auteur == request.user.auteur:
            article.delete()
        
    except Exception as e :
        print(e)

    return redirect('/liste-article/')