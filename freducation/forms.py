from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV3 

class recaptchaV3(forms.Form):
    recaptcha = ReCaptchaField(widget=ReCaptchaV3)