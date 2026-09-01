"""Crea una clase Persona. Con atributos nombre y edad. 
Además, crear un método cumpleaños, que aumente en 1 
la edad de la persona cuando se invoque sobre un objeto 
creado con Persona.
"""

class Persona:

    def __init__(self, nombre,edad):
        self.__nombre = nombre
        self.__edad = edad

    def get_e(self):
        return self.__edad

    def cumpleaños(self):
        self.__edad = self.__edad + 1





sujeto1 = Persona('nahuel', 37 )     
sujeto1.cumpleaños() 
print(sujeto1.get_e()) 

        