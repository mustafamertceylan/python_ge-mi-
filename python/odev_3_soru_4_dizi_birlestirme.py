import random
def sirala(dizi1,dizi2):
    birlesmis_dizi=dizi1+dizi2
    
    for i in range(20):
        for j in range(i+1,19):
            if birlesmis_dizi[i]>birlesmis_dizi[j]:
                birlesmis_dizi[i],birlesmis_dizi[j]=birlesmis_dizi[j],birlesmis_dizi[i]
    print(dizi1)
    print(dizi2)
    print(birlesmis_dizi)
#ana program
dizi1=[random.randint(0,20) for i in range(10)]
dizi2=[random.randint(0,20) for i in range(10)]
sirala(dizi1,dizi2)