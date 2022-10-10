# Generated by Django 4.0.2 on 2022-09-05 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0004_alter_cafe_latitude_alter_cafe_longitude_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cafe',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='cafe',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='cafe',
            name='main_image',
            field=models.ImageField(blank=True, null=True, upload_to='map/static/map/main_images'),
        ),
        migrations.AlterField(
            model_name='cafe',
            name='review',
            field=models.TextField(blank=True, help_text='Cafe Review', null=True),
        ),
        migrations.AlterField(
            model_name='cafe',
            name='sub_images',
            field=models.ImageField(blank=True, null=True, upload_to='map/static/map/sub_images'),
        ),
    ]
