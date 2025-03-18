#listedeki elemanların toplamını ekrana yazdırma
import random
dizi=[]
for i in range(20):
    dizi=random.randint(0,20)
def topla(dizi):
    toplam=0
    for i in range(20):
        toplam+=dizi[i]
    return toplam
print(topla(dizi))