# 💳 Ejercicio — Medios de Pago

Se desea modelar un sistema que permita realizar pagos utilizando diferentes medios de pago.

## Clase base `MedioPago`

Cada medio de pago posee:

- `titular`
- `saldo`

Los atributos deben estar **encapsulados**.

La clase debe tener:

- `pagar(monto)` → será redefinido por las subclases.
- `consultar_saldo()` → devuelve el saldo actual.
- `estado()` → devuelve un texto con el titular y el saldo.

La clase debe validar que el saldo inicial no sea negativo.

## Subclases

### 💵 `Efectivo`

- Hereda de `MedioPago`.
- Al realizar un pago, descuenta el monto del saldo.

### 💳 `Tarjeta`

- Hereda de `MedioPago`.
- Al realizar un pago, descuenta el monto del saldo.
- Además, informa `"Pago realizado con tarjeta"`.

### 📱 `BilleteraVirtual`

- Hereda de `MedioPago`.
- Al realizar un pago, descuenta el monto del saldo.
- Además, informa `"Pago realizado con billetera virtual"`.

## Reglas

- No se puede realizar un pago si el monto es mayor al saldo disponible.
- El monto a pagar debe ser mayor que 0.
- Cada subclase debe **sobrescribir `pagar(monto)`**.
- El programa debe poder trabajar con una lista de objetos `MedioPago` que contenga diferentes medios de pago.
- Al recorrer la lista y llamar al mismo método `pagar(monto)`, cada objeto debe ejecutar su propia versión del método.

## Prueba

Crear:

- un objeto `Efectivo`,
- un objeto `Tarjeta`,
- un objeto `BilleteraVirtual`.

Guardarlos en una lista de `MedioPago`.

Recorrer la lista y realizar un pago de prueba utilizando el mismo método `pagar()`.

Finalmente, mostrar el estado de cada medio de pago.
