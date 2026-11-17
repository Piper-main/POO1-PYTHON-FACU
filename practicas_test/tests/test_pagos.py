import unittest

from pagos import Empresa, Pago, PagoContado, PagoConTarjeta


class TestPagos(unittest.TestCase):

    def test_consultar_monto(self):
        pago = Pago(5000)

        self.assertEqual(pago.consultar_monto(), 5000)


class TestEmpresa(unittest.TestCase):

    def test_importe_total(self):
        empresa= Empresa()

        empresa.agregar_pago(PagoContado(2300))
        empresa.agregar_pago(PagoContado(2500))
        empresa.agregar_pago(PagoContado(2600))

        self.assertEqual(empresa.importe_total(), 7400)


if __name__ == "__main__":
    unittest.main()
    
