from tp4ej1 import ingreso_entero, IngresoIncorrecto


def suma_lenta(numero, otro_numero):
    return numero + otro_numero    
    
def prueba():
    try:
        ingreso_entero("pa sumar")
    except IngresoIncorrecto as oops:
        print(f"OOOPS {oops}")
    
    
def test_suma_lenta():
    resultado = suma_lenta(10, 10)
    esperado = 20
    
if __name__ == "__main__":
    print(__name__)
    prueba()
