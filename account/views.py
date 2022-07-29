from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render , redirect
from django.contrib.auth import logout, login, authenticate
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
from django.contrib.auth.decorators import login_required

from account.forms.profil_form import ClientForm, ClientUserForm



def signout(request):
    logout(request)
    return redirect("main:accueil")


@login_required(login_url='/account/login')
def client_profil(request):

   user = request.user
   client = request.user.client
   form = ClientForm(instance=client)
   user_form = ClientUserForm(instance=user)

   if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        user_form = ClientUserForm(request.POST, instance=user)
        if form.is_valid() and user_form.is_valid():
            form.save()
            user_form.save()
            
            messages.success(request, 'Profil mis à jour avec succès')


   context = {'form': form, "form2":user_form}

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


def connexion(request):
	redirect_to = request.POST.get('next')
	if request.method == 'POST':
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
			if 'next' in request.POST:
					return HttpResponseRedirect(redirect_to)
			else:
				return redirect(settings.LOGIN_REDIRECT_URL)
	return render(request=request, template_name='login.html')
