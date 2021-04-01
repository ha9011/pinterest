from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articles.models import Article


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, null = True, related_name="comment")
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null = True, related_name="comment")
    content = models.TextField(null=False)
    create_at = models.DateField(auto_now_add=True)