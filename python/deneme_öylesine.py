def yaz():
    toplam=0
    for i in range(1,20):
        if(toplam<=100):
            toplam+=i
        elif (toplam>100):
            print("toplam",toplam)
            break
        

        
yaz()