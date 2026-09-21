



class Animal:

    def __init__(self, nombre, edad):
        self.__nombre = nombre
        if edad < 0:
            raise RuntimeError ("la edad no puede ser menor a 0")
        self.__edad = edad


    def hacer_sonido(self):
        pass

    def cumplir_anio(self):
        self.__edad = self.__edad + 1

    def estado(self):
        return f"el nombre es {self.__nombre} y su edad es {self.__edad}"


class Perro(Animal):

    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

    def hacer_sonido(self):
        return "Guau guau"

class Gato(Animal):

    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
        
    def hacer_sonido(self):
        return "Miau"
    
class Loro(Animal):

    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
        
    def hacer_sonido(self):
        return "hola"


perro = Perro('pedro', 2)
gato = Gato('kata', 3)
loro = Loro('feli', 9)

animales = [perro, gato, loro]

for animal in animales:
    print(animal.hacer_sonido())
    print(animal.estado())