# Generated by Django 3.2.7 on 2021-10-04 04:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='statusmodel',
            options={'verbose_name': 'Status post', 'verbose_name_plural': 'Status posts'},
        ),
    ]