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
    ingreso = input(mensaje + " # ")
    try:
        entero = int(ingreso)
    except ValueError as err:
        raise IngresoIncorrecto(f"'{ingreso}' no era un número!") from err
    return entero

def ingreso_entero_reintento(mensaje, cantidad_reintentos=5):
    intentos = cantidad_reintentos
    while cantidad_reintentos > 0:
        try:
            return ingreso_entero(mensaje)
        except IngresoIncorrecto as err:
            print(f"No era un número, quedan {cantidad_reintentos}")
            cantidad_reintentos = cantidad_reintentos - 1
    raise IngresoIncorrecto(f"Luego de {intentos}")
    
    
def ingreso_entero_restringido(mensaje,valor_minimo=0, valor_maximo=10):
    msg = f"{mensaje} entre {valor_minimo} y {valor_maximo}"
    num = ingreso_entero(msg)
    if (num >= valor_minimo and num <= valor_maximo):
        return num
    else:
        print(f"el ingreso no era un numero entre "
              f"entre {valor_minimo} y {valor_maximo}")
        raise IngresoIncorrecto(msg)
    print("Y acá? que hacemos?")

# Reemplazar por las funciones del ejercicio


def prueba():
    msg = "Dame un número vieja!"
#     num = ingreso_entero(msg)
#     print(f"El número, vieja; es {num}")
#     
#     num = ingreso_entero_reintento(msg, cantidad_reintentos=2)
#     print(f"El número, vieja; es {num}")
    
    num = ingreso_entero_restringido(msg, 2, 8)
    print(f"El número, vieja; es {num}")

    
print("TP4ej1 " + __name__)

if __name__ == "__main__":
    prueba()
