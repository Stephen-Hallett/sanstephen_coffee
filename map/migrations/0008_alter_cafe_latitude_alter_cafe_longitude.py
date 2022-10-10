# Generated by Django 4.0.2 on 2022-10-01 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0007_alter_cafe_latitude_alter_cafe_longitude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cafe',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=21, max_digits=25, null=True),
        ),
        migrations.AlterField(
            model_name='cafe',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=21, max_digits=25, null=True),
        ),
    ]
