# Generated by Django 4.2.7 on 2023-11-25 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Pharmacy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_address', models.CharField(max_length=200)),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.medicine')),
                ('pharmacy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.pharmacy')),
            ],
        ),
        migrations.AddField(
            model_name='medicine',
            name='pharmacy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.pharmacy'),
        ),
    ]
