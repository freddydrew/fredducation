from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox

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

