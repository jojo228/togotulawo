from cProfile import label
from logging import PlaceHolder
from django import forms
from froala_editor.widgets import FroalaEditor
from account.models import Auteur
from main.models.article import Article, Categorie


# option = (
#         ('Agronomie', 'Agronomie'), ('Biologie', 'Biologie'), ('Business', 'Business'), ('Chimie', 'Chimie'), ('Comptabilité', 'Comptabilité'), ('Droit', 'Droit'), ('Economie', 'Economie'),
#         ('Finance', 'Finance'), ('GRH', 'GRH'), ('Geographie', 'Geographie'), ('Histoire', 'Histoire'), ('Informatique', 'Informatique'), ('Langues', 'Langues'),
#         ('Médecine', 'Médecine'), ('Maths', 'Maths'), ('Physique', 'Physique'), ('Statistique', 'Statistique'), 
#     )

option= Categorie.objects.all().values_list('name', 'name')

choice_list = []

for item in option:
    choice_list.append(item)


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
            'video_link': "Lien de la video"

        }



class ProfilForm(forms.ModelForm):
    class Meta:
        model = Auteur
        fields = ['affiliation', 'pays_affiliation', 'faculte', 'niveau_etude', 'grade', 'annee_graduation', 'tel',
         'website', 'image', 'bio']

        widgets = {
            'pays_affiliation': forms.TextInput(attrs={'class': 'form-control'}),
            'affiliation': forms.TextInput(attrs={'class': 'form-control'}),
            'website': forms.TextInput(attrs={'class': 'form-control'}),
            'niveau_etude': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'grade': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'faculte': forms.TextInput(attrs={'class': 'form-control'}),   
            'annee_graduation': forms.TextInput(attrs={'class': 'form-control'}),  
            'tel': forms.TextInput(attrs={'class': 'form-control'}),  
            'bio': forms.Textarea(attrs={'class': 'form-control'}),  
        }

        labels = {
            "website": "Lien (Linkedin/Twitter/Facebook/Instagram)",
            "niveau_etude": "Niveau d'étude",
            "faculte": "Domaine",
            "annee_graduation": "Année de graduation",
            "tel": "Téléphone",
            "pays_affiliation": "Pays d'affiliation",
            "affiliation": "Affiliation",
            "grade": "Grade",
            "bio": "Biographie",
            "image": "Photo de profil",
            
        }


        



        
    