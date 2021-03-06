# Generated by Django 3.1.3 on 2020-11-28 16:31

from django.db import migrations, models
import dreams_slider.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('link', models.URLField()),
                ('image', models.ImageField(blank=True, null=True, upload_to=dreams_slider.models.upload_image_path)),
            ],
        ),
    ]
