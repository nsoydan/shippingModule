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



 #-------------- Gelen kutusu ile karşılaştırmak için  için  MZD --------------------    

    
    conn=pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                        'Server=ANADOLUSERVER;'
                        'Database=LOGODB;'
                        'UID=sa;'
                        'PWD=Vega1234;'
                        'Trusted_Connection=No;')

    cursor=conn.cursor()                   #0                               1                       2                           3                       4                   5                         6                        7                   8                    9                   10                  11                      12               13                  14                       15                     16                     17                              18                                                                                                                                                                     
    cursor.execute ('SELECT  LG_002_01_ORFICHE.FICHENO,LG_002_ITEMS.NAME,LG_002_01_ORFLINE.AMOUNT,LG_002_01_ORFICHE.GENEXP1,LG_002_01_ORFICHE.DATE_,LG_002_CLCARD.SPECODE,LG_002_01_ORFLINE.PRICE,LG_002_CLCARD.DEFINITION_,LG_002_CLCARD.CODE,LG_002_SHIPINFO.ADDR1,LG_002_SHIPINFO.CITY,LG_002_SHIPINFO.TOWN,LG_002_CLCARD.ADDR1,LG_002_CLCARD.CITY,LG_002_CLCARD.TOWN,LG_002_01_ORFLINE.LINEEXP,LG_002_01_ORFICHE.SPECODE,LG_002_01_ORFLINE.STATUS,LG_002_01_ORFLINE.SHIPPEDAMOUNT FROM LG_002_01_ORFLINE LEFT JOIN LG_002_ITEMS ON LG_002_01_ORFLINE.STOCKREF = LG_002_ITEMS.LOGICALREF LEFT JOIN LG_002_CLCARD ON LG_002_01_ORFLINE.CLIENTREF = LG_002_CLCARD.LOGICALREF LEFT JOIN LG_002_01_ORFICHE ON LG_002_01_ORFLINE.ORDFICHEREF = LG_002_01_ORFICHE.LOGICALREF LEFT JOIN LG_002_SHIPINFO ON LG_002_01_ORFLINE.CLIENTREF=LG_002_SHIPINFO.CLIENTREF WHERE LG_002_01_ORFLINE.STATUS=4 OR LG_002_01_ORFLINE.STATUS=1 ORDER BY LG_002_01_ORFICHE.FICHENO')
    

    for row in cursor:
        objGelen=Gelen_Tablosu( gelenfisNo='MZD'+row[0] )
        kayit3=False
        for g in Gelen_Tablosu.objects.all():
            if  g.gelenfisNo == ('MZD'+row[0]):     # gelen kayıt veritabanında varsa
                kayit3=False
                break
            else:       # gelen kayıt veritabanında yoksa
                kayit3=True
                break
         
        if kayit3:
            objGelen.save() 


      #-------------- Gelen kutusu ile karşılaştırmak için  GÜVEN --------------------    
      

    conn=pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                            'Server=ANADOLUSERVER;'
                            'Database=LOGODB;'
                            'UID=sa;'
                            'PWD=Vega1234;'
                            'Trusted_Connection=No;')

    cursor=conn.cursor()                   #0                               1                       2                           3                       4                   5                         6                        7                   8                    9                   10                  11                      12               13                  14                       15                     16                     17                              18                                                                                                                                                                     
    cursor.execute ('SELECT LG_001_01_ORFICHE.FICHENO FROM LG_001_01_ORFLINE LEFT JOIN LG_001_01_ORFICHE ON LG_001_01_ORFLINE.ORDFICHEREF = LG_001_01_ORFICHE.LOGICALREF WHERE (LG_001_01_ORFLINE.STATUS=4 OR LG_001_01_ORFLINE.STATUS=1) ORDER BY LG_001_01_ORFICHE.FICHENO')
    #♣SELECT LG_001_01_ORFICHE.FICHENO,LG_001_ITEMS.NAME,LG_001_01_ORFLINE.AMOUNT,LG_001_01_ORFICHE.GENEXP1,LG_001_01_ORFICHE.DATE_,LG_001_CLCARD.SPECODE,LG_001_01_ORFLINE.PRICE,LG_001_CLCARD.DEFINITION_,LG_001_CLCARD.CODE,LG_001_SHIPINFO.ADDR1,LG_001_SHIPINFO.CITY,LG_001_SHIPINFO.TOWN,LG_001_CLCARD.ADDR1,LG_001_CLCARD.CITY,LG_001_CLCARD.TOWN,LG_001_01_ORFLINE.LINEEXP,LG_001_01_ORFICHE.SPECODE,LG_001_01_ORFLINE.STATUS,LG_001_01_ORFLINE.SHIPPEDAMOUNT FROM LG_001_01_ORFLINE LEFT JOIN LG_001_ITEMS ON LG_001_01_ORFLINE.STOCKREF = LG_001_ITEMS.LOGICALREF LEFT JOIN LG_001_CLCARD ON LG_001_01_ORFLINE.CLIENTREF = LG_001_CLCARD.LOGICALREF LEFT JOIN LG_001_01_ORFICHE ON LG_001_01_ORFLINE.ORDFICHEREF = LG_001_01_ORFICHE.LOGICALREF LEFT JOIN LG_001_SHIPINFO ON LG_001_01_ORFLINE.CLIENTREF=LG_001_SHIPINFO.CLIENTREF WHERE LG_001_01_ORFLINE.STATUS=4 OR LG_001_01_ORFLINE.STATUS=1 ORDER BY LG_001_01_ORFICHE.FICHENO

    for row in cursor:
        objGelen=Gelen_Tablosu( gelenfisNo='GVN'+row[0] )
        kayit4=False
        for g in Gelen_Tablosu.objects.all():
            if  g.gelenfisNo == ('GVN'+row[0]):     # gelen kayıt veritabanında varsa
                kayit4=False
                break
            else:       # gelen kayıt veritabanında yoksa
                kayit4=True
                break
        
        if kayit4:
            objGelen.save() 








    #####        GÜVENE VERİLEN SİPARİŞLERİ ÇEKMEK İÇİN     ##################################

       

    siparisler=Guven_Siparis_List.objects.all()

    conn=pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                        'Server=ANADOLUSERVER;'
                        'Database=LOGODB;'
                        'UID=sa;'
                        'PWD=Vega1234;'
                        'Trusted_Connection=No;')

    cursor=conn.cursor()                        #0                  1                       2                       3                           4                   5                       6                           7                8                      9                   10                     11                12                  13                14                        15                         16                      17                          18                         19                         20                         21                  22                                                                                                                                                                                      
    cursor.execute ('SELECT LG_001_01_ORFICHE.FICHENO,LG_001_ITEMS.NAME,LG_001_01_ORFLINE.AMOUNT,LG_001_01_ORFICHE.GENEXP1,LG_001_01_ORFICHE.DATE_,LG_001_CLCARD.SPECODE,LG_001_01_ORFLINE.PRICE,LG_001_CLCARD.DEFINITION2,LG_001_CLCARD.CODE,LG_001_SHIPINFO.ADDR1,LG_001_SHIPINFO.CITY,LG_001_SHIPINFO.TOWN,LG_001_CLCARD.ADDR1,LG_001_CLCARD.CITY,LG_001_CLCARD.TOWN,LG_001_01_ORFLINE.LINEEXP,LG_001_01_ORFICHE.SPECODE,LG_001_01_ORFLINE.STATUS,LG_001_01_ORFLINE.SHIPPEDAMOUNT,LG_001_01_ORFLINE.LINEEXP,LG_001_01_ORFICHE.GENEXP2,LG_001_01_ORFICHE.GENEXP3,LG_001_01_ORFICHE.DOCTRACKINGNR FROM LG_001_01_ORFLINE LEFT JOIN LG_001_ITEMS ON LG_001_01_ORFLINE.STOCKREF = LG_001_ITEMS.LOGICALREF LEFT JOIN LG_001_CLCARD ON LG_001_01_ORFLINE.CLIENTREF = LG_001_CLCARD.LOGICALREF LEFT JOIN LG_001_01_ORFICHE ON LG_001_01_ORFLINE.ORDFICHEREF = LG_001_01_ORFICHE.LOGICALREF LEFT JOIN LG_001_SHIPINFO ON LG_001_01_ORFLINE.CLIENTREF=LG_001_SHIPINFO.CLIENTREF WHERE (LG_001_01_ORFLINE.STATUS=4 OR LG_001_01_ORFLINE.STATUS=1)  ORDER BY LG_001_01_ORFICHE.FICHENO')


    
    for row in cursor:
       
        print("------------------")
        print(date.today)
        print("Fiş no",row[0])
        print("amount :",row[2])
        print("shippedamount : ",row[18])
        if row[17] ==4:
            sevkiyatDurumu="Siparişte"
        if row[17] ==1:
            sevkiyatDurumu="Öneride" 

        obj=Guven_Siparis_List( siparisFisNo='GVN'+row[0],
                                siparisCinsi=row[1],
                                siparisMiktari=row[2],
                                siparisNotu=row[3]+' '+row[20]+' '+row[21]+' '+row[19],
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
                                sevkiyatDurumu=sevkiyatDurumu            ###### GÜVENE VERİLEN SİPARİŞLER  #######                    
                       )
       
        

        
        for s in Guven_Siparis_List.objects.all():
            kayit2=False
            if ('GVN'+row[0]) == s.siparisFisNo and row[1] == s.siparisCinsi:     # gelen kayıt veritabanında varsa
                if row[17] == s.siparisStatusu:   # veritabanındaki sipariş statüsü ile gelen sipariş statüsü aynı ise:
                    if row[18]==0:                # sevkedilmiş miktar sıfır ise:
                        print("bu kayıt var................",s.siparisFisNo)
                        kayit2=False
                        break
                    else:                       # sEVKEDİLMİŞ MİKTAR SIFIRDAN FARKLI İSE, FATURA KESİLMİŞ İSE:
                        Guven_Siparis_List.objects.filter(siparisFisNo=('GVN'+row[0])).update(sevkiyatDurumu="Faturalandı")
                        kayit2=False
                        break
                else:                           # VERİTABANINDAKİ SİPARİŞ STATÜSÜ GELEN STATÜDEN FARKLI İSE:
                    if row[17] == 4:            # GELEN STATÜ ONAYLANDI İSE 
                        Guven_Siparis_List.objects.filter(siparisFisNo=('GVN'+row[0])).update(siparisStatusu=row[17])
                        Guven_Siparis_List.objects.filter(siparisFisNo=('GVN'+row[0])).update(sevkiyatDurumu="Siparişte")
                        print("kayit güncellendiiiii....siparişe çekildi...........",row[0])
                        kayit2=False
                        break 
                    if row[17] == 1:            #GELEN STATÜ ÖNERİ İSE
                        Guven_Siparis_List.objects.filter(siparisFisNo=('GVN'+row[0])).update(siparisStatusu=row[17])
                        Guven_Siparis_List.objects.filter(siparisFisNo=('GVN'+row[0])).update(sevkiyatDurumu="Öneri")
                        print("kayit güncellendiiiii....öneriye çekildi...........",row[0])
                        kayit2=False
                        break 
            else:
                print("bu kayıt veri tabanında yok",row[0])       # gelen kayıt veritabanında yoksa
                if row[18]==0:
                    kayit2=True
                    
           
        if kayit2:
            print("yeni kayıt eklendi...:",('GVN'+row[0]))
            kayit2=False
            obj.save()  
      
   

################ #####        MZD YE VERİLEN SİPARİŞLERİ ÇEKMEK İÇİN     ##################################

    conn=pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                        'Server=ANADOLUSERVER;'
                        'Database=LOGODB;'
                        'UID=sa;'
                        'PWD=Vega1234;'
                        'Trusted_Connection=No;')

    cursor=conn.cursor()                   #0                               1                       2                           3                       4                   5                         6                        7                   8                    9                   10                  11                      12               13                  14                       15                     16                     17                        18                        19                        20                          21                                                                                           
    cursor.execute ('SELECT LG_002_01_ORFICHE.FICHENO,LG_002_ITEMS.NAME,LG_002_01_ORFLINE.AMOUNT,LG_002_01_ORFICHE.GENEXP1,LG_002_01_ORFICHE.DATE_,LG_002_CLCARD.SPECODE,LG_002_01_ORFLINE.PRICE,LG_002_CLCARD.DEFINITION_,LG_002_CLCARD.CODE,LG_002_SHIPINFO.ADDR1,LG_002_SHIPINFO.CITY,LG_002_SHIPINFO.TOWN,LG_002_CLCARD.ADDR1,LG_002_CLCARD.CITY,LG_002_CLCARD.TOWN,LG_002_01_ORFLINE.LINEEXP,LG_002_01_ORFICHE.SPECODE,LG_002_01_ORFLINE.STATUS,LG_002_01_ORFLINE.SHIPPEDAMOUNT,LG_002_01_ORFLINE.LINEEXP,LG_002_01_ORFICHE.GENEXP2,LG_002_01_ORFICHE.GENEXP3,LG_002_01_ORFICHE.DOCTRACKINGNR FROM LG_002_01_ORFLINE LEFT JOIN LG_002_ITEMS ON LG_002_01_ORFLINE.STOCKREF = LG_002_ITEMS.LOGICALREF LEFT JOIN LG_002_CLCARD ON LG_002_01_ORFLINE.CLIENTREF = LG_002_CLCARD.LOGICALREF LEFT JOIN LG_002_01_ORFICHE ON LG_002_01_ORFLINE.ORDFICHEREF = LG_002_01_ORFICHE.LOGICALREF LEFT JOIN LG_002_SHIPINFO ON LG_002_01_ORFLINE.CLIENTREF=LG_002_SHIPINFO.CLIENTREF WHERE LG_002_01_ORFLINE.STATUS=4 OR LG_002_01_ORFLINE.STATUS=1 ORDER BY LG_002_01_ORFICHE.FICHENO')

    for row in cursor:
        kayit1=False
        if row[17] ==4:
            sevkiyatDurumu="Siparişte"
        if row[17] ==1:
            sevkiyatDurumu="Öneride" 


        obj=Guven_Siparis_List( siparisFisNo='MZD'+row[0],
                                siparisCinsi=row[1],
                                siparisMiktari=row[2],
                                siparisNotu=row[3]+' '+row[20]+' '+row[21]+' '+row[19],
                                siparisDateTime=row[4],
                                siparisEden=row[5],
                                birimFiyat=row[6],
                                cariAdi=row[7],                                         #### MZD nin gelen siparişler
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
            if 'MZD'+row[0] == s.siparisFisNo:     # gelen kayıt veritabanında varsa
                if row[17] == s.siparisStatusu:  # veritabanındaki sipariş statüsü ile gelen sipariş statüsü aynı ise:
                    if row[18]==0:              # sevkedilmiş miktar sıfır ise:
                        print("bu kayıt var................",s.siparisFisNo)
                        kayit1=False
                        break
                    else:
                        Guven_Siparis_List.objects.filter(siparisFisNo=('MZD'+row[0])).update(sevkiyatDurumu="Faturalandı")
                        kayit1=False
                        break
                else:
                    if row[17] == 4:
                        Guven_Siparis_List.objects.filter(siparisFisNo=('MZD'+row[0])).update(siparisStatusu=row[17])
                        Guven_Siparis_List.objects.filter(siparisFisNo=('MZD'+row[0])).update(sevkiyatDurumu="Siparişte")
                        print("kayit güncellendiiiii...............",row[0])
                        kayit1=False
                        break 
                    if row[17] == 1:
                        Guven_Siparis_List.objects.filter(siparisFisNo=('MZD'+row[0])).update(siparisStatusu=row[17])
                        Guven_Siparis_List.objects.filter(siparisFisNo=('MZD'+row[0])).update(sevkiyatDurumu="Öneri")
                        print("kayit güncellendiiiii...............",row[0])
                        kayit1=False
                        break 
            
            else:       # gelen kayıt veritabanında yoksa
               
                if row[18]==0:
                    kayit1=True
           
        if kayit1:
            kayit1=False
            obj.save()  
      
    
    print("--------------------------SİLİNMİŞ Mİ?-------------------------------------------------------------")

#    for s in Guven_Siparis_List.objects.all().exclude(id=1):    
#        trig=0
        
#        for g in Gelen_Tablosu.objects.all():
#            if g.gelenfisNo == s.siparisFisNo:
#                trig=1
#                break
#            else:
#                trig=0                   
#
#        if trig:
#            print("bu kayıt silinmemiş........:",s.siparisFisNo)
#        else:
#            s.sevkiyatDurumu="Silinmiş kayıt"
#            s.save()
           #print("silinmiş kayıt var")               


    return redirect(index)           

# Create your views here.
@login_required
def index(request):
    
    
    sepets=Guven_Sevkiyat_Sepeti.objects.filter(sepetiOlusturan=request.user.first_name).order_by('-id')   
    

    q1=Guven_Siparis_List.objects.all().order_by('-id').exclude(id=1)
    myFilter=ListFilter(request.GET,queryset=q1)
    sipariss=myFilter.qs

    YHs=Guven_Sevkiyat_Sepeti.objects.filter(sevkiyatSepetiKayitTarihSaat__gt=(date.today()-timedelta(days=7)))
    

    print("..........................")
  
    print(date.today())
    print(date.today()-timedelta(days=7))  
    print("..........................")

    context={
        'sipariss':sipariss,
        'sepets':sepets,
        'myFilter':myFilter,
        'YHs':YHs,
    }
    return render(request,'siparisListesiSevkiyat.html',context)

@login_required
def sevkiyataGonder(request,id):
    print("sevkiyatagönder çalışıyor")
    url=request.META.get('HTTP_REFERER')
    gelenSepetAdi = request.POST.get('sepetAdi')
    hiddenid=request.POST.get('hiddenid')
    print(hiddenid)
    firma=request.user.last_name


    
    if not gelenSepetAdi:
        hataMesaji="Yol haritası adı giriniz."
        context={
                'hataMesaji':hataMesaji,
            }
        return render(request,'hata.html',context)

    todo = get_object_or_404(Guven_Siparis_List,id=id)
    todo.sevkiyatDurumu = 'Sevkiyatta'
    todo.yolHaritasiAdi=gelenSepetAdi
    print(gelenSepetAdi)
    print("////////////////////////")

    obj=get_object_or_404(Guven_Sevkiyat_Sepeti,sepetAdi=gelenSepetAdi)
   

    #obj = Guven_Sevkiyat_Sepeti.objects.get(sepetAdi=gelenSepetAdi) #Gelen sepet adi ile bir sepet var mı? 


    #print(obj)
    print("++++++++++++++++++++++")
    print(type(todo.siparisMiktari)) 
    #print(type(obj.dokmeToplami))

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
 
    yhs=Guven_Sevkiyat_Sepeti.objects.filter(sepetiOlusturan=request.user.first_name).order_by('id')
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
        obj.sevkiyatDurumu="Siparişte"
    
    
    obj.yolHaritasiAdi=None
    sepet.save()
    obj.save()

    return redirect(url)


@login_required
def incele(request,sepetAdi):
    print(sepetAdi)
    #obj=get_object_or_404(Guven_Sevkiyat_Sepeti, id=id)
    sipariss= Guven_Siparis_List.objects.filter(yolHaritasiAdi=sepetAdi).order_by('positions')
    totalSevkiyatMiktari=Guven_Siparis_List.objects.filter(siparisCinsi='DÖKME ADBLUE',yolHaritasiAdi=sepetAdi).aggregate(Sum('sevkiyatMiktari'))
    totalSiparisMiktari=Guven_Siparis_List.objects.filter(siparisCinsi='DÖKME ADBLUE',yolHaritasiAdi=sepetAdi).aggregate(Sum('siparisMiktari'))
    sepet=Guven_Sevkiyat_Sepeti.objects.get(sepetAdi=sepetAdi)
    print(sepet.alinanYakit)
    
    context={
        'sipariss':sipariss,
        'sepet':sepet,
        'sepetAdi':sepetAdi,
        'totalSevkiyatMiktari':totalSevkiyatMiktari,
        'totalSiparisMiktari':totalSiparisMiktari,
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
    print(eskiAd,yeniAd)
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
        obj.gidisTarihi=gidisTarihi
        obj.donusTarihi=donusTarihi
        obj.fark=float(yuklenen)-float(dagitilan)
        obj.yapilanKm=int(donusKm)-int(cikisKm)
        obj.mazotYuzdesi=round(float(alinanYakit)/(int(donusKm)-int(cikisKm)),2)
        
        obj.save()

        return redirect(yolHaritasiListesi) 