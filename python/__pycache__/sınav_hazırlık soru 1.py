metin=input("bir metin giriniz....")
liste=metin.split();
liste2={}
sayac=0
for j in liste:
    for i in liste:
        if j==i:
            sayac+=1
    liste2[j]=sayac
    sayac=0
    


print(liste)
print(liste2)