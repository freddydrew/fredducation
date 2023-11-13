from django.shortcuts import render
from .models import article
from django.views.generic import ListView, View 
from django.http import JsonResponse
from django.contrib.postgres.search import (
    SearchQuery, 
    SearchVector, 
    SearchRank 
)
from django.contrib.postgres.aggregates import StringAgg

# Different article model views
def oneArticleView(request,slug=None):
    obj = article.objects.get(slug=slug)
    context = {
        'obj': obj
    }
    return render(request,'articles/oneArticle.html',context=context)

class allArticlesView(ListView):
    '''
    Default name is object_list for returned query  with this method
    of rendering pages with generics and a class
    '''
    model = article
    template_name = 'articles/allArticles.html'

    def get_queryset(self):
        return article.objects.filter(publish=True).order_by('-publishDate')[0:8]
    
class allArticlesJsonView(View):
    def get(self,*args,**kwargs):
        articles = list(article.objects.filter(publish=True).order_by('-publishDate').values())
        return JsonResponse({'data': articles},safe=False)

def articleSearchView(request):
    q = request.GET.get('q')
    query = SearchQuery(q)
        
    vector = SearchVector('title',
                          'city',
                          'country',
                          'description',
                          'content',
                          'contentEsp',
                          'postType',
                          'publishDate',
                          StringAgg('tags__name',delimiter=' '))
    
    # Full text search with postgresql
    object_list = article.objects.annotate(
        rank=SearchRank(vector,query)).filter(publish=True,rank__gte=0.001).order_by('-rank')
    
    # Using old custom search queryset methods defined in model
    # object_list = article.objects.search(query=query).filter(publish=True)
    context={
        'object_list': object_list, #default name
        'searchQuery': q
    }

    return render(request,'articles/search.html',context=context)