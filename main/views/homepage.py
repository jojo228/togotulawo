from urllib import request
from django.shortcuts import redirect, render
from main.models.article import Article, Categorie
from django.views.generic import ListView
from django.utils import timezone

def HomePage(request):
    article = Article.objects.filter(active=True, is_draft=False,)

    category = Categorie.objects.all()


    context = {'article':article, 'category':category}

    return render(request, template_name = "main_base.html", context=context)
