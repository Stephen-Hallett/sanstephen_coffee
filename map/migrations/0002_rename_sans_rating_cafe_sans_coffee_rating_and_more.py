# Generated by Django 4.0.2 on 2022-09-05 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cafe',
            old_name='sans_rating',
            new_name='sans_coffee_rating',
        ),
        migrations.RenameField(
            model_name='cafe',
            old_name='stephen_rating',
            new_name='stephen_coffee_rating',
        ),
        migrations.AddField(
            model_name='cafe',
            name='main_image',
            field=models.ImageField(blank=True, max_length=1, upload_to='map/static/map/main_images'),
        ),
        migrations.AddField(
            model_name='cafe',
            name='sub_images',
            field=models.ImageField(blank=True, max_length=4, upload_to='map/static/map/sub_images'),
        ),
    ]
