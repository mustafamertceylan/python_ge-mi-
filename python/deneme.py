def artan_alt_dizi(dizi):
    en_uzun = []  
    gecici = [dizi[0]]  
    for i in range(1, len_fonksiyonu(dizi)):
        if dizi[i] > dizi[i - 1]:
            gecici = append_fonksiyonu(gecici, dizi[i])  
        else:
            if len_fonksiyonu(gecici) > len_fonksiyonu(en_uzun):
                en_uzun = gecici
            gecici = [dizi[i]]  
    if len_fonksiyonu(gecici) > len_fonksiyonu(en_uzun):
        en_uzun = gecici
    return en_uzun

def len_fonksiyonu(dizi):
    eleman_sayisi = 0
    for i in dizi:
        eleman_sayisi += 1
    return eleman_sayisi

def append_fonksiyonu(dizi, yeni_eleman):
    return dizi + [yeni_eleman]  

# Ana program
dizi = [1, 2, 3, 1, 2, 3, 4, 5, 6, 5, 6, 7, 8]
sonuc = artan_alt_dizi(dizi)
print(sonuc)  
