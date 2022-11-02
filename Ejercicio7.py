#Programa que acepte una frase, determinar la cantidad de vocales que contiene la misma.

frase = input("Escribe una frase: ")

b = 0 
for i in frase:
    if i in "aeiou":
        b = b+1
print("La cantidad de vocales son: ", b)
        