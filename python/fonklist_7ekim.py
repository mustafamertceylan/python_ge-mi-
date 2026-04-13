def toplam(sayi,sayi1):
    print(sayi+sayi1)

def carpma(sayi,sayi1):
    print(sayi*sayi1)

def buyuk(dizi):
    en_buyuk=dizi[0]
    for i in range(len(dizi)):
        if dizi[i]>en_buyuk:
            en_buyuk=dizi[i]
    print(en_buyuk)

def kucuk(dizi):
    en_kucuk=dizi[0]
    for i in range(len(dizi)):
        if dizi[i]<en_kucuk:
            en_kucuk=dizi[i]
    print(en_kucuk)

def arama(dizi,aranan):
    for i in range(len(dizi)):
        if dizi[i]==aranan:
            print(f"aranan eleman {i}. indiste bulundu")

    


def ortalama(dizi):
    toplam=0
    for i in dizi:
        toplam+=i
    print(f"dizinin ortalaması {toplam/len(dizi)}")