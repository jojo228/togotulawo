from sunau import Au_read
from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from main.helpers import *
from account.models import Auteur, Client
from django.urls import reverse



class Categorie(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=300, unique=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('accueil')

    def save(self , *args, **kwargs): 
        self.slug = generate_slug(self.name)
        super(Categorie, self).save(*args, **kwargs)



class Article(models.Model):

    option =(
        ('Thèse', 'Thèse'),
        ('Mémoire', 'Mémoire'),
        ('Rapport de stage', 'Rapport de stage'),
        ('Document de synthèse', 'Document de synthèse'),
        ('Article', 'Article'),
        ('Livre', 'Livre'),
    )

    class Meta:
        ordering = ["-publish_date"]
        get_latest_by = "publish_date"

    title = models.CharField(max_length=300, unique=True)
    subtitle = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(max_length=300, unique=True)
    contenu = FroalaField()
    couverture = models.ImageField(upload_to='files/couverture', null=True, blank=True)
    auteur = models.ForeignKey(Auteur, null=False, on_delete=models.CASCADE)
    domaine = models.ForeignKey(Categorie, null=False, on_delete=models.CASCADE)
    type = models.CharField(max_length=100, choices=option)
    resource = models.FileField(
        upload_to="files/resource", null=True, blank=True)

    discount = models.IntegerField(null=False, default=0)
    price = models.IntegerField(null=False)

    is_draft = models.BooleanField(default=True)
    active = models.BooleanField(default=False)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title + ' | ' + str(self.auteur)

    def save(self , *args, **kwargs): 
        self.slug = generate_slug(self.title)
        super(Article, self).save(*args, **kwargs)



class ArticleProperty(models.Model):
    description = models.CharField(max_length=100, null=False)
    article = models.ForeignKey(Article, null=False, on_delete=models.CASCADE)

    class Meta:
        abstract = True



class Tag(ArticleProperty):
    pass



class CouponCode(models.Model):
    code = models.CharField(max_length=6)
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name='coupons')
    discount = models.IntegerField(default=0)



class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000, null=True)
    rate = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)