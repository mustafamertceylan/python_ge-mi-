def fonksiyon_adi(): #basına def yazmamız gerekiyor ve sonuna noktalı virgül koymayı unutma
    dil="python dili"
    print(dil)
#fonksiyon adlarında türkçe karakter olmamalı
#def tek():
#   print("girilen sayi tektir")
#def cift():
#   print("girilen sayi çifttir")
#sayi=int(input("bir sayi giriniz"))
#if sayi%2==0:
#   cift()
#else:
# tek()
def vefa_abi(isim):#fonksiyonlara argüman göndermek bu şekilde yapılır
    print("ketenpereye geldin ",isim)
vefa_abi("meric")
#argümansız olarak veya birden fazla argümanla çağırmak hataya sebebiyet verir
vefa_abi(32)
#girilen argümanda tip ayırımı yapmıyor
def deneme(a,b,c):
    print(a*b)
    print(c)
deneme(5,4,"merhaba")
deneme(5,"merhaba",5)
#karışıklığı önlmek için aşağıdaki gibi yapılır
deneme(a=3,c="merhaba",b=8)
# http://docs.python.org/library/functions.html sitesinden gömülü fonksiyonların listesine erişmek mümkündür
def carpim(a):
    global sayi1
    sayi1=1
    #global deyimi ile sayi1 değişkenine fonksiyon dışında da erişim sağlanır
    for i in range(len(a)):
        sayi1=sayi1*a[i]
    print(sayi1)  
liste=[10,20,30]
carpim(liste)
sayi1=5
carpim(liste)#çıktı yine 600 olur
#çıktının 3000 olması için sayi1 değişkenini fonksiyon içinde değer vermememiz gerekir
def carpim(a):
    global sayi1
    for i in range(len(a)):
        sayi1=sayi1*a[i]
    print(sayi1)  
liste=[10,20,30]
sayi1=5
carpim(liste)


   
