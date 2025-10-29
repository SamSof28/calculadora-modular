def potencia_modular(a,b,n):

    resultado = (a**b) % n
    return resultado

a = 12
b = 5
n = 7

print(f"{potencia_modular(a,b,n)}")