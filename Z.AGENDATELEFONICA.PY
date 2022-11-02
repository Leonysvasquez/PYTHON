import os
import pandas as pd 

def cls():
     os.system('cls')
cls()
print('AGENDA TELEFONICA')

INFO=[]
def AGREGAR():
  PERSONA=[]
  PERSONA.append(input("INGRESAR NOMBRE: "))
  PERSONA.append(input("INGRESAR APELLIDO :"))
  PERSONA.append(input("INGRESAR TELEFONO :"))
  PERSONA.append(input("INGRESAR CORREO ELETRONICO"))
  PERSONA.append(input("INGRESAR FECHA DE NACIMIENTO"))
  PERSONA.append(input("INGRESAR USAURIO DE INSTAGRAM"))
  PERSONA.append(input("INGRESAR COMENTARIO"))
  return PERSONA

def CONSULTAR():
    for PERSONA in INFO:
        print("NOMBRE: ", PERSONA[0])
        print("APELLIDO:",PERSONA[1])
        print("TELEFONO:",PERSONA[2])
        print("CORREO:",PERSONA[3])
        print("FECHA DE NACIMIENTO:",PERSONA[4])
        print("USER INSTAGRAM: ",PERSONA[5])
        print("COMENTARIO:",PERSONA[6])
        print('____________________________________________________________________________________________')

dtmp=pd.read_.csv('Contact.csv')
tmp=dtmp.value.tolist

for lin in tmp:
    t=[]
    t.append(lin[1])
    t.append(lin[2])
    t.append(lin[3])
    t.append(lin[4])
    t.append(lin[5])
    t.append(lin[6])
    t.append(lin[7])
    INFO.append(t)

def MENU():
    print('1.AGREGAR')
    print('2.CONSULTAR')
    print('3.MODIFICAR')
    print('4.ELIMINAR')
    print('5.SALIR')
    OP=input("Ingrese la opcion deseada : ")
    if OP=="1":
        INFO.append(AGREGAR())
        input("Se han guardado correctamente los conctactos.\nPresione enter para volver a menu")
        MENU()
    if OP=="2":
        CONSULTAR()
    
        
        

MENU()
