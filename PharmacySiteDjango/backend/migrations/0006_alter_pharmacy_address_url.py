# Generated by Django 4.2.7 on 2023-11-27 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_remove_pharmacy_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pharmacy',
            name='address_url',
            field=models.CharField(max_length=2000),
        ),
    ]
