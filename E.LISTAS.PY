#CREAR LISTAS 

import os
def cls():
    os.system('cls')


cls()
Estudiantes=['ANTHONY','BRADY','BEYKER','JOSE','JAZER',
'JIMMY','MANUEL','RAMSES','WILMER','LEONYS']
frutas=["MANGO","FRESA","GUINEO",'MANZANA ',' NARANJA' ,'PERA']
cantidades=['1','2','3',"4","5","6","7","8","9","10"]
matriz=[[1,2,4],[4,5,6],[7,8,9]]
print(frutas)
print(cantidades)
print(matriz)
print(Estudiantes)

#CREANDO LISTA CON EL TECLADO
"""Estudiantes=[]
e=int(input("Cuantos estudiantes quiere agregar a la lista: "))
for i in range(e):
    Estudiante=input("Estudiante: ")
    Estudiantes.append(Estudiante)
print(Estudiantes)
"""
#Remplezar elementos
Estudiantes[0]='LEONYS'
print(Estudiantes)
Estudiantes[-1]='LEONYS'
print(Estudiantes)
Estudiantes[1:3]='LEONYS','ANTHONY'
print(Estudiantes)
Estudiantes[1:3]=[]
print(Estudiantes)
Estudiantes[0:7]=[]
print(Estudiantes)
del Estudiantes[0]
print(Estudiantes)
Estudiantes=['ANTHONY','BRADY','BEYKER','JOSE','JAZER',
'JIMMY','MANUEL','RAMSES','WILMER','LEONYS']
print(Estudiantes)
Estudiantes.remove('ANTHONY')
print(Estudiantes)

#INSERTAR 
Estudiantes=['ANTHONY','BRADY','BEYKER','JOSE','JAZER',
'JIMMY','MANUEL','RAMSES','WILMER','LEONYS']
print(Estudiantes)
Estudiantes[5:5]=['ELVIS', 'KENDRA','MEL']
print(Estudiantes)
Estudiantes.insert(13,"MARIA")
print(Estudiantes)
#COPIAS LISTAS
Estudiantes2=Estudiantes.copy()
print(Estudiantes2)
Estudiantes3=Estudiantes[:]
print(Estudiantes3)

#POP :ELMINAR ELEMENTOS
Estudiantes3.pop()
print(Estudiantes3)
Estudiantes3.pop(12)
print(Estudiantes3)
Estudiantes.extend(Estudiantes3)
print(Estudiantes)
Estudiantes2.clear()
print(Estudiantes2)

#Modificar valores de una lista
r=['A','B','C','D','E']
for i ,letra in enumerate(r):
    r[i]=letra.lower() 
print(r)


