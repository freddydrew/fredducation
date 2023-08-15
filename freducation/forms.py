from django import forms
from django.core.mail import EmailMessage 
from .settings import EMAIL_HOST_USER

# Contact Form
class contactForm(forms.Form):
    fullName = forms.CharField(label="Full Name")
    email = forms.CharField(label="Email Address")
    subject = forms.CharField(label="Subject")
    message = forms.CharField(label="Message",
                              widget=forms.Textarea)

'''
This sends me the contact forms contents so I can respond
by simply hitting reply from my email, super simple.
'''
def contactFormSendMail(form):

    # Email Contents
    emailMessage = f'''
FROM:           {form.data["fullName"]}
EMAIL:          {form.data["email"]}

MESSAGE:
{form.data["message"]}
    '''
    
    emailSubject = f"CONTACT FORM: {form.data['subject']}"
    emailSentTo = [EMAIL_HOST_USER]
    emailReplyTo = [f'{form.data["email"]}']
    # Send Email
    email = EmailMessage(emailSubject, emailMessage, 
                        '', emailSentTo,
                         reply_to = emailReplyTo)
    email.send()
