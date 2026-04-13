#while :
#    islem1
#    islem2
#    islem3
#   islem4 -------->islem4 while döngüsünün icinde yer almamaktadir.yani hizalama onemlidir
for i in range(5,25,3):#range fonksiyonu ile 3er 3er atlayarak 5ten 25e kadar olan sayilari yazdirdik
    print(i)
for harf in "marmara":
    if harf=='r':
        break#her zaman kullanılan break deyimi kosul sağlanırsa döngü biter
        #continue deyimi dongunun o anki iterasyonunu atlar
    print(harf)    