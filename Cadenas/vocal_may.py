# Escribir un programa que pida al usuario que introduzca una frase en la consola y
# una vocal, y después muestre por pantalla la misma frase, pero con la vocal
# introducida en mayúscula.

frase = input(" Introduce una frase: ")
vocal = input(" Introduce una vocal: ")

for cada_letra in frase:      # en cada vuelta almacena la letra en la variable cada_letra                 
    if cada_letra == vocal:   # comparo la letra almacenada por vuelta con la ingresada
        vocal = vocal.upper() # cuando encuentro la letra la transformo a mayuscula
        frase = frase.replace(cada_letra,vocal) # reemplazo la letra comparada con la vocal en MAY
        print(f" {frase}")    # imprimo la frase con la vocal encontrada y comparada transforamda a MAY
    
print(" no se pudo hacer la conversion")