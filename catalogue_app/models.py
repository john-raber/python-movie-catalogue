from django.conf import settings
from django.db import models
from django.utils import timezone


class Movie(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    genre = models.TextField()
    link = models.TextField()
    year = models.IntegerField()
