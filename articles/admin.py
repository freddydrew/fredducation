from django.contrib import admin
from .models import article, articleImage

# Here I Register models so they can be seen in the admin panel.
# I also specify the types of models and it's relation to others.

'''
This inline model will be shown below an Article model if I choose
to add one. First I must tell Django, 'this will be an inline'
'''
class articleImageInline(admin.StackedInline):
    model = articleImage #specify the model to be an inline
    extra = 0 #default is 0 to be shown under another model

# Main model for articles, its the blueprint for posts on the site
class articleAdmin(admin.ModelAdmin):
    # What fields I will see in the multiple objects view
    list_display = ['title','publish','publishDate','postType','country']
    # For the uneditable fields to be seen as well
    readonly_fields = ['timestamp','updated','alpha3','slug']

    '''
    So I can add or subtract Image Model Objects from a given Article 
    Model Object, in the same window. This allows me to easily see and
    change what Images are attached to each Article. I did not 
    register this model seperately because I only wish to edit it 
    from the Articles that it's objects will be attached to. 
    '''
    inlines = [articleImageInline]

# Register the model in this Django App, the article and its admin
admin.site.register(article,articleAdmin)