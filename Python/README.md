# Calculadora Geométrica de área y volumen

Programa en Python que calcula el área o el volumen según la entrada del usuario.
La entrada del usuario solo permie introducir numeros positivos.

Este programa tiene 6 funciones definidas:

    - main() -> Función principal. Es donde empieza el programa.
    - get_user_input(msg) -> Función para obtener el input de usuario de forma obligatoria.
    - get_user_input_or_empty(msg) -> Función para obtener número o vacío.
    - calculate_area_or_volume(width, height, depth) -> Función para calcular el volumen o el área.
    - calculate_area(width, height) -> Función para calcular el área.
    - calculate_volume(width, height, depth) -> Función para calcular el volumen.

## Funcionamiento

El flujo de este programa es:
main()
  ↓
Mostrar "Calculadora..."
  ↓
width = get_user_input()
  ↓
height = get_user_input()
  ↓
depth = get_user_input_or_empty()
  ↓
calculate_area_or_volume(width, height, depth)
        ↓
        ¿depth es None (vacío)?
        ├─ Sí → calculate_area(width, height)
        │        ↓
        │     Mostrar área
        │
        └─ No → calculate_volume(width, height, depth)
                 ↓
              Mostrar volumen
  ↓
Fin

## Ejecución

Para poder ejecutarlo:

```bash
python calculadora_vol_geo.py
```

**Ejemplo (Área):**
```
Ingrese el ancho...: 10
Ingrese la altura...: 5
Ingrese la profundidad...: Dejar vacío
El área es: 50.0 m2.
```
**Ejemplo (Volumen):**
```
Ingrese el ancho...: 10
Ingrese la altura...: 5
Ingrese la profundidad...: 2
El volumen es: 100.0 m3.
```

---

## Pruebas

Las pruebas ahora se realizarán con el módulo `unittest`.

### Ejecución de las pruebas
Desde la terminal, ejecutar:

```bash
python -m unittest test_calculadora_vol_geo.py
```

### Descripción
Se prueban las funciones calculate_area y calculate_volume.
Como estas funciones imprimen el resultado en pantalla, se utiliza unittest.mock.patch junto con StringIO para capturar la salida y compararla con la esperada.

El archivo incluye tres pruebas:

test_for_area (test correcto)

test_for_volume (test correcto)

test_for_area_error (test incorrecto)