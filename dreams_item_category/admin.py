from django.contrib import admin
from .models import Category


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'title']

    class Meta:
        model = Category


admin.site.register(Category, CategoryAdmin)
