from django.contrib.auth.models import User
from django.db import models


class projetModel(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    duration = models.TextField(blank=True, null=True)
    photoUrl = models.ImageField(upload_to="photo_folder/", blank=True, null=True)
    logoUrl = models.ImageField(upload_to="logo_folder/", blank=True, null=True)
    sponsorLogoUrl = models.ImageField(upload_to="logo_sponsor/", blank=True, null=True)
    link = models.CharField(max_length=255, default=" ")
    createdAt = models.DateTimeField(auto_now_add=True)
    editeAt = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=200, blank=False, default="")

    def __str__(self):
        return f"project, {self.title } created!"
