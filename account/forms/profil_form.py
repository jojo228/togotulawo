from django import forms
from account.models import Client



class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['user',
         'telephone']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telephone': forms.NumberInput(attrs={'class': 'form-control'}),  
        }

        labels = {
            "first_name": "Nom",
            "last_name": "Prénoms",
            "email": "Email",
            "telephone": "Téléphone",
            
        }