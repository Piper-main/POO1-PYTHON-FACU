#  🚀  **Combate de Naves Espaciales**

Queremos simular un combate entre distintos tipos de naves espaciales. Todas comparten ciertas características básicas, pero cada una **ataca de manera diferente** según su naturaleza. Esto nos permitirá trabajar con **herencia** y **sobreescritura de métodos**.

---

## **Clase base: `Nave`**

### **Atributos:**

* `nombre` → identificador de la nave.

* `salud` → puntos de vida de la nave.  
* `danio` → puntos de salud que resta en su oponente cuando ataca  
  

### **Métodos:**

* `atacar(otra)` → será redefinido en las subclases.

* `recibir_danio(atacante)` → resta salud a la nave de acuerdo a quien la ataca (no puede bajar de 0).

* `esta_destruida()` → devuelve `True` si la salud llega a 0 o menos.

* `estado()` → devuelve un string con nombre y salud actual.

---

## **Subclases**

1. **`Caza`**

   * Salud inicial: 100

   * Cada ataque inflige **15 de daño**.

2. **`Bombardero`**

   * Salud inicial: 150

   * Cada ataque inflige **25 de daño**, pero la nave recibe **5 de autodaño** (recoil).

3. **`Crucero`**

   * Salud inicial: 300

   * Cada ataque inflige **40 de daño**, pero **solo puede atacar si tiene más de 50 de salud**.

          
    	             `┌───────────────────────┐`  
                   `│          Nave           │`  
                   `├─────────────────────────┤`  
                   `│ - __nombre: str         │`  
                   `│ - __salud: int          │`  
                   `│ - __danio: int          │`  
                   `├─────────────────────────┤`  
                   `│ + danio: int {property} │`  
                   `│ + salud: int {property} │`  
                   `│ + atacar(otra: Nave)    │`  
                   `│ + recibir_danio(otra: Nave)  │`  
                   `│ + esta_destruida(): bool│`  
                   `│ + estado(): str         │`  
                   `└───────────▲─────────────┘`  
                               `│`  
          `┌────────────────────┼─────────────────────┐`  
          `│                    │                     │`  
 `┌─────────────────┐  ┌─────────────────┐   ┌─────────────────┐`  
 `│      Caza       │  │   Bombardero    │   │     Crucero     │`  
 `├─────────────────┤  ├─────────────────┤   ├─────────────────┤`  
 `│ salud = 100     │  │ salud = 150     │   │ salud = 300     │`  
 `│ danio = 15      │  │ danio = 25      │   │ danio = 40      │`  
 `├─────────────────┤  ├─────────────────┤   ├─────────────────┤`  
 `│ + atacar(otra)  │  │ + atacar(otra)  │   │ + atacar(otra)  │`  
 `│ inflige 15      │  │ inflige 25 y    │   │ inflige 40 si   │`  
 `│                 │  │ se autodaña -5  │   │ salud > 50      │`  
 `└─────────────────┘  └─────────────────┘   └─────────────────┘`

[nave.py](https://drive.google.com/file/d/1y1Wkd5ycHm0NHbVK5XANxTOaYsPUW2nG/view?usp=sharing)  
[test\_nave.py](https://github.com/leoblautzik/poo1-2026-2doCuatrimestre/blob/main/com1/03-herencia/tests/test_nave.py)