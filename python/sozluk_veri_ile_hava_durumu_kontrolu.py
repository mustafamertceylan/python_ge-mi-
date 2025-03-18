soru=input("hangi sehirin hava durumunu öğrenmek istiyorsun")
cevap={"samsun":"dört dörtlük","izmir":"gavur hamamı gibi","istanbul":"yaşanabilir","erzurum":"insanından ne hayır gördükde havasını soruyon"}
print(cevap.get(soru,"girilen sehire ait hava durumu bilgisi mevcut değildir"))