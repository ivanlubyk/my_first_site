# Generated by Django 4.2.7 on 2023-12-27 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name': 'Новина', 'verbose_name_plural': 'Новини'},
        ),
    ]