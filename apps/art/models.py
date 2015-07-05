from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication = models.DateTimeField(auto_now_add = True)
    category = models.CharField(max_length=100)
    hero_image = models.CharField(max_length=100)
    optional_image = models.CharField(max_length=100)
    body_text = models.TextField()
    