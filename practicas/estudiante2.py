
"""
Realizar un programa que conste de una clase llamada Estudiante, 
que tenga  como atributos el nombre y la nota del alumno. 
Definir los métodos para inicializar sus atributos, imprimirlos y 
mostrar un mensaje con el resultado de la nota y si ha aprobado o no
"""

class Estudiante:

    def __init__(self, n, no):
        self.nombre = n
        self.nota = no

    def mostrar_datos(self):
        print(f"el nombre es {self.nombre} y la nota es {self.nota}")

    def aprobado(self):
        if self.nota >= 4:
            print("El estudiante aprobo")
        elif self.nota < 4:
            print("El estudiante no aprobo")

Estudiante1 = Estudiante("Nahuel", 2)
Estudiante1.mostrar_datos()
Estudiante1.aprobado()
    
        