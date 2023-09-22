from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3

class recaptchaV3(forms.Form):
    recaptcha = ReCaptchaField(widget=ReCaptchaV3)