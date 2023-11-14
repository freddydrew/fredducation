from django.contrib import admin
from articles.models import article, articleChoiceField
from .models import letter
from .utils import sendNewsLetter

# Register your models here.
class letterAdmin(admin.ModelAdmin):
    @admin.action(description='Send subscriber email')
    def sendLetter(modelAdmin,request,queryset):
        if queryset.count() != 1:
            warningMsg = 'Only one letter can be sent at a time.'
            modelAdmin.message_user(request,warningMsg)
        else:
            obj = queryset[0]
            sendNewsLetter(obj)
            obj.setSent()
            obj.setDateSent()
            confirmationMsg = 'Message Sent'
            modelAdmin.message_user(request,confirmationMsg)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'article':
            return articleChoiceField(queryset=article.objects.filter(publish=True))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    
    list_display = ['title','sent','dateSent']
    readonly_fields = ['sent','dateSent']
    actions = [sendLetter]

    

admin.site.register(letter,letterAdmin)