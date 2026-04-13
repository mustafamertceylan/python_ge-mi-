metin=input("bir metin giriniz")
c=input("aranılan karakteri giriniz")
bulundu=False
for i in range(len(metin)):
    if c==metin[i]:
        print(f"{i}. indiste bulundu aranılan karakter {c}")
        bulundu=True
if bulundu==False:
    print("aranılan eleman bulunamadı")
    
