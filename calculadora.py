import math

# Calculadora Modular con 10 funcionalidades

#1. Suma Modular
def suma_modular(a, b, n):
    return (a + b) % n

#2. Producto Modular
def producto_modular(a, b, n):
    return (a * b) % n

#3. Inverso Modular
def inverso_modular(a, n):
    if n <= 0:
        raise ValueError("El módulo n no puede ser menor o igual a cero.")
    if math.gcd(n, a) == 1:
        for x in range(1, n):
            if (a * x) % n == 1:
                return x
            
#4. División Modular
def division_modular(a, b, n):
    inverso_mod = inverso_modular(b, n)
    if inverso_mod is None:
        raise ValueError(f"No existe inverso modular para {b} en Z_{n}.")
    return (a * inverso_mod) % n

#5. Raíz Modular r*r ≡ a
def raiz_modular(a, n):
    if n <= 0:
        raise ValueError("El módulo n no puede ser menor o igual a cero.")
    
    soluciones = []
    for r in range(n):
        if (r * r) % n == a:
            soluciones.append(r)
    return soluciones
        
    
#6. Potencia Modular
def potencia_modular(a, b, n):
    if n <= 0:
        raise ValueError("El módulo n no puede ser menor o igual a cero.")
    
    if pow(a, b) < n:
        return pow(a, b) % n

#7. Cuadrado Perfecto Modular

#8. Encriptación Modular

#9. Desencriptación Modular


def main():
    while True:
        try:
            a = int(input("Ingrese el número a: "))
            b = int(input("Ingrese el número b: "))
            n = int(input("Ingrese el tamaño del conjunto Z_n (n > 1): "))
            if n <= 1:
                print("n debe ser mayor que 1. Intenta de nuevo.")
                continue
            break
        except ValueError:
            print("Entradas inválidas. Introduce enteros.")

    print(f"\nResultados en Z_{n}:")
    print("suma_modular:", suma_modular(a, b, n))
    print("producto_modular:", producto_modular(a, b, n))
    inv_b = inverso_modular(b, n)
    print("inverso_modular(b):", inv_b)
    print("potencia_modular a^b:", potencia_modular(a, b, n))
    print("raiz_modular a:", raiz_modular(a, n))
    try:
        print("division_modular a/b:", division_modular(a, b, n))
    except ValueError as e:
        print("division_modular:", e)

if __name__ == "__main__":
    main()



 
