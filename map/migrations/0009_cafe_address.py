# Generated by Django 4.0.2 on 2022-10-04 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0008_alter_cafe_latitude_alter_cafe_longitude'),
    ]

    operations = [
        migrations.AddField(
            model_name='cafe',
            name='address',
            field=models.CharField(default='None', max_length=25),
            preserve_default=False,
        ),
    ]
