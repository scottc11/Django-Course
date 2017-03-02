from django.db import models

# Create your models here.
class About(models.Model):
    image = models.ImageField(upload_to='media/')
    body = models.TextField()
