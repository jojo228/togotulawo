from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField


related_name_string = "%(app_label)s_%(class)s_related"
related_query_name_string = "%(app_label)s_%(class)ss"

class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_editor = models.BooleanField(default=False)
    is_author = models.BooleanField(default=False)
    is_reviewer = models.BooleanField(default=False)
    is_reader = models.BooleanField(default=False)


   

class UserCommonInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name=related_name_string,
        related_query_name=related_query_name_string,
)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.PositiveIntegerField(null=True, blank=True,)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.first_name()

    class Meta:
        abstract = True



# class Affiliation(models.Model):
#     institution_name = models.CharField(max_length=50)
#     institution_department = models.CharField(max_length=50)
#     city = models.CharField(max_length=50)
#     country = models.CharField(max_length=50)



class Author(UserCommonInfo):
    orcid_id = models.CharField(max_length=25, unique=True, null=True)
    affiliation = models.CharField(max_length=200)
    image = models.ImageField(default='files/profic_pic/t_user.png', null=True, blank=True, upload_to='files/profic_pic')



class Reviewer(UserCommonInfo):
    pass


class Reader(UserCommonInfo):
    pass


class Editor(UserCommonInfo):
    pass
    
