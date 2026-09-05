class Nave:

    def __init__(self, modelo, autonomia):
        self.modelo = modelo
        self.autonomia = autonomia

    def __str__(self):
        return f"Nave {self.modelo} (autonomia {self.autonomia})"

class Escuadron:

    def __init__(self, nombre):
        self.nombre = nombre
        self.naves = []

    def __str__(self):
        naves_texto = ", ".join(str(nave) for nave in self.naves)
        return f"Escuadron {self.nombre} (naves: {naves_texto})"

    def agregar_nave(self, nave):
        if nave in self.naves:
            raise RuntimeError("La nave ya está en el escuadrón")
        self.naves.append(nave)        


    def naves_con_autonomia(self, distancia) -> list[Nave]:
        resultado = []

        for nave in self.naves:
            if nave.autonomia >= distancia * 2:
                resultado.append(nave)

        return resultado

nave = Nave("X-Wing", 120)

alfa = Escuadron("Rogue")

alfa.agregar_nave(nave)
alfa.agregar_nave(Nave("Y-Wing", 80))
alfa.agregar_nave(Nave("Y-Wing", 80))
alfa.agregar_nave(Nave("A-Wing", 60))
alfa.naves_con_autonomia(50)

print(alfa.naves_con_autonomia(50))

print(alfa)


        