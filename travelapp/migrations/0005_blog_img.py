# Generated by Django 3.2.16 on 2022-11-12 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0004_auto_20221112_0556'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='img',
            field=models.ImageField(null=True, upload_to='photos'),
        ),
    ]
