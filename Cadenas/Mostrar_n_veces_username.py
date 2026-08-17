"""
Escribir un programa que pregunte el nombre del usuario en la consola y un
número entero e imprima por pantalla en líneas distintas el nombre del usuario
tantas veces como el número introducido

"""

nombre = input(" Ingresa tu nombre: ")

num = int(input(" Ingresa un numero: "))

for n in range(num):
    print(f"{nombre}")