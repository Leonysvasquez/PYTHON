import os

def cls():
    os.system('cls')

cls()

Estudiantes=['ANTHONY','BRADY','BEYKER','JOSE','JAZER',
'JIMMY','MANUEL','RAMSES','WILMER','LEONYS']

seleccion=input('1.AGREGAR \n2.MODIFICAR\n3.BORRAR\nQUE DESEA HACER: ' )

if seleccion ==1:
    cls()
A=int(input('Cuantos Estudiantes quiere agregar: '))
cls()
for i in range(A):
    Estudiante=input('Estudiante :')
Estudiantes.insert(Estudiante) 
print(Estudiantes)
















