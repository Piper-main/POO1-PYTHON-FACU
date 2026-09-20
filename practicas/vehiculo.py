



class Vehiculo:

    def __init__(self, km):
        self.__km= km
        self.__chofer= None

    
class Motocicleta:

    def __init__(self, km):
        self.__acompañante=[]


class autobus:
    def __init__(self,pasajeros):
        self.__pasajeros=pasajeros

class Persona:

    def __init__(self, nombre):
        self.__nombre=nombre

    def __str__(self):
        return self.__nombre

    def __repr__(self):
        return self.__str__()