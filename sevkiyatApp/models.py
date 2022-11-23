from django.db import models

# Create your models here.


class Gelen_Tablosu(models.Model):
    id=models.AutoField(primary_key=True)
    gelenfisNo=models.CharField(max_length=20,null=True,blank=True)
    
    def __str__(self):
        return self.gelenfisNo



class Guven_Siparis_List(models.Model):
    id=models.AutoField(primary_key=True)
    siparisFisNo=models.CharField(max_length=20,null=True,blank=True)
    siparisCinsi=models.CharField(max_length=100,null=True,blank=True)
    siparisMiktari=models.FloatField(blank=True,null=True)
    siparisStatusu=models.SmallIntegerField(blank=True,null=True)
    siparisNotu=models.CharField(max_length=100,null=True,blank=True)
    siparisNotu2=models.CharField(max_length=100,null=True,blank=True)
    siparisDateTime=models.DateTimeField(null=True,blank=True)
    siparisEden=models.CharField(max_length=50,null=True,blank=True)
    birimFiyat=models.FloatField(null=True,blank=True)
    cariAdi=models.CharField(max_length=100,null=True,blank=True)
    cariKodu=models.CharField(max_length=15,null=True,blank=True)
    cariAdresi=models.CharField(max_length=200,null=True,blank=True)
    cariCity=models.CharField(max_length=20,null=True,blank=True)
    cariTown=models.CharField(max_length=30,null=True,blank=True)
    fabrikaKodu=models.CharField(max_length=30,null=True,blank=True)
    sevkiyatDateTime=models.DateTimeField(null=True,blank=True)
    sevkiyatAdresi=models.CharField(max_length=200,null=True,blank=True)
    sevkiyatCity=models.CharField(max_length=20,null=True,blank=True)
    sevkiyatTown=models.CharField(max_length=30,null=True,blank=True)
    sevkiyatMiktari=models.IntegerField(null=True,blank=True)
    sevkiyatDurumu=models.CharField(default=" ", max_length=20,null=True,blank=True)
    yolHaritasiAdi=models.CharField(max_length=100,null=True,blank=True)
    yolHaritasıYapan=models.CharField(max_length=30,null=True,blank=True)
    positions=models.IntegerField(null=True,blank=True)
    guncellendi=models.BooleanField(null=True,blank=True)
    guncellenmeTarihSaati=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    siparisİzlemeNo=models.CharField(max_length=500,blank=True,null=True)
    makbuzNo=models.CharField(max_length=50,blank=True,null=True)
    verilenMiktar=models.IntegerField(null=True,blank=True)
    makbuzTarihi=models.DateField(null=True,blank=True)
    ilgili=models.CharField(max_length=50,blank=True,null=True)
    tel1=models.CharField(max_length=12,blank=True,null=True)
    tel2=models.CharField(max_length=12,blank=True,null=True)

    def __str__(self):
        return self.siparisFisNo



class Mzd_Siparis_List(models.Model):
    id=models.AutoField(primary_key=True)
    siparisFisNo=models.CharField(max_length=20,null=True,blank=True)
    siparisCinsi=models.CharField(max_length=100,null=True,blank=True)
    siparisMiktari=models.FloatField(blank=True,null=True)
    siparisStatusu=models.SmallIntegerField(blank=True,null=True)
    siparisNotu=models.CharField(max_length=100,null=True,blank=True)
    siparisDateTime=models.DateTimeField(null=True,blank=True)
    siparisEden=models.CharField(max_length=50,null=True,blank=True)
    birimFiyat=models.FloatField(null=True,blank=True)
    cariAdi=models.CharField(max_length=100,null=True,blank=True)
    cariKodu=models.CharField(max_length=15,null=True,blank=True)
    cariAdresi=models.CharField(max_length=200,null=True,blank=True)
    cariCity=models.CharField(max_length=20,null=True,blank=True)
    cariTown=models.CharField(max_length=30,null=True,blank=True)

    sevkiyatDateTime=models.DateTimeField(null=True,blank=True)
    sevkiyatAdresi=models.CharField(max_length=200,null=True,blank=True)
    sevkiyatCity=models.CharField(max_length=20,null=True,blank=True)
    sevkiyatTown=models.CharField(max_length=30,null=True,blank=True)
    sevkiyatMiktari=models.IntegerField(null=True,blank=True)
    sevkiyatDurumu=models.CharField(default="Siparişte",max_length=20,null=True,blank=True)
    yolHaritasiAdi=models.CharField(max_length=100,null=True,blank=True)
    yolHaritasıYapan=models.CharField(max_length=30,null=True,blank=True)
    positions=models.IntegerField(null=True,blank=True)
    def __str__(self):
        return self.siparisFisNo



class Guven_Sevkiyat_Sepeti(models.Model):
    id=models.AutoField(primary_key=True)
    sepetAdi=models.CharField(max_length=100,null=True,blank=True)
    sepetNotu=models.CharField(max_length=1000,null=True,blank=True)
    sepetiOlusturan=models.CharField(max_length=100,null=True,blank=True)
    dokmeToplami=models.IntegerField(null=True,blank=True)
    sevkiyatSepetiKayitTarihSaat=models.DateTimeField(auto_now_add=True)
    yuklenen=models.IntegerField(null=True,blank=True)
    dagitilan=models.IntegerField(null=True,blank=True)
    cikisKm=models.IntegerField(null=True,blank=True)
    donusKm=models.IntegerField(null=True,blank=True)
    alinanYakit=models.FloatField(null=True,blank=True)
    alinanAdblue=models.IntegerField(null=True,blank=True)
    dokmeToplami=models.IntegerField(null=True,blank=True)
    yakitTutari=models.FloatField(null=True,blank=True)
    surucu=models.CharField(max_length=30,null=True,blank=True)
    gidisTarihi=models.DateTimeField(null=True,blank=True)
    donusTarihi=models.DateTimeField(null=True,blank=True)
    fark=models.IntegerField(null=True,blank=True)
    mazotYuzdesi=models.FloatField(null=True,blank=True)
    yapilanKm=models.IntegerField(null=True,blank=True)
    # donusRaporu=models.ImageField(blank=True, upload_to='donusRaporu/%Y/%m/%d/')    

    def __str__(self):
        return self.sepetAdi


class Mzd_Sevkiyat_Sepeti(models.Model):
    id=models.AutoField(primary_key=True)
    sepetAdi=models.CharField(max_length=100,null=True,blank=True)
    sepetNotu=models.CharField(max_length=1000,null=True,blank=True)
    sepetiOlusturan=models.CharField(max_length=100,null=True,blank=True)
    dokmeToplami=models.IntegerField(null=True,blank=True)
    sevkiyatSepetiKayitTarihSaat=models.DateTimeField(auto_now_add=True)
   
    #donusRaporu=models.ImageField(blank=True, upload_to='donusRaporu/%Y/%m/%d/')    

    def __str__(self):
        return self.sepetAdi