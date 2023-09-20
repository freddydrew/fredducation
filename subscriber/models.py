from django.db import models

# Create your models here.
class subscriber(models.Model):
    # What the user submits to me
    firstName = models.CharField(max_length=50,blank=False)
    lastName = models.CharField(max_length=50,blank=True)
    email = models.EmailField(max_length=75,blank=False)
    subscribeTime = models.DateTimeField(auto_now_add=True)
