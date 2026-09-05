"""
Crear la clase Nota:
* constructor que reciba como parámetro valorInicial comprendido entre 0 y 10
* obtenerValor(): devuelve el valor numérico de la Nota, comprendido entre 0 y 10
* aprobado(): devuelve valor booleano que indica si la Nota permite o no la aprobación
* desaprobado(): devuelve valor booleano que indica si la Nota implica desaprobación
* recuperar(nuevoValor): recibe como parámetro nuevoValor comprendido entre 0 y 10 y 
modifica el valor numérico de la Nota, cambiándolo por nuevoValor, siempre y cuando 
nuevoValor sea superior al valor numérico actual.
"""


class Nota:

    def __init__(self, valorInicial):
        if not 0 <= valorInicial <= 10:
            raise ValueError("El valor debe estar entre 0 y 10.")
        self.__valor = valorInicial

    def obtenerValor(self):
        return self.__valor

    def aprobado(self):
        return self.__valor >= 5

    def desaprobado(self):
        return self.__valor < 5

    def recuperar(self, nuevoValor):
        if not 0 <= nuevoValor <= 10:
            raise ValueError("El valor debe estar entre 0 y 10.")
        self.__valor = max(self.__valor, nuevoValor)


