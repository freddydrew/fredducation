from django.db import models

# Create your models here.
class contact(models.Model):
    # What the user submits to me
    firstName = models.CharField(max_length=50,blank=False,editable=False)
    lastName = models.CharField(max_length=50,blank=False,editable=False)
    email = models.EmailField(max_length=75,blank=False,editable=False)
    subject = models.CharField(max_length=75,blank=False,editable=False)
    message = models.TextField(blank=False,editable=False)

    # What I use to track submitted messages
    timeSent = models.DateTimeField(auto_now_add=True,editable=False)
    updated = models.DateTimeField(auto_now=True,editable=False)
    responded = models.TextField(blank=True,null=True)
    closed = models.BooleanField(default=False)
