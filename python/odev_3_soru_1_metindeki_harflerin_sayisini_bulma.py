#metin alıcaz
#sözlük tanımla alfabeki harfleri içeren
#metni fonksiyona geçir
#fonksiyonun işlevi sözlüğü ekrana bastırmak

def bul(metin):
    harfler=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","v","y","z"]
    sayac=0
    for i in range(len(harfler)):
        for j in range(len(metin)):
            if harfler[i]==metin[j]:
                sayac+=1
        print(f"{harfler[i]} harfi metin icinde {sayac} kere tekrar etmektedir ")
        sayac=0
#ana program
metin=input("bir metin giriniz  ")
metin.lower()
bul(metin)
