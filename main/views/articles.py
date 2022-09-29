from django.http import HttpResponse
from django.shortcuts import render, redirect
from entreprise.models import Problematique
from main.models.article import Article, Comment, Categorie
from main.forms.comment import CommentForm
from main.models.user_article import UserArticle
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin




# @method_decorator(login_required(login_url='login') , name='dispatch')
class ArticleList(ListView):
    model = Article
    template_name = 'article_list.html'
    paginate_by = 12

    def get_queryset(self):
        filter_val=self.request.GET.get("filter","")
        order_by=self.request.GET.get("orderby","id")
        article = Article.objects.all()
        if filter_val:
            article = article.filter(Q(title__icontains=filter_val) | Q(contenu__icontains=filter_val) | Q(price__icontains=filter_val)).order_by(order_by)

        return article

    def get_context_data(self,**kwargs):
        context=super(ArticleList,self).get_context_data(**kwargs)
        context["filter"]=self.request.GET.get("filter","")
        context["orderby"]=self.request.GET.get("orderby","id")
        context["all_table_fields"]=Article._meta.get_fields()
        return context



def article_page(request, slug):

    article = Article.objects.get(slug=slug)

    comment = article.comment_set.all().count()
    
    
    context = {
        "article" : article , 
        """ "video" : video , 
        'videos':videos, """
        'comment':comment,
    }
 
    return render(request, template_name="pageArticle.html", context=context)


@login_required(login_url='/account/login')
def comment(request, id):
    url = request.META.get('HTTP_REFERER')
    
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            data = Comment()
            data.text = form.cleaned_data['text']
            data.rate = form.cleaned_data['rate']
            data.article_id = id
            data.user = request.user
            data.save()
            messages.success(request, 'Merci! Commentaire ajouté.')
            return redirect(url)
    


def categorie_articles(request, slug):

    categorie = Categorie.objects.get(slug=slug)
    article = Article.objects.filter(domaine=categorie)

    context = {
        "article" : article, 
        "categorie" : categorie, 
    }

    return render(request, template_name="categorie_article.html", context=context)



def problematique(request, slug):

    categorie = Categorie.objects.get(slug=slug)
    problematique = Problematique.objects.filter(domaine=categorie)

    context = {
        "probs" : problematique, 
        "categorie" : categorie, 
    }

    return render(request, template_name="prob_categorie.html", context=context)



def recherche(request,):

    query = request.GET.get("filter")
    order_by= request.GET.get("orderby","id")
    article = Article.objects.filter(Q(title__icontains=query) | Q(contenu__icontains=query) | Q(price__icontains=query) 
    | Q(auteur__user__first_name__icontains=query) | Q(auteur__user__last_name__icontains=query)).order_by(order_by)

    context = {
        "article" : article, 
    }

    return render(request, template_name="search.html", context=context)


class Bibliotheque(LoginRequiredMixin, ListView):
    model = UserArticle
    template_name = 'bibliotheque.html'
    paginate_by = 12

    def get_queryset(self):
        user = self.request.user
        filter_val=self.request.GET.get("filter","")
        order_by=self.request.GET.get("orderby","id")
        article = UserArticle.objects.filter(user=user).all()
        if filter_val:
            article = article.filter(Q(title__icontains=filter_val) | Q(contenu__icontains=filter_val) | Q(price__icontains=filter_val)).order_by(order_by)

        return article 

    def get_context_data(self,**kwargs):
        context=super(Bibliotheque,self).get_context_data(**kwargs)
        context["filter"]=self.request.GET.get("filter","")
        context["orderby"]=self.request.GET.get("orderby","id")
        context["all_table_fields"]=UserArticle._meta.get_fields()
        return context