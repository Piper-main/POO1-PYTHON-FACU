"""
Escribir un programa que pregunte el nombre del usuario en la consola y después
de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras,
donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de
letras que tienen el nombre
"""

nombre = input(" ¿cual es tu nombre?: ")
lon = len(nombre) 
""" len() recibe un argumento entre parentesis, el nombre de la variable que
    que queremos contar sus caracteres, luego guardamos ese conteo en otra variable
    para luego poder utilizarla
"""


print(f"{nombre.upper()} tiene {lon} letras")