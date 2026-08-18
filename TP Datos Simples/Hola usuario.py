"""
Escribir un programa que pregunte el nombre del usuario en la consola 
y después de que el usuario lo introduzca muestre por pantalla 
la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido
"""

nombre = input("cual es tu nombre?")

print(f"¡hola {nombre}!")

edad = int(input("ingrese su edad"))

print(f"tu edad es: {edad + 1}")

# poner f al principio y muestra dentro de las "" las variables poniendolas 
# dentro de {} llaves, 