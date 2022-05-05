from django.shortcuts import redirect, render
from main.models.article import Article, Categorie
from dashboard.forms import *

def HomePage(request):

    return render(request, template_name = "index.html")


def Profil(request):

   user = request.user.auteur
   form = ProfilForm(instance=user)

   if request.method == 'POST':
        form = ProfilForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()

   context = {'form': form}

   return render(request, 'profil.html', context)



def article_detail(request , slug):
    context = {}
    try:
        article_obj = Article.objects.filter(slug = slug).first()
        context['article_obj'] =  article_obj
    except Exception as e:
        print(e)
    return render(request , 'article_detail.html' , context)


def see_article(request):
    context = {}
    
    try:
        article = Article.objects.filter(auteur=request.user.auteur, is_draft=False)
        context['article'] =  article
    except Exception as e: 
        print(e)
    
    print(context)
    return render(request , 'publications.html' ,context)


def publier(request):
    
    context = {'form' : ArticleForm}
    try:
        if request.method == 'POST':
            form = ArticleForm(request.POST)
            print(request.FILES)
            couverture = request.FILES['couverture']
            ressource = request.FILES['resource']
            title = request.POST.get('title')
            price = request.POST.get('price')
            discount = request.POST.get('discount')
            publish_date = request.POST.get('publish_date')
            type = request.POST.get('type')
            domaine = request.POST.get('domaine')
            active = request.POST.get('active')
            draft = request.POST.get('is_draft')
            user = request.user
            
            if form.is_valid():
                contenu = form.cleaned_data['contenu']
            
            article = Article.objects.create(
                user = user , title = title, domaine = domaine,
                ressource = ressource, publish_date = publish_date,
                contenu = contenu, couverture = couverture, price = price,
                discount = discount, type = type, active = active, draft =draft
            )
            print(article)
            return redirect('/see-article/')
    
    except Exception as e :
        print(e)
    
    return render(request , 'publier.html' , context)


def Brouillon(request):

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