from enum import Enum


class CategoriaPlato(Enum):
    ENTRADA=1
    PRINCIPAL=2
    POSTRE=3
    BEBIDA=4

class Plato:

    def __init__(self, nombre, precio, categoria):
        self.__nombre = nombre
        self.__precio = precio
        self.__categoria = categoria

    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
            return self.__precio

    def get_categoria(self):
            return self.__categoria

    def set_precio(self, nuevo_precio):
         if nuevo_precio<= 0:
              raise RuntimeError("Precio no puede ser Negativo")
         self.__precio = nuevo_precio

    def set_nombre(self, nuevo_nombre):
         self.__nombre = nuevo_nombre

    def set_categoria(self, nueva_categoria):
         self.__categoria = nueva_categoria

class Pedido:
  

     def __init__(self):
         self.__lista_plato = []

     def agregar_plato(self, plato):
         self.__lista_plato.append(plato)

     def calcular_total(self):
         total = 0    
         for p in self.__lista_plato:
            total = total + p.get_precio()
            
         return total

     def ticket(self):
          

          for p in self.__lista_plato:
               nombre = p.get_nombre()
               precio = p.get_precio()
               categoria = p.get_categoria()

               print(nombre)
               print(precio)
               print(categoria)

          print(self.calcular_total())
             
               
plato1 = Plato('Fideos', 4575, 'ENTRADA')
plato2 = Plato('Milanesas', 9000, 'PRICIPAL')

pedido1 = Pedido()
pedido1.agregar_plato(plato1)
pedido1.agregar_plato(plato2)
pedido1.ticket()