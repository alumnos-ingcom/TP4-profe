def suma_lenta(numero, otro_numero):
    return numero + otro_numero


    assert suma_lenta(10,11) == 20
    
    
def def test_suma_lenta():
    resultado = suma_lenta(10, 10)
    esperado = 20
    assert resultado == esperado