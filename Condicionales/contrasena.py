"""
Escribir un programa que almacene la cadena de caracteres 
contraseña en una variable, pregunte al usuario por la 
contraseña e imprima por pantalla si la contraseña introducida 
por el usuario coincide con la guardada en la variable sin tener 
en cuenta mayúsculas y minúsculas
"""

con = "contraseña"

tex1 = input(" Ingrese la contraseña: ")

if con == tex1:
    print(" La contraseña coincide")
else:
    print(" La contrase NO coincide")
