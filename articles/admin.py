from django.contrib import admin
from .models import article, articleImage

# All my models registered here so we can see them in the admin
class articleImageInline(admin.StackedInline):
    model = articleImage
    extra = 0

class articleAdmin(admin.ModelAdmin):
    # What fields I will see in the multiple objects view
    list_display = ['title','publish','publishDate','postType','country']
    # For the uneditable fields
    readonly_fields = ['timestamp','updated','alpha3','slug']
    inlines = [articleImageInline]

# Register the model
admin.site.register(article,articleAdmin)