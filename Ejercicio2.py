#Programa que acepte 3 angulos de un triangulo: Rectángulo, Acutángulo u Obtusángulo.  

a = float(input("Ingrese un angulo: "))

if(a == 90): 
    print("El triangulo es rectangulo")
elif(a < 90):
    print("el triangulo es Acutángulos ")
elif(a > 90):
    print("el triangulo Obtusángulo ")