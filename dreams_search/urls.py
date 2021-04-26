from django.urls import path
from .views import SearchItem

urlpatterns = [
    path('search', SearchItem.as_view(), name='search'),
]
