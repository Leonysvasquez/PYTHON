#Programa que acepte una palabra o frase en español, busque esta en la wikipedia y muestre el resumen de lo encontrado.

import wikipedia

wikipedia.set_lang("es")

print(wikipedia.summary("dragon ball"))
