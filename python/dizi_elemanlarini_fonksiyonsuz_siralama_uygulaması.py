sayilar=[1,8,17,2,3,78,98]
boyut=len(sayilar)
for i in range(0,boyut):
    for j in range(i+1,boyut):
        if sayilar[i]>sayilar[j]:#buradaki büyüktür isaretini kucuktur yaparsak buyuktten kucuge sıralar
            gecis_elemani=sayilar[i]
            sayilar[i]=sayilar[j]
            sayilar[j]=gecis_elemani
print(sayilar)