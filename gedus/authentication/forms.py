from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import authenticate , login
from django.forms import ValidationError
from gedus.authentication.models import Auteur, Client, Entreprise



class LoginForm(AuthenticationForm):

    username = forms.EmailField(max_length=25 , required = True , label='Email')
    def clean(self):
        email = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = None
        try:
            user = User.objects.get(email = email)
            result = authenticate(username = user.username , password = password)


            if(result is not None):
                return result
            else:
                raise ValidationError("Email ou mot de passe invalide")
        except:
            raise ValidationError("Email ou mot de passe invalide")
        
    

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ["telephone"]

        widgets = {
            "telephone": forms.NumberInput(attrs={"class": "form-control"}),
        }

        labels = {
            "telephone": "Téléphone",
        }


class ClientUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]

        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
        }

        labels = {
            "first_name": "Nom",
            "last_name": "Prénoms",
            "email": "Email",
        }



class CreateUserForm(UserCreationForm):
    email = forms.EmailField(max_length=25 , required = True)

    class Meta:
        model = User
        fields = ['first_name'
         , 'last_name' , 'username'
          , "email" , 'password1'  , 'password2' ]
        
    def save(self, commit=True):
        user  = super(CreateUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
            
        if commit:
            user.save()
        return user



class EntrepriseUserForm(UserCreationForm):
    email = forms.EmailField(max_length=25 , required = True)

    class Meta:
        model = User
        fields = ['username'
          , "email" , 'password1'  , 'password2' ]
        
    def save(self, commit=True):
        user = super(EntrepriseUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
            
        if commit:
            user.save()
        return user

    

class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        exclude = ("user",)


class AuteurForm(forms.ModelForm):

    class Meta:
        model = Auteur
        exclude = ("user",)


class EntrepriseForm(forms.ModelForm):

    class Meta:
        model = Entreprise
        exclude = ("user",)