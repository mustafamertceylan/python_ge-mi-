yazi=["ahmet","altı","yasında","zeynep","dört","yasında","esra","iki","ayse","bir","yasında"]
sayilar={"bir":"1","iki":"2","üç":"3","dört":"4","bes":"5","altı":"6","yedi":"7","sekiz":"8","dokuz":"9"}
eleman_sayisi=0
for i in yazi:
    eleman_sayisi+=1

for i in range(eleman_sayisi):
    if yazi[i] in sayilar:
        yazi[i]=sayilar[yazi[i]]
print(yazi)