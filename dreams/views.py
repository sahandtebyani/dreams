from django.shortcuts import render
from dreams_item.models import Item
from dreams_slider.models import Slider
from dreams_setting.models import SiteSetting


def header(request, *args, **kwargs):
    context = {}
    return render(request, 'shared/Header.html', context)


def footer(request, *args, **kwargs):
    setting = SiteSetting.objects.first()
    context = {
        'setting':setting
    }
    return render(request, 'shared/Footer.html', context)


def home_page(request):
    sliders = Slider.objects.all()
    most_visit = Item.objects.order_by('-visit_count').all()[:6]
    latest_add = Item.objects.order_by('-id').all()[:6]
    context = {
        'sliders': sliders,
        'most_visit': most_visit,
        'latest_add': latest_add
    }
    return render(request, 'home_page.html', context)


def about_us(request):
    about = SiteSetting.objects.first()
    context = {
        'about': about
    }
    return render(request, 'about_us.html', context)
