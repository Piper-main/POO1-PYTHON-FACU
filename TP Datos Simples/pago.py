# Escribir un programa que pregunte al usuario por el número de horas 
# trabajadas y el coste por hora. Después debe mostrar por pantalla 
# el pago que le corresponde.

hora = int(input("Cuantas horas trabajo?: "))
costo = int(input("Cual es el costo por hora?: "))

pago= hora*costo

print("el pago correspondiente es: ", pago)
print()
input("Presioná ENTER para finalizar...")