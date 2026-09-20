





class Nave:

    def __init__(self, nombre, salud, danio):
        self.__nombre = nombre
        self.__salud = salud
        self.__danio = danio

    @property
    def nombre(self):
        return self.__nombre

    @property
    def salud(self):
        return self.__salud

    @salud.setter
    def salud(self, nueva_salud):
        self.__salud = max(0, nueva_salud)

    @property
    def danio(self):
        return self.__danio

    @danio.setter
    def danio(self, nuevo_danio):
        self.__danio = nuevo_danio

    def atacar(self, otra):
        pass

    def recibir_danio(self, atacante):
        self.salud -= atacante.danio

    def esta_destruida(self):
        return self.salud <= 0

    def estado(self):
        return f"{self.nombre}: {self.salud} de salud"


class Caza(Nave):

    def __init__(self, nombre):
        super().__init__(nombre, 100, 15)

    def atacar(self, otra):
        otra.recibir_danio(self)


class Bombardero(Nave):

    def __init__(self, nombre):
        super().__init__(nombre, 150, 25)

    def atacar(self, otra):
        otra.recibir_danio(self)
        self.salud -= 5


class Crucero(Nave):

    def __init__(self, nombre):
        super().__init__(nombre, 300, 40)

    def atacar(self, otra):
        if self.salud > 50:
            otra.recibir_danio(self)


# Prueba
caza = Caza("X-Wing")
bombardero = Bombardero("Bombardero-1")
crucero = Crucero("Crucero-1")

print(caza.estado())
print(bombardero.estado())
print(crucero.estado())

caza.atacar(bombardero)
print(bombardero.estado())

bombardero.atacar(caza)
print(bombardero.estado())
print(caza.estado())

crucero.atacar(caza)
print(caza.estado())