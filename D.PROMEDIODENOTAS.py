n=int(input('ingrese la cantidad de notas a promediar'))
suma=0
i=1
while (i <= n):
    print('Ingrese la nota numero',i)
    nota=float(input())
    suma=suma+nota
    i+=1
prom=suma/n
print('El promedio de nota es ',prom)