from django.db import models
from django.contrib.auth.models import User

option = (
    ('License', 'License'),
    ('Maîtrise', 'Maîtrise'),
    ('Master', 'Master'),
    ('Doctorat', 'Doctorat'),
    ('DEA', 'DEA'),
    ('Professorat', 'Professorat'),
)


class Auteur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    niveau_etude = models.CharField(max_length=50, choices=option)
    faculte = models.CharField(max_length=50)
    annee_graduation = models.DateField()
    tel = models.CharField(max_length=8)
    website = models.URLField(max_length=200, blank=True)
    bio = models.CharField(max_length=1000, blank=True)
    token = models.CharField(max_length=100)
    image = models.ImageField(
        default="profile2.png", null=True, blank=True, upload_to='files/profic_pic')

    def __str__(self):
        return self.user.get_full_name()


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=8)

    def __str__(self):
        return self.user.get_full_name()


class Entreprise(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    raison_social = models.CharField(max_length=200)
    objet_social = models.CharField(max_length=200)
    adresse = models.CharField(max_length=200)
    telephone = models.CharField(max_length=8)
    image = models.ImageField(default="static/dashboard/assets/images/user/user.png",
                              null=True, blank=True, upload_to='files/ense_pic')

    def __str__(self):
        return self.raison_social
