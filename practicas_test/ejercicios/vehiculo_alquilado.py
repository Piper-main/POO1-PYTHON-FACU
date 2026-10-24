

class VehiculoAlquilado:

    def __init__(self, marca='', patente='', precio=0):
        self.__marca=marca
        self.__patente=patente
        self.__precio=precio

    def mostrar_datos(self):
        return f"La marca es: {self.__marca}, la patente: {self.__patente}, y su precios es: ${self.__precio}"

    def calcular_costos(self, dias):
        costo=0
        costo= self.__precio*dias
        return costo
    
class AutoAlquilado(VehiculoAlquilado):

    def __init__(self, marca='', patente='', precio=0, cantidad_puertas=0):
        super().__init__(marca, patente,precio)
        self.__catidad_puertas=cantidad_puertas

    def mostrar_datos(self):
        return f" {super().mostrar_datos()}, y tiene: {self.__catidad_puertas} puertas"

class MotoAlquilada(VehiculoAlquilado):

    def __init__(self, marca='', patente='', precio=0, cilindrada=0):
        super().__init__(marca, patente, precio)
        self.__cilindrada=cilindrada

    def mostrar_datos(self):
        return f"{super().mostrar_datos()}, y su cilindrada es {self.__cilindrada} cc"


auto1 = AutoAlquilado('Ford', 'jeq440', 10000, 4)
moto1 = MotoAlquilada('zanella', 'jeq441', 2000, 125)
print()
print(auto1.mostrar_datos())
print(moto1.mostrar_datos())
print()
print(f"el costo de alquiler es ${auto1.calcular_costos(5)} pesos")
print(f"el costo de alquiler es ${moto1.calcular_costos(5)} pesos")