from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
# from django.core.mail import EmailMessage 

# Contact Form
class contactForm(forms.Form):
    firstName = forms.CharField(label="First Name:",required=True,
                                help_text="Example: Derf")
    lastName = forms.CharField(label="Last Name (Optional):",required=False,
                               help_text="Example: Werd")
    email = forms.EmailField(label="EMAIL:",required=True,
                             help_text="Example: derfwerd@mail.com")
    subject = forms.CharField(label="Subject:",required=True,
                            help_text="Example: I found a typo...")
    message = forms.CharField(label="Message:",
                              widget=forms.Textarea,required=True,
                              max_length=2000,
                              help_text="In X article you forgot the ñ in...")
    recaptcha = ReCaptchaField(widget=ReCaptchaV2Checkbox(
        attrs={
            'data-theme': 'light',
            'data-size': 'compact',
        }
    ))

'''
This sends me the contact forms contents so I can respond
by simply hitting reply from my email, super simple.
'''
# def contactFormSendMail(form):

#     # Email Contents
#     emailMessage = f'''
# FROM:           {form.data["fullName"]}
# EMAIL:          {form.data["email"]}

# MESSAGE:
# {form.data["message"]}
#     '''
    
#     emailSubject = f"CONTACT FORM: {form.data['subject']}"
#     emailSentTo = [EMAIL_HOST_USER]
#     emailReplyTo = [f'{form.data["email"]}']
#     # Send Email
#     email = EmailMessage(emailSubject, emailMessage, 
#                         '', emailSentTo,
#                          reply_to = emailReplyTo)
#     email.send()
