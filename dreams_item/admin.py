from django.contrib import admin
from .models import Item, ItemGallery


# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'title', 'active']

    class Meta:
        model = Item


admin.site.register(Item, ItemAdmin)
admin.site.register(ItemGallery)
