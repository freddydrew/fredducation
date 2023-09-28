from django.db import models
from articles.models import article

# Create your models here.
class letter(models.Model):
    title = models.CharField(max_length=75,blank=False)
    message = models.TextField()
    article = models.ForeignKey(article,on_delete=models.PROTECT)
    sent = models.BooleanField(default=False,editable=False)
    dateSent = models.DateField(null=True,editable=False)
    


