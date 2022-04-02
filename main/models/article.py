from sunau import Au_read
from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from main.helpers import *
from account.models import Auteur, Client
from django.urls import reverse



class Categorie(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('accueil')


class TypeDoc(models.Model):
    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('accueil')



class Article(models.Model):

    class Meta:
        ordering = ["-publish_date"]
        get_latest_by = "publish_date"

    title = models.CharField(max_length=300, unique=True)
    subtitle = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(max_length=300, unique=True)
    contenu = FroalaField()
    couverture = models.ImageField(upload_to='files/couverture')
    auteur = models.ForeignKey(Auteur, null=True , on_delete=models.CASCADE)
    domaine = models.CharField(max_length=50)
    resource = models.FileField(upload_to="files/resource")

    discount = models.IntegerField(null=False, default=0)
    price = models.IntegerField(null=False)

    is_draft = models.BooleanField(default=True)
    active = models.BooleanField(default=False)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

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
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000, null=True)
    rate = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)