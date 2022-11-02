#Programa que acepte 3 lados de un triangulo, indique si este es equilatero, Isósceles, Escaleno.

a = float(input("Ingrese un numero: "))
b = float(input("Ingrese otro numero: "))
c = float(input("Ingrese otro numero: "))


if(a==b and b==c):
    print("El triangulo es Equilatero")
if(a==b or b==c or c==a ):
    print("El triangulo es Isosleceles")
else:
    print("El Triangulo es Escaleno ")
    

        
