from django.db import models
import os


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.site_title}{ext}"
    return f"items/{final_name}"


class SiteSetting(models.Model):
    site_title = models.CharField(max_length=150)
    address = models.CharField(max_length=300)
    email = models.EmailField
    phone = models.IntegerField
    logo_image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    copyright = models.CharField(max_length=200)
    about_us = models.CharField(max_length=300)

    def __str__(self):
        return self.site_title
