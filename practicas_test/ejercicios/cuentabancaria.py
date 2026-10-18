from abc import ABC, abstractmethod


class CuentaBancaria(ABC):

    def __init__(self, titular, numero_cuenta, saldo=0):
        self.__titular=titular
        self.__numero_cuenta=numero_cuenta
        self.saldo=saldo

    #Implementar el método info() para mostrar los datos de la cuenta.
    #Sobrescribir el método info() en ambas clases para mostrar todos los datos correspondientes.
    @abstractmethod
    def info(self):
        return f'{self.__titular}, {self.__numero_cuenta}, {self.__saldo}'

    #Implementar una propiedad saldo y su correspondiente setter. El saldo no puede ser negativo.
    @property
    def saldo(self):
        return self.__saldo
        
    @saldo.setter
    def saldo(self, nuevo_saldo):
        if nuevo_saldo < 0:
            raise ValueError
        self.__saldo=nuevo_saldo

    #Implementar el método depositar(monto), que permita incrementar el saldo de la cuenta.
    def depositar(self, monto):
        if monto <= 0:
            raise ValueError("El depósito debe ser mayor que cero")
        self.saldo += monto

#Crear una clase CuentaAhorro que herede de CuentaBancaria 
# y agregue el atributo tasa_interes (por defecto 0).

class CuentaAhorro(CuentaBancaria):

    def __init__(self, titular, numero_cuenta, saldo=0, tasa_interes=0):
        super().__init__(titular, numero_cuenta, saldo)
        self.__tasa_interes=tasa_interes
    
    def info(self):
        return f'{super().info()}, {self.__tasa_interes}'

#crear una clase CuentaCorriente que herede de CuentaBancaria 
# y agregue el atributo limite_descubierto (por defecto 0).

class CuentaCorriente(CuentaBancaria):

    def __init__(self, titular, numero_cuenta, saldo=0, limite_descubierto=0):
        super().__init__(titular, numero_cuenta, saldo)
        self.__limite_descubierto=limite_descubierto

    def info(self):
        return f'{super().info()}, {self.__limite_descubierto}'


#Implementar una función calcular_saldo_total(lista_cuentas) que reciba 
# una lista de cuentas bancarias y devuelva la suma de los saldos de todas las cuentas.
def calcular_saldo_total(lista_cuentas):
    acum=0
    for cuenta in lista_cuentas:
        acum += cuenta.saldo
    return acum

#Crear dos objetos de la clase CuentaAhorro 
# y dos de la clase CuentaCorriente, y mostrar su información.

nahuel = CuentaAhorro('Nahuel', 1000, 1000, )
azul = CuentaAhorro('Azul', 1001, 1500, 15 )
pichu = CuentaCorriente('pichu', 1002, 1500, )
meli = CuentaCorriente('meli', 1003, 2000, 4000)

print(nahuel.info())
print(azul.info())
print(pichu.info())
print(meli.info())

nahuel.depositar(500)

print(nahuel.info())

lista = [nahuel, azul, pichu, meli]

print(calcular_saldo_total(lista))

print(nahuel.saldo)
nahuel.depositar(1500)
print(nahuel.saldo)