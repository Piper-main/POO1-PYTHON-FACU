"""
Escribir un programa que pida al usuario un número entero 
y muestre por pantalla si es un número primo o no
"""

numero = int(input("Ingrese un número entero: "))

if numero < 2:
    print("No es primo")
else:
    primo = True

    for i in range(2, numero):
        if numero % i == 0:
            primo = False
            break

    if primo:
        print("Es primo")
    else:
        print("No es primo")


input("Presioná ENTER para finalizar...")