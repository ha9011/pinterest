from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projects.models import Project


class Subscribe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="subscrive")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="subscrive")

    class Meta:
        unique_together = ("user","project")
