# Generated by Django 4.2.7 on 2023-11-27 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_pharmacy_address_url_pharmacy_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pharmacy',
            name='name',
        ),
    ]
