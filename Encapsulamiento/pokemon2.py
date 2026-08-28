class Pikachu:             # declaramos la clase con la palabra reservada "class" y su nombre
    tipo = 'Electrico'     # declaramos un atriburo de clase


    def __init__(self, nombre,nivel,salud,voltaje_max,amperaje_max,color):  
        self._nombre = nombre                                               
        self.__nivel = nivel
        self.salud = salud
        self.voltaje_maximo = voltaje_max
        self.apmperaje_maximo = amperaje_max
        self.color = color

    def atacar(self):
        print(f" pikachu ataca y genera {self.nivel/4} de daño")

Pikachu1 = Pikachu('nahuel', 780,100,6,2,'amarillo')



Pikachu1.__nivel = 900    # esto si por que el pokemon evoluciono y subio de nivel
Pikachu1.tipo = 'fuego' #esto no deberia poder hacerse. no puede cambiar la clase nunca.

print(f" El pikachu llamada {Pikachu1._nombre} es de color {Pikachu1.color} y tiene un nivel de {Pikachu1.__nivel} y es de tipo {Pikachu1.tipo}")
