


class Unidad:

    def __init__(self, salud, danio, posicion):
        self.__salud = salud
        self.__danio = danio
        self.__posicion = posicion

    @property
    def salud(self):
        return self.__salud

    @salud.setter
    def salud(self, nueva_salud):
        self.__salud = nueva_salud

    def puede_atacar(self, unidad):
        return self.__salud >= 0
            
    
    def atacar(self, unidad):
        print(f"{unidad} ataco y saco {self.__danio}") 

    def recibir_ataque(self, unidad):
        print(f"El {unidad} recibio un ataque")

    def esta_vivo(self):
        return self.__salud > 0
    
    def distancia(self, unidad):
        pass


class Arquero(Unidad):

    def __init__(self, salud, danio, posicion, flechas):
        super().__init__(salud, danio, posicion)
        self.__flechas = flechas

    def puede_atacar(self):
        return self.distancia > 1 and self.distancia < 6 and self.__flechas > 0

    def atacar(self, unidad):
        print(f"El arquero ataco a {unidad} y le hizo 5 de daño")



class Lancero(Unidad):

    def __init__(self, salud, danio, posicion):
        super().__init__(salud, danio, posicion)

    def puede_atacar(self):
            return self.distancia > 0 and self.distancia < 4

    def atacar(self, unidad):
        print(f"El Lancero ataco a {unidad} y le hizo 25 de daño")

class Soldado(Unidad):

    def __init__(self, salud, danio, posicion, energia):
        super().__init__(salud, danio, posicion)
        self.__energia = energia

    


class Caballo:

    def __init__(self, ataques):
        self.__ataque_realizados = ataques


class Caballero(Unidad, Caballo):

    def __init__(self, salud, danio, posicion, ataques):
        super().__init__(salud, danio, posicion)
        super().__init__(ataques)

class Aguatero:

    def recibir_agua(self):
        pass



