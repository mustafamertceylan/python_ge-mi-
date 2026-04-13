print("bu program asal sayıları bulacagı icin pozitif degerler giriniz ")
alt_deger=int(input("sorgulamak itediginiz aralıgın alt degerini giriniz "))
ust_deger=int(input("sorgulamak istediginiz aralıgın üst degerini giriniz "))
asallik_kontrol=True
for j in range(alt_deger,ust_deger+1):
    
    for i in range(2,j):
        if  i==j:
            break
        elif j % i == 0:
            print(f"{j} sayisi asal degildir")
            print(f"{j} sayisinin bolenleri ")
            for a in range(1,j+1):
                if j%a==0:
                    print(a)  
            asallik_kontrol=False
            print()
            break
    if asallik_kontrol==True:
        print(f"{j} sayisi asaldir")
        print()
    asallik_kontrol=True   
    


        