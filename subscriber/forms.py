from django import forms

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