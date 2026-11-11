


class Pago:

    def __init__(self, monto):
        self.__monto = monto

class PagoContado(Pago):

    def __init__(self, monto):
        super().__init__(monto)

    def importe_final(self):
        return self.__monto

class PagoConTarjeta(Pago):

    def __init__(self, monto, porcentaje):
        super().__init__(monto)
        self.__porcentajedepago = porcentaje

    def importe_final(self):
        total=0
        total = self.__monto + self.__monto * self.__porcentajedepago / 100
        return total

efectivo = Pago(4000)
pago = PagoContado(2000)
pago1 = PagoConTarjeta(2000)

print(pago.importe_final())