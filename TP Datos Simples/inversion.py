# Escribir un programa que pregunte al usuario una cantidad a invertir,
# el interés anual y el número de años, y muestre por pantalla el capital 
# obtenido en la inversión

dinero = int(input(" Cual es la cantidad a invertir: "))
print()
interes = int(input(" Cual es el interes anual: "))
print()
años= int(input(" A cuantos años es la inversion: "))
print()


for n in range(años):
    i = (dinero * interes) / 100
    dinero = dinero + i

print(f"El capital obtenido es:{dinero:.2f}")

input("Presioná ENTER para finalizar...")

# variable + .2f entre corchetes muestra 2 numeros despues de la coma