sayi=int(input("Asalligini kontrol etmek istediginiz sayiyi giriniz"))
asallik_kontrol=True
for i in range(2,sayi):
    if  i==sayi:
        break
    elif sayi % i == 0:
        print("girilen sayi asal degildir")
        asallik_kontrol=False
        break
if asallik_kontrol==True:
    print("Girilen sayi asaldir")
        
