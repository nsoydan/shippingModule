# Generated by Django 3.2.8 on 2021-10-21 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sevkiyatApp', '0002_siparis_list_positions'),
    ]

    operations = [
        migrations.AddField(
            model_name='siparis_list',
            name='cariAdresi',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='siparis_list',
            name='cariCity',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='siparis_list',
            name='cariTown',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]