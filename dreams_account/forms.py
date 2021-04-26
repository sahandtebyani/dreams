from django import forms
from django.contrib.auth.forms import User


class RegisterForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Please Enter Your FirstName'}),
        label='First Name'
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Please Enter Your LastName'}),
        label='Last Name'
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Please Enter Your Email'}),
        label='Email'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Please Enter Your Password'}),
        label='Password'
    )
    password_2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Please Confirm Your Password'}),
        label='Re-enter Password'
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        is_exists_user_by_email = User.objects.filter(email=email).exists()
        if is_exists_user_by_email:
            raise forms.ValidationError('This email already signed up')
        else:
            return email

    def clean_password_2(self):
        password = self.cleaned_data.get('password')
        password_2 = self.cleaned_data.get('password_2')
        if password != password_2:
            raise forms.ValidationError("Passwords doesn't match")
        else:

            return password


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Enter Email'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'})
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        is_exists_email = User.objects.filter(email=email).exists()
        if not is_exists_email:
            raise forms.ValidationError("This Email Doesn't Register")
        else:
            return email
