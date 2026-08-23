"""
Leer dos valores numéricos enteros e indicar cual es el mayor 
y cual es el menor. Considerar que ambos valores son diferentes
"""

num1 = int(input(" Ingrese un valor: "))
num2 = int(input(" Ingrese otro valor: "))

if num1 > num2 :
    print(" El primer valor es mayor que el segundo")
elif num2 > num1:
    print(" El segundo valor es mayor que el primero")
else:
    print(" los 2 valores son iguales")
