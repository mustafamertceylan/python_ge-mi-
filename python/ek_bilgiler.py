
sayi=34
print(type(sayi))#type(sayi) komutu ile sayi degiskeninin türünü öğrenebiliriz
sayi=float(sayi)#bu sekilde sayi degiskeninin türünü degistirebiliriz
print(type(sayi))
a=21
b=19# bu ifadeler yerine a,b=21,19 seklinde yazabiliriz
a,b=b,a #bu gösterimde a ve ifadelerinin icindeki degerleri degistirebiliriz
print(a,b)
print(13/2,12/2)#bolme isleminde tek / isareti kullanırsak floa bir deger dondurur bize
print(type(13/2))
#ama biz bolme isleminde // isareti kullanırsak bize int  bir ifade dondurur
print(13//2,12//2)
print(type(13//2),type(12//2))
print('mert\'in denemesi')
#bu ifadede string ifadelerde tek tırnak kullanılırken çıkan sorunları bu sekilde (\ ters bölme isareti) giderebiliriz
#string ifadelerde toplama ve carpma yapılabilir
metin="mert"
metin1="ahmet"
print(metin+metin1)#bu ifade strinleri birlestirir
print(metin*3)#bu ifade ise metin degiskeninin 3 kere yazılmasına sebep olur
print(metin[0])#string ifadeleri sanki dizi elemanlarını arıyormus gibi parcalayabiliriz
print(metin[0:4:3])#bu sekilde sanki dizi elemanlarını getirtebiliriz
#metin[baslama_indeksi:bitis_indeksi:atlama_degeri]
print(metin[::-1])#bu ifade stringi tersten yazdırır
x=y="turuncu"
print(x,y)#bu sekilde tanımlamaya izin verir
metin2="""""veysel
ahmet
mert"""
print(metin2)#bu sekilde stringleri alt alta yazdırabiliriz
print("metin1\tmetin2")#\t ifadesi ile iki string arasında 4 karakterlik bir bosluk bırakır
print("12","08","2024")
print("12","08","2024",sep=".") 
#sep="araya konulacak karakter" ifadesi ile biren fazla string ifade bastırırken 
# aralarına konulacak karakteri belirtmemize yarar
print(*"python")#buradaki * karakteri metindeki karakterler arasına bir bosluk bırakılmasına neden olur
print(*"python",sep=".")
print(*"TBMM",sep=".")
sayi1=12
sayi2=10
print("yukarıdaki sayilar {} ve {} sayılarıdır".format(sayi1,sayi2))
#boyle bir kullanım oldugu aklında bulunsun