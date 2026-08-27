import aritmeticas.ope_basicas as ob

                                        #importa del directorio aritmeticas/ del archivo ope_basicas.py la funcion
                                        #sumar y restar, le pongo un alias ob

num1 = int(input(" Ingrese un numero: "))
num2 = int(input(" Ingrese el segundo numero: "))

resultado = ob.sumar(num1,num2)      #llamo a la funcion que quiero usar, pero antes le pongo el alias que declare en el import

print(f" el resultado es {resultado}")