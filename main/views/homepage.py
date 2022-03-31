from urllib import request
from django.shortcuts import redirect, render
from main.models.article import Article
from django.views.generic import ListView

def HomePage(request):
    article = Article.objects.filter(active=True, is_draft=False)

    context = {'article':article}

    return render(request, template_name = "main_base.html", context=context)


