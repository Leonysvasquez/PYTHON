import os 

def cls():
    os.system("cls")

cls()
 
def dolares():
    dolar=55.5
    pesos=int(input('Ingrese la cantidad de pesos a converitir'))
    resultado= pesos/dolar
    print(round(resultado,2))

def euros():
    euros=57
    pesos=int(input('Ingrese la cantidad de pesos a converitir'))
    resultado= euros/pesos
    print(round(resultado,2))

def colombianos():
    colombiano=0.15
    pesos=int(input('Ingrese la cantidad de pesos a converitir'))
    resultado=colombianos/pesos
    print(round(resultado,2))

seguir=True

while seguir:
    print("**Welcome Bank*")
    print("Cambio de divisas \n")
    print("[1] Pesos dominicanos a Dolares ")
    print("[2] Pesos dominicanos a Euros ")
    print("[3] Pesos dominicanos a Pesos Colombianos ")
    print("[4] Salir")

    convertir=int(input('Ingrese la moneda que desea convertir :'))
    
    if convertir==1:
        dolares()
        print('-------------------------------------------------------------------------------------------------------------------------------')
    elif convertir==2:
        euros()
        print('-------------------------------------------------------------------------------------------------------------------------------')
    elif convertir==3:
        colombianos()
        print('-------------------------------------------------------------------------------------------------------------------------------')
    elif convertir==4:
        seguir=False
        print('Gracias por utilizar el programa')
        input('Presione enter para salir')
    else:
        print('Por favor escriba la  moneda que quiere convertir')
        input("Presione enter para volver. ")
        print('-------------------------------------------------------------------------------------------------------------------------------')
   
