"""
Escribir una función que calcule el total de una factura tras aplicarle el IVA. 
La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y 
devolver el total de la factura. Si se invoca la función sin pasarle el 
porcentaje de IVA, deberá aplicar un 21%.
"""

def iva(monto_sin_iva, porcentaje_iva):
    monto = monto_sin_iva + ((monto_sin_iva*porcentaje_iva)/100)
    return monto

m = int(input(" Ingrese el monto sin iva: "))
print()
p = int(input(" Ingrese el porcentaje de IVA a aplicar: "))

total = iva(m, p)
print()

print(f" El monto total de tu factura es: {total}")