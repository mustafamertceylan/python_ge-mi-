def asal_mi(sayi):
    asal=True
    for i in range(2,sayi):
        if sayi%i==0:
            asal=False
    return asal
def bolen(sayi):
    dizi=[]
    for i in range(1,sayi+1):
        if sayi%i==0:
            dizi.append(i)
    return dizi
def kendinden_onceki_asallar(sayi):
    dizi=[]
    for i in range(2,sayi):
        if asal_mi(i):
            dizi.append(i)
    return [dizi,sum(dizi)]


sayi=int(input("sayi giriniz"))
print(asal_mi(sayi))
print(bolen(sayi))
print(kendinden_onceki_asallar(sayi))
