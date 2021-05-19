################
# Martín René - @martinvilu
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

class IngresoIncorrecto(Exception):
    """Esta es la Excepcion para el ingreso incorrecto"""
    pass 

def ingreso_entero(mensaje):
    """
    Esta funcion muestra un mensaje y agrega la # para indicar el ingreso
    de un número entero.
    """
    ingreso = input(mensaje + " #")
    try:
        entero = int(ingreso)
    except ValueError as err:
        raise IngresoIncorrecto("'{ingreso}' no era un número!") from err
    return entero

def ingreso_entero_reintento(mensaje, cantidad_reintentos=5):
    intentos = cantidad_reintentos
    while cantidad_reintentos > 0:
        try:
            return ingreso_entero(mensaje)
        except IngresoIncorrecto as err:
            cantidar_reintentos = cantidad_reintentos - 1
    raise IngresoIncorrecto("Luego de {intentos}")
    
    
    
def ingreso_entero_restringido(mensaje,valor_minimo=0, valor_maximo=10):
    pass
    


# Reemplazar por las funciones del ejercicio


def prueba():
    num = ingreso_entero("Dame un número vieja!")
    print(f"El número, vieja; es {num}")

if __name__ == "__main__":
    prueba()
