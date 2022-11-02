import os
def cls():
    os.system("cls")  
cls()
print("De 0 kw a 200   precio 5.55","\n" "De 201 kw a 300 precio 7.88","\n" "De 301 kw a 700 precio 11.46","\n" "Mayor  701 kw a  precio 11.68")
KLOW=int(input("Ingrese la cantidad de KiloWatts consumido: "))
N1,B1,N2,B2,N3,B3,N4,B4=0,0,0,0,0,0,0,0
cls()
if KLOW > 200:
    N1 = 200*5.55
    B1 = 200
    if KLOW >200 and KLOW <=300:   
        N2 = (KLOW-200)*7.88
        B2 = KLOW-200
    else:
        N2 = 100*5.55
        B2=100    
        if KLOW >300 and KLOW <=700:
            N3 = (KLOW-300)*11.46
            B3 = KLOW-300
        else:
            N3 = 400*11.46
            B3 = 400
            if KLOW >=701:
                N4 = (KLOW-700)*11.68
                B4 = KLOW-700
else:
    N1 = KLOW*5.55
    B1 = 200
    TOTAL=N1+N2+N3+N4
print(B1,'KWH X 5.55  RD$',N1)
print(B2,'KWH X 7.88  RD$',N2)
print(B3,'KWH X 11.46 RD$',N3)
print(B4,'KWH X 11.68 RD$',N4)
print('El total de kwh a pagar es de: ', TOTAL)