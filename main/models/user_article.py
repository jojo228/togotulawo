from django.db import models
from main.models.article import Article
from django.contrib.auth.models import User



class UserArticle(models.Model):
    user = models.ForeignKey(User , null = False , on_delete=models.CASCADE)
    article = models.ForeignKey(Article , null = False , on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.article.title}'

    

