from cProfile import label
from logging import PlaceHolder
from django import forms
from account.models import Auteur
from main.models.article import Article, Categorie


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
        model = Auteur
        fields = ['affiliation', 'pays_affiliation', 'faculte', 'niveau_etude', 'grade', 'annee_graduation', 'tel',
         'twitter_link','linkedin_link','fbook_link','insta_link', 'image', 'bio']

        widgets = {
            'pays_affiliation': forms.TextInput(attrs={'class': 'form-control'}),
            'affiliation': forms.TextInput(attrs={'class': 'form-control'}),
            'twitter_link': forms.TextInput(attrs={'class': 'form-control'}),
            'linkedin_link': forms.TextInput(attrs={'class': 'form-control'}),
            'fbook_link': forms.TextInput(attrs={'class': 'form-control'}),
            'insta_link': forms.TextInput(attrs={'class': 'form-control'}),
            'niveau_etude': forms.Select(attrs={'class': 'form-control'}),
            'grade': forms.Select(attrs={'class': 'form-control'}),
            'faculte': forms.TextInput(attrs={'class': 'form-control'}),   
            'annee_graduation': forms.TextInput(attrs={'class': 'form-control'}),  
            'tel': forms.TextInput(attrs={'class': 'form-control'}),  
            'bio': forms.Textarea(attrs={'class': 'form-control'}),  
        }

        labels = {
            "twitter_link": "Lien Twitter (optionel)",
            "linkedin_link": "Lien Linkedin (optionel)",
            "fbook_link": "Lien Facebook (optionel)",
            "insta_link": "Lien Instagram (optionel)",
            "niveau_etude": "Niveau d'étude",
            "faculte": "Domaine",
            "annee_graduation": "Année de graduation",
            "tel": "Téléphone(Numéro Flooz ou Tmoney. Vous recevrez tous les montants de vos ventes sur ce numéro)",
            "pays_affiliation": "Pays d'affiliation",
            "affiliation": "Affiliation",
            "grade": "Grade",
            "bio": "Biographie",
            "image": "Photo de profil",
            
        }


        



        
    