
from django.contrib import admin
from django.urls import include, path
from django.shortcuts import HttpResponse
from main.views.articles import Bibliotheque, categorie_articles, article_page, comment, recherche
from main.views.ckeckout import checkout, verify_payment
from main.views.homepage import home_page
from main.views.demo_and_faq import faq
from django.conf import settings
from django.conf.urls.static import static
from main.views.newsletter import mail_letter

from main.views.offers import OfferList, offer_detail, offer_create, success_message

app_name = 'main'

urlpatterns = [
    #HomePage urls
    path('', home_page, name='accueil'),
    path('faq/', faq, name='faq'),
    path('mail_letter/', mail_letter, name='mail-letter'),

    #Articles urls
    path('article/<str:slug>', article_page, name='article'),
    path('checkout/<str:slug>', checkout , name = 'checkout'),
    path('verify_payment', verify_payment , name = 'verify_payment'),
    path('recherche/', recherche , name = 'recherche'),
    path('categorie/<str:slug>', categorie_articles, name = 'categorie'),
    path('submit_review/<int:id>', comment, name='submit_review'),


    path('offers/', OfferList.as_view(), name='offers'),
    path('offer_detail/<str:slug>', offer_detail, name='offer_detail'),
    path('offer_create/<int:id>', offer_create, name="offer_create"),

    path('success-message/', success_message , name = 'success_message'),

    path('bibliotheque/', Bibliotheque.as_view(), name='bibliotheque'),
    
    





]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
