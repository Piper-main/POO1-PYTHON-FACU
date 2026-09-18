# 🏋️ Desafío — Gimnasio

Se desea modelar un sistema básico para gestionar los socios de un gimnasio.

Cada socio posee un **nombre, una edad y un plan de entrenamiento**. Los planes disponibles son **BÁSICO, INTERMEDIO y AVANZADO**.

El gimnasio debe permitir **registrar socios**. No se debe permitir registrar dos veces al mismo socio, considerando que **dos referencias al mismo objeto representan al mismo socio**. Dos socios diferentes pueden tener el mismo nombre.

El sistema debe permitir **consultar la información de los socios registrados**.

El gimnasio ofrece distintas **actividades**. Cada actividad tiene una **edad mínima requerida** y un **plan mínimo requerido**.

Un socio puede participar de una actividad si:

- su edad es **mayor o igual** a la edad mínima requerida, y
- su plan de entrenamiento es **igual o superior** al plan mínimo requerido.

El sistema debe permitir consultar **qué socios están habilitados para participar de una actividad determinada**.

Para probar el funcionamiento del sistema, se deberán crear varios socios, registrarlos, intentar registrar nuevamente uno de ellos y realizar una consulta de los socios habilitados para una actividad.
