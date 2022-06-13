
from django.contrib import admin
from django.urls import include, path
from django.shortcuts import HttpResponse
from main.views.articles import categorie_articles, article_page, comment, recherche
from main.views.ckeckout import checkout, verifyPayment
from main.views.homepage import home_page
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    #HomePage urls
    path('', home_page, name='accueil'),

    #Articles urls
    path('article/<str:slug>', article_page, name='article'),
    path('checkout/<str:slug>', checkout , name = 'checkout'),
    path('verify_payment', verifyPayment , name = 'verify_payment'),
    path('recherche/', recherche , name = 'recherche'),
    path('categorie/<str:slug>', categorie_articles, name = 'categorie'),
    path('submit_review/<int:id>', comment, name='submit_review'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
