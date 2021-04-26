from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.forms import User
from .forms import RegisterForm, LoginForm


# Create your views here.

def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    register_form = RegisterForm(request.POST or None)
    if register_form.is_valid():
        first_name = register_form.cleaned_data.get('first_name')
        last_name = register_form.cleaned_data.get('last_name')
        email = register_form.cleaned_data.get('email')
        password = register_form.cleaned_data.get('password')
        User.objects.create_user(username=email, first_name=first_name, last_name=last_name, email=email, password=password)
        return redirect('/login')
    context = {
        'register_form': register_form
    }
    return render(request, 'accuont/register.html', context)


def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        email = login_form.cleaned_data.get('email')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, username=email,  email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            login_form.add_error('email','There is no user with this information')

    context = {
        'login_form': login_form
    }
    return render(request, 'accuont/login.html', context)


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/login')
