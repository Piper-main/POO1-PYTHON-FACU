"""Realizar un programa en el cual se declaren dos valores
enteros por teclado utilizando el método __init__.
Calcular después la suma, resta, multiplicación y división.
Utilizar un método para cada una e imprimir los
resultados obtenidos. Llamar a la clase Calculadora.
"""


class Calculadora:

    def __init__(self, pv, sv):
        self.__pv = pv
        self.__sv = sv

    def suma(self):
        return self.__pv + self.__sv

    def resta(self):
        return self.__pv - self.__sv

    def multi(self):
        return self.__pv * self.__sv

    def dividir(self):
        return self.__pv / self.__sv


pv = int(input("Ingrese el primer valor: "))
sv = int(input("Ingrese el segundo valor: "))

calculadora = Calculadora(pv, sv)

print(f"La suma es {calculadora.suma()}")
print(f"La resta es {calculadora.resta()}")
print(f"La multiplicación es {calculadora.multi()}")
print(f"La división es {calculadora.dividir()}")