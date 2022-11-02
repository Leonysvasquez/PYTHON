#Programa que acepte un numero, mostrar en la consola la tabla de multiplicar de manera

a = float(input("Ingrese un numero: "))

for i in range(1,11):
    print(f'{i} x {a} = {i*a}')
    