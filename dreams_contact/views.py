from django.shortcuts import render
from .forms import ContactForm
from .models import ContactUs


def contact_us(request, *args, **kwargs):
    contact_form = ContactForm(request.POST or None)
    if contact_form.is_valid():
        full_name = contact_form.cleaned_data.get('full_name')
        email = contact_form.cleaned_data.get('email')
        subject = contact_form.cleaned_data.get('subject')
        message = contact_form.cleaned_data.get('message')
        ContactUs.objects.create(fullname=full_name, email=email, subject=subject, message=message)
        contact_form = ContactForm()
    context = {
        'form': contact_form
    }
    return render(request, 'contact/contact_us.html', context)
