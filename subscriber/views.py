from django.shortcuts import render
from freducation.forms import recaptchaV3
from .forms import subscribeForm, unsubscribeForm
from .models import subscriber


# Create your views here.
def subscribeView(request):
    robotForm = recaptchaV3(request.POST or None)
    form = subscribeForm(request.POST or None)
    context = {
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
    return render(request,'subscribe/subscribe.html',context=context)

def unsubscribeView(request):
    robotForm = recaptchaV3(request.POST or None)
    form = unsubscribeForm(request.POST or None)
    context = {
        "form": form,
        "robotForm": robotForm
    }

    if request.method == 'POST':
        if form.is_valid() and robotForm.is_valid():
            
            if subscriber.objects.filter(email=form.cleaned_data['email'].lower()).exists():
                subscriber.objects.filter(email=form.cleaned_data['email'].lower()).delete()
            else:
                pass
            return render(request,'subscribe/successUnsub.html')
    return render(request,'subscribe/unsubscribe.html',context=context)

