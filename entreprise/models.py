from django.db import models
from froala_editor.fields import FroalaField

from account.models import Entreprise
from main.helpers import generate_slug
from main.models.article import Categorie

# Create your models here.



class Problematique(models.Model):
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    titre = models.CharField(max_length=300)
    domaine = models.ForeignKey(Categorie, null=True, on_delete=models.SET_NULL)
    description = FroalaField()
    slug = models.SlugField(max_length=300, unique=True)
    profil_rechercher = FroalaField()
    duree_recherche = models.IntegerField()
    is_draft = models.BooleanField(default=True)
    active = models.BooleanField(default=False)
    publish_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre

    def save(self , *args, **kwargs): 
        self.slug = generate_slug(self.titre)
        super(Problematique, self).save(*args, **kwargs)


class Postuler(models.Model):
    problematique = models.ForeignKey(Problematique, on_delete=models.CASCADE)
    nom_du_candidat = models.CharField(max_length=50)
    prenom_du_candidat = models.CharField(max_length=50)
    contact_du_candidat = models.IntegerField()
    email_du_candidat = models.EmailField()
    motivation_du_candidat = FroalaField()
    postule_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom_du_candidat

    
