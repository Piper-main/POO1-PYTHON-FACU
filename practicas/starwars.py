

class Nave:

    def __init__(self, modelo, autonomia):
        self.modelo = modelo 
        self.autonomia = autonomia 

    def __str__(self):
        return f"nave {self.modelo} (autonomia {self.autonomia})"

    def __repr__(self):
            return self.__str__()

class Escuadron:

    def __init__(self, nombre):
        self.nombre = nombre
        self.naves = []

    def __str__(self):
        return f"Escuadro {self.nombre} naves {self.naves}"

    

    def __repr__(self):
        return self.__str__()

    
    def agregar_nave(self, nave):

        for n in self.naves:
            if n is nave:
                raise RuntimeError ("Nave duplicada")
        self.naves.append(nave)

    def naves_con_autonomia(self, distancia):
        lista = []

        for n in self.naves:
            if n.autonomia >= distancia * 2:
                lista.append(n)

        return lista


nave1 = Nave("X-Wing", 120)
nave2 = Nave('nahu', 75)
nave3 = Nave('feli', 120)
nave4 = Nave('azul', 60)



escuadron = Escuadron("Familia")
escuadron.agregar_nave(nave1)
escuadron.agregar_nave(nave2)
escuadron.agregar_nave(nave3)
escuadron.agregar_nave(nave4)

resultado = escuadron.naves_con_autonomia(32)
print(resultado)

print(f"el escuadron se llama {escuadron.nombre}")



    
        

        