# Generated by Django 3.1.3 on 2020-11-17 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dreams_item_category', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'Categories'},
        ),
    ]