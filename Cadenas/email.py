# Escribir un programa que pregunte el correo electrónico del usuario en la consola
# y muestre por pantalla otro correo electrónico con el mismo nombre (la parte
# delante de la arroba @) pero con dominio argentina.ar


email = input(" Ingrese su Correo Electronico: ")


lista = email.split('@') # .split() Parte la cadena en subcadenas (devuelve una lista)
                         # dentro de los () agrego el delimitador, en este caso el @, 
                         # y lo almaceno en la variable lista = ['ejemplo', 'dominio']


print(f" lista = {lista}") # ejemplo de lo que hace .split('@')


nd = "argentina.ar"  # creo una variable con el dominio que me pide


print(f" {lista[0]}@{nd}")

# concateno la primer cadena de la lista(lista[0]) el @ y la variable 
# nueva con el dominio que quiero agregar o cambiar.