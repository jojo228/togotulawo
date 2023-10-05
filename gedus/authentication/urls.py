from django.urls import path
from account.signup_views import auteur_signup, client_signup, signup_choice, ense_signup, activate
from account.views import client_profil, connexion, password_reset_request, signout
from django.conf import settings
from django.conf.urls.static import static

app_name="gedus"

urlpatterns = [

    #Authentication urls
    path('login', connexion , name = 'connexion'),
    path('logout', signout , name = 'logout'),

    path('password_reset', password_reset_request, name='password_reset'),

    path('signup_choice', signup_choice , name = 'signup_choice'),
    path('client_signup', client_signup , name = 'client_signup'),
    path('auteur_signup', auteur_signup, name='auteur_signup'),
    path('ense_signup', ense_signup, name='ense_signup'),



    path('profil', client_profil, name='profil'),

    path('activate/<uidb64>/<token>', activate, name='activate'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
