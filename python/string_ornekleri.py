message=" ornek cumle "
print(message.strip())#string ifadenin başında ve sonundaki boşlukları kaldırır
print(message.lstrip())#stringin başındaki boşlukları ve istenmeyen karakterleri kaldırır
print(message.rstrip())#stringin sonundaki boşlukları ve istenmeyen karakterleri kaldırır
print(message*2)
message_2="marmara "
print("metnimiz %s ve %s olarak iki tanedir"%(message,message_2))
print("metnimiz "+message+" ve "+message_2+" olarak iki tanedir")
sayi=5
print(oct(sayi))#girilen sayının 8 lik tabanda karşılığını verir
print(hex(sayi))#girilen sayının 16 lık tabanda karşılığını verir
print(bin(sayi))#girilen sayının binary karşılığını verir