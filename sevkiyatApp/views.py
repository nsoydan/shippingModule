from re import S
from django.http.response import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from sevkiyatApp.models import Gelen_Tablosu, Guven_Siparis_List,Mzd_Siparis_List,Guven_Sevkiyat_Sepeti,Mzd_Sevkiyat_Sepeti,Gelen_Tablosu
from django.contrib.auth.decorators import login_required
from django.db.models import Sum,Q
import pyodbc
from sevkiyat.filters import ListFilter
from datetime import date, datetime,timedelta

import json
@login_required
def guncelle(request):
    Gelen_Tablosu.objects.all().exclude(id=1).delete()







    #####        GÜVENE VERİLEN SİPARİŞLERİ ÇEKMEK İÇİN     ##################################

       

    siparisler=Guven_Siparis_List.objects.all()

    conn=pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                        'Server=ANADOLUSERVER;'
                        'Database=LOGODB;'
                        'UID=sa;'
                        'PWD=Vega1234;'
                        'Trusted_Connection=No;')

    cursor=conn.cursor()                        #0                  1                       2                       3                           4                   5                       6                           7                8                      9                   10                     11                12                  13                14                        15                         16                      17                          18                         19                         20                         21                  22                                  23                         24                      25                      26                         27                                                                                                                                
    cursor.execute ('SELECT LG_001_01_ORFICHE.FICHENO,LG_001_ITEMS.NAME,LG_001_01_ORFLINE.AMOUNT,LG_001_01_ORFICHE.GENEXP1,LG_001_01_ORFICHE.DATE_,LG_001_CLCARD.SPECODE,LG_001_01_ORFLINE.PRICE,LG_001_CLCARD.DEFINITION2,LG_001_CLCARD.CODE,LG_001_SHIPINFO.ADDR1,LG_001_SHIPINFO.CITY,LG_001_SHIPINFO.TOWN,LG_001_CLCARD.ADDR1,LG_001_CLCARD.CITY,LG_001_CLCARD.TOWN,LG_001_01_ORFLINE.LINEEXP,LG_001_01_ORFICHE.SPECODE,LG_001_01_ORFLINE.STATUS,LG_001_01_ORFLINE.SHIPPEDAMOUNT,LG_001_01_ORFLINE.LINEEXP,LG_001_01_ORFICHE.GENEXP2,LG_001_01_ORFICHE.GENEXP3,LG_001_01_ORFICHE.DOCTRACKINGNR,LG_001_SHIPINFO.INCHANGE,LG_001_SHIPINFO.TELNRS1,LG_001_SHIPINFO.TELNRS2,LG_001_01_ORFICHE.GENEXP4,LG_001_01_ORFICHE.GENEXP5 FROM LG_001_01_ORFLINE LEFT JOIN LG_001_ITEMS ON LG_001_01_ORFLINE.STOCKREF = LG_001_ITEMS.LOGICALREF LEFT JOIN LG_001_CLCARD ON LG_001_01_ORFLINE.CLIENTREF = LG_001_CLCARD.LOGICALREF LEFT JOIN LG_001_01_ORFICHE ON LG_001_01_ORFLINE.ORDFICHEREF = LG_001_01_ORFICHE.LOGICALREF LEFT JOIN LG_001_SHIPINFO ON LG_001_01_ORFLINE.CLIENTREF=LG_001_SHIPINFO.CLIENTREF WHERE (((LG_001_01_ORFLINE.STATUS=4 OR LG_001_01_ORFLINE.STATUS=1) AND LG_001_01_ORFLINE.SHIPPEDAMOUNT =0 AND LG_001_01_ORFLINE.CLOSED=0) OR LG_001_01_ORFLINE.STATUS=2)  ORDER BY LG_001_01_ORFICHE.FICHENO')


    
    for row in cursor:
       
        #print("------------------")
        #print(date.today)
        #print("Fiş no",row[0])
        #print("amount :",row[2])
        #print("shippedamount : ",row[18])
        if row[17] ==4:
            sevkiyatDurumu="Siparişte"
        if row[17] ==1:
            sevkiyatDurumu="Öneride"
        if row[17] ==2:
            sevkiyatDurumu="Reddedildi" 

        obj=Guven_Siparis_List( siparisFisNo='GVN'+row[0],
                                siparisCinsi=row[1],
                                siparisMiktari=row[2],
                                siparisNotu=row[3]+' '+row[20]+' '+row[21]+' '+row[26]+' '+row[27],
                                siparisDateTime=row[4],
                                siparisEden=row[5],
                                birimFiyat=row[6],
                                cariAdi=row[7],
                                cariKodu=row[8],
                                sevkiyatAdresi=row[9],
                                sevkiyatCity=row[10],
                                sevkiyatTown=row[11],
                                cariAdresi=row[12],
                                cariCity=row[13],
                                cariTown=row[14],
                                siparisNotu2=row[15],
                                fabrikaKodu=row[16],
                                siparisStatusu=row[17],
                                siparisİzlemeNo=row[22],
                                ilgili=row[23],
                                tel1=row[24],
                                tel2=row[25],
                                sevkiyatDurumu=sevkiyatDurumu            ###### GÜVENE VERİLEN SİPARİŞLER  #######                    
                       )
       
        

        
        for s in Guven_Siparis_List.objects.all():
            kayit2=False
            if ('GVN'+row[0]) == s.siparisFisNo and row[1] == s.siparisCinsi:     # gelen kayıt veritabanında varsa
                #print("Bu kayıt var: GVN", row[0]  )
                Guven_Siparis_List.objects.filter(siparisFisNo=('GVN'+row[0]),siparisCinsi=row[1]).update(siparisMiktari=row[2])
                Guven_Siparis_List.objects.filter(siparisFisNo=('GVN'+row[0])).update(siparisNotu=row[3]+' '+row[20]+' '+row[21]+' '+row[26]+' '+row[27]+' '+row[19])
                Guven_Siparis_List.objects.filter(siparisFisNo=('GVN'+row[0])).update(fabrikaKodu=row[16])
                Guven_Siparis_List.objects.filter(siparisFisNo=('GVN'+row[0])).update(sevkiyatAdresi=row[9])
                Guven_Siparis_List.objects.filter(siparisFisNo=('GVN'+row[0])).update(tel1=row[24])
                
                
                if row[17] == s.siparisStatusu:   # veritabanındaki sipariş statüsü ile gelen sipariş statüsü aynı ise:
                    if row[18]==0:                # sevkedilmiş miktar sıfır ise:
                        #print("bu kayıt var................",s.siparisFisNo)
                        
                        kayit2=False
                        break
                    else:                       # sEVKEDİLMİŞ MİKTAR SIFIRDAN FARKLI İSE, FATURA KESİLMİŞ İSE:
                        #Guven_Siparis_List.objects.filter(siparisFisNo=('GVN'+row[0])).update(sevkiyatDurumu="Faturalandı")
                        kayit2=False
                        break
                else:                           # VERİTABANINDAKİ SİPARİŞ STATÜSÜ GELEN STATÜDEN FARKLI İSE:
                    if row[17] == 4:            # GELEN STATÜ ONAYLANDI İSE 
                        Guven_Siparis_List.objects.filter(siparisFisNo=('GVN'+row[0])).update(siparisStatusu=row[17])
                        Guven_Siparis_List.objects.filter(siparisFisNo=('GVN'+row[0])).update(sevkiyatDurumu="Siparişte")
                        #print("kayit güncellendiiiii....siparişe çekildi...........",row[0])
                        kayit2=False
                        break 
                    if row[17] == 1:            #GELEN STATÜ ÖNERİ İSE
                        Guven_Siparis_List.objects.filter(siparisFisNo=('GVN'+row[0])).update(siparisStatusu=row[17])
                        Guven_Siparis_List.objects.filter(siparisFisNo=('GVN'+row[0])).update(sevkiyatDurumu="Öneri")
                        #print("kayit güncellendiiiii....öneriye çekildi...........",row[0])
                        kayit2=False
                        break
                    if row[17] == 2:            #GELEN STATÜ RED İSE
                        Guven_Siparis_List.objects.filter(siparisFisNo=('GVN'+row[0])).update(siparisStatusu=row[17])
                        Guven_Siparis_List.objects.filter(siparisFisNo=('GVN'+row[0])).update(sevkiyatDurumu="Reddedildi")
                        #print("kayit güncellendiiiii....RED RED RED  çekildi...........",row[0])
                        kayit2=False
                        break 
            else:
                #print("bu kayıt veri tabanında yok",row[0])       # gelen kayıt veritabanında yoksa
                if row[18]==0:
                    kayit2=True
                    
           
        if kayit2:
            #print("yeni kayıt eklendi...:",('GVN'+row[0]))
            kayit2=False
            obj.save()  
      
   

################ #####        MZD YE VERİLEN SİPARİŞLERİ ÇEKMEK İÇİN     ##################################

    conn=pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                        'Server=ANADOLUSERVER;'
                        'Database=LOGODB;'
                        'UID=sa;'
                        'PWD=Vega1234;'
                        'Trusted_Connection=No;')

    cursor=conn.cursor()                   #0                               1                       2                           3                       4                   5                         6                        7                   8                    9                   10                  11                      12               13                  14                       15                     16                     17                        18                        19                        20                          21                22                                 23                           24                                               
    cursor.execute ('SELECT LG_002_01_ORFICHE.FICHENO,LG_002_ITEMS.NAME,LG_002_01_ORFLINE.AMOUNT,LG_002_01_ORFICHE.GENEXP1,LG_002_01_ORFICHE.DATE_,LG_002_CLCARD.SPECODE,LG_002_01_ORFLINE.PRICE,LG_002_CLCARD.DEFINITION_,LG_002_CLCARD.CODE,LG_002_SHIPINFO.ADDR1,LG_002_SHIPINFO.CITY,LG_002_SHIPINFO.TOWN,LG_002_CLCARD.ADDR1,LG_002_CLCARD.CITY,LG_002_CLCARD.TOWN,LG_002_01_ORFLINE.LINEEXP,LG_002_01_ORFICHE.SPECODE,LG_002_01_ORFLINE.STATUS,LG_002_01_ORFLINE.SHIPPEDAMOUNT,LG_002_01_ORFLINE.LINEEXP,LG_002_01_ORFICHE.GENEXP2,LG_002_01_ORFICHE.GENEXP3,LG_002_01_ORFICHE.DOCTRACKINGNR,LG_002_01_ORFICHE.GENEXP4,LG_002_01_ORFICHE.GENEXP5 FROM LG_002_01_ORFLINE LEFT JOIN LG_002_ITEMS ON LG_002_01_ORFLINE.STOCKREF = LG_002_ITEMS.LOGICALREF LEFT JOIN LG_002_CLCARD ON LG_002_01_ORFLINE.CLIENTREF = LG_002_CLCARD.LOGICALREF LEFT JOIN LG_002_01_ORFICHE ON LG_002_01_ORFLINE.ORDFICHEREF = LG_002_01_ORFICHE.LOGICALREF LEFT JOIN LG_002_SHIPINFO ON LG_002_01_ORFLINE.CLIENTREF=LG_002_SHIPINFO.CLIENTREF WHERE (((LG_002_01_ORFLINE.STATUS=4 OR LG_002_01_ORFLINE.STATUS=1)  AND LG_002_01_ORFLINE.SHIPPEDAMOUNT=0) OR LG_002_01_ORFLINE.STATUS=2) ORDER BY LG_002_01_ORFICHE.FICHENO')

    for row in cursor:
        kayit1=False
        if row[17] ==4:
            sevkiyatDurumu="Siparişte"
        if row[17] ==1:
            sevkiyatDurumu="Öneride"
        if row[17] ==2:
            sevkiyatDurumu="Reddedildi" 


        obj=Guven_Siparis_List( siparisFisNo='MZD'+str(row[0]),
                                siparisCinsi=row[1],
                                siparisMiktari=row[2],
                                siparisNotu=str(row[3])+' '+str(row[20])+' '+str(row[21])+' '+str(row[23])+' '+str(row[24])+' '+str(row[19]),
                                siparisDateTime=row[4],
                                siparisEden=row[5],
                                birimFiyat=row[6],
                                cariAdi=row[7],                         #### MZD nin gelen siparişler
                                cariKodu=row[8],
                                sevkiyatAdresi=row[9],
                                sevkiyatCity=row[10],
                                sevkiyatTown=row[11],
                                cariAdresi=row[12],
                                cariCity=row[13],
                                cariTown=row[14],
                                siparisNotu2=row[15],
                                fabrikaKodu=row[16],
                                sevkiyatDurumu=sevkiyatDurumu,
                                siparisStatusu=row[17],
                                siparisİzlemeNo=row[22] 
                           ) 

       
        for s in Guven_Siparis_List.objects.all():
            kayit1=False
            if 'MZD'+str(row[0]) == s.siparisFisNo  and row[1] == s.siparisCinsi:     # gelen kayıt veritabanında varsa
                Guven_Siparis_List.objects.filter(siparisFisNo=('MZD'+str(row[0]))).update(siparisMiktari=row[2]) #Gelen siparis miktarını güncelle
                                

                if row[17] == s.siparisStatusu:  # veritabanındaki sipariş statüsü ile gelen sipariş statüsü aynı ise:
                    if row[18]==0:              # sevkedilmiş miktar sıfır ise:
                        #print("bu kayıt var................",s.siparisFisNo)
                        kayit1=False
                        break
                    else:
                        #Guven_Siparis_List.objects.filter(siparisFisNo=('MZD'+row[0])).update(sevkiyatDurumu="Faturalandı")
                        kayit1=False
                        break
                else:
                    if row[17] == 4:
                        Guven_Siparis_List.objects.filter(siparisFisNo=('MZD'+row[0])).update(siparisStatusu=row[17])
                        Guven_Siparis_List.objects.filter(siparisFisNo=('MZD'+row[0])).update(sevkiyatDurumu="Siparişte")
                        #print("kayit güncellendiiiii...............",row[0])
                        kayit1=False
                        break 
                    if row[17] == 1:
                        Guven_Siparis_List.objects.filter(siparisFisNo=('MZD'+row[0])).update(siparisStatusu=row[17])
                        Guven_Siparis_List.objects.filter(siparisFisNo=('MZD'+row[0])).update(sevkiyatDurumu="Öneride")
                        #print("kayit güncellendiiiii...............",row[0])
                        kayit1=False
                        break 
                    if row[17] == 2:
                        Guven_Siparis_List.objects.filter(siparisFisNo=('MZD'+row[0])).update(siparisStatusu=row[17])
                        Guven_Siparis_List.objects.filter(siparisFisNo=('MZD'+row[0])).update(sevkiyatDurumu="Reddedildi")
                        #print("kayit güncellendiiiii...............",row[0])
                        kayit1=False
                        break         
            else:       # gelen kayıt veritabanında yoksa
               
                if row[18]==0:
                    kayit1=True
           
        if kayit1:
            kayit1=False
            obj.save()  
      
   

    return redirect(index)           

# Create your views here.
@login_required
def index(request):
    

    
    sepets=Guven_Sevkiyat_Sepeti.objects.filter(sepetiOlusturan=request.user.first_name).order_by('-id')   
    q1=Guven_Siparis_List.objects.all().order_by('-id').exclude(id=1)
    
    myFilter=ListFilter(request.GET,queryset=q1)
    sipariss=myFilter.qs
    if date.today().day == 25 :
        if datetime.now().hour == 11: 
            return redirect(index)
    YHs=Guven_Sevkiyat_Sepeti.objects.filter(sevkiyatSepetiKayitTarihSaat__gt=(date.today()-timedelta(days=7)))
    

    context={
        'sipariss':sipariss,
        'sepets':sepets,
        'myFilter':myFilter,
        'YHs':YHs,
    }
    return render(request,'siparisListesiSevkiyat.html',context)

@login_required
def sevkiyataGonder(request,id):
    url=request.META.get('HTTP_REFERER')
    gelenSepetId = request.POST.get('sepetAdi')
    hiddenid=request.POST.get('hiddenid')
    firma=request.user.last_name

 
    if not gelenSepetId:
        hataMesaji="Yol haritası adı giriniz."
        context={
                'hataMesaji':hataMesaji,
            }
        return render(request,'hata.html',context)

    todo = get_object_or_404(Guven_Siparis_List,id=id)
    todo.sevkiyatDurumu = 'Sevkiyatta'
    obj=get_object_or_404(Guven_Sevkiyat_Sepeti,id=gelenSepetId)
    todo.yolHaritasiAdi=obj.sepetAdi
    
    
   

    #obj = Guven_Sevkiyat_Sepeti.objects.get(sepetAdi=gelenSepetAdi) #Gelen sepet adi ile bir sepet var mı? 


    

    if todo.siparisCinsi == "DÖKME ADBLUE":                         #Eğer gönderilen Dökme ise ekle
        obj.dokmeToplami=obj.dokmeToplami+todo.siparisMiktari

        
    obj.save()
    todo.save()


    
    return redirect(url)




@login_required
def yolHaritasiKaydet(request):
    yolHaritasiAdi = request.POST.get('yolHaritasiAdi')
    sepets=Guven_Sevkiyat_Sepeti.objects.all()
    for sepet in sepets:
        if sepet.sepetAdi == yolHaritasiAdi:
            hataMesaji="Bu Yol Haritası adı mevcut.Başka bir isim seçiniz..."
            context={
                'hataMesaji':hataMesaji,
            }
            return render(request,'hata.html',context)
       
  
    obj= Guven_Sevkiyat_Sepeti(sepetAdi=yolHaritasiAdi,
                            dokmeToplami=0,
                            sepetiOlusturan=request.user.first_name,
                            )
    obj.save()

    print(yolHaritasiAdi)
    return redirect(index)

@login_required
def yolHaritasiListesi(request):    
 
    
    yhs=Guven_Sevkiyat_Sepeti.objects.filter(sepetiOlusturan=request.user.first_name).order_by('-id')
    
    context={
        'yhs':yhs,
    }

    return render(request,'yolHaritasiListesi.html',context)


@login_required
def sevkiyattanCikar(request,id):
    url=request.META.get('HTTP_REFERER')
    obj=get_object_or_404(Guven_Siparis_List, id=id)
    sepet=get_object_or_404(Guven_Sevkiyat_Sepeti,sepetAdi=obj.yolHaritasiAdi)
    #sepet=Sevkiyat_Sepeti.objects.get(sepetAdi=obj.sepet.sepetAdi)
    
    if obj.siparisCinsi == "DÖKME ADBLUE":
        sepet.dokmeToplami=sepet.dokmeToplami - obj.siparisMiktari
    
    #print(sepet)
    #print("-----------")
    if obj.sevkiyatDurumu=="Sevkiyatta":    
        if obj.siparisStatusu == 4: 
                obj.sevkiyatDurumu="Siparişte"
        if obj.siparisStatusu == 1: 
                obj.sevkiyatDurumu="Öneride"        
    
    
    obj.yolHaritasiAdi=None
    sepet.save()
    obj.save()

    return redirect(url)


@login_required
def incele(request,id):
    print(".............................................")
    print(id)
    obj=get_object_or_404(Guven_Sevkiyat_Sepeti, id=id)
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<")
    sepetAdi=obj.sepetAdi
    #for s in Guven_Siparis_List.objects.filter(yolHaritasiAdi=sepetAdi):
    #    if s.makbuzNo != 0:
    #        s.positions=s.makbuzNo
    #        s.save() 
    q1=Guven_Siparis_List.objects.filter(yolHaritasiAdi=sepetAdi,sevkiyatDurumu="Tamamlandı")
    if q1.exists():
        sipariss= Guven_Siparis_List.objects.filter(yolHaritasiAdi=sepetAdi).order_by('makbuzNo')
    else:
        sipariss= Guven_Siparis_List.objects.filter(yolHaritasiAdi=sepetAdi).order_by('positions')
      
    #sipariss= Guven_Siparis_List.objects.filter(yolHaritasiAdi=sepetAdi).order_by('positions')
    
    totalSevkiyatMiktari=Guven_Siparis_List.objects.filter(siparisCinsi='DÖKME ADBLUE',yolHaritasiAdi=sepetAdi).aggregate(Sum('sevkiyatMiktari'))
    totalSiparisMiktari=Guven_Siparis_List.objects.filter(siparisCinsi='DÖKME ADBLUE',yolHaritasiAdi=sepetAdi).aggregate(Sum('siparisMiktari'))
    totalVerilenMiktar=Guven_Siparis_List.objects.filter(siparisCinsi='DÖKME ADBLUE',yolHaritasiAdi=sepetAdi).aggregate(Sum('verilenMiktar'))
    sepet=Guven_Sevkiyat_Sepeti.objects.filter(sepetAdi=sepetAdi)
    
    
        
    context={
        'sipariss':sipariss,
        'surucu':sepet[0].surucu,
        'yuklenen':sepet[0].yuklenen,
        'dagitilan':sepet[0].dagitilan,
        'fark':sepet[0].fark,
        'cikisKm':sepet[0].cikisKm,
        'donusKm':sepet[0].donusKm,
        'yapilanKm':sepet[0].yapilanKm,
        'mazotYuzdesi':sepet[0].mazotYuzdesi,
        'alinanYakit':sepet[0].alinanYakit,
        'alinanAdblue':sepet[0].alinanAdblue,
        'yakitTutari':sepet[0].yakitTutari,
        'gidisTarihi':sepet[0].gidisTarihi,
        'donusTarihi':sepet[0].donusTarihi,
       
        
        

        'sepetAdi':sepetAdi,
        'totalSevkiyatMiktari':totalSevkiyatMiktari,
        'totalSiparisMiktari':totalSiparisMiktari,
        'totalVerilenMiktar':totalVerilenMiktar,
    }
    
    return render(request,'incele.html',context)


@login_required
def addposition(request):
    positions=request.POST.get('positions')
    updated=request.POST.get('updated')
    #depos=Depo.objects.filter(firma__firmaAdi=firmaAdi)
    data=json.loads(positions)
    #print(positions)
    #print(positions[0])
    
    for row in (data['positions']):
        if row[0] != None:
            print(row[0])
            print(row[2])
            obj=get_object_or_404(Guven_Siparis_List,id=row[0])
            print(obj.cariAdi)
            obj.positions=row[2]
            obj.save()
    
    print("add positions un içindeyiz")
    print("---------------------")
    
    return HttpResponse(status=200)



@login_required
def kayitSil(request,id):
    url=request.META.get('HTTP_REFERER')
    obj=get_object_or_404(Guven_Siparis_List, id=id)
    
    obj.delete()

    return redirect(url)


@login_required
def miktarGonder(request):
    value=request.POST.get('value')
    id=request.POST.get('id')
    print(id,value)
    obj=get_object_or_404(Guven_Siparis_List, id=id)
    print("eski sevkiyatMiktari değeri : ", obj.sevkiyatMiktari)
    obj.sevkiyatMiktari=value
    print("yeni sevkiyatMiktari değeri : ", value)
    obj.save()
    return HttpResponse(status=200)

    
@login_required
def adresGonder(request):
    adres=request.POST.get('value')
    id=request.POST.get('id')
    print(id,adres)
    obj=get_object_or_404(Guven_Siparis_List, id=id)
    print("eski sevkiyatadresi değeri : ", obj.sevkiyatAdresi)
    obj.sevkiyatAdresi=adres
    print("yeni sevkiyatadresi değeri : ", adres)
    obj.save()
    return HttpResponse(status=200)


    
@login_required
def yolHaritasiAdiDegistir(request):
    url=request.META.get('HTTP_REFERER')
    yeniAd=request.POST.get('yeniAd')
    eskiAd=request.POST.get('eskiAd')
    
    if not yeniAd:
        html= "<html><body><h1>HATA: Yeni ismi girmelisiniz...</h1></body></html>"
        return HttpResponse(html)

    print(yeniAd)
    Guven_Siparis_List.objects.filter(yolHaritasiAdi=eskiAd).update(yolHaritasiAdi=yeniAd)
    Guven_Sevkiyat_Sepeti.objects.filter(sepetAdi=eskiAd).update(sepetAdi=yeniAd)



    return redirect(url)

       
@login_required
def yhSil(request,sepetAdi):
    url=request.META.get('HTTP_REFERER')
    print(sepetAdi)
    print(Guven_Siparis_List.objects.filter(yolHaritasiAdi=sepetAdi))
    
    if not Guven_Siparis_List.objects.filter(yolHaritasiAdi=sepetAdi):
        obj=get_object_or_404(Guven_Sevkiyat_Sepeti,sepetAdi=sepetAdi)
        obj.delete()
    else:
        html= "<html><body><h1>HATA: Yol Haritasının içi doluyken silinemez.Önce siparişleri yol haritasından çıkarınız...</h1></body></html>"
        return HttpResponse(html)
    return redirect(url)



@login_required
def veriEkle(request,sepetAdi):
    url=request.META.get('HTTP_REFERER') 
    if request.method == "GET":
        context={
           'sepetAdi':sepetAdi,
        } 

        return render(request,'veriEkle.html',context) 
    
    if request.method == "POST":
        yuklenen=request.POST.get('yuklenen')
        dagitilan=request.POST.get('dagitilan')
        cikisKm=request.POST.get('cikisKm')
        donusKm=request.POST.get('donusKm')
        alinanYakit=request.POST.get('alinanYakit')
        mazotYuzdesi=request.POST.get('mazotYuzdesi')
        alinanAdblue=request.POST.get('alinanAdblue')
        yakitTutari=request.POST.get('yakitTutari')
        surucu=request.POST.get('surucu')
        gidisTarihi=request.POST.get('gidisTarihi')
        donusTarihi=request.POST.get('donusTarihi')
        
       
        print(yuklenen)
        print(dagitilan)
        print(cikisKm)
        print(donusKm)
        print(alinanYakit)
        print(alinanAdblue)
        print(yakitTutari)
        print(surucu)
        print(gidisTarihi)
        print(donusTarihi)
        obj= get_object_or_404(Guven_Sevkiyat_Sepeti,sepetAdi=sepetAdi)
        obj.yuklenen=int(yuklenen)
        obj.dagitilan=int(dagitilan)
        obj.cikisKm=int(cikisKm)
        obj.donusKm=int(donusKm)
        obj.alinanYakit=float(alinanYakit)
        obj.alinanAdblue=int(alinanAdblue)
        obj.yakitTutari=float(yakitTutari)
        obj.surucu=surucu
        obj.mazotYuzdesi=float(mazotYuzdesi)
        obj.gidisTarihi=gidisTarihi
        obj.donusTarihi=donusTarihi
        obj.fark=float(yuklenen)-float(dagitilan)
        obj.yapilanKm=int(donusKm)-int(cikisKm)
        obj.save()

        return redirect(yolHaritasiListesi) 



@login_required
def veriDegistir(request,sepetAdi):
    url=request.META.get('HTTP_REFERER') 
    if request.method == "GET":
        context={
           'sepetAdi':sepetAdi,
        } 

        return render(request,'veriDegistir.html',context) 
    
    if request.method == "POST":
        yuklenen=request.POST.get('yuklenen')
        dagitilan=request.POST.get('dagitilan')
        cikisKm=request.POST.get('cikisKm')
        donusKm=request.POST.get('donusKm')
        alinanYakit=request.POST.get('alinanYakit')
        mazotYuzdesi=request.POST.get('mazotYuzdesi')
        alinanAdblue=request.POST.get('alinanAdblue')
        yakitTutari=request.POST.get('yakitTutari')
        surucu=request.POST.get('surucu')
        gidisTarihi=request.POST.get('gidisTarihi')
        donusTarihi=request.POST.get('donusTarihi')
        
       
        print(yuklenen)
        print(dagitilan)
        print(cikisKm)
        print(donusKm)
        print(alinanYakit)
        print(alinanAdblue)
        print(yakitTutari)
        print(surucu)
        print(gidisTarihi)
        print(donusTarihi)

        if yuklenen:
            Guven_Sevkiyat_Sepeti.objects.filter(sepetadi=sepetAdi).update(yuklenen=yuklenen)        
        if dagitilan:
            Guven_Sevkiyat_Sepeti.objects.filter(sepetadi=sepetAdi).update(dagitilan=dagitilan)        
        if cikisKm:
            Guven_Sevkiyat_Sepeti.objects.filter(sepetadi=sepetAdi).update(cikisKm=cikisKm)        
        if donusKm:
            Guven_Sevkiyat_Sepeti.objects.filter(sepetadi=sepetAdi).update(donusKm=donusKm)        
        if alinanYakit:
            Guven_Sevkiyat_Sepeti.objects.filter(sepetadi=sepetAdi).update(alinanYakit=alinanYakit)        
        if mazotYuzdesi:
            Guven_Sevkiyat_Sepeti.objects.filter(sepetadi=sepetAdi).update(mazotYuzdesi=mazotYuzdesi)        
        if alinanAdblue:
            Guven_Sevkiyat_Sepeti.objects.filter(sepetadi=sepetAdi).update(alinanAdblue=alinanAdblue)        
        if yakitTutari:
            Guven_Sevkiyat_Sepeti.objects.filter(sepetadi=sepetAdi).update(yakitTutari=yakitTutari)
        if surucu:
            Guven_Sevkiyat_Sepeti.objects.filter(sepetadi=sepetAdi).update(surucu=surucu)
        if gidisTarihi:
            Guven_Sevkiyat_Sepeti.objects.filter(sepetadi=sepetAdi).update(gidisTarihi=gidisTarihi)
        if donusTarihi:
            Guven_Sevkiyat_Sepeti.objects.filter(sepetadi=sepetAdi).update(donusTarihi=donusTarihi)
                
        

        return redirect(yolHaritasiListesi) 




@login_required
def tamamla(request,id):
    url=request.META.get('HTTP_REFERER')
    print(id) 
    if request.method == "GET":
        siparis=Guven_Siparis_List.objects.get(id=id)
        
        context={
           'siparis':siparis,
        } 

        return render(request,'tamamla.html',context) 
    
    if request.method == "POST":
        
        makbuzNo=request.POST.get('makbuzNo')
        verilenMiktar=request.POST.get('verilenMiktar')
        makbuzTarihi=request.POST.get('makbuzTarihi')
        
        print(makbuzNo)
        print(verilenMiktar)
        print(makbuzTarihi)


        obj= get_object_or_404(Guven_Siparis_List,id=id)
        obj.makbuzNo=makbuzNo
        obj.verilenMiktar=int(verilenMiktar)
        obj.makbuzTarihi=makbuzTarihi
        obj.sevkiyatDurumu="Tamamlandı"

        sepetAdi=obj.yolHaritasiAdi
        sepet=get_object_or_404(Guven_Sevkiyat_Sepeti,sepetAdi=sepetAdi)
        
        obj.save()

        print("--------- ",id)
        id=sepet.id
        print(">>>>>>>> sepet id:",id)
        print(obj.yolHaritasiAdi)
        return redirect('http://localhost:51/yolHaritasiListesi/incele/'+str(sepet.id))