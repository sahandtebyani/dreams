from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=150)
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title
