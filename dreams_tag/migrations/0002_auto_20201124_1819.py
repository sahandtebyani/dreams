# Generated by Django 3.1.3 on 2020-11-24 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dreams_tag', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='product',
            new_name='item',
        ),
    ]
