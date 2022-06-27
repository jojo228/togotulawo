
from django.contrib import admin
from django.urls import include, path
from django.shortcuts import HttpResponse
from account.views import AuteurSignupView, ClientSignupView, EnseSignupView, SignupView, client_profil, connexion, password_reset_request, signout, signup_choice
from django.conf import settings
from django.conf.urls.static import static

app_name="account"

urlpatterns = [

    #Authentication urls
    path('login', connexion , name = 'connexion'),
    path('signup', SignupView.as_view() , name = 'signup'),
    path('logout', signout , name = 'logout'),

    path('password_reset', password_reset_request, name='password_reset'),

    path('signup_choice', signup_choice , name = 'signup_choice'),
    path('client_signup', ClientSignupView.as_view() , name = 'client_signup'),
    path('auteur_signup', AuteurSignupView.as_view(), name='auteur_signup'),
    path('ense_signup', EnseSignupView.as_view(), name='ense_signup'),



    path('profil', client_profil, name='profil'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
