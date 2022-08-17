from django.db import models
from main.models.article import Article
from main.models.user_article import UserArticle
from django.contrib.auth.models import User


class Payment(models.Model):
    order_id = models.CharField(max_length = 50 , null = False)
    payment_id = models.CharField(max_length = 50)
    user_article = models.ForeignKey(UserArticle , null = True , blank = True ,  on_delete=models.CASCADE)
    user = models.ForeignKey(User ,  on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=8, null=True)
    network = models.CharField(max_length=6, null=True)
    article = models.ForeignKey(Article , on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

   
    




    