class Pikachu:             # declaramos la clase con la palabra reservada "class" y su nombre
    tipo = 'Electrico'     # declaramos un atriburo de clase


    def __init__(self, nombre,nivel,salud):  # declaramos el iniciador con el texto que esta <----
        self.nombre = nombre                 # creamos la variables de instancia "self.nombre"
        self.nivel = nivel
        self.salud = salud
    """CREAMOS UN METODO DENTRO DE LA CLASE"""
    """UN METODO ES UNA ACCION O COMPORTAMIENTO QUE PUEDE TENER LE OBJETO"""
    def atacar(self):
        print(f" pikachu ataca y genera {self.nivel/4} de daño")


    """AHORA CREAMOS EL OBJETO PARA USAR SUS ATRIBUTOS"""
# creo el objeto poniendole un nombre y es = al nombre de la clase y le puedo poner los valores
# que utilizaran sus variables de instancia.
Pikachu1 = Pikachu('Felipe',1000,5000)
Pikachu2 = Pikachu('Nahuel', 1500, 4000)


print(f"el pikachu llamada {Pikachu1.nombre} ataca.")
Pikachu1.atacar()  #llamamos a la funcion atacar con el nombre de objeto y tomara sus valores para atacar

print(f"el pikachu llamada {Pikachu2.nombre} ataca.")
Pikachu2.atacar()