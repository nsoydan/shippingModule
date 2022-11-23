# Generated by Django 3.2.8 on 2021-10-26 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sevkiyatApp', '0006_auto_20211025_1700'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mzd_Sevkiyat_Sepeti',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sepetAdi', models.CharField(blank=True, max_length=100, null=True)),
                ('sepetNotu', models.CharField(blank=True, max_length=1000, null=True)),
                ('sepetiOlusturan', models.CharField(blank=True, max_length=100, null=True)),
                ('dokmeToplami', models.IntegerField(blank=True, null=True)),
                ('sevkiyatSepetiKayitTarihSaat', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Sevkiyat_Sepeti',
            new_name='Guven_Sevkiyat_Sepeti',
        ),
    ]