from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import transaction
from gedus.models import User, Reader, Editor, Author, Reviewer
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class AuthorSignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    first_name = forms.CharField(widget=forms.TextInput())
    last_name = forms.CharField(widget=forms.TextInput())
    affiliation = forms.CharField(widget=forms.TextInput())
    phone_number = forms.CharField(widget=forms.TextInput())
    orcid_id = forms.CharField(widget=forms.TextInput())

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_author = True
        if commit:
            user.save()
        author = Author.objects.create(user=user, first_name=self.cleaned_data.get('first_name'), 
                                       last_name=self.cleaned_data.get('last_name'), 
                                       affiliation=self.cleaned_data.get('affiliation'), 
                                       phone_number=self.cleaned_data.get('phone_number'), 
                                       orcid_id=self.cleaned_data.get('orcid_id'))
        return user
    


class ReviewerSignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    first_name = forms.CharField(widget=forms.TextInput())
    last_name = forms.CharField(widget=forms.TextInput())
    phone_number = forms.CharField(widget=forms.TextInput())

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_reviewer = True
        if commit:
            user.save()
        reviewer = Reviewer.objects.create(user=user, first_name=self.cleaned_data.get('first_name'), last_name=self.cleaned_data.get('last_name'), phone_number=self.cleaned_data.get('phone_number'))
        return user
    


class ReaderSignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    first_name = forms.CharField(widget=forms.TextInput())
    last_name = forms.CharField(widget=forms.TextInput())
    phone_number = forms.CharField(widget=forms.TextInput())

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_reader = True
        if commit:
            user.save()
        reader = Reader.objects.create(user=user, first_name=self.cleaned_data.get('first_name'), last_name=self.cleaned_data.get('last_name'), phone_number=self.cleaned_data.get('phone_number'))
        return user
    


class EditorSignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    first_name = forms.CharField(widget=forms.TextInput())
    last_name = forms.CharField(widget=forms.TextInput())
    phone_number = forms.CharField(widget=forms.TextInput())

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_editor = True
        if commit:
            user.save()
        editor = Editor.objects.create(user=user, first_name=self.cleaned_data.get('first_name'), last_name=self.cleaned_data.get('last_name'), phone_number=self.cleaned_data.get('phone_number'))
        return user
    


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())