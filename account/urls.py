from django.urls import path
from account.signup_views import auteur_signup, client_signup, signup_choice, ense_signup, activate
from account.views import client_profil, password_reset_request, signout
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .form import AuthenticationFormWithEmail
from django.urls import reverse_lazy




app_name="account"

urlpatterns = [

    #Authentication urls
    #path('login', connexion , name = 'connexion'),
    # login
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="login.html",
            authentication_form=AuthenticationFormWithEmail,
            next_page=reverse_lazy("main:accueil"),
        ),
        name="connexion"),
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
