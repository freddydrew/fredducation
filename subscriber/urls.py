from django.urls import path

from .views import subscribeView

app_name = 'subscriber'
urlpatterns = [
    path('', subscribeView, name='subscribe'),
]
