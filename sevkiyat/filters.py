from django.db.models.fields import CharField
import django_filters
from sevkiyatApp.models import Guven_Siparis_List 
from django_filters import CharFilter,ChoiceFilter,DateFilter,NumberFilter
from django import forms



#fabrika_CHOICES=(
#    ("Güven Anadolu",'Güven Anadolu'),
#    ("MZD",'MZD'),
#    ("Amasya",'Amasya'),
#    ("Hadımköy",'Hadımköy'),
#)



siparisEden_CHOICES=(
    ("İ.TORUN",'İlkyaz Torun'),
    ("A.ÖLMEZ",'Ali Ölmez'),
    ("M.DEMİR",'Muharrem Demir'),
    ("Ş.EVCİL",'Şakir Evcil'),
    
    ("M.BULUT",'Müslüm Bulut'),
   
    
    ("Verdi Demir",'Verdi Demir'),
    ("Erdal Hatım",'Erdal Hatım'),
    ("K.HOZAN",'Kerim Hozan'),
    ("MARMARA",'Zeydan Demir'),
    ("Nurcan Demir",'Nurcan Demir'),
    ("Kemal Yıldız",'Kemal Yıldız'),
    ("Tuba Demir",'Tuba Demir'),
    ("A.KILIÇ",'Alper Kılıç'),
)

sevkiyatDurumu_CHOICES=(
    ("Sevkiyatta",'Sevkiyatta'),
    ("Siparişte",'Siparişte'),
    ("Öneride",'Öneride'),
    ("Tamamlandı",'Tamamlandı'),
    ("Reddedildi",'Reddedildi'),
    
) 

fabrikaKodu_CHOICES=(
    ("GÜVENDEN",'GÜVEN'),
    ("MZDDEN",'MZD'),
    ("SULUOVADAN",'SULUOVA'),
    ("HADIMKÖYDE",'HADIMKÖY'),
) 

class ListFilter(django_filters.FilterSet):
    siparisFisNo=CharFilter(field_name='siparisFisNo', lookup_expr='icontains', label='Sipariş Fiş No')
    makbuzNo=CharFilter(field_name='makbuzNo', lookup_expr='icontains', label='Tes. Mak. No')
    cariKodu=CharFilter(field_name='cariKodu', lookup_expr='icontains', label='Cari Kodu')
    cariAdi=CharFilter(field_name='cariAdi', lookup_expr='icontains', label='Cari Adı')
    siparisCinsi=CharFilter(field_name='siparisCinsi', lookup_expr='icontains', label='Ürün')
    siparisMiktari=CharFilter(field_name='siparisMiktari', lookup_expr='icontains', label='Miktar')
    siparisNotu=CharFilter(field_name='siparisNotu', lookup_expr='icontains', label='Sipariş Notu')
    siparisEden=ChoiceFilter(choices=siparisEden_CHOICES,label='Saha Müdürü')
    sevkiyatCity=CharFilter(field_name='sevkiyatCity', lookup_expr='icontains', label='İl')
    sevkiyatTown=CharFilter(field_name='sevkiyatTown', lookup_expr='icontains', label='İlçe')
    sevkiyatDurumu=ChoiceFilter(choices=sevkiyatDurumu_CHOICES,label='Durumu')
    sevkiyatAdresi=CharFilter(field_name='sevkiyatAdresi',lookup_expr='icontains',label='Sevkiyat Adresi')
    yolHaritasiAdi=CharFilter(field_name='yolHaritasiAdi',lookup_expr='icontains',label='Yol Haritası')
    fabrikaKodu=ChoiceFilter(choices=fabrikaKodu_CHOICES,label='Fabrika')
    #kdvDurumu=ChoiceFilter(choices=kdvDurumu_CHOICES,label='Kdv')    
    #firmaSehir=CharFilter(field_name='firmaSehir', lookup_expr='icontains', label='Şehir')   
    start_date= DateFilter(field_name='siparisDateTime',lookup_expr=('gte'),widget=forms.DateInput(attrs={'type':'date'}),label='Sipariş İlk Tarih')
    end_date= DateFilter(field_name='siparisDateTime',lookup_expr=('lte'),widget=forms.DateInput(attrs={'type':'date'}),label='Sipariş Son Tarih') 
    
    class Meta:
        model=Guven_Siparis_List
        fields=['siparisFisNo','cariKodu','cariAdi','siparisCinsi','siparisMiktari','siparisNotu','siparisEden','cariCity','cariTown','siparisDateTime']  