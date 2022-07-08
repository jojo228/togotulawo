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
    niveau_etude = models.CharField(max_length=50, choices=option, null=True, blank=True,)
    faculte = models.CharField(max_length=50, null=True, blank=True,)
    annee_graduation = models.DateField(null=True, blank=True,)
    tel = models.PositiveIntegerField(null=True, blank=True,)
    website = models.URLField(max_length=200, null=True, blank=True,)
    bio = models.CharField(max_length=1000, null=True, blank=True,)
    image = models.ImageField(
        default="dashboard/assets/images/user/user.png", null=True, blank=True, upload_to='files/profic_pic')

    def __str__(self):
        return self.user.get_full_name()


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telephone = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.user.get_full_name()


class Entreprise(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    raison_social = models.CharField(max_length=200)
    objet_social = models.CharField(max_length=200)
    adresse = models.CharField(max_length=200)
    telephone = models.PositiveIntegerField(blank=True, null=True)
    image = models.ImageField(default="dashboard/assets/images/user/user.png",
                              null=True, blank=True, upload_to='files/ense_pic')

    def __str__(self):
        return self.raison_social
