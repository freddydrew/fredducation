from django.contrib import admin
from .models import subscriber

# Register your models here.
class subscriberAdmin(admin.ModelAdmin):
    list_display = ['id','firstName','lastName','email','subscribeTime']

admin.site.register(subscriber,subscriberAdmin)