from django.db import models
from dreams_item.models import Item
from django.db.models.signals import pre_save
from .utils import unique_slug_generator


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    item = models.ManyToManyField(Item, blank=True)

    def __str__(self):
        return self.title

    def get_tag_url(self):
        return f'/tag/{self.title.replace(" ", "-")}'


def tag_pre_save_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(tag_pre_save_generator, sender=Tag)
