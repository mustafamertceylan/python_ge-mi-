calisanlar={"mert":"yazilim","ahmet":"siber güvenlik","enes":"boş işler müdürü"}
print(calisanlar["ahmet"])
calisanlar["meric"]={"dangalaklık departmanı"}#bu satırda yeni bir eleman ekledik
print(calisanlar)
calisanlar["meric"]={"bos gezenin bos kalfasi"}#sözlükteki veriyi değiştirmeye yarar
print(calisanlar)
del calisanlar["meric"]#del fonksiyonu silme görevi görür
print(calisanlar)

print(calisanlar.keys())# buradaki anahtarlar aslında ilk değerler yani primery keyler olarak düşünülebilir
print(calisanlar.values())# bu satır ise anahtarların tuttuğu değerleri gösterir
print(calisanlar.items())#sözlükteki anahtar değer çiftlerinin ekrana bastırır

# calisanlar.clear()    sözlüğü temizler

kisi=input("sorgulanacak ismi giriniz")
print(calisanlar.get(kisi,"sorgulanan isim bulunamadi"))
# get() fonksiyonu ile aranılan kelimenin sözlükte olup olmadığı kontrol edilir  
# yoksa hata mesajı döndürür. Eğer varsa sözlükteki değeri döndürülür
