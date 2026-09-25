



class MedioPago():

    def __init__(self, titular, saldo):
        self.__titular = titular
        if saldo < 0:
            raise RuntimeError ("El saldo no puede ser negativo")
        self.__saldo = saldo

    def pagar(self, monto):
        pass

    def consultar_saldo(self):
        return self.__saldo

    def estado(self):
        return f"Titular {self.__titular} el saldo es ${self.__saldo}"

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, nuevo_saldo):
        if nuevo_saldo < 0:
            raise RuntimeError("El monto ingresado no puede ser negativo")
        self.__saldo = nuevo_saldo

class Efectivo(MedioPago):

    def __init__(self, titular, saldo):
        super().__init__(titular, saldo)

    def pagar(self, monto):
        if monto > self.saldo:
            raise RuntimeError ("Saldo insuficiente")
        if monto > 0:    
            self.saldo = self.saldo - monto
        else:
            raise RuntimeError("Ingrese el monto a pagar")
        print("pago realizado en efetivo")

class Tarjeta(MedioPago):

    def __init__(self, titular, saldo):
        super().__init__(titular, saldo)

    def pagar(self, monto):
        if monto > self.saldo:
            raise RuntimeError ("Saldo insuficiente")
        if monto > 0:    
            self.saldo = self.saldo - monto
        else:
            raise RuntimeError("Ingrese el monto a pagar")
        print("pago realizado con tarjeta")

class BilleteraVirtual(MedioPago):

    def __init__(self, titular, saldo):
        super().__init__(titular, saldo)

    def pagar(self, monto):
        if monto > self.saldo:
            raise RuntimeError ("Saldo insuficiente")
        if monto > 0:    
            self.saldo = self.saldo - monto
        else:
            raise RuntimeError("Ingrese el monto a pagar")
        print("pago realizado con Billetera Virtual")

efectivo = Efectivo('Nahuel', 150000)
tarjeta = Tarjeta('Felipe', 200000)
billeteraVitual = BilleteraVirtual('Azul', 100000)

efectivo.pagar(75000)
tarjeta.pagar(100000)
billeteraVitual.pagar(50000)

lista = [efectivo, tarjeta, billeteraVitual]

for estado in lista:
    print(estado.estado())

        
        
        