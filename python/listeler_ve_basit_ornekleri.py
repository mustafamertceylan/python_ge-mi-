dizi=["mert","ceylan",21,45]#pythonda listelerde dizi elemanları aynı tipte olmak zorunda degildir
eleman_sayisi=len(dizi)#len() fonksiyonu dizinin eleman sayısını verir
print(eleman_sayisi)
dizi.append("marmara üniverstesi")
print(dizi)#append() fonksiyonu listenin sonuna ekleme yapar.aynı anda sadece tek bir eleman ekleme yapar

dizi.insert(0,"170423020")#insert ile belirtilen fonksiyonda 0 hangi sıraya eleman ekleyeceğimizi gösterir
#ve elemanları kaydırır yani o eleman yyarine başka eleman eklemez
print(dizi)
dizi2=["ornek dizi"]
dizi.extend(dizi2)#extend() dizinin sonuna başka bir diziyi ekleme yapar
print(dizi)
dizi.remove("ornek dizi") #remove() fonksiyonu diziden çıkarma yapar
print(dizi)
dizi.pop(0)#diziden belirtilen indisli elemanı çıkartır eğer içine bi indeks girilmezse son elemanı getirir
print(dizi)

x=dizi.index("mert")#index() fonksiyonu girilen elemanın dizinin kaçıncı elemanı olduğunu yani index numarasını verir
print(f"index {x}")

#y=dizi.index("ahmet")#olmayan bir elemanı arattığımızda hata mesajı veriyor
#print(y)

sayilar=[4,2,18,7,3,21,4,4]
sayilar.sort()#dizideki elemanları sıralamaya yarar
print(sayilar)

sayilar.reverse()#reverse() fonksiyonu dizi elemanlarını ters çevirmeye yarar
print(sayilar)

kac_tekrar=sayilar.count(4)
print(f"4 sayisi {kac_tekrar} defa tekrar etmekte")

liste=[] # ile liste=list() aynı şeyi ifade eder ikiside boş liste oluşturur
print(liste)


