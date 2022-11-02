#Programa que acepte 3 números, indique en que posición (según el orden que se ingresan) están el mayor y el menor. Si hay un empate debe especificarlos. 

n1 = float(input("Ingrese el numero 1 : "))
n2 = float(input("Ingrese el numero 2 : "))
n3 = float(input("Ingrese el numero 3 : "))

if(n1>n2>n3):
    print("el numero mayor es: ", n1)
else:
    if(n2>n3):
        print("el numero mayor es: ", n2)
    else:
        print("el numero mayor es: ", n3)

if(n1<n2<n3):
    print("el numero menor es: ", n1)
else:
    if(n2<n3):
        print("el numero menor es: ", n2)
    else:
        print("el numero menor es: ", n3)