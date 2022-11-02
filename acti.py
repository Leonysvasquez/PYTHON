#Persona que creo este programa:
#Elvis Nuñez, 2021-2144

from Funciones import *


seguir = True 

while seguir: 
    cls()
    
    repro('saludo.wav')
    
    print(""" 
       Saludos este programa fue hecho por Elvis Nuñez, 2021-2144
       Bienvenido al menu general, por favor selecciona la accion que quieres hacer
       1 - Agregar 
       2 - Modificar 
       3 - Borrar   
       4 - Exportar 
       5 - Salir 
          """)
    ho = input("Digite el que quieras usar: ")
    if ho == "1":
        repro('Agre.wav')
        agregar()
    elif ho == "2":
        repro('modi.wav')
        modificar()
    elif ho == "3":
        repro('borrar.wav')
        borrar()
    elif ho == "4":
        repro('expo.wav')
        exportar()
    elif ho == "5":
        seguir = False 
        repro('Bay.wav')
        input("BAY BAY Charli..... presiona enter para salir")
    else:
        repro('No.wav')
        input("Por favor amigo, digite un numero del 1 al 5 ")

