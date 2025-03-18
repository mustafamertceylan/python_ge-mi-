sayi=100
while sayi<1000:
    sayi1=sayi
    birler_basamagi=sayi%10
    sayi1/10
    onlar_basamagi=sayi1%10
    sayi1/10
    yuzler_basamagi=sayi1
    if birler_basamagi+yuzler_basamagi-onlar_basamagi>0:
        print(sayi1)
    sayi+=1

