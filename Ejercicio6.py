#Programa que acepte un numero, mostrar los números comprendidos desde el hasta el 1 de manera descendente.

a = int(input("Ingrese un numero: "))

for contador in range( a, 0, -1):
    print(contador)
