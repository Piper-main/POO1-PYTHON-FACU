

class Empleado:

    def __init__(self, nombre='', dni=0, sueldo_basico=0):
        self.__nombre=nombre
        self.__dni=dni
        self.__sueldo_basico=sueldo_basico


    def mostrar_datos(self):
        return f"Nombre: {self.__nombre}, DNI: {self.__dni}, y sueldo: {self.__sueldo_basico}"

    def obtener_sueldo_basico(self):
        return self.__sueldo_basico
    

class EmpleadoAdministrativo(Empleado):

    def __init__(self, nombre='', dni=0, sueldo_basico=0, horas_extras=0):
        super().__init__(nombre, dni, sueldo_basico)
        self.__horas_extras=horas_extras

    def mostrar_datos(self):
        return f"{super().mostrar_datos()}, horas extras: {self.__horas_extras}"

    def calcular_sueldo(self):
            return self.obtener_sueldo_basico() + (self.__horas_extras * 5000)

class EmpleadoTecnico(Empleado):

    def __init__(self, nombre='', dni=0, sueldo_basico=0, nivel=1):
        super().__init__(nombre, dni, sueldo_basico)
        self.__nivel=nivel


    def mostrar_datos(self):
        return f"{super().mostrar_datos()}, y el nivel: {self.__nivel}"

    def calcular_sueldo(self):
        
        adicional = (self.__nivel - 1) * 0.10
        
        return self.obtener_sueldo_basico() * (1 + adicional)

def calcular_gasto_sueldos(lista_empleados):
    
    acum=0
    for empleado in lista_empleados:
        acum += empleado.calcular_sueldo()
    return acum




 

nahuel = EmpleadoAdministrativo("nahuel", 34248671, 100000, 5)
pichu = EmpleadoAdministrativo("pichu", 30085500, 200000, 5)
silvia = EmpleadoTecnico("silvia", 28974456, 100000, 5)
melina = EmpleadoTecnico("melina", 38596985, 150000, 5)

print(nahuel.mostrar_datos())
print(pichu.mostrar_datos())
print(silvia.mostrar_datos())
print(melina.mostrar_datos())

print(nahuel.calcular_sueldo())
print(pichu.calcular_sueldo())
print(silvia.calcular_sueldo())
print(melina.calcular_sueldo())

lista = [nahuel, pichu, silvia, melina]  

print(calcular_gasto_sueldos(lista))

        
        



