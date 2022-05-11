"""
a01707267
Erick Eduardo Bautista Acosta
Ciclo while
ejercicio 1

Divisores propios
Los divisores propios de un número n son aquellos divisores
positivos menores que n.

Un número entero positivo n se dice que es perfecto si la
suma de sus divisores propios es igual a n.

Realiza un programa que lea un número y muestre un mensaje
indicando si es perfecto o no."""

n=int(input("dame un numero entero positivo "))
cont=0
b=0
if n>0:
    while cont<n:
        cont=cont+1
        a= n%cont
        if a==0 and cont<n:
            b=b+cont
        else:
            b=b

    if b==n:
        print(n,"es un numero perfecto")
    elif b<n or b>n:
        print(n,"no es perfecto")
else:
    print("este dato no es valido")