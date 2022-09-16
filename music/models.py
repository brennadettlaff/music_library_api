from django.db import models

# Create your models here.

class Music(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    album = models.CharField(max_length=100)
    release_date = models.DateField()
    genre = models.CharField(max_length=100)