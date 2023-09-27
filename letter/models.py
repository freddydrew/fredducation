from django.db import models

# Create your models here.
class letter(models.Model):
    message = models.TextField()

