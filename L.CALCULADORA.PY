import os
def cls():
    os.system('cls')
cls()
def suma(A,B):
    return A+B

def resta(A,B):
    return A-B

def multiplicar(A,B):
    return A*B

def Division(A,B):
    return A/B
print("CALCULADORA")
Numero1=float(input('Ingrese el primer numero'))
if '' in Numero1:
    input('Por favor ingrese un numero.\nPresione enter para volver ')
    Numero1=float(input('Ingrese el primer numero'))

Numero2=float(input('Ingrese el segundo numero'))
if '' in Numero2:
    input('Por favor ingrese un numero.\nPresione enter para volver ')
    Numero1=float(input('Ingrese el primer numero'))

operacion=int(input("Ingrese el numero de la operacion: \n1.Suma\n2.Resta\n3.Multiplicacion\n4.Division\n5.SALIR\n"))
if operacion==1:
    print('El resultado es:',suma(Numero1,Numero2))

elif operacion==2:
    print('El resultado es:',resta(Numero1,Numero2))

elif operacion==3:
    print('El resultado es:',multiplicar(Numero1,Numero2))

elif operacion==4:
    print('El resultado es:',Division(Numero1,Numero2))

elif operacion==5:
    print('Gracias por utilizar el programa')
    input ('Presione enter para volver')
    operacion=int(input("Ingrese el numero de la operacion: \n1.Suma\n2.Resta\n3.Multiplicacion\n4.Division\n5.SALIR\n"))
if operacion >5:
    input('Por favor eliga una de las opciones dadas.\nPresione enter para volver a la caludora basica')

    operacion=int(input("Ingrese el numero de la operacion: \n1.Suma\n2.Resta\n3.Multiplicacion\n4.Division\n5.SALIR\n"))
    
