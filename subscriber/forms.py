from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

class subscribeForm(forms.Form):
    email = forms.EmailField(required=True,
                             help_text="Example: derf@mail.com",
                             label="Your Email")
    
class unsubscribeForm(forms.Form):
    email = forms.EmailField(required=True,
                             help_text="Example: derf@mail.com",
                             label="Your Email")