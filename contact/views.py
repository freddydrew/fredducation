from django.shortcuts import render
from .forms import contactForm
from .models import contact

# Create your views here.
def contactView(request):
    context = {}
    form = contactForm(request.POST or None)
    context['form'] = form

    if request.method == "POST":

        # If the fields in the form are validated successfully
        if form.is_valid():
            # Create new contact object in database
            newContact = contact(
                firstName=form.cleaned_data['firstName'],
                lastName=form.cleaned_data['lastName'],
                email=form.cleaned_data['email'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message']
            )
            newContact.save()

            # Send user to success page 
            return render(request,'contact/success.html')

    return render(request,'contact/contact.html',context=context)

