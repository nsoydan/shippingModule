# Generated by Django 3.2.8 on 2021-10-21 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sevkiyatApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='siparis_list',
            name='positions',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
