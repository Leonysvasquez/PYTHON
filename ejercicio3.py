#Programa que cargue los datos de un usuario, mostrar el nombre, apellido y fecha de nacimiento de la persona

import requests

url = "https://randomuser.me/api/?results=1"

data = requests.get(url).json()


print("nombre: ", data["results"][0]["name"]["first"])
print("apellido: ", data["results"][0]["name"]["last"])
print("fecha de nacimiento: ", data["results"][0]["dob"]["date"])





