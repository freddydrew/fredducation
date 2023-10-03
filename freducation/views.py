# freducation only, others will be kept in their apps folder
from django.shortcuts import render
from articles.models import article
from .forms import recaptchaV3
from subscriber.forms import subscribeForm
from subscriber.models import subscriber

def homeView(request):
    form = subscribeForm(request.POST or None)
    robotForm = recaptchaV3(request.POST or None)
    sliderObjList = article.objects.all().filter(publish=True).order_by('-publishDate')[0:3]
    pinnedObjList = article.objects.all().filter(pinned=True).order_by('-publishDate')
    context = {
        "sliderObjList": sliderObjList,
        "pinnedObjList": pinnedObjList,
        "form": form,
        "robotForm": robotForm
    }

    if request.method == 'POST':
        if form.is_valid() and robotForm.is_valid():
            if subscriber.objects.filter(email=form.cleaned_data['email'].lower()).exists():
                pass
            else:
                newSubscriber = subscriber(
                    email=form.cleaned_data['email'].lower() 
                )
                newSubscriber.save()
            return render(request,'subscribe/success.html')
    
    return render(request,'home.html',context=context)

def aboutView(request):
    context = {}
    return render(request,'about.html',context=context)

