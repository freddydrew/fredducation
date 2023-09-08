from django.shortcuts import render
from .models import article
from django.views.generic import ListView, View 
from django.http import JsonResponse

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
        return article.objects.filter(publish=True).order_by('-publishDate')[0:6]
    
class allArticlesJsonView(View):
    def get(self,*args,**kwargs):
        articles = list(article.objects.filter(publish=True).order_by('-publishDate').values())
        return JsonResponse({'data': articles},safe=False)

def articleSearchView(request):
    query = request.GET.get('q')
    object_list = article.objects.search(query=query).filter(publish=True)
    context={
        'object_list': object_list #default name
    }
    return render(request,'articles/search.html',context=context)