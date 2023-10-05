from django import forms
from account.models import Entreprise
from entreprise.models import Livre, Problematique
from main.models.article import Categorie


# option= Categorie.objects.all().values_list('name', 'name').order_by('name')

# choice_list = []

# for item in option:
#     choice_list.append(item)


class ProblematiqueForm(forms.ModelForm):
    class Meta:
        model = Problematique
        fields = ['titre', 'domaine', 'description', 'profil_rechercher', 'duree_recherche', 'is_draft', 'active']


        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control'}),
            # 'domaine': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'duree_recherche': forms.NumberInput(attrs={'class': 'form-control'}),
            
        }

        labels = {
            "titre": "Titre",
            "domaine": "Domaine",
            "description": "Description de votre problème",
            "profil_rechercher": "Decrivez le profil recherché",
            "duree_recherche": "Durée prévisionnelle de la recherche(en mois)",
            "is_draft": "Enregistré comme brouillon",
            "active": "Rendre visible sur le site",
        }



class LivreForm(forms.ModelForm):
    class Meta:
        model = Livre
        fields = ['titre', 'description', 'document']

        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            
        }

        labels = {
            "titre": "Titre",
            "description": "Description du document(optionel)",
            "document": "Ajouter le fichier",
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