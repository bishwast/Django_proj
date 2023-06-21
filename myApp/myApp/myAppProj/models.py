from django.db import models

# Create your models here.
class Feature(models.Model):        # converts this class into Model
    name = models.CharField(max_length=100)    # Stores characters
    details = models.CharField(max_length=500)
