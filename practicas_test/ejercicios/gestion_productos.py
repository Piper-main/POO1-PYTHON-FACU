

class Producto:

    def __init__(self, nombre='', codigo='', precio_unitario=0):
        self.__nombre=nombre
        self.__codigo=codigo
        self.__precio_unitario=precio_unitario

    def info(self):
        return f"{self.__nombre}, el codigo es {self.__codigo}, el precio es de {self.__precio_unitario} pesos"


    def calcular_costo(self, cantidad):
        return self.__precio_unitario * cantidad



class ProductoPerecedero(Producto):

    def __init__(self, nombre='', codigo='', precio_unitario=0, dias_vencimiento=0):
        super().__init__(nombre, codigo, precio_unitario)
        self.__dias_vencimiento=dias_vencimiento


    def info(self):
        return f"{super().info()}, y tiene {self.__dias_vencimiento} dias de vencimiento."

class ProductoElectronico(Producto):

    def __init__(self, nombre='', codigo='', precio_unitario=0, meses_garantia=0):
        super().__init__(nombre, codigo, precio_unitario)
        self.__meses_garantia=meses_garantia

    def info(self):
        return f" {super().info()}, y tiene {self.__meses_garantia} meses de garantia."



def calcular_total_compra(lista_productos, cantidades):
    acum = 0
    for i in range(len(lista_productos)):
        acum += lista_productos[i].calcular_costo(cantidades[i])

    return acum


fideo1 = ProductoPerecedero('fideos san remo', 542, 10, 60)
fideo2 = ProductoPerecedero('fideos matarazzo', 543, 20, 60)
auriculares1= ProductoElectronico('auri sony', 845, 50, 6)
auriculares2 = ProductoElectronico('auri aiwa', 846, 25, 12)
print()
print(fideo1.info())
print(fideo2.info())
print()
print(auriculares1.info())
print(auriculares2.info())
print()

lista = [fideo1, fideo2, auriculares1, auriculares2]
cantidades = [5, 5, 10, 10]

print(calcular_total_compra(lista, cantidades))