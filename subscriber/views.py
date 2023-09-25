from django.shortcuts import render
from freducation.forms import recaptchaV3
from .forms import subscribeForm
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
                    firstName=form.cleaned_data['firstName'].lower(),
                    lastName=form.cleaned_data['lastName'].lower(),
                    email=form.cleaned_data['email'].lower()                )
                newSubscriber.save()
            return render(request,'subscribe/success.html')
    return render(request,'subscribe/subscribe.html',context=context)

