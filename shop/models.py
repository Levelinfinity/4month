from django.db import models

# Create your models here.
class Shop(models.Model):
    name = models.CharField(max_length=60)
    color = models.CharField(max_length=30)
    logo = models.ImageField(upload_to='logo/', blank=True, null=True)