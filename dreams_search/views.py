from django.shortcuts import render
from django.views.generic import ListView
from dreams_item.models import Item
from django.db.models import Q
from dreams_tag.models import Tag


# Create your views here.


class SearchItem(ListView):
    template_name = 'item/item_list.html'
    paginate_by = 6

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')
        lookup = (
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(tag__title__icontains=query)
        )
        if query is not None:
            return Item.objects.filter(lookup, active=True).distinct()
        else:
            return Item.objects.get_active_items()
