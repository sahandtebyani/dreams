import itertools
from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView
from dreams_item_category.models import Category
from .models import Item, ItemGallery
from dreams_tag.models import Tag



# Create your views here.

class ItemList(ListView):
    template_name = 'item/item_list.html'
    paginate_by = 6

    def get_queryset(self):
        return Item.objects.get_active_items()


class ItemCategory(ListView):
    template_name = 'item/item_list.html'
    paginate_by = 6

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        category = Category.objects.filter(name__iexact=category_name).first()
        if category is None:
            raise Http404('item not found')
        return Item.objects.get_item_by_category(category_name)


class ItemTag(ListView):
    template_name = 'item/item_list.html'
    paginate_by = 6

    def get_queryset(self):
        tag_name = self.kwargs['tag_name']
        tag = Tag.objects.filter(slug__iexact=tag_name).first()
        if tag is None:
            raise Http404('not found any item that contains this tag')
        return Item.objects.get_item_by_tag(tag_name)


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


def item_detail(request, *args, **kwargs):
    selected_item_id = kwargs['item_id']
    item = Item.objects.get_item_id(selected_item_id)

    if item is None or not item.active:
        raise Http404('item not found')

    tags = item.tag_set.all()

    item.visit_count += 1
    item.save()

    related_items = Item.objects.get_queryset().filter(categories__item=item).distinct()
    grouped_items = my_grouper(4, related_items)

    galleries = ItemGallery.objects.filter(item_id=selected_item_id)
    item_gallery = list(my_grouper(4, galleries))


    context = {
        'item': item,
        'tags': tags,
        'item_gallery': item_gallery,
        'related_item': grouped_items,
    }
    return render(request, 'item/item_detail.html', context)


def item_category(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'item/item_category_partial.html', context)
