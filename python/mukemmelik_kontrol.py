sayi=int(input("mükemmelliğini araştırmak istediğiniz sayiyi giriniz "))
def kontrol(sayi1):
    toplam=0
    for i in range(sayi1-1):
        if sayi1%i==0:
            toplam+=i
    if toplam==sayi1:
        print(f"{sayi1} sayisi mükemmel sayidir")
    else:
        print(f"{sayi1} sayisi mükemmel sayı değildir")
kontrol(sayi)