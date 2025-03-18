dizi=[]
dizi[0]=int(input())
for i in range(,10):
    eleman=int(input(f"{i+1}. elemanı giriniz"))
    if i>=1:
        if dizi[i-1]>eleman:
            dizi.remove(eleman)
            print("baska bir eleman girin")
            eleman=int(input(f"{i+1}. elemanı giriniz"))
            dizi.append(eleman)
dizi.reverse()
print(dizi)

    