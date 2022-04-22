from django.shortcuts import redirect, render
from main.models.article import Article, Categorie

def HomePage(request):

    return render(request, template_name = "index.html")
