import random
def my_title(metin):
    return " ".join(word.capitalize() for word in metin.split())

def my_upper(metin):
    result=""
    for char in metin:
        if 'a'<=char <='z':
            result+=chr(ord(char)-32)
        else:
            result+=char
    return result


def my_lower(metin):
    result=""
    for char in metin:
        if "A"<=char <="Z":
            result+=chr(ord(char)+32)
        else:
            result+=char
    return result

def my_strip(metin):
    result=""
    for char in metin:
        if char==" ":
            continue
        else:
            result+=char
    return result

def my_len(metin):
    sayac=0
    for i in metin:
        sayac+=1
    return sayac

def asallik_kontrol(sayi):
    durum=True
    for i in range(2,sayi):
        if sayi%i==0:
            durum=False
    return durum
        
def bolenler(sayi):
    dizi=[]
    
    for i in range(1,sayi+1):
        if sayi%i==0:
            dizi.append(i)
            
    print(dizi)

def sayiReverse(sayi):
    metin=str(sayi)
    sayiReverse=[]
    for i in range(0,len(metin)):
        sayiReverse.append((int)(metin[-1-i]))
    print(sayiReverse)
    sayi2=0
    for i in sayiReverse:
        sayi2=sayi2*10
        sayi2+=i
    
    return sayi2

def binaryDonustur(sayi):
    dizi=[]
    while(sayi>0):
        dizi.append(sayi%2)
        sayi=sayi//2
    sayi2=0
    for i in range(0,len(dizi)):
        print(dizi[-1-i],end="")
def mukemmelSayi(sayi):
    toplam=0
    for i in range(1,sayi):
        if (sayi%i==0):
            toplam+=i
    
    if toplam==sayi:
        return True
    else:
        return False
def tahminOyunu():
    tahmin=int(input("tahmininizi giriniz"))
    sayi=random.randint(1,100)
    while(tahmin!= sayi):
        if(tahmin<sayi):
             tahmin=int(input("daha yüksek bir tahmin giriniz giriniz"))
        else:
             tahmin=int(input("daha küçük bir tahmin giriniz"))
    print("tahmininiz başarılı "+str(sayi))
def kullanıcı():
    isim=input("isminizi giriniz")
    soyisim=input("soy isim")
    lakap=input("lakabınızı giriniz")
    sehir=input("sehrinizi giriniz")
    dizi=[]
    dizi.append(isim)
    dizi.append(soyisim)
    dizi.append(lakap)
    dizi.append(sehir)
    print(dizi)
 
def myCount(dizi,sayi):
    sayac=0
    for i in dizi:
        if i==sayi:
            sayac+=1
    return sayac
def diziReverse(dizi):
    dizi1=[]
    for i in range(0,len(dizi)):
        dizi1.append(dizi[-1-i])
    return dizi1
def mySample(dizi,sayi):
    returndizi=[]
    sayi1=0
    for i in range(0,3):
        sayi1=random.randint(0,len(dizi))
        returndizi.append(dizi[sayi1])        
    return returndizi
def dizikontrol(dizi):
    toplam=0
    for i in dizi:
        toplam+=i
        if(toplam>=100):
            ilk=i
            break
    print(f"toplam {toplam}  son eleman {ilk}")

def aynı(sayi):
    metin=str(sayi)
    if (metin[0]+metin[2]>metin[1]):
        return True
    else: 
        return False





"""
metin="sene 1872 uçağımız rötar yaptı"
metin=metin.split("ı",maxsplit=-1)
print(metin)
"""
#str.split("hangi karaktere göre bölecek",maxsplit=bölünecek sayi) bu fonksiyon metni böler ve her bir elemanı bir listeye atar


str1="HELLO WORLD"
str2="hello word"
print(my_upper(str2))
print(my_title(str2))
print(my_lower(str1))
print(my_strip(str2))
print(len(str2))
print(my_len(str2))
print(asallik_kontrol(1))
bolenler(60)

for i in range(3,10):
    print(asallik_kontrol(i))
    bolenler(i)
    print("\n")
sayi=100
print(oct(sayi),hex(sayi),bin(sayi))

isim="mert"
soyisim="ceylan"
lakap="MMC"

kişiBilgisi=isim+" "+soyisim+" "+lakap
print(kişiBilgisi)


print(sayiReverse(7845))
binaryDonustur(578)
print(" ")
for i in range(1,100):
    if(mukemmelSayi(i)==True):
        print(i,end=" ")
print("")
liste1=["samsun","istanbul"]
liste2=["alaçam","tuzla"]
liste3=liste1+liste2
print(liste3)
liste1.extend(liste2)
print(liste1)

dizi1=[1,2,3,4,5,6,7,8,9,6,7,5,1,6,8,7,2,5,7]
dizi=[1,2,3,45,6,7,8,9,4,5,6,6,6,2,1,3,4,5,6,6,6]
print(myCount(dizi,6))

newdizi=diziReverse(dizi)
print(newdizi)


print(mySample(dizi,5))
dizikontrol(dizi)

rehber={"ahmet":25422,"selin":455635}
print(rehber["ahmet"])
def myraplece(metin,harf1,harf2):
    yenimetin=""
    for i in metin:
        if i==harf1:
            yenimetin+=harf2
        else:
            yenimetin+=i
    return yenimetin
metin ="marmara"
print(myraplece(metin,"a",""))
