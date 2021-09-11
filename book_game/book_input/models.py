from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    year = models.PositiveIntegerField()
    blurb = models.CharField(max_length=1000)
    first_line = models.CharField(max_length=250)
    last_line = models.CharField(max_length=250)
    notes = models.CharField(max_length=1000)