# 🐾 Ejercicio — Sistema de Animales

Se desea modelar un sistema para gestionar diferentes tipos de animales.

## Clase base `Animal`

Cada animal posee:

- `nombre`
- `edad`

Los atributos deben estar **encapsulados**.

La clase debe tener:

- `hacer_sonido()` → será redefinido por las subclases.
- `cumplir_anio()` → aumenta la edad en 1.
- `estado()` → devuelve un texto con el nombre y la edad.

## Subclases

### 🐶 `Perro`

- Hereda de `Animal`.
- Su sonido es `"Guau guau"`.

### 🐱 `Gato`

- Hereda de `Animal`.
- Su sonido es `"Miau"`.

### 🐦 `Loro`

- Hereda de `Animal`.
- Su sonido es `"Hola"`.

## Reglas

- La edad no puede ser negativa.
- Cada subclase debe **sobrescribir** `hacer_sonido()`.
- El programa debe poder trabajar con una lista de objetos `Animal` que contenga perros, gatos y loros.
- Al recorrer esa lista y llamar a `hacer_sonido()`, cada animal debe producir su propio sonido.

## Prueba

Crear:

- un perro,
- un gato,
- un loro.

Guardarlos en una lista de `Animal` y recorrerla mostrando:

1. El estado de cada animal.
2. El sonido que realiza.
