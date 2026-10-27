from enum import Enum


class CategoriaPlato(Enum):
    ENTRADA=1
    PRINCIPAL=2
    POSTRE=3
    BEBIDA=4


class Plato:

    def __init__(self,nombre, precio, categoria):
        self.__nombre=nombre
        self.__precio=precio
        self.__categoria=categoria

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio <= 0:
            raise RuntimeError("el precio debe ser mayor a 0")
        else:    
            self.__precio = nuevo_precio

class Pedido:

    def __init__(self):
        self.__lista_platos = []

    def agregar_plato(self):
        self.__lista_plato.append(Plato)


    def calcular_total(self):
        acum=0
        for i in self.__lista_platos:
            acum+= i.precio

        return acum


    def ticket(self):   
         texto=""
         for i in self.__lista_platos:
            texto= f"{i.nombre}, ${i.precio}, {i.categoria}"

            total=self.calcular_total()
        
            return f"{texto} Total del ticket: ${total}"

