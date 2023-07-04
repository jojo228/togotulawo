from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render , redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User, Group
from django.template import RequestContext
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.db.models.query_utils import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from account.forms.login_form import LoginForm
from account.forms.profil_form import ClientForm, ClientUserForm

from rest_framework import viewsets
from rest_framework import permissions
from account.serializers import UserSerializer, GroupSerializer
from .tokens import account_activation_token
from django.contrib.sites.shortcuts import get_current_site






def signout(request):
    logout(request)
    return redirect("main:accueil")


@login_required(login_url='account.togotulawo.com/login')
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
					email_template_name = 'password_reset_email.txt'
					c = {
					"email":user.email,
					'domain':get_current_site(request).domain,
					'site_name': 'Togotulawo',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': account_activation_token.make_token(user),
					'protocol': 'https' if request.is_secure() else 'http'
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'togotulawo@gmail.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name='main/password/password_reset.html', context={"password_reset_form":password_reset_form})


def connexion(request):
	redirect_to = request.POST.get('next')
	form = AuthenticationForm()
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
		else:
			""" for key, error in list(form.errors.items()):

				if key == 'captcha' and error[0] == 'This field is required.':
					messages.error(request, "Desolé, vous devez absolument passer le test de Recaptcha")
					continue """
					
			messages.error(request, "Email/Nom d'utilisateur ou mot de passe incorrect !")

	context = {'form': form}


	return render(request=request, template_name='login.html', context=context)




#SERIALIZERS VIEWS

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
