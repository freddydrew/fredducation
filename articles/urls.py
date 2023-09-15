from django.urls import path

from .views import (
    articleSearchView,
    oneArticleView,
    allArticlesView,
    allArticlesJsonView
)


app_name = 'articles'
urlpatterns = [
    path('search/',articleSearchView,name="search"),
    path('',allArticlesView.as_view(),name='allArticles'),
    path('jsonListView/',allArticlesJsonView.as_view(),name='articlesJson'),
    path('<slug:slug>/',oneArticleView, name='oneArticle'),
] 
