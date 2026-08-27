class Pikachu:             # declaramos la clase con la palabra reservada "class" y su nombre
    tipo = 'Electrico'     # declaramos un atriburo de clase


    def __init__(self, nombre,nivel,salud):  # declaramos el iniciador con el texto que esta <----
        self.nombre = nombre                 # creamos la variables de instancia "self.nombre"
        self.nivel = nivel
        self.salud = salud

"""AHORA CREAMOS EL OBJETO PARA USAR SUS ATRIBUTOS"""
# creo el objeto poniendole un nombre y es = al nombre de la clase y le puedo poner los valores
# que utilizaran sus variables de instancia.
Pikachu1 = Pikachu('Felipe',1000,5000)
Pikachu2 = Pikachu('Nahuel', 1500, 4000)



print(Pikachu1.tipo,Pikachu1.nombre,Pikachu1.nivel)
print(Pikachu2.tipo,Pikachu2.nombre,Pikachu2.nivel)