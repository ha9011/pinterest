from django.contrib.auth.models import User
from django.db import models

# Create your models hec

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    # request.user.profile로 접근 가능


    # media root 밑에 profile이 생기면서 저장됨
    image = models.ImageField(upload_to="profile/", null=True )
    nickname = models.CharField(max_length=20, unique=True)
    message = models.CharField(max_length=100, null=True)
