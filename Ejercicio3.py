#Programa que acepte la medida de los cuatro ángulos de una figura: Determinar si esta es un cuadrado. 

a = float(input("Ingrese un numero menor a 5: "))
    
b = a - 2 

c = b * 180 

d = c

e = c/4

print("La medida de los lados es de: ", e )

if(d == 360 ):
    print("Es un cuadrado ")
else:
    print("NO es un cuadrado ")
    



