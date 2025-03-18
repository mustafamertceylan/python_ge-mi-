import math
a=int(input("a katsayısını giriniz"))
b=int(input("b katsayısını giriniz"))
c=int(input("c sabit sayısını giriniz"))
delta=b*b-4*a*c
x1=(-b-math.sqrt(delta))/2*a
x2=(-b+math.sqrt(delta))/2*a
if delta<0:
    print("Girilen katsayılar sonucu denklemin reel kökü yoktur")
elif delta==0:
    print(f"Girilen katsayılar sonucu denklemin çift katlı kökü vardır ve kökü {x1}")
else:
    print(f"Girilen katsayılar sonucu denklemin birbirinde farklı 2 reel kökü vardır x1= {x1} x2= {x2}")