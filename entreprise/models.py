from django.db import models
from main.helpers import generate_slug
from account.models import Entreprise
from main.models.article import Categorie
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.


class Problematique(models.Model):
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    titre = models.CharField(max_length=300)
    domaine = models.ForeignKey(Categorie, null=True, on_delete=models.SET_NULL)
    description = RichTextUploadingField()
    slug = models.SlugField(max_length=300, unique=True)
    profil_rechercher = RichTextUploadingField()
    duree_recherche = models.IntegerField()
    is_draft = models.BooleanField(default=True)
    active = models.BooleanField(default=False)
    publish_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre

    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.titre)
        super(Problematique, self).save(*args, **kwargs)


class Postuler(models.Model):
    problematique = models.ForeignKey(Problematique, on_delete=models.CASCADE)
    nom_du_candidat = models.CharField(max_length=50)
    prenom_du_candidat = models.CharField(max_length=50)
    contact_du_candidat = models.IntegerField()
    email_du_candidat = models.EmailField()
    motivation_du_candidat = RichTextUploadingField()
    postule_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom_du_candidat


class Livre(models.Model):
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    titre = models.CharField(max_length=200)
    slug = models.SlugField(max_length=300, unique=True)
    description = models.TextField(max_length=2000, null=True, blank=True)
    document = models.FileField(upload_to="files/documents")
    date_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre

    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.titre)
        super(Livre, self).save(*args, **kwargs)
