import random
def sirala(dizi ):
    eleman_sayisi=0
    for i in dizi:
        eleman_sayisi+=1
    for i in range(eleman_sayisi):
        for j in range(i+1,eleman_sayisi):
            if dizi[i]>dizi[j]:
                dizi[i],dizi[j]=dizi[j],dizi[i]
    return dizi

#ana program

dizi1=[random.randint(0,50) for i in range(10)]
dizi2=[random.randint(0,50) for i in range(10)]
print("1. dizi : ",dizi1)
print("2. dizi : ",dizi2)
birlesmis_dizi=[]
for i in range(10):
    if dizi2[i] not in dizi1:
        birlesmis_dizi.append(dizi2[i])     
for i in range(10):
    if dizi1[i] not in dizi2:
        birlesmis_dizi.append(dizi1[i])


print("<birlesmis ve ortak elemanlar cikarilmis dizi \n",birlesmis_dizi)
sirali_dizi=sirala(birlesmis_dizi) 
print("siralanmis dizi\n ",birlesmis_dizi)              


    
