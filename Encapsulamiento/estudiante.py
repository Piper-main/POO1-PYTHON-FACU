"""
Realizar un programa que conste de una clase llamada Estudiante, 
que tenga  como atributos el nombre y la nota del alumno. 
Definir los métodos para inicializar sus atributos, imprimirlos y 
mostrar un mensaje con el resultado de la nota y si ha aprobado o no
"""

class Estudiante:

    def __init__(self, nombre, nota):
        self.__nombre = nombre
        self.__nota = nota

    def imprimir(self):
        print("Nombre:", self.__nombre)
        print("Nota:", self.__nota)

    def aprobo(self):
        if self.__nota > 4:
            print("Aprobó")
        else:
            print("Desaprobó")


a = Estudiante("Nahuel", 6)

a.imprimir()
a.aprobo()