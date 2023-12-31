from django.db import models


# Create your models here.
class CourseModels(models.Model):
    title = models.CharField(max_length=200, blank=False, default="")
    description = models.CharField(max_length=200, blank=False, default="")
    link = models.CharField(max_length=200, blank=False, default="")
    author = models.CharField(max_length=200, blank=False, default="")
    published = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    editeAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
