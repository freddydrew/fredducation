from django.shortcuts import render
from .forms import subscribeForm
from .models import subscriber

# Create your views here.
def subscribeView(request):
    context = {}
    form = subscribeForm(request.POST or None)
    context['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            if subscriber.objects.filter(email=form.cleaned_data['email']).exists():
                pass
            else:
                newSubscriber = subscriber(
                    firstName=form.cleaned_data['firstName'],
                    lastName=form.cleaned_data['lastName'],
                    email=form.cleaned_data['email']
                )
                newSubscriber.save()
            return render(request,'subscribe/success.html')
   
    return render(request,'subscribe/subscribe.html',context=context)

