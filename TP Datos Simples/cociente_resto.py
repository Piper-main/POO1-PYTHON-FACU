# Escribir un programa que pida al usuario dos números enteros y muestre 
# por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde 
# <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el 
# cociente y el resto de la división entera respectivamente

n = int(input("Introduce un numero: "))
print()
m = int(input("Introduce otro numero: "))
print()

c= n//m 

r=n%m

print("El cociente entre", str(n)," y",str(m),"es: ", c)
print()
print("El resto entre", str(n)," y",str(m),"es: ", r)
print()
input("Presioná ENTER para finalizar...")
