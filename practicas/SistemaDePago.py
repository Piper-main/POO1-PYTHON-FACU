


class Pago:

    def __init__(self, monto):
        self.__monto = monto

    def consultar_monto(self):
        return self.__monto

    def __str__(self):
        return f"Pago por ${self.__monto}"


class PagoContado(Pago):

    def __init__(self, monto):
        super().__init__(monto)

    def importe_final(self):
        return super().consultar_monto()

    def __str__(self):
        return "Pago Contado"
        

class PagoConTarjeta(Pago):

    def __init__(self, monto, porcentaje):
        super().__init__(monto)
        self.__porcentajedepago = porcentaje

    def importe_final(self):
        total=0
        total = super().consultar_monto() + super().consultar_monto() * self.__porcentajedepago / 100
        return total

    def __str__(self):
            return "Pago con Tarjeta"

pago = PagoContado(2000)
pago1 = PagoConTarjeta(2000, 15)
pago2 = PagoContado(520)
pago3 = PagoContado(7000)

print(pago.importe_final())
print(pago1.importe_final())
print(pago2.importe_final())
print(pago3.importe_final())

class Empresa:

    def __init__(self):
        self.__lista= []

    def agregar_pago(self, pago):
        self.__lista.append(pago)
     

    def importe_total(self):
        total=0
        for p in self.__lista:
            total += p.importe_final()
        return total

    def pago_mayor(self):
        pago= None
        importe=0
        mayor=0
        if (len(self.__lista)) == 0:
            pago = None
        else:
            for p in self.__lista:
                importe = p.importe_final()
                if importe > mayor:
                    mayor = importe
                    pago = p
        return pago

empresa = Empresa()
empresa.agregar_pago(pago)
empresa.agregar_pago(pago1)
empresa.agregar_pago(pago2)
empresa.agregar_pago(pago3)
print(f"La suma total es {empresa.importe_total()}")
print(f"El pago de mayor monto fue un: {empresa.pago_mayor()}")

