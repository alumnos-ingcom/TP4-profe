# TP4-plantilla Python 1

## Forma de entrega
* Cada punto debe ser entregado en un archivo independiente

* El nombre de cada archivo debe ser ser `tp4-ej` seguido del numero de ejercicio mas `.py` (el primer ejercicio sera entonces `tp4-ej1.py`

* Cada función a implementar requiere escribir un programa que haga uso de la función de manera interactiva.

* Cada archivo debe seguir la estructura indicada dentro del archivo `plantilla.py`, reemplacen con su nombre y nombre de usuario de GitHub. 

* Siguiendo con la `plantilla.py`; el programa que hace uso de lo que  debe residir dentro de la función `prueba` de forma de que pueda ser ignorado al usarlo como libreria. (Al final de este documento copio la plantilla para referencia tambien)

* En ningún caso se aceptara el uso de variables globales. Toda la información necesaria para el funcionamiento de las funciones a desarrollar tienen que ser pasados como argumentos de las mismas.

* Se provee el prototipo de la funcion a implementar en todos los ejercicios

* Usen nombres de variables descriptivos siempre.


## Importante
Muchas de las funciones pedidas ya se encuentran implementadas como parte de Python, implementen las funciones sin depender de esta funcionalidad integrada, sin embargo, pueden usar esta funcionalidad para verificar su funcionamiento. Esto incluye tambíen a los atajos, usen lazos.

## Ejercicios
### 1. Ingreso de números enteros
Limitar el ingreso de valores y gestionar los errores que dicha actividad puedan producir es una actividad cotidiana en los primeros programas a desarrollar. Por lo que es un excelente primer ejercicio.

Escribir una funcion que solicite el ingreso de un número entero y vuelva a solicitarlo en caso de ingresar un valor incorrecto

Escribir una funcion que solicite el ingreso de un número entero entre dos valores.

Las tres funciones al rechazar el ingreso de valores incorrectos, deben levantar la excepción `IngresoIncorrecto` con un mensaje que indique lo sucedido.


``` python
def ingreso_entero_reintento(mensaje, cantidad_reintentos=5):
def ingreso_entero_restringido(mensaje,valor_minimo=0, valor_maximo=10):

class IngresoIncorrecto(Exception):
    """Esta es la Excepcion para el ingreso incorrecto"""
    pass 
```

#### Ejemplo de implementación

``` python
def ingreso_entero(mensaje):
    """
    Esta funcion muestra un mensaje y agrega la # para indicar el ingreso
    de un número entero.
    """
    ingreso = input(mensaje + " #")
    try:
        entero = int(ingreso)
    except ValueError as err:
        raise IngresoIncorrecto("No era un número!") from err
    return entero
```

#### Uso
Este es el primer ejercicio, para poder darle uso en todos los ejercicios siguientes. ¡Esto mismo lo pueden hacer con cualquier otro ejercicio!

```python
import tp4ej1 as soporte

soporte.ingreso_entero("Hola Mundo")
```

### 2. Suma lenta

Escribir una función que haga la suma entre dos números enteros sin hacer la operación de manera directa. Esto quiere decir que para hacer la suma entre 4 y 3, las operaciones resultantes deberán ser 4+1+1+1.

La funcion debe ser capaz de sumar cualquier numero entero positivo y negativo.

``` python
def suma_lenta(numero, otro_numero):
```

### 3. Conversión de temperaturas

Se quiere transformar temperaturas en grados fahrenheit a grados centígrados y viceversa.

Escribir las funciones para convertir la temperatura en grados centigrados en fahrenheit como un número real, utilice esta formula para calcular los grados centígrados y retorne el resultado obtenido. Y viceversa.

``` python
def convertir_a_fahrrenheit(centigrados):
def convertir_a_centigrados(fahrenheit):
```

### 4. Comparación de números

Escribir una función que reciba dos valores y retorne:
 * Retornar `-1` si el primero es menor que el segundo
 * Retornar `0` si son iguales
 * Retornar `1` si el primero es mayor que el segundo

``` python
def compara(numero, otro_numero):
```

### 5. Números positivos y negativos

Escribir una función que reciba un número e indique si el mismo es positivo, negativo o cero.

``` python
def signo(numero):
```

### 6. Máximo / Mínimo

Escribir una función que dada una lista de valores enteros, retorne el menor ellos. E implementar otra función que retorne el valor máximo del conjunto de valores.
``` python
def minimo(lista):
def maximo(lista):
```

### 7. Restas sucesivas
Escribir una función que mediante restas sucesivas, obtenga el valor del cociente y resto de dos números enteros.

``` python
def division_lenta(dividendo, divisor):
```

### 8. Ordenar 3 valores
Escribir una función que a partir de tres variables de tipo entero retorne una tupla con dichos valores ordenados de menor a mayor. Y Viceversa
Interfaz
``` python
def ordenar_mayor_a_menor(uno, dos, tres):
def ordenar_menor_a_mayor(uno, dos, tres):
```

### 9. Números primos
Escribir una función que indique con `True` si un numero indicado es Primo.

``` python
def es_primo(numero):
```

### 10. Factores Primos
Escribir una función que retorne una `tuple` con factores primos de un numero entero positivo.

``` python
def factores_primos(numero):
```
### 10. Palíndromo
Escribir una función que indique con True si una palabra o frase ingresada se trata de un palindromo.
Palíndromo, es si se lee igual de derecha a izquierda que de izquierda a derecha.

``` python
def es_palindromo(texto)
```

## Plantilla de entrega individual

```python
################
# Martín René - @martinvilu
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio


def prueba():
    pass

if __name__ == "__main__":
    prueba()
```
