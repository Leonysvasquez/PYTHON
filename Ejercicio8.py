#Programa que permita saber si un año es bisiesto: debe ser divisible por 4, no debe ser visible por 100, excepto que también sea divisible por 400. 

a = int(input("Ingrese un año: "))
 
if(a%4== 0 ):
    if(a%100 != 0 ):
        print("El año es bisiesto")
        if(a/400 == 0):
            print("El año es bisiesto")
    else:
        print("El año no es bisiesto")
else:
    print("El año no es bisiesto")