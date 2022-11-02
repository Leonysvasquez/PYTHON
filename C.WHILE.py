
import os
def cls():
 os.system('cls')


cls()
print("Hace un programa que seleccione tres opciones de un menu.")

print("OPCION 1:"  + "IMPRIMIR DEL 1 AL 50")
print("OPCION 2:"  + "IMPRIMIR DEL 1 AL 20")
print("OPCION 3:"  + "SALIR")

i=0
seleccion=int
seleccion=input( 'Que opcion desea hacer: \n OPCION 1 \n OPCION 2 \n OPCION 3 \n')
if seleccion=='1':   
  while i<=50:
    print(i)
    i+=10

elif seleccion =='2':
  while i<=20:
    print(i)
    i+=5
  
elif seleccion=='3':
  print('Gracias por utilizar el programa')
  input('Presione enter  para salir') 

else:
  print('Por favor seleccione una opcion')
  input('Presione enter para salir')