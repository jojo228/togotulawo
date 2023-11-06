from django.contrib import admin
from django.urls import path
from gedus.main.views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'gedus'

urlpatterns = [
    path('', home, name='home'),
    path('coming-soon', coming_soon, name='coming_soon'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)






# urlpatterns = [
#     #HomePage urls

#     path('faq/', faq, name='faq'),
#     path('terms_conditions/', term_condition, name='terms_conditions'),
#     path('police_privee/', police_privee, name='police_privee'),

#     path('mail_letter/', mail_letter, name='mail-letter'),
#     path('fav/<str:slug>/', favourite_add, name='favourite_add'),

#     #Articles urls
#     path('article/<str:slug>', article_page, name='article'),
#     path('checkout/<str:slug>', checkout , name = 'checkout'),
#     path('verify_payment', verify_payment , name = 'verify_payment'),
#     path('recherche/', recherche , name = 'recherche'),
#     path('categorie/<str:slug>', categorie_articles, name = 'categorie'),
#     path('issues/<str:slug>', issues, name = 'issues'),
#     path('submit_review/<int:id>', comment, name='submit_review'),


#     path('offers/', OfferList.as_view(), name='offers'),
#     path('offer_detail/<str:slug>', offer_detail, name='offer_detail'),
#     path('offer_create/<int:id>', offer_create, name="offer_create"),

#     path('success-message/', success_message , name = 'success_message'),

#     path('bibliotheque/', Bibliotheque.as_view(), name='bibliotheque'),

# ]
