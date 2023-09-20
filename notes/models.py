from django.db import models

from authapp.models import User


# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=32)
    repository_link = models.URLField(blank=True, null=True)
    users = models.ManyToManyField(User, related_name='projects')

    def __str__(self):
        return self.name


class Note(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.text
