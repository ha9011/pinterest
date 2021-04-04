from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articles.models import Article


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='likes')

    class Meta:
        unique_together = ("user", "article")