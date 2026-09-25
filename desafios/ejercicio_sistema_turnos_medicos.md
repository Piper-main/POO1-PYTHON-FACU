# 🏥 Ejercicio — Sistema de Turnos Médicos

Se desea modelar un sistema básico para gestionar turnos médicos.

## Clase base `Profesional`

Cada profesional posee:

- `nombre`
- `matricula`
- `especialidad`

Los atributos deben estar **encapsulados**.

La clase debe tener:

- `atender_paciente(paciente)` → será redefinido por las subclases.
- `estado()` → devuelve un texto con los datos del profesional.

La matrícula debe ser un número positivo.

## Subclases

### 👨‍⚕️ `Clinico`

Hereda de `Profesional`.

Al atender a un paciente:

- informa `"El clínico atiende a <nombre del paciente>"`.
- registra que el paciente fue atendido.

### 🦷 `Odontologo`

Hereda de `Profesional`.

Al atender a un paciente:

- informa `"El odontólogo atiende a <nombre del paciente>"`.
- registra que el paciente fue atendido.

### 🧠 `Psicologo`

Hereda de `Profesional`.

Al atender a un paciente:

- informa `"El psicólogo atiende a <nombre del paciente>"`.
- registra que el paciente fue atendido.

## Clase `Paciente`

Cada paciente posee:

- `nombre`
- `dni`

Los atributos deben estar **encapsulados**.

El DNI debe ser positivo.

La clase debe tener:

- `estado()` → devuelve un texto con nombre y DNI.

## Clase `Consultorio`

El consultorio debe mantener una **lista de profesionales**.

Debe permitir:

- `agregar_profesional(profesional)` → agrega un profesional al consultorio.
- `atender_paciente(profesional, paciente)` → hace que el profesional indicado atienda al paciente.
- `mostrar_profesionales()` → muestra la información de todos los profesionales registrados.

No se debe permitir registrar **dos veces la misma instancia de profesional**.

Dos profesionales diferentes pueden tener la misma especialidad.

## Polimorfismo

El consultorio debe poder trabajar con una lista que contenga objetos de tipo:

- `Clinico`
- `Odontologo`
- `Psicologo`

Al llamar:

`profesional.atender_paciente(paciente)`

cada tipo de profesional debe ejecutar **su propia versión del método**.

## Prueba

Crear:

- 2 pacientes.
- 1 clínico.
- 1 odontólogo.
- 1 psicólogo.
- 1 consultorio.

Registrar los tres profesionales en el consultorio.

Intentar registrar nuevamente uno de ellos.

Hacer que distintos profesionales atiendan a los pacientes.

Finalmente, mostrar el estado de los profesionales registrados.
