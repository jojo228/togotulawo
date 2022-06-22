
from django.contrib import admin
from django.urls import include, path
from django.shortcuts import HttpResponse
from account.views import LoginView, SignupView, client_profil, signout
from django.conf import settings
from django.conf.urls.static import static

app_name="account"

urlpatterns = [

    #Authentication urls
    path('login', LoginView.as_view() , name = 'login'),
    path('signup', SignupView.as_view() , name = 'signup'),
    path('logout', signout , name = 'logout'),

    path('profil', client_profil, name='profil'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
