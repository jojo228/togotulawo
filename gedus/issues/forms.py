from django import forms
from gedus.main.models import *
from gedus.issues.models import *
from gedus.models import *


# option= Categorie.objects.all().values_list('name', 'name').order_by('name')

# choice_list = []

# for item in option:
#     choice_list.append(item)


class IssuesForm(forms.ModelForm):
    class Meta:
        model = Issues
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



