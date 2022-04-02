
from django.contrib import admin
from django.urls import include, path
from django.shortcuts import HttpResponse
from main.views.articles import articlePage, MyArticleList, comment
from main.views.ckeckout import checkout, verifyPayment
from main.views.homepage import HomePage
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    #HomePage urls
    path('', HomePage, name='accueil'),

    #Articles urls
    path('article/<str:slug>', articlePage, name='article'),
    path('checkout/<str:slug>', checkout , name = 'checkout'),
    path('verify_payment', verifyPayment , name = 'verify_payment'),
    path('my-courses', MyArticleList.as_view() , name = 'my-courses'),
    path('submit_review/<int:id>', comment, name='submit_review'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
