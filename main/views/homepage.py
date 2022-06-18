from urllib import request
from django.shortcuts import redirect, render
from entreprise.models import Problematique
from main.models.article import Article, Categorie
from django.views.generic import ListView
from django.utils import timezone

def home_page(request):
    article = Article.objects.filter(active=True, is_draft=False,)

    category = Categorie.objects.all()

    problematique = Problematique.objects.filter(is_draft=False, active=True)

    context = {'article':article, 'category':category, 'prob':problematique}

    return render(request, template_name = "main_base.html", context=context)





