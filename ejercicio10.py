#programa que acepte un nombre, apellido, telefono y email. Guarde estos datos en un archivo html bonito, con colores en su computadora y luego muéstrelo en el navegador.

import webbrowser
import requests


url = "https://randomuser.me/api/?results=1"

datos = requests.get(url).json()

nom = print("nombre: ", datos["results"][0]["name"]["first"])
ape = print("apellido: ", datos["results"][0]["name"]["last"])
tele = print("telefono", datos["results"][0]["phone"])
ema = print("email: ", datos["results"][0]["email"])

html = """
<html>
      <head>
     
       <title> Ejercicio 10 </title>
     
       <meta charset = utf-8>
       </head>
     
     
     <body>
     
      <h1> Datos Personales </h1>
     
      <h2> Nombre </h2>
      <h3> @nom </h3>
      <h2> Apellido </h2>
      <h3> @ape </h3>
      <h2> telefono </h2>
      <h3> @tele </h3>
      <h2> email </h2>
      <h3> @ema</h3>
     </body>
     
 </html> """

html = html.replace('@nom', nom)
html = html.replace('@ape', ape)
html = html.replace('@tele', tele)
html = html.replace('@ema', str(ema))


archi = open('ejercicio10.html', 'w')
archi.write(html)
archi.close()
webbrowser.open('ejercicio10.html')
