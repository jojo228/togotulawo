from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render , redirect
from django.contrib.auth import logout, login, authenticate
from account.forms import RegistrationForm , LoginForm
from django.views import View
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.db.models.query_utils import Q
from django.contrib import messages 





from account.forms.profil_form import ClientForm


class SignupView(FormView):
    template_name="courses/signup.html" 
    form_class = RegistrationForm
    success_url  = '/login'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class AuteurSignupView(FormView):
    template_name="author_signup.html" 
    form_class = RegistrationForm
    success_url  = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ClientSignupView(FormView):
    template_name="client_signup.html" 
    form_class = RegistrationForm
    success_url  = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class EnseSignupView(FormView):
    template_name="ense_signup.html" 
    form_class = RegistrationForm
    success_url  = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    

def connexion(request):
    redirect_to = request.GET.get('next', '/')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username= form.cleaned_data.get('username')
            password= form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Send the user back to some page.
                return HttpResponseRedirect(redirect_to)
    return render(request=request, template_name='login.html')


def signout(request):
    logout(request)
    return redirect("main:accueil")


def signup_choice(request):

   return render(request, 'signup_choice.html')


def client_profil(request):

   user = request.user.client
   form = ClientForm(instance=user)

   if request.method == 'POST':
        form = ClientForm(request.POST, instance=user)
        if form.is_valid():
            form.save()

   context = {'form': form}

   return render(request, 'client_profil.html', context)


def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "account/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="main/password/password_reset.html", context={"password_reset_form":password_reset_form})