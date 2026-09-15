

class Monedero:

    def __init__(self, DP):
        self.__dinero_disponible = DP

    def meter_dinero(self, dinero_nuevo):
        self.__dinero_disponible = self.__dinero_disponible + dinero_nuevo
    
    def sacar_dinero(self, sacar):
        if sacar <= self.__dinero_disponible:
            self.__dinero_disponible = self.__dinero_disponible - sacar
        else:
            raise RuntimeError(" Operacion no disponible")

    def consultar_dinero(self):
        return self.__dinero_disponible    

monedero1 = Monedero(0)
monedero1.meter_dinero(100)
monedero1.sacar_dinero(30)
monedero1.sacar_dinero(100)
print(monedero1.consultar_dinero())
        