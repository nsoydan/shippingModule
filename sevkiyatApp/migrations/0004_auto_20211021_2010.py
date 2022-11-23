# Generated by Django 3.2.8 on 2021-10-21 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sevkiyatApp', '0003_auto_20211021_1938'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guven_Siparis_List',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('siparisFisNo', models.CharField(blank=True, max_length=20, null=True)),
                ('siparisCinsi', models.CharField(blank=True, max_length=100, null=True)),
                ('siparisMiktari', models.FloatField(blank=True, null=True)),
                ('siparisStatusu', models.SmallIntegerField(blank=True, null=True)),
                ('siparisNotu', models.CharField(blank=True, max_length=100, null=True)),
                ('siparisDateTime', models.DateTimeField(blank=True, null=True)),
                ('siparisEden', models.CharField(blank=True, max_length=50, null=True)),
                ('birimFiyat', models.FloatField(blank=True, null=True)),
                ('cariAdi', models.CharField(blank=True, max_length=100, null=True)),
                ('cariKodu', models.CharField(blank=True, max_length=15, null=True)),
                ('cariAdresi', models.CharField(blank=True, max_length=200, null=True)),
                ('cariCity', models.CharField(blank=True, max_length=20, null=True)),
                ('cariTown', models.CharField(blank=True, max_length=30, null=True)),
                ('sevkiyatDateTime', models.DateTimeField(blank=True, null=True)),
                ('sevkiyatAdresi', models.CharField(blank=True, max_length=200, null=True)),
                ('sevkiyatCity', models.CharField(blank=True, max_length=20, null=True)),
                ('sevkiyatTown', models.CharField(blank=True, max_length=30, null=True)),
                ('sevkiyatMiktari', models.IntegerField(blank=True, null=True)),
                ('sevkiyatDurumu', models.CharField(blank=True, max_length=20, null=True)),
                ('yolHaritasiAdi', models.CharField(blank=True, max_length=100, null=True)),
                ('yolHaritasıYapan', models.CharField(blank=True, max_length=30, null=True)),
                ('positions', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mzd_Siparis_List',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('siparisFisNo', models.CharField(blank=True, max_length=20, null=True)),
                ('siparisCinsi', models.CharField(blank=True, max_length=100, null=True)),
                ('siparisMiktari', models.FloatField(blank=True, null=True)),
                ('siparisStatusu', models.SmallIntegerField(blank=True, null=True)),
                ('siparisNotu', models.CharField(blank=True, max_length=100, null=True)),
                ('siparisDateTime', models.DateTimeField(blank=True, null=True)),
                ('siparisEden', models.CharField(blank=True, max_length=50, null=True)),
                ('birimFiyat', models.FloatField(blank=True, null=True)),
                ('cariAdi', models.CharField(blank=True, max_length=100, null=True)),
                ('cariKodu', models.CharField(blank=True, max_length=15, null=True)),
                ('cariAdresi', models.CharField(blank=True, max_length=200, null=True)),
                ('cariCity', models.CharField(blank=True, max_length=20, null=True)),
                ('cariTown', models.CharField(blank=True, max_length=30, null=True)),
                ('sevkiyatDateTime', models.DateTimeField(blank=True, null=True)),
                ('sevkiyatAdresi', models.CharField(blank=True, max_length=200, null=True)),
                ('sevkiyatCity', models.CharField(blank=True, max_length=20, null=True)),
                ('sevkiyatTown', models.CharField(blank=True, max_length=30, null=True)),
                ('sevkiyatMiktari', models.IntegerField(blank=True, null=True)),
                ('sevkiyatDurumu', models.CharField(blank=True, max_length=20, null=True)),
                ('yolHaritasiAdi', models.CharField(blank=True, max_length=100, null=True)),
                ('yolHaritasıYapan', models.CharField(blank=True, max_length=30, null=True)),
                ('positions', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Siparis_List',
        ),
    ]