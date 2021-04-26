from django.urls import path
from .views import ItemList, item_detail, ItemCategory, item_category, ItemTag

urlpatterns = [
    path('items', ItemList.as_view(), name='items'),
    path('items/<item_id>/<name>', item_detail),
    path('item/<category_name>', ItemCategory.as_view()),
    path('tag/<tag_name>', ItemTag.as_view()),
    path('item-category-partial', item_category, name='item-category-partial')
]
