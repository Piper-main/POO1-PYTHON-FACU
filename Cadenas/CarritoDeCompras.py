

# Escribir un programa que pregunte por consola por los productos de un carrito de
# compras, separados por comas, y muestre por pantalla cada uno de los productos
# en una línea distinta.
print()
print(" ====================================================")
print(" Ingrese los productos del carrito separados por coma")
print()

carrito = input(" Productos: ")

lista = carrito.split(',')

for producto in lista:
    print(f"{producto}")