# Generated by Django 5.0.4 on 2024-04-08 20:34

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('color', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='colormodel',
            options={'verbose_name': 'Цвет', 'verbose_name_plural': 'Цвета'},
        ),
        migrations.AlterModelTable(
            name='colormodel',
            table='color_color',
        ),
    ]