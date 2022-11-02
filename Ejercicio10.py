#Programa que solicite un numero, luego lea la siguiente url: https://randomuser.me/api/?results=10, cambiando el 10 por el numero que digito el usuario, luego mostrar en HTML el nombre, apellido y foto de cada persona. Indicar al final cuantas personas hay por genero. 

import webbrowser
import requests

he = input("Digite la cantidad de personas que quieres ver: ")

datos = requests.get("https://randomuser.me/api/?results="+he).json()

circulitos = []
hombres = 0
mujeres = 0 

for persona in datos["results"]:
     if persona ['gender'] == 'male' :
         hombres = hombres + 1
     else:
         mujeres = mujeres +1 
         
     fila = f""" 
         <div>
             <div>
             <img src="{persona['picture']['large']}"/>
             </div> 
             
             {persona['name']['first']}
             {persona['name']['last']}
             ({persona['gender']})
         </div>""" 
     circulitos.append(fila)
     
todas = "".join(circulitos)
html = """ 
    <html>
        <head>
         <meta charset ="utf-8">
        
         <title> Ejercicio 10 </title>
        </head>

        <body>
            <div>
              #personas
            </div>
         
            <div>
              Mujeres: #mujeres  Hombres: #hombres Total: #total
            </div>
        </body>
    </html>
"""
html = html.replace('#personas', todas)
html = html.replace('#mujeres', str(mujeres))
html = html.replace('#hombres', str(hombres))
html = html.replace('#total', str(hombres + mujeres))


f = open('ejercicio10.html', 'w', encoding= 'utf-8')
f.write(html)
f.close()

webbrowser.open('ejercicio10.html')