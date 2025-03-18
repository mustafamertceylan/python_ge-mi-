kenar1=int(input("1.kenar uzunlugunu giriniz"))
kenar2=int(input("2. kenar uzunlugunu giriniz"))
kenar3=int(input("3.kenar uzunlugunu giriniz"))
if kenar1==kenar2==kenar3:
    print("kenarları girilen ucgen eskenar ucgendir")
elif kenar1==kenar2 or kenar1==kenar3 or kenar2==kenar3:
    print("girilen ucgen ikizkenar ucgendir")
else:
    print("girilen ucgen cesit kenar bir ucgendir")