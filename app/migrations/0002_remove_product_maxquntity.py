# Generated by Django 2.2.4 on 2023-11-27 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='maxquntity',
        ),
    ]
