"""
Escribir un programa que pregunte el nombre completo del usuario en la 
consola y después muestre por pantalla el nombre completo del usuario 
tres veces, una con todas las letras minúsculas, otra con todas las letras 
mayúsculas y otra solo con la primera letra del nombre y de los apellidos 
en mayúscula. El usuario puede introducir su nombre combinando mayúsculas 
y minúsculas como quiera.
"""

nombre = input(" ¿Cual es tu nombre?: ")

print(nombre.upper()) # .upper() hace todas mayucuslas.
print(nombre.lower()) # .lower() hace todas minusculas.
print(nombre.title()) # .Title() hace las primeras letras mayusculas.
                      # .capitalize() hace mayuscula solo el primer caracter de toda la cadena.
                      # .replace('o', 'x') lleva 2 argumentos el primero el que quiero remplazar. 
                                          # y el segundo por el que lo voy a remplazar.
                      # .split() lleva 1 argumento, sirve para separa la cadena cuando encuenta ese argumento.