dizi=["ahmet",124,"mert",154]
isim=input("isim girin")
if isim in dizi:
    print("numarası "+dizi[dizi.index(isim)+1])
else:
    print("kayıt yapılıyor")
    dizi.append(isim)
    print("yeni kisinin numarasını giriniz")
    number=int(input())
    dizi.append(number)