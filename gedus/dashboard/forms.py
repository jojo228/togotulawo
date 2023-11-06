from cProfile import label
from logging import PlaceHolder
from django import forms
from gedus.models import Author
from gedus.main.models import *


# option = (
#         ('Agronomie', 'Agronomie'), ('Biologie', 'Biologie'), ('Business', 'Business'), ('Chimie', 'Chimie'), ('Comptabilité', 'Comptabilité'), ('Droit', 'Droit'), ('Economie', 'Economie'),
#         ('Finance', 'Finance'), ('GRH', 'GRH'), ('Geographie', 'Geographie'), ('Histoire', 'Histoire'), ('Informatique', 'Informatique'), ('Langues', 'Langues'),
#         ('Médecine', 'Médecine'), ('Maths', 'Maths'), ('Physique', 'Physique'), ('Statistique', 'Statistique'), 
#     )



class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'contenu', 'domaine', 'type', 'couverture',
         'resource', 'price', 'discount', 'video_link', 'is_draft', 'active']


        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'discount': forms.TextInput(attrs={'class': 'form-control'}),   
            'video_link': forms.TextInput(attrs={'class': 'form-control'}),   
            'domaine': forms.Select(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
        }

        labels = {
            "title": "Titre",
            "price": "Prix",
            "discount": "Remise(%)",
            "type": "Type",
            "contenu": "Resumé ou sommaire",
            "resource": "Ressource (le fichier PDF de votre publication)",
            "is_draft": "Enregistré comme brouillon",
            "active": "Rendre visible sur le site",
            "couverture": "Photo de couverture",
            "domaine": "Domaine",
            'video_link': "Lien de la video(optionel)"

        }



class ProfilForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['affiliation', 'phone_number', 'image',]

        widgets = {
            'affiliation': forms.TextInput(attrs={'class': 'form-control'}),  
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),  
        }

        labels = {
            
            "phone_number": "Téléphone(Numéro Flooz ou Tmoney. Vous recevrez tous les montants de vos ventes sur ce numéro)",
            "pays_affiliation": "Pays d'affiliation",
            "affiliation": "Affiliation",
            "image": "Photo de profil",
            
        }


        



        
    