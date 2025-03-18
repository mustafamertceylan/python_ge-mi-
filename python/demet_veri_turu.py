calısan1=("ayse","cengiz",1998,2024)
print(calısan1)#demet veri türünde ekleme çıkarma yapılamaz 
#bu yüzden daha güvenilirdir
isim,soyisim,dgm_trh,yıl=calısan1#bu sekilde parcalara ayrılabilir
print(isim)

#demetlerde 2 tane fonksiyon kullanabiliriz 
#ilki count() fonksiyonudur. Bu fonksiyon demet içinde girilen elemanın kaç defa tekrar ettiğini verir
print(calısan1.count(1998))
  # diğer fonksiyon ise index() fonksiyonudur
  # bu fonksiyon elemanın kaçıncı indekste olduğunu verir
  #olmayan bir eleman girersen hata verir
print(calısan1.index("ayse"))


demet=(1)# bu şekilde bir tanımlama tuple yazmaz yani tek elemanlı bir tuple oluştururken bu hatalıdır tuple değil int olur
print(type(demet))
demet=3#bir int değer olduğu için içindeki değeri değiştirebildik
print(demet)

#tek elemanlı bir tuple tanımlamak istiyorsak 
demet1=(1,)
print(type(demet1))