from django import forms
from account.models import Entreprise
from entreprise.models import Postuler, Problematique
from main.models.article import Categorie



option= Categorie.objects.all().values_list('name', 'name')

choice_list = []

for item in option:
    choice_list.append(item)


class ProblematiqueForm(forms.ModelForm):
    class Meta:
        model = Problematique
        fields = ['domaine', 'description', 'profil_rechercher', 'duree_recherche', 'is_draft', 'active']


        widgets = {
            'domaine': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'duree_recherche': forms.NumberInput(attrs={'class': 'form-control'}),
            
        }

        labels = {
            "domaine": "Domaine",
            "description": "Description de votre problème",
            "profil_rechercher": "Decrivez le profil recherché",
            "duree_recherche": "Durée estimé de la recherche(en mois)",
            "is_draft": "Enregistré comme brouillon",
            "active": "Rendre visible sur le site",
        }



class PostuleForm(forms.ModelForm):
    class Meta:
        model = Postuler
        fields = ['nom_du_candidat', 'prenom_du_candidat', 'contact_du_candidat', 'email_du_candidat', 'motivation_du_candidat',]


        widgets = {
            'nom_du_candidat': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom_du_candidat': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_du_candidat': forms.NumberInput(attrs={'class': 'form-control'}),
            'email_du_candidat': forms.EmailInput(attrs={'class': 'form-control'}),
            
        }

        labels = {
            "motivation_du_candidat": "Motivation",
            "nom_du_candidat": "Nom",
            "prenom_du_candidat": "Prénoms",
            "contact_du_candidat": "Contact",
            "email_du_candidat": "Email",
            
        }



class EntrepriseForm(forms.ModelForm):
    class Meta:
        model = Entreprise
        fields = ['raison_social', 'objet_social', 'adresse',
         'telephone', 'image']

        widgets = {
            'raison_social': forms.TextInput(attrs={'class': 'form-control'}),
            'objet_social': forms.TextInput(attrs={'class': 'form-control'}),
            'adresse': forms.TextInput(attrs={'class': 'form-control'}),
            'telephone': forms.NumberInput(attrs={'class': 'form-control'}),  
        }

        labels = {
            "raison_social": "Raison Sociale",
            "objet_social": "Objet Social",
            "adresse": "Adresse",
            "telephone": "Téléphone",
            "image": "Photo de profil",
            
        }