
import mysql.connector as sq

imlec=""
veritabaniAdi=""
tabloAdi=""
tabloBasliklar=[]
tabloTipler=[]
GelenVeriler=[]
db=""

#verdiğiniz adda veritabani oluşturur                         -> "VeriTabanim"
def SqlBagla(ad):
    global db
    dbadi=ad
    dbadi=dbadi.lower()
    db=dbadi
    ad=sq.connect(
        host="localhost",
        user="root",
        password="",
    )

    global imlec
    global veritabaniAdi
    veritabaniAdi=ad
    imlec=ad.cursor()
    varmi=False
    imlec.execute("SHOW DATABASES")
    for i in imlec:
        i=str(i)
        i=i.strip("( ) ' ,")
        if i==dbadi:
            varmi=True
    if varmi==True:
        ad=sq.connect(
        host="localhost",
        user="root",
        password="",
        database=dbadi
        )
    else:
        sorgu="CREATE DATABASE "+dbadi
        imlec.execute(sorgu)

    


#verdiğiniz adlara göre tablo ve sutunlar oluşturur           ->"Ogrenci","OgrenciAdi TEXT","OgrenciNo INTEGER"
def sqlTabloYap(ad,*sutunlar):
    global tabloTipler
    global tabloBasliklar
    global imlec
    global tabloAdi
    global veritabaniAdi
    tabloAdi=ad
    global db
    db1=sq.connect(
        host="localhost",
        user="root",
        password="",
        database=db
        )
    imlec=db1.cursor()
    sutun="CREATE TABLE IF NOT EXISTS " +ad+"("
    x=0
    for a in sutunlar:
        s=a.split(" ")
        tabloBasliklar.append(s[0])
        tabloTipler.append(s[1])
        if x==len(sutunlar)-1:
            sutun+=a
        else:
            sutun+=a+","
        x+=1
    sutun+=")"
    imlec.execute(sutun)
    db1.commit()

#verdiğiniz veriyi ekler tabloya                              ->"ad",no
def sqlVeriEkle(*veriler):
    global imlec
    global tabloAdi
    global tabloBasliklar
    global tabloTipler
    global veritabaniAdi
    global db
    db1=sq.connect(
        host="localhost",
        user="root",
        password="",
        database=db
        )
    imlec=db1.cursor()
    sorgu="INSERT INTO "+tabloAdi+"("
    x=0
    for i in tabloBasliklar:
        if x==len(tabloBasliklar)-1:
            sorgu+=i
        else:
            sorgu+=i+","
        x+=1
    sorgu+=") VALUES("
    x=0
    for a in veriler:
        if x==len(veriler)-1:
            if tabloTipler[x]=='TEXT':
                sorgu+="'"+a+"'"
            else:
                sorgu+=str(a)
        else:
            if tabloTipler[x]=='TEXT':
                sorgu+="'"+a+"',"
            else:
                sorgu+=str(a)+","
        x+=1
    sorgu+=")"
    imlec.execute(sorgu)
    db1.commit()

#tablo verilerini listeler                                    ->"*"
def sqlVeriListele(*icerikler):
    global imlec
    global tabloAdi
    global veritabaniAdi
    global GelenVeriler
    global db
    db1=sq.connect(
        host="localhost",
        user="root",
        password="",
        database=db
        )
    imlec=db1.cursor()

    sorgu="SELECT "
    x=0
    for i in icerikler:
        if x==len(icerikler)-1:
            sorgu+=i
        else:
            sorgu+=i+","
        x+=1
    sorgu+=" FROM "+tabloAdi
    imlec.execute(sorgu)
    GelenVeriler=imlec.fetchall()
    print(GelenVeriler)

#verdiğiniz kayıtlı içerikli veriyi siler                     ->"OgrenciNo=3"
def sqlveriSil(*silinecekler):
    global imlec
    global tabloAdi
    global veritabaniAdi
    global db
    db1=sq.connect(
        host="localhost",
        user="root",
        password="",
        database=db
        )
    imlec=db1.cursor()
    
    sorgu="DELETE FROM "+tabloAdi+" WHERE "
    x=0
    for i in silinecekler:
        if x==len(silinecekler)-1:
            sorgu+=i
        else:
            sorgu+=i+","
        x+=1
    imlec.execute(sorgu)
    db1.commit()

#verdiğiniz veri kaydının verdiğiniz içeriklerini günceller   ->"OgrenciNo=2","OgrenciAdi='kiraz'","OgrenciNo=5"
def sqlveriGuncelle(sartlar,*gunceller):
    global imlec
    global tabloAdi
    global veritabaniAdi
    global db
    db1=sq.connect(
        host="localhost",
        user="root",
        password="",
        database=db
        )
    imlec=db1.cursor()
    
    sorgu="UPDATE "+tabloAdi+" SET "
    x=0
    for i in gunceller:
        if x==len(gunceller)-1:
            sorgu+=i
        else:
            sorgu+=i+","
        x+=1
    sorgu+=" WHERE "+sartlar
    imlec.execute(sorgu)
    db1.commit()

#verdiğiniz şartlara göre veriyi listeler                     ->"OgrenciNo>3","*"
def sqlveriSartliListele(sart,*icerikler):
    global imlec
    global tabloAdi
    global veritabaniAdi
    global GelenVeriler
    global db
    db1=sq.connect(
        host="localhost",
        user="root",
        password="",
        database=db
        )
    imlec=db1.cursor()

    sorgu="SELECT "
    x=0
    for i in icerikler:
        if x==len(icerikler)-1:
            sorgu+=i
        else:
            sorgu+=i+","
        x+=1
    sorgu+=" FROM "+tabloAdi+" WHERE "+sart
    imlec.execute(sorgu)
    GelenVeriler=imlec.fetchall()
    print(GelenVeriler)

#SQL den cikis yapar ve bellek verilerini boşaltir. (veritabani dosyanız kayıtlı kalır)
def sqlKapat():
    global veritabaniAdi
    global imlec
    global tabloAdi
    global tabloBasliklar
    global tabloTipler
    global GelenVeriler
    veritabaniAdi.close()
    veritabaniAdi=""
    imlec=""
    tabloAdi=""
    tabloBasliklar.clear()
    tabloTipler.clear()
    GelenVeriler.clear()
    print("SQL cikis yapildi!")


SqlBagla("benimtaban")
sqlTabloYap("Ogrenci","OgrenciAdi TEXT","OgrenciSoyadi TEXT","OgrenciNo INTEGER")
sqlVeriEkle("ENES","BAYRI",1)
sqlVeriEkle("beyza","nur",2)
sqlVeriEkle("gamze","demet",3)
sqlVeriEkle("emre","bagmanci",4)
sqlVeriListele("*")
sqlveriSil("OgrenciNo=3")
sqlveriGuncelle("OgrenciNo=2","OgrenciAdi='kiraz'","OgrenciNo=5")
sqlveriSartliListele("OgrenciNo>3","*")
"""for a in veriler:
        if x==len(veriler)-1:
            sorgu+="%s"
        else:
            sorgu+="%s, "  
        x+=1
"""
