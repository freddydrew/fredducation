from django.contrib import admin
from .models import contact

# Register your models here.
class contactAdmin(admin.ModelAdmin):
    list_display = ['subject','timeSent','updated','closed']
    readonly_fields = ['firstName','lastName','email',
                       'subject','message',
                       'timeSent','updated']

admin.site.register(contact,contactAdmin)