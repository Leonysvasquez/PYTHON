import os
os.system('cls')

from tkinter import*
Ventana =Tk()
Ventana.title("Calculadora")

i=0
#Para reconocer todo los eventos que pasen ,todas las aplicaciones en tkinter deben de tener.
#Ventana.mainloop()

#ENTRADA 
e_texto=Entry(Ventana,font=("Calibri 20"))
e_texto.grid(row=0 , column=0,columnspan=4,padx=5,pady=5)


#Funciones
def click_botton(valor):
    global i
    e_texto.insert(i,valor)
    i+=1

def borrar():
    e_texto.delete(0, END)

def operaciones():
    ecuacion=e_texto.get()
    resultado=eval(ecuacion)
    e_texto.delete(0, END)
    e_texto.insert(0,resultado)
    i=0



#Botones 
boton1= Button(Ventana,text="1",width=5, height=2,command=lambda:click_botton(1))
boton2= Button(Ventana,text="2",width=5, height=2,command=lambda:click_botton(2)) 
boton3= Button(Ventana,text="3",width=5, height=2,command=lambda:click_botton(3))
boton4= Button(Ventana,text="4",width=5, height=2,command=lambda:click_botton(4))
boton5= Button(Ventana,text="5",width=5, height=2,command=lambda:click_botton(5))
boton6= Button(Ventana,text="6",width=5, height=2,command=lambda:click_botton(6))
boton7= Button(Ventana,text="7",width=5, height=2,command=lambda:click_botton(7))
boton8= Button(Ventana,text="8",width=5, height=2,command=lambda:click_botton(8))
boton9= Button(Ventana,text="9",width=5, height=2,command=lambda:click_botton(9))
boton0= Button(Ventana,text="0",width=13, height=2,command=lambda:click_botton(0))


botonBorrar= Button(Ventana,text="AC",width=5, height=2,command=lambda:borrar())
botonParentesis1= Button(Ventana,text="(",width=5, height=2,command=lambda:click_botton("("))
botonParentesis2= Button(Ventana,text=")",width=5, height=2,command=lambda:click_botton(")"))
botonPunto= Button(Ventana,text=".",width=5,height=2,command=lambda:click_botton("."))



botonSuma= Button(Ventana,text="+",width=5, height=2,command=lambda:click_botton("+"))
botonResta=Button(Ventana,text="-",width=5, height=2,command=lambda:click_botton("-"))
botonMultiplicacion= Button(Ventana,text="x",width=5, height=2,command=lambda:click_botton("*"))
botonDivision= Button(Ventana,text="÷",width=5, height=2,command=lambda:click_botton("/"))
botonIgual= Button(Ventana,text="=",width=5,height=2,command=lambda:operaciones())

#AGREGAR BOTONES EN PANTALLA 
botonBorrar.grid     (row=1,      column=0,     padx =5, pady= 5)
botonParentesis1.grid(row=1,      column=1,      padx =5, pady= 5)
botonParentesis2.grid(row=1,      column=2,      padx =5, pady= 5)
botonDivision.grid   (row=1,      column=3,      padx =5, pady= 5)

boton7.grid(row=2, column=0 , padx =5, pady= 5)
boton8.grid(row=2, column= 1, padx =5, pady= 5)
boton9.grid(row=2, column= 2 , padx =5, pady= 5)
botonMultiplicacion.grid(row= 2, column=3 , padx =5, pady= 5)

boton4.grid(row=3, column=0, padx =5, pady= 5)
boton5.grid(row=3, column=1 , padx =5, pady= 5)
boton6.grid(row=3, column=2 , padx =5, pady= 5)
botonSuma.grid(row=3, column=3, padx =5, pady= 5)

boton1.grid(row=4, column=0 , padx =5, pady= 5)
boton2.grid(row=4, column=1 , padx =5, pady= 5)
boton3.grid(row=4, column=2 , padx =5, pady= 5)
botonResta.grid(row=4, column=3,padx =5, pady= 5)



boton0.grid(row=5, column= 0,columnspan=2 , padx =5, pady= 5)
botonPunto.grid(row=5, column=2 , padx =5, pady= 5)
botonIgual.grid(row=5, column=3 , padx =5, pady= 5)


Ventana.mainloop()


