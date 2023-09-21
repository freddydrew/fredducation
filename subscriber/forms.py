from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

class subscribeForm(forms.Form):
    firstName = forms.CharField(required=True,
                                help_text="Example: Derf",
                                label="First Name")
    lastName = forms.CharField(required=False,
                               help_text="Example: Werd",
                               label="Last Name (Optional)")
    email = forms.EmailField(required=True,
                             help_text="Example: derf@mail.com",
                             label="Your Email")
    recaptcha = ReCaptchaField(widget=ReCaptchaV2Checkbox(
        attrs={
            'data-theme': 'light',
            'data-size': 'compact',
        }
    ))