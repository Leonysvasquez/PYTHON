lista = ["Manuel", "Martin", "Brady", "Leonys", "Jazer"]
print(lista)

seleccion = input("Que acción desea hacer\nmodificar \nagregar \nborrar \n"  )

if seleccion == "agregar":
   agregar = input("Coloque el nombre de a quien quieres agregar")
   lista.append(agregar)
   print(lista)

if seleccion == "borrar":
   quitar = input("A quien deseas quitar")
   lista.remove(quitar)
   print(quitar, "ha sido eliminado", lista)

if seleccion == "modificar":
   modificar = input("Coloque a quien quiere sustituir")
   sustitucion = input("por quien lo quieres sustituir")
   lugar = int(input("Coloque en que posicion de la lista lo quieres coloca"))
   lista.remove(modificar)
   lista.insert(lugar,sustitucion)
   print(modificar, "ha sido sustituido por ", sustitucion, "\n",lista )