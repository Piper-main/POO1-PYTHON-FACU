
# Escribir un programa que pregunte por consola el precio de un producto en pesos
# con dos decimales y muestre por pantalla el número de pesos y el número de
# centavos del precio introducido

precio = input(" Ingrese el precio con 2 decimales: ")

lista = precio.split('.')  # .split() divide la cadena donde esta '.' y crea una lista.

lista1 = len(lista[0]) # almaceno en una variable lo que obtengo de contar con len(lista[0]) en la primer cadena de la lista creada
lista2 = len(lista[1]) # almaceno en una variable lo que obtengo de contar con len(lista[1]) en la segunda cadena de la lista creada


print(f"el numero de pesos es {lista1}")     # imprimo el numero de caracteres contado almacenados en la lista1
print(f"el numero de centevos es {lista2}")  # imprimo el numero de caracteres contado almacenados en la lista2