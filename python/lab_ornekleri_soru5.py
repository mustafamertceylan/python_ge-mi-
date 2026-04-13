tuple=(1,1,2,3,4,4,5,5,9,9)
sayac=0
for i in range(0,10):
    for j in range(0,10):
        if tuple[i]==tuple[j]:
            sayac+=1
    print(f"{i+1}. elemandan {sayac} tane var")
    sayac=0
    