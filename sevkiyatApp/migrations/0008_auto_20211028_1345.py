# Generated by Django 3.2.8 on 2021-10-28 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sevkiyatApp', '0007_auto_20211026_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guven_siparis_list',
            name='sevkiyatDurumu',
            field=models.CharField(blank=True, default='Siparişte', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='mzd_siparis_list',
            name='sevkiyatDurumu',
            field=models.CharField(blank=True, default='Siparişte', max_length=20, null=True),
        ),
    ]
