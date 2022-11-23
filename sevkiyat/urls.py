"""sevkiyat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from sevkiyatApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('accounts/',include('accounts.urls')),
    path('',views.index),
    path('sevkiyata-gonder/<int:id>',views.sevkiyataGonder),
    path('guncelle',views.guncelle),
    path('yolHaritasiKaydet',views.yolHaritasiKaydet),
    path('yolHaritasiListesi',views.yolHaritasiListesi),
    path('yolHaritasiListesi/incele/<int:id>',views.incele),
    path('yolHaritasiListesi/incele/<str:sepetAdi>',views.incele), 
    path('yolHaritasiListesi/isimDegistir/<int:id>',views.incele),    
    path('sevkiyattanCikar/<int:id>',views.sevkiyattanCikar),
    path('kayitSil/<int:id>',views.kayitSil),
    path('yolHaritasiAdiDegistir/',views.yolHaritasiAdiDegistir),
    path('yolHaritasiListesi/sil/<str:sepetAdi>',views.yhSil),
    path('yolHaritasiListesi/veriEkle/<str:sepetAdi>',views.veriEkle),
    path('yolHaritasiListesi/veriDegistir/<str:sepetAdi>',views.veriDegistir),
    path('tamamla/<int:id>',views.tamamla),

    path('ajax/addposition', views.addposition),
    path('ajax/miktarGonder', views.miktarGonder),
    path('ajax/adresGonder', views.adresGonder),

]
