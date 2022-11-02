import os

def cls():
    os.system('cls')

cls()

SEGUIR= True

while SEGUIR:
    print("**Welcome Bank*")
    print("Cambio de divisas \n")
    print("[1] Pesos dominicanos a Dolares ")
    print("[2] Pesos dominicanos a Euros ")
    print("[3] Pesos dominicanos a Colombianos ")
    print("[4] Salir")
    

    converitr=int(input('A que moneda  desea  convertir :'))

    pesos=float(input('Cuantos pesos desea converitr :'))

    if converitr==1:
        resultado=pesos*0.018
        print("{} Pesos equivales a {} Dolares".format(pesos,resultado))
        print('-------------------------------------------------------------------------------------------------------------------------------')
        
    elif converitr==2:
        resultado=pesos*0.017
        print("{} Pesos equivale a {} Euros".format(pesos,resultado))
        print('-------------------------------------------------------------------------------------------------------------------------------')
        

    elif converitr==3:
        resultado=pesos*68.15
        print("{} Pesos equivale a {} Colombianos".format(pesos,resultado))
        print('-------------------------------------------------------------------------------------------------------------------------------')
    
    elif converitr==4:
        SEGUIR=False
        print('Gracias por utilizar el programa')

        input('Presione enter para salir')
        
    
    else:
        print('Por favor escriba la  moneda que quiere convertir')
        input("Presione enter para volver a convertidor. ")
        print('-------------------------------------------------------------------------------------------------------------------------------')
        

  




















