girdi=input("kare mi daire mi")
if girdi=="kare":
    kenar=int(input("karenin kenar alanını giriniz"))
    kare(kenar)
else:
    cap=int(input("yarıcapı giriniz"))
    cember(cap)

def kare(kenar)
    alan=kenar*kenar
    cevre=kenar*4
    print(f"alan {alan} cevre {cevre}")
def cember(cap):
    alan=float(cap*cap*3.14)
    cevre=(float)2*3.14*cap
    print(f"alan {alan} cevre {cevre}")