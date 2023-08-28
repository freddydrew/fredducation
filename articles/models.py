from django.db import models
from django.db.models.signals import post_save
from django.db.models import Q
from django.urls import reverse
from django.utils import timezone
from .utils import slugfiy
import pycountry

# Define Custom QuerySet behavior
class articleQuerySet(models.QuerySet):
    def search(self, query=None):
        if query is None or query == "" or query.strip() == '':
                return self.none() # Empty query list
        # Q lookups
        lookups = Q(title__icontains=query) | Q(
            content__icontains=query) | Q(
            city__icontains=query) | Q(
            country__icontains=query) | Q(
            alpha3__icontains=query) | Q(
            slug__icontains=query) | Q(
            postType__icontains=query)
        return self.filter(lookups)

# Modifying the base manager function for my class
class articleManager(models.Manager):
    # Custom QuerySet function call
    def get_queryset(self):
        return articleQuerySet(self.model,using=self._db)
    
    # Custom search function
    def search(self, query=None):
        return self.get_queryset().search(query=query)

# My article model
class article(models.Model):
    title = models.CharField(max_length=75)
    content = models.TextField(null=True,blank=True)
    contentEsp = models.TextField(null=True,blank=True)
    city = models.CharField(max_length=50,null=True,blank=True,default=None)
    country = models.CharField(max_length=50,null=True,blank=True,default=None)
    description = models.CharField(max_length=100,null=True,blank=True,default=None)
    alpha3 = models.CharField(max_length=10,null=True,editable=False)
    timestamp = models.DateTimeField(auto_now_add=True,editable=False) 
    updated = models.DateTimeField(auto_now=True,editable=False)
    pinned = models.BooleanField(null=True,blank=True,default=False)
    publish = models.BooleanField(null=True,blank=True,default=False)
    publishDate = models.DateField(null=True,blank=True,default=None)
    slug = models.SlugField(null=True,editable=False)
    thumbnail = models.ImageField(blank=False,upload_to='static/articles/')
    postType = models.CharField(max_length=75,null=True,default=None,blank=True,
                                choices=[("person","Person"),
                                         ("place","Place"),
                                         ("media","Media"),
                                         ("resource","Resource"),
                                         ("food","Food")])
    
    # Custom Manager Call 
    objects = articleManager()

    ## Getters
    def getTitle(self):
        return self.title
    
    def getContent(self):
        return self.content
    
    def getCity(self):
        return self.city
    
    def getCountry(self):
        return self.country
    
    def getPublish(self):
        return self.publish
    
    def getAbsoluteUrl(self):
        return reverse('articles:oneArticle',kwargs={'slug': self.slug})
    
    ## Setters 
    def setUpdated(self):
        article.objects.filter(id=self.id).update(updated=timezone.now())

    def setAlpha3(self):
        alpha3 = pycountry.countries.get(name=self.country).alpha_3
        self.alpha3 = alpha3
        article.objects.filter(id=self.id).update(alpha3=alpha3)

    def setSlug(self):
        if self.postType != "person" and self.postType != 'place':
            tmpSlug = f'{self.postType}-{self.title}'
        elif self.city == None:
            tmpSlug = f'{self.postType}-{self.title}-{self.alpha3}'
        else:
            tmpSlug = f'{self.postType}-{self.title}-{self.city}-{self.alpha3}'
        slug = slugfiy(tmpSlug)
        if article.objects.filter(slug=slug).count() != 0:
            slug = f'{slug}-{article.objects.filter(slug=slug).count()+1}'
        article.objects.filter(id=self.id).update(slug=slug)
    
    # Overwrite default save to use post_save signals 
    def save(self, *args, **kwargs):
        try:
            old = article.objects.get(pk=self.pk) #get old object
            new = self #get new object
            updatedFields = [] #for any fields that might be changed
            for field in article._meta.get_fields():
                fieldName = field.name
                #seeing if any fields have changed between the old and new objects
                #if so the field name is added to the updated fields list
                try:
                    if getattr(old,fieldName) != getattr(new,fieldName):
                        updatedFields.append(fieldName)
                #pass otherwise, nothing needed to be done
                except Exception as ex:
                    pass
                kwargs["update_fields"] = updatedFields
        except:
            pass
        return super().save(*args, **kwargs)
    
# Image class, dynamic. May add multiple images under an object    
class articleImage(models.Model):
    article = models.ForeignKey(article,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/articles/')
    
# Post save signal method for the article model
def articlePostSave(instance, created, *args,**kwargs):
    if created or kwargs["update_fields"] != []:
        if instance.postType != "person" and instance.postType != 'place':
            pass
        else:
            instance.setAlpha3()
        instance.setSlug() 
        instance.setUpdated()
    
# Connect save to the post save signal
post_save.connect(articlePostSave,sender=article)