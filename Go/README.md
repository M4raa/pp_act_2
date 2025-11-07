# Contador de Vocales

Programa en Go que cuenta las vocales según la entrada del usuario.  
No distingue entre mayúsculas y minúsculas.

Este programa tiene 2 funciones definidas:
    - main() -> Función principal. Pide al usuario introducir una frase.

    - CountVowels(text string) int -> Función que recibe una cadena y devuelve el número total de vocales que contiene.

## Funcionamiento del Programa

El flujo de este programa es:
main()
  ↓  
Mostrar "Contador de Vocales..."
  ↓  
Solicitar entrada de texto
  ↓  
Llamar a CountVowels(texto)
  ↓  
Mostrar el resultado por pantalla
  ↓  
Fin

## Ejecución

Para ejecutarlo:

```bash
go run contador_de_vocales.go
```

**Ejemplo:**
```
Contador de Vocales en Go
Introduce una frase: hola
La frase contiene 2 vocal(es).
```

---

## Pruebas

Las pruebas ahora se realizarán con el módulo integrado en Go.

### Ejecución de las pruebas
Desde la terminal, ejecutar:

```bash
go mod init contador
go test
```

### Descripción
Se prueba la función CountVowels.
El archivo de test incluye tres pruebas:

TestCountVowelsSimple → Test correcto (vocales normales)

TestCountVowelsWithUppercase → Test correcto (vocales en mayúsculas)

TestCountVowelsIncorrect → Test incorrecto intencional para mostrar fallo en test