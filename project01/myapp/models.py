from django.db import models

# Create your models here.

class contact(models.Model):
    name = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    email = models.CharField(max_length=60)