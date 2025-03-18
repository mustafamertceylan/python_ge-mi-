import random #import ile kütüphaneyi dahil ediyoruz
sayi=random.randint(50,100)#50 ile 100 arasında bir sayi döndürür sınırlar dahildir
print(sayi)
sayi2=random.randrange(50,100)
print(sayi2)#sınırlar dahil olmadan bir sayı döndürür
sayilar=range(50)
print(random.sample(sayilar,3))#belirtilen liste içinden belirtilen sayı kadar rastgele sayı döndürür

liste=range(20)#listemizi 0dan 20ye kadar olan sayılarla doldurduk(20 dahil değil)
print(random.choice(liste))#random.choice(liste) ile liste içinden rastgele 1 eleman getirdik

