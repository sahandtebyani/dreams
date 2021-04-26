from django.db import models
import os
from dreams_item_category.models import Category


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"items/{final_name}"


def upload_gallery_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"items/gallery/{final_name}"


class ItemManager(models.Manager):
    def get_active_items(self):
        return self.get_queryset().filter(active=True)

    def get_item_by_category(self, category_name):
        return self.get_queryset().filter(categories__name__iexact=category_name, active=True)

    def get_item_by_tag(self, tag_name):
        return self.get_queryset().filter(tag__slug__iexact=tag_name, active=True)

    def get_item_id(self, item_id):
        qs = self.get_queryset().filter(id=item_id)
        if qs.count() == 1:
            return qs.first()
        else:
            return None


class Item(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    favorite = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    categories = models.ManyToManyField(Category, blank=True)
    visit_count = models.IntegerField(default=0)

    objects = ItemManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/items/{self.id}/{self.title.replace(" ","-")}'


class ItemGallery(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to=upload_gallery_image_path)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
