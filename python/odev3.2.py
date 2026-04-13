def sehirleri_grupla(sehirler):
    kitalar={}
    for sehir in sehirler:
        kita=sehirler[sehir]['kıta']
        if (kita in kitalar):
            kitalar[kita].append(sehir)
        else:
            kitalar[kita]=[sehir]
    print(kitalar)

#ana program
cities = {
    'Istanbul': {'population': 15000000, 'kıta': 'Europe', 'country': 'Turkey'},
    'Tokyo': {'population': 37000000, 'kıta': 'Asia', 'country': 'Japan'},
    'New_york': {'population': 8400000, 'kıta': 'North America', 'country': 'United States'},
    'Mumbai': {'population': 20000000, 'kıta': 'Asia', 'country': 'India'},
    'Cairo': {'population': 20000000, 'kıta': 'Africa', 'country': 'Egypt'},
    'Seoul': {'population': 9765000, 'kıta': 'Asia', 'country': 'South Korea'},
    'London': {'population': 8908081, 'kıta': 'Europe', 'country': 'United Kingdom'},
    'Samsun (KİNG OF THE NORTH)':{'population':1335736,'kıta':'Asia','country':'Türkiye Cumhuriyeti'}
}
sehirleri_grupla(cities)