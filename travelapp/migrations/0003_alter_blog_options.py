# Generated by Django 3.2.16 on 2022-11-11 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0002_blog'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-date']},
        ),
    ]
