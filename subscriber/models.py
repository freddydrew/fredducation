from django.db import models

# Create your models here.
class subscriber(models.Model):
    # What the user submits to me
    email = models.EmailField(max_length=75,blank=False)
    subscribeTime = models.DateTimeField(auto_now_add=True)



