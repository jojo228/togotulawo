from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from gedus.authentication.views import (
    signup_choice,
    activate,
    AuthorSignUpView,
    ReaderSignUpView,
    ReviewerSignUpView
)
from gedus.authentication.views import lecteur_profil, password_reset_request
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Authentication urls
    path("login/", views.LoginView.as_view(), name="login"),
    path("signup/author/", views.AuthorSignUpView.as_view(), name="author-signup"),
    path("signup/reader/", views.ReaderSignUpView.as_view(), name="reader-signup"),
    path("signup/reviewer/", views.ReviewerSignUpView.as_view(), name="reviewer-signup"),
    path('logout/', auth_views.LogoutView.as_view(template_name="authentication/logout.html"), name="logout"),
    path("password_reset", password_reset_request, name="password_reset"),
    path("signup_choice", signup_choice, name="signup_choice"),
    path("profil", lecteur_profil, name="profil"),
    path("activate/<uidb64>/<token>", activate, name="activate"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
