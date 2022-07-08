from django.shortcuts import render
from django.contrib import messages
from account.forms.registration_form import AuteurForm, ClientForm, CreateUserForm, EntrepriseForm, EntrepriseUserForm
from django.contrib.auth import login


def signup_choice(request):

   return render(request, 'signup_choice.html')


def client_signup(request):
    user_form = CreateUserForm()

    if request.method == 'POST':
        user_form = CreateUserForm(request.POST)
        client_form = ClientForm(request.POST)
        if user_form.is_valid() and client_form.is_valid():
            user = user_form.save()
            client = client_form.save(commit=False)
            client.user = user
            client.save()
            login(request, user)
            username = user_form.cleaned_data.get('username')

            messages.success(request, 'Compte crée avec succès pour ' + username)

    context = {'form':user_form}
    return render(request, 'client_signup.html', context)



def auteur_signup(request):
    user_form = CreateUserForm()

    if request.method == 'POST':
        user_form = CreateUserForm(request.POST)
        auteur_form = AuteurForm(request.POST)
        if user_form.is_valid() and auteur_form.is_valid():
            user = user_form.save()
            auteur = auteur_form.save(commit=False)
            auteur.user = user
            auteur.save()
            login(request, user)
            username = user_form.cleaned_data.get('username')

            messages.success(request, 'Compte crée avec succès pour ' + username)

    context = {'form':user_form}
    return render(request, 'author_signup.html', context)



def ense_signup(request):
    user_form = EntrepriseUserForm()

    if request.method == 'POST':
        user_form = EntrepriseUserForm(request.POST)
        ense_form = EntrepriseForm(request.POST)
        if user_form.is_valid() and ense_form.is_valid():
            user = user_form.save()
            ense = ense_form.save(commit=False)
            ense.user = user
            ense.save()
            login(request, user)
            username = user_form.cleaned_data.get('username')

            messages.success(request, 'Compte crée avec succès pour ' + username)

    context = {'form':user_form}
    return render(request, 'ense_signup.html', context)
