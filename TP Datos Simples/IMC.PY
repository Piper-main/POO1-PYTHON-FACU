# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
# calcule el índice de masa corporal y lo almacene en una variable, y muestre por 
# pantalla la frase: Tu índice de masa corporal es <imc> donde <imc> es el índice 
# de masa corporal calculado redondeado con dos decimales

p = int(input("indique su peso: "))

print()

a = int(input("Indique su altura en Metros: "))

imc = p / (a*a)

print()