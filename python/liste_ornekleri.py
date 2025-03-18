sehirler=["samsun","sakarya","istanbul","adana","mugla","adıyaman"]
print(sehirler[-1])#-1 sonuncu elemanı -2 sondan bir önceki elemanın indisiymiş bu şekilde de devam etmekteymiş
#print(sehirler[-7]) eleman sayısı kadar - li deger varmış
print(sehirler[2:5])#5. index dahil edilmezmiş başlangıçtan sondan 1 öncekine kadar olanları yazdırır
print(sehirler[:3])#3. indexe kadar olanları bastırır
print(sehirler[2:])#baslangıçtan sona kadar olan elemanları bastırır
sehirler[7:7]=["Gaziantep","Şanlıurfa"]#eğer indexler aynı olursa eleman ekleyeceğimiz anlamına geliyormuş
print(sehirler)
sehirler[3:3]=["hatay","Kahramanmaraş"]#eklemeyi ortadan yaptık
print(sehirler)
