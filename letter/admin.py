from django.contrib import admin
from .models import letter

# Register your models here.
class letterAdmin(admin.ModelAdmin):
    list_display = ['title','sent','dateSent','article']
    readonly_fields = ['sent','dateSent']

admin.site.register(letter,letterAdmin)