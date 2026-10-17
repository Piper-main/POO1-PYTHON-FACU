from abc import ABC, abstractmethod


class Vehiculo(ABC):

    def __init__(self, marca, modelo='', consumo_100km=0):
        self.__marca=marca
        self.__modelo=modelo
        self.__consumo_100km=consumo_100km

    
    @abstractmethod
    def info(self):
        return f'{self.__marca}, {self.__modelo} {self.__consumo_100km}'

    def calcular_consumo(self, cant_km):
        return (self.__consumo_100km * cant_km) / 100


class Auto(Vehiculo):

    def __init__(self, marca, modelo, consumo_100km, cantidad_puertas):
        super().__init__(marca, modelo, consumo_100km)
        self.__cantidad_puertas=cantidad_puertas 
    
    def info(self):
        return f"{super().info()}, {self.__cantidad_puertas}"
        

class Camion(Vehiculo):

    def __init__(self, marca, modelo, consumo_100km, capacidad_carga):
        super().__init__(marca, modelo, consumo_100km)
        self.__capacidad_carga=capacidad_carga

    def info(self):
        return f"{super().info()}, {self.__capacidad_carga}"


def calcular_costo_combustible(lista_vehiculos, km, valor_litro=2100.0):
    acum = 0
    for vehiculo in lista_vehiculos:
        acum += vehiculo.calcular_consumo(km) * valor_litro
    return acum


auto1= Auto('Ford', 'KA', 10, 3)
auto2= Auto('Ford', 'fiesta', 7, 5)
camion1 = Camion('Ford', 'Cargo', 25, 2)
camion2 = Camion('Mercedez', 1114 , 30, 2)

print(auto1.info())
print(auto2.info())
print(camion1.info())
print(camion2.info())
print(auto1.calcular_consumo(260))
print(auto2.calcular_consumo(300))
print(camion1.calcular_consumo(260))
print(camion2.calcular_consumo(300))
lista = [auto1, auto2, camion1, camion2]
print(calcular_costo_combustible(lista, 100))
    
    