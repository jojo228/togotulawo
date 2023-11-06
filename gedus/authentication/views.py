from django.conf import settings
from django.urls import reverse
from django.views.generic import CreateView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from gedus.authentication.tokens import account_activation_token
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from django.contrib.auth import views as auth_views
from gedus.authentication.decorators import *
from .tokens import account_activation_token
from gedus.authentication.forms import (
    AuthorSignUpForm,
    LoginForm,
    ReviewerSignUpForm,
    ReaderSignUpForm,
    EditorSignUpForm,
)


class AuthorSignUpView(CreateView):
    model = User
    form_class = AuthorSignUpForm
    template_name = 'authentication/author_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'author'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('author-home')
    

class ReviewerSignUpView(CreateView):
    model = User
    form_class = ReviewerSignUpForm
    template_name = 'authentication/reviewer_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'reviewer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('reviewer-home')
    

class ReaderSignUpView(CreateView):
    model = User
    form_class = ReaderSignUpForm
    template_name = 'authentication/reader_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'reader'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('reader-home')


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'authentication/login-register.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def get_success_url(self):
        user = self.request.user
        if user.is_authenticated:
            if user.is_author:
                return reverse('author-home')
            elif user.is_reader:
                return reverse('reader-home')
            elif user.is_reviewer:
                return reverse('reviewer-home')
            elif user.is_editor:
                return reverse('editor-home')
        else:
            return reverse('login')




















@login_required(login_url="account:login")
def lecteur_profil(request):
    user = request.user
    lecteur = request.user.lecteur
    form = ReaderForm(instance=lecteur)
    user_form = ReaderUserForm(instance=user)

    if request.method == "POST":
        form = ReaderForm(request.POST, instance=lecteur)
        user_form = ReaderUserForm(request.POST, instance=user)
        if form.is_valid() and user_form.is_valid():
            form.save()
            user_form.save()

            messages.success(request, "Profil mis à jour avec succès")

    context = {"form": form, "form2": user_form}

    return render(request, "authentication/lecteur_profil.html", context)


######### EMAIL ACTIVATION AND PASSWORD RESET ##########


def activateEmail(request, user, to_email):
    mail_subject = "Activate your user account."
    message = render_to_string(
        "template_activate_account.html",
        {
            "user": user.username,
            "domain": get_current_site(request).domain,
            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
            "token": account_activation_token.make_token(user),
            "protocol": "https" if request.is_secure() else "http",
        },
    )
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(
            request,
            f"Cher {user}, Nous vous avons envoyé sur votre e-mail {to_email} des instructions pour activer votre compte. Si vous ne recevez pas de mail, veuillez vérifier vos spams.",
        )
    else:
        messages.error(
            request,
            f"Problème d envoi de l e-mail de confirmation à {to_email}, vérifiez si vous l avez saisi correctement.",
        )


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(
            request,
            "Merci pour votre confirmation. Vous pouvez maintenant vous connecter à votre compte.",
        )
        return redirect("account:connexion")
    else:
        messages.error(request, "Lien d Activation Invalide!")

    return redirect("main:accueil")


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data["email"]
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "password_reset_email.txt"
                    c = {
                        "email": user.email,
                        "domain": get_current_site(request).domain,
                        "site_name": "Togotulawo",
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        "token": account_activation_token.make_token(user),
                        "protocol": "https" if request.is_secure() else "http",
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(
                            subject,
                            email,
                            "togotulawo@gmail.com",
                            [user.email],
                            fail_silently=False,
                        )
                    except BadHeaderError:
                        return HttpResponse("Invalid header found.")
    password_reset_form = PasswordResetForm()
    return render(
        request=request,
        template_name="main/password/password_reset.html",
        context={"password_reset_form": password_reset_form},
    )


######### LOGIN AND LOGOUT ##########
def connexion(request):
    redirect_to = request.POST.get("next")
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
            if "next" in request.POST:
                return HttpResponseRedirect(redirect_to)
            else:
                return redirect(settings.LOGIN_REDIRECT_URL)
        else:
            messages.error(
                request, "Email/Nom d'utilisateur ou mot de passe incorrect !"
            )

    context = {"form": form}

    return render(
        request=request, template_name="authentication/login.html", context=context
    )


def signout(request):
    logout(request)
    return redirect("main:accueil")


######### SIGNUP VIEWS ##########


def signup_choice(request):
    return render(request, "authentication/signup_choice.html")


def lecteur_signup(request):
    user_form = CreateUserForm()

    if request.method == "POST":
        user_form = CreateUserForm(request.POST)
        lecteur_form = ReaderForm(request.POST)
        if user_form.is_valid() and lecteur_form.is_valid():
            user = user_form.save(commit=False)
            user.is_active = False
            lecteur = lecteur_form.save(commit=False)

            lecteur.user = user
            user.save()
            lecteur.save()
            activateEmail(request, user, user_form.cleaned_data.get("email"))
            username = user_form.cleaned_data.get("username")

    context = {"form": user_form}
    return render(request, "authentication/lecteur_signup.html", context)


def auteur_signup(request):
    user_form = CreateUserForm()

    if request.method == "POST":
        user_form = CreateUserForm(request.POST)
        auteur_form = AuteurForm(request.POST)
        if user_form.is_valid() and auteur_form.is_valid():
            user = user_form.save()
            auteur = auteur_form.save(commit=False)
            auteur.user = user
            auteur.save()
            login(request, user)
            username = user_form.cleaned_data.get("username")

            messages.success(request, "Compte crée avec succès pour " + username)

    context = {"form": user_form}
    return render(request, "authentication/author_signup.html", context)


def ense_signup(request):
    user_form = EntrepriseUserForm()

    if request.method == "POST":
        user_form = EntrepriseUserForm(request.POST)
        ense_form = EntrepriseForm(request.POST)
        if user_form.is_valid() and ense_form.is_valid():
            user = user_form.save()
            ense = ense_form.save(commit=False)
            ense.user = user
            ense.save()
            login(request, user)
            username = user_form.cleaned_data.get("username")

            messages.success(request, "Compte crée avec succès pour " + username)

    context = {"form": user_form}
    return render(request, "authentication/ense_signup.html", context)
