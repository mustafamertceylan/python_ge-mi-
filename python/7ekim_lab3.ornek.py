metin=input("lütfen formülü giriniz")
toplam=0
for i in range(len(metin)):
    if( metin[i]=="(" or metin[i]==")"):
        toplam+=1
if(toplam%2==0):
    print("herhangi bir formül hatası yoktur")
else:
    print("girilen formülde parantez hatası vardır lütfen formülü tekrar kontrol edin")
