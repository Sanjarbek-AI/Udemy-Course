# Generated by Django 3.2.7 on 2021-10-01 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('updates', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updatemodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='updates'),
        ),
    ]