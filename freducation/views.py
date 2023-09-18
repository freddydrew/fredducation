# freducation only, others will be kept in their apps folder
from django.shortcuts import render
from articles.models import article

def homeView(request):
    sliderObjList = article.objects.all().filter(publish=True).order_by('-publishDate')[0:3]
    pinnedObjList = article.objects.all().filter(pinned=True).order_by('-publishDate')
    context = {
        "sliderObjList": sliderObjList,
        "pinnedObjList": pinnedObjList
    }
    return render(request,'home.html',context=context)

def aboutView(request):
    context = {}
    return render(request,'about.html',context=context)

