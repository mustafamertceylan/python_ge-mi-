def giris(dizi):
    dizi["adı"]=input("adınızi giriniz")
    dizi["vize notu"]=int(input("vize notunuzu giriniz"))
    dizi["final notu"]=int(input("final notunuzu giriniz"))
    dizi["ortalama"]=str(dizi["vize notu"]/2+dizi["final notu"]/2)
ogrenci={"adı":"","vize notu":"","final notu":"","ortalama":""}
giris(ogrenci)
print(ogrenci)