from enum import Enum

class TipoHabitacion(Enum):
    SIMPLE = 1
    DOBLE = 2
    SUITE = 3

class EstadoHabitacion(Enum):
    LIBRE = 1 
    OCUPADO = 2
    EN_LIMPIEZA = 3


class Habitacion():

    def __init__(self, numero, tipo, estado):
        if numero < 0:
            raise RuntimeError("numero incorrecto")
        self.__numero = numero
        self.__tipo = tipo
        self.__estado = estado

    @property
    def tipo(self):
        return self.__tipo
    
    @property
    def numero(self):
        return self.__numero

    @property
    def estado(self):
        return self.__estado
    
    @tipo.setter
    def tipo(self, tipo):
        if tipo not in TipoHabitacion:
            raise RuntimeError("Tipo de Habitacion incorrecto")
        self.__tipo = tipo

    @numero.setter
    def numero(self,numero):
        if numero  < 0 :
            raise RuntimeError("Numero de Habitacion Invalido")
        self.__numero = numero

    @estado.setter
    def estado(self,estado):
        if estado not in EstadoHabitacion:
            raise RuntimeError("Estado Ingresado Invalido")
        self.__estado= estado

        