import random
def eleman_kontrol(dizi):
    while True:
        eleman_sayisi=0
        for i in dizi:
            eleman_sayisi+=1
        eleman=dizi[0]
        tekrar=0
        for i in range(eleman_sayisi):
            if dizi[i]==eleman:
                tekrar+=1
        if tekrar>1:
            print(f"{eleman} ögesinden {tekrar} tane vardır")
        gecici_dizi=[]
        for x in dizi:
            if x != eleman:
                gecici_dizi.append(x)  
        dizi[:] = gecici_dizi
            
#ana program
dizi=[random.randint(0,10) for i in range(15)]
print(dizi)
eleman_kontrol(dizi)


