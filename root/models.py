from django.db import models

# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=42)
    breed = models.CharField(max_length=42)
    age = models.IntegerField()
    owner = models.CharField(max_length=42)
    