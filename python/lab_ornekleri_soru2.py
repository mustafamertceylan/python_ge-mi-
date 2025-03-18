import random
dizi=[]
for i in range(0,20):
    dizi.append(random.randint(1,25))
toplam=0
for i in range(20):
    toplam+=dizi[i]
    if toplam>=100:
        print(dizi[i])
        print(dizi)
        break