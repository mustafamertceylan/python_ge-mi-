def gun_hesapla(tarih1,tarih2):
    gun1=tarih1[0]*365+tarih1[1]*30+tarih1[2]
    gun2=tarih2[0]*365+tarih2[1]*30+tarih2[2]
    print("iki tarih arasındaki gün farkı : ",(gun1-gun2) if gun1>gun2 else (gun2-gun1) )

def hafta_hesapla(tarih1,tarih2):
    hafta1=(tarih1[0]*365+tarih1[1]*30+tarih1[2])//7
    hafta2=(tarih2[0]*365+tarih2[1]*30+tarih2[2])//7
    print("iki tarih arasındaki hafta farkı : ",(hafta1-hafta2) if (hafta1>hafta2) else (hafta2-hafta1) )


yil=int(input("1. tarihin yilını giriniz "))
ay=int(input("1. tarihin ayını giriniz "))
if(ay>12 and ay<1):
    while(ay<=12 and ay>0):
        print("geçersiz bir ay girdiniz lütfen tekrar giriniz ")
        ay=int(input("1. tarihin ayını giriniz"))
gun=int(input("1. tarihin gününü giriniz "))
tarih1=[yil,ay,gun]

yil=int(input("2. tarihin yilını giriniz "))
ay=int(input("2. tarihin ayını giriniz "))
if(ay>12 and ay<1):
    while(ay<=12 and ay>0):
        print("geçersiz bir ay girdiniz lütfen tekrar giriniz")
        ay=int(input("2. tarihin ayını giriniz "))
gun=int(input("2. tarihin gününü giriniz "))
tarih2=[yil,ay,gun]
gun_hesapla(tarih1,tarih2)
hafta_hesapla(tarih1,tarih2)