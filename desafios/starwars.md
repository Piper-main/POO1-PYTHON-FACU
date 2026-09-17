# Star Wars (Final Julio 2026\)

Modelar en Python las clases Nave y Escuadron.

**Nave**: 

atributos:

**modelo** (str, ej. "X-Wing") y **autonomia** (float, distancia máxima que puede recorrer con el combustible disponible).

**Escuadron**: atributos **nombre** (str) y **naves** (lista de objetos Nave, inicializada vacía). 

Ambas clases con constructor y `__str__` que muestre sus datos.

Implementar en la clase **Escuadron** los siguientes métodos:

**`def agregar_nave(self, nave):`**

Agrega la nave a la lista del escuadrón. No se debe permitir agregar la misma nave dos veces (la misma instancia ya presente en la lista); si se intenta, se debe lanzar un RunTimeError. Dos naves distintas con el mismo modelo sí pueden coexistir en el escuadrón.

**`def naves_con_autonomia(self, distancia) -> list[Nave]:`**

El escuadrón debe partir hacia un objetivo ubicado a distancia unidades de la base, cumplir la misión y regresar. El método debe devolver una lista con las naves cuya autonomia les permite cubrir el viaje de ida y vuelta sin modificar el estado del escuadrón ni de las naves.

Por ejemplo: 

`nave = Nave("X-Wing", 120)`

`alfa = nave`

`escuadron = Escuadron("Rogue")`

`escuadron.agregar_nave(nave)`

`escuadron.agregar_nave(Nave("Y-Wing", 80))`

`escuadron.agregar_nave(Nave("Y-Wing", 80))`

`escuadron.agregar_nave(Nave("A-Wing", 60))`

`escuadron.agregar_nave(alfa)  # duplicado, debe rechazarse`

`>>> escuadron.naves_con_autonomia(50)`

`[Nave X-Wing (autonomia 120)]`

[`test_star_wars.py`](https://github.com/leoblautzik/poo1-2026-2doCuatrimestre/blob/main/com1/02-encapsulamiento/tests/test_star_wars.py)