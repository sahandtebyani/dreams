from django import forms
from django.core import validators


class ContactForm(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Fullname'}),
        validators=[
            validators.MaxLengthValidator(200, 'Fullname can not be more than 200 characters')
        ]
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email Address'}),
        validators=[
            validators.MaxLengthValidator(200, 'Email can not be more than 200 characters')
        ]
    )
    subject = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Subject'}),
        validators=[
            validators.MaxLengthValidator(200, 'Subject can not be more than 200 characters')
        ]
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Your Message'})
    )
