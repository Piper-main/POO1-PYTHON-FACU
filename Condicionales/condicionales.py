"""Leer tres valores numéricos enteros, indicar cual es el mayor, cuál es el del medio 
y cuál el menor. Considerar que los tres valores son diferentes.
"""
menor = 0
medio = 0
mayor = 0

a = int(input("Ingrese el primer valor entero: "))
b = int(input("Ingrese el segundo valor entero: "))
c = int(input("Ingrese el tercer valor entero: "))

if a < b and a < c:
    menor = a
elif b < a and b < c:
    menor = b
else:
    menor = c

if a > b and a > c:
    mayor = a
elif b > a and b > c:
    mayor = b
else:
    mayor = c

if a != menor and a != mayor:
    medio = a
elif b != menor and b != mayor:
    medio = b
else:
    medio = c

print(f"El menor es {menor}")
print(f"El medio es {medio}")
print(f"El mayor es {mayor}")

input("Presioná ENTER para finalizar...")