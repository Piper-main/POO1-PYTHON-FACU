
# Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato
# dd/mm/aaaa y muestra por pantalla, el día, el mes y el año
print()
print()
print(" =========================================================")
print(" Ingres abajo su fecha de nacimiento en formato dd/mm/aaaa")
print(" =========================================================")
fecha = input(" -- Fecha de Nacimiento--:  ")

lista = fecha.split('/')
print()
print(" =====================")
print(f" El dia es: {lista[0]}")
print(f" El mes es: {lista[1]}")
print(f" El año es: {lista[2]}")
print(" =====================")
print()

