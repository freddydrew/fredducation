from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox

class subscribeForm(forms.Form):
    email = forms.EmailField(required=True,
                             help_text="Example: derf@mail.com",
                             label="Your Email")
    
class unsubscribeForm(forms.Form):
    email = forms.EmailField(required=True,
                             help_text="Example: derf@mail.com",
                             label="Your Email")