import os
from peewee import *
import simpleaudio as sa
from prettytable import PrettyTable
import webbrowser

mydb = SqliteDatabase('duro.sqlite')

class Alumno(Model):
    matricula = CharField(20)
    nombre = CharField(15)
    apellido = CharField(15)
    N1 = IntegerField()
    N2 = IntegerField()
    
    class Meta: 
        database = mydb
    
mydb.connect()

mydb.create_tables([Alumno])

def cls():
    os.system('cls')

def repro(audio):
    obj = sa.WaveObject.from_wave_file(f"audios/{audio}")
    obj.play()
    
def calEQ(Nota):
    eq = "F"
    if (Nota>= 90):
        eq = "A"
    elif(Nota>= 80):
        eq = "B"
    elif(Nota>= 70):
        eq = "C"
    return eq

def mostrarA():
    xb = PrettyTable()
    xb.field_names = ["Id", "Matricula", "Nombre", "Apellido", "N1", "N2", "Promedio", "Eq"]
    for alum in Alumno.select():
        pro = (alum.N1+alum.N2)/2
        xb.add_row([alum.id, alum.matricula, alum.nombre, alum.apellido, alum.N1, alum.N2, pro, calEQ(pro)])
    return(xb)
    
def agregar():
    cls()
    print("Ahora procederas agregar al alumno ")
    alum = Alumno()
    alum.matricula = input("Digite la matricula: ")
    alum.nombre = input("Digite el nombre: ")
    alum.apellido = input("Digite el apellido: ")
    alum.N1 = input("Digite la nota 1: ")
    alum.N2 = input("Digite la nota 2: ")
    alum.save()
    repro('agreg.wav')
    input("Este alumno ha sido guardado con exito.....presiona enter para salir")
    
  
def condato(campo, valor):
    print("El campo", campo, "El valor", valor)
    dmd = input("Digite el valor o dejelo en blanco para no editar: ")
    if dmd == "":
        return valor 
    else:
        return dmd
    
 
def modificar():
    cls()
    print("Procede a digitar el id del alumno que quieres modificar")
    print(mostrarA())
    Ido = input("Digite el id que quieres editar, y si no quieres modificar pon e: ")
    if Ido == "e":
        return False
    alum = Alumno.select().where(Alumno.id == Ido).get()
    
    alum.matricula = condato('Matricula', alum.matricula)
    alum.nombre = condato('nombre', alum.nombre)
    alum.apellido = condato('apellido', alum.apellido)
    alum.N1 = int(condato('Nota 1', str(alum.N1)))
    alum.N2 = int(condato('Nota 2', str(alum.N2)))
    alum.save()
    repro('modifi.wav')
    input("La ediccion ya esta guardada.. presiona enter para salir")
    
def borrar():
     cls()
     print("Digite el id del alumno que quieres eliminar")
     print(mostrarA())
     Ido = input("Digite el id y si no quieres eliminar pon e: ")
     if Ido == "e":
         return False
     alum = Alumno.select().where(Alumno.id == Ido).get()
     alum.delete_instance()
     repro('borrar2.wav')
     input(f"El alumno {alum.matricula} => {alum.nombre} ha sido eliminado.... presiona enter para salir")
     
     
def exportar():
    datos = mostrarA()
    t_html = datos.get_html_string()
    
    t_html = t_html.replace('<table>', '<table class = "table table-striped table-bodered">')
    html = f""" 
    <!doctype html>
    <html lang="en">
         <head>
         <title> Alumnos </title>
          <meta charset="utf-8">
          <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
         </head>
    
         <body>
            <div class = 'container'>
             <h3> Datos de los Alumnos exportados: </h3>
              {t_html}
            </div>
         </body>
    </html>
    """
    b = open('exportar.html', 'w')
    b.write(html)
    b.close()
    webbrowser.open('exportar.html')
    input("Presione enter para salir")