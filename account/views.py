from django.shortcuts import render , redirect
from django.contrib.auth import logout , login
from account.forms import RegistrationForm , LoginForm
from django.views import View
from django.views.generic.edit import FormView

from account.forms.profil_form import ClientForm


class SignupView(FormView):
    template_name="courses/signup.html" 
    form_class = RegistrationForm
    success_url  = '/login'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    

class LoginView(FormView):
    template_name="courses/login.html" 
    form_class = LoginForm
    success_url  = '/'

    def form_valid(self, form):
        login(self.request , form.cleaned_data)
        next_page = self.request.GET.get('next')
        if next_page is not None:
            return redirect(next_page)
        return super().form_valid(form)


def signout(request ):
    logout(request)
    return redirect("home")



def client_profil(request):

   user = request.user.client
   form = ClientForm(instance=user)

   if request.method == 'POST':
        form = ClientForm(request.POST, instance=user)
        if form.is_valid():
            form.save()

   context = {'form': form}

   return render(request, 'client_profil.html', context)


