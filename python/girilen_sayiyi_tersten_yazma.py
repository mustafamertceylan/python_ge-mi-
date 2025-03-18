sayi=int(input("tersten yazmak istediginiz sayiyi giriniz"))
toplam=0
while sayi>0:
    toplam=toplam*10+sayi%10
    sayi=sayi//10
print(f"sayinin tersten yazilmis hali {toplam}")
