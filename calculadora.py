import math

# ============================================
# CALCULADORA MODULAR - MATEMÁTICAS DISCRETAS
# ============================================

# Lista de caracteres para encriptación/desencriptación (posición 0-64)
CARACTERES = "abcdefghijklmnopqrstuvwxyzáéíóúü !?ABCDEFGHIJKLMNOPQRSTUVWXYZÁÉÍÓÚÜ"


def validar_modulo(n: int):
    if n <= 1:
        raise ValueError("El módulo n debe ser mayor que 1.")
    return True

#1. Suma Modular
def suma_modular(a: int, b: int, n: int) -> int:
    validar_modulo(n)
    return (a + b) % n

#2. Producto Modular
def producto_modular(a: int, b: int, n: int) -> int:
    validar_modulo(n)
    return (a * b) % n

#3. Inverso Modular
def inverso_modular(a: int, n: int) -> int:
    validar_modulo(n)
    
    if math.gcd(a, n) != 1:
        return None
    
    for x in range(1, n):
        if (a * x) % n == 1:
            return x
    return None

#4. División Modular
def division_modular(a: int, b: int, n: int) -> int:
    validar_modulo(n)
    inverso_b = inverso_modular(b, n)
    if inverso_b is None:
        raise ValueError(f"No existe inverso modular para {b} en Z_{n}. gcd({b}, {n}) = {math.gcd(b, n)} != 1")
    return (a * inverso_b) % n

#5. Raíces Cuadradas Modulares
def raices_cuadradas(a: int, n: int) -> list[int]:
    validar_modulo(n)
    
    soluciones = []
    for r in range(n):
        if (r * r) % n == a:
            soluciones.append(r)
    return soluciones

#6. Cuadrados Perfectos en Zn
def cuadrados_perfectos(n: int) -> list[int]:
    validar_modulo(n)
    cuadrados = []

    for r in range(n):
        cuadrado = (r * r) % n

        if cuadrado not in cuadrados:
            cuadrados.append(cuadrado)

    return sorted(cuadrados)

#7. Potencia Modular
def potencia_modular(a: int, b: int, n: int) -> int:
    validar_modulo(n)
    resultado = (a**b) % n
    return resultado


#8. Encriptación Modular
def encriptar(mensaje, a, b, n):
    # Validar que el mensaje solo contenga caracteres válidos
    for char in mensaje:
        if char not in CARACTERES:
            raise ValueError(f"El carácter '{char}' no está en la lista de caracteres permitidos.")
    
    # Validar que a y n sean coprimos
    if math.gcd(n, a) != 1:
        raise ValueError(f"El coeficiente a={a} y n={n} deben ser primos relativos (mcd(n, a)=1)")
    
    mensaje_encriptado = ""
    
    # Para cada carácter del mensaje
    for caracter in mensaje:
        # 1. Obtener la posición x del carácter en la lista
        x = CARACTERES.index(caracter)
        
        # 2. Aplicar la función de cifrado: y = (ax + b) mod n
        y = (a * x + b) % n
        
        # 3. Obtener el carácter cifrado correspondiente a la posición y
        char_cifrado = CARACTERES[y]
        
        # 4. Agregar el carácter cifrado al mensaje
        mensaje_encriptado += char_cifrado
    
    return mensaje_encriptado


#9. Desencriptación Modular
def desencriptar(mensaje_encriptado, a, b, n):
    # Validar que el mensaje solo contenga caracteres válidos
    for caracter in mensaje_encriptado:
        if caracter not in CARACTERES:
            raise ValueError(f"El carácter '{caracter}' no está en la lista de caracteres permitidos.")
    
    # Validar que n y a sean primos relativos y obtener el inverso modular de a
    a_inv = inverso_modular(a, n)
    if a_inv is None:
        raise ValueError(f"El coeficiente a={a} y n={n} deben ser primos relativos (mcd(n, a)=1)")
    
    mensaje_desencriptado = ""
    
    # Para cada carácter del mensaje encriptado
    for caracter in mensaje_encriptado:
        # 1. Obtener la posición y del carácter cifrado en la lista
        y = CARACTERES.index(caracter)
        
        # 2. Aplicar la función de descifrado: x = a^(-1)(y - b) mod n
        # Primero (y - b) mod n para asegurar que el resultado sea positivo
        y_menos_b = (y - b)
        # Luego multiplicar por el inverso modular de a
        x = (a_inv * y_menos_b) % n
        
        # 3. Obtener el carácter original correspondiente a la posición x
        char_original = CARACTERES[x]
        
        # 4. Agregar el carácter original al mensaje
        mensaje_desencriptado += char_original
    
    return mensaje_desencriptado


# ============================================
# MENÚ PRINCIPAL
# ============================================

def mostrar_menu():
    """Muestra el menú de opciones"""
    print("\n" + "="*60)
    print("     CALCULADORA MODULAR - MATEMÁTICAS DISCRETAS")
    print("="*60)
    print("1. Suma modular (a + b) mod n")
    print("2. Producto modular (a * b) mod n")
    print("3. Inverso modular de un número")
    print("4. División modular (a / b) mod n")
    print("5. Raíces cuadradas de un número en Zn")
    print("6. Lista de cuadrados perfectos en Zn")
    print("7. Potencia modular (a^b) mod n")
    print("8. Encriptar un mensaje")
    print("9. Desencriptar un mensaje")
    print("0. Salir")
    print("="*60)

def leer_entero(prompt, permitir_negativos=False):
    """Lee un número entero con validación"""
    while True:
        try:
            valor = int(input(prompt))
            if not permitir_negativos and valor < 0:
                print("Error: El valor no puede ser negativo.")
                continue
            return valor
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")

def leer_modulo():
    """Lee el módulo n con validación"""
    while True:
        n = leer_entero("Ingrese el módulo n (n > 1): ")
        try:
            validar_modulo(n)
            return n
        except ValueError as e:
            print(f"Error: {e}")

def leer_elemento_zn(n, nombre="número"):
    """Lee un elemento de Zn con validación"""
    while True:
        valor = leer_entero(f"Ingrese el {nombre} (0 <= valor < {n}): ")
        if 0 <= valor < n:
            return valor
        print(f"Error: El {nombre} debe estar entre 0 y {n-1}.")

def main():
    """Función principal con menú interactivo"""
    print("\n¡Bienvenido a la Calculadora Modular!")
    
    while True:
        try:
            mostrar_menu()
            opcion = input("\nSeleccione una opción (0-9): ").strip()
            
            if opcion == "0":
                print("\n¡Gracias por usar la Calculadora Modular! Hasta luego.")
                break
            
            elif opcion == "1":  # Suma modular
                print("\n--- SUMA MODULAR ---")
                n = leer_modulo()
                a = leer_elemento_zn(n, "primer número")
                b = leer_elemento_zn(n, "segundo número")
                resultado = suma_modular(a, b, n)
                print(f"\n({a} + {b}) mod {n} = {resultado}")
            
            elif opcion == "2":  # Producto modular
                print("\n--- PRODUCTO MODULAR ---")
                n = leer_modulo()
                a = leer_elemento_zn(n, "primer número")
                b = leer_elemento_zn(n, "segundo número")
                resultado = producto_modular(a, b, n)
                print(f"\n({a} * {b}) mod {n} = {resultado}")
            
            elif opcion == "3":  # Inverso modular
                print("\n--- INVERSO MODULAR ---")
                n = leer_modulo()
                a = leer_elemento_zn(n, "número")
                inverso = inverso_modular(a, n)
                if inverso is None:
                    print(f"\n{a} NO tiene inverso modular en Z_{n}.")
                    print(f"Razón: gcd({a}, {n}) = {math.gcd(a, n)} ≠ 1")
                else:
                    print(f"\nEl inverso de {a} en Z_{n} es: {inverso}")
                    print(f"Verificación: ({a} * {inverso}) mod {n} = {(a * inverso) % n}")
            
            elif opcion == "4":  # División modular
                print("\n--- DIVISIÓN MODULAR ---")
                n = leer_modulo()
                a = leer_elemento_zn(n, "dividendo")
                b = leer_elemento_zn(n, "divisor")
                try:
                    resultado = division_modular(a, b, n)
                    print(f"\n({a} / {b}) mod {n} = {resultado}")
                    print(f"Verificación: ({b} * {resultado}) mod {n} = {(b * resultado) % n}")
                except ValueError as e:
                    print(f"\nError: {e}")
            
            elif opcion == "5":  # Raíces cuadradas
                print("\n--- RAÍCES CUADRADAS MODULARES ---")
                n = leer_modulo()
                a = leer_elemento_zn(n, "número")
                raices = raices_cuadradas(a, n)
                if raices:
                    print(f"\nLas raíces cuadradas de {a} en Z_{n} son: {raices}")
                    for r in raices:
                        print(f"  {r}² mod {n} = {(r*r) % n}")
                else:
                    print(f"\n{a} NO tiene raíces cuadradas en Z_{n}.")
            
            elif opcion == "6":  # Cuadrados perfectos
                print("\n--- CUADRADOS PERFECTOS EN Zn ---")
                n = leer_modulo()
                cuadrados = cuadrados_perfectos(n)
                print(f"\nLos cuadrados perfectos en Z_{n} son: {cuadrados}")
                print(f"Total: {len(cuadrados)} cuadrados perfectos de {n} elementos.")
            
            elif opcion == "7":  # Potencia modular
                print("\n--- POTENCIA MODULAR ---")
                n = leer_modulo()
                a = leer_elemento_zn(n, "base")
                b = leer_entero("Ingrese el exponente: ")
                if b < 0:
                    print("Error: El exponente debe ser no negativo.")
                    continue
                resultado = potencia_modular(a, b, n)
                print(f"\n{a}^{b} mod {n} = {resultado}")
            
            elif opcion == "8":  # Encriptar
                print("\n--- ENCRIPTACIÓN MODULAR ---")
                print(f"Alfabeto usado ({len(CARACTERES)} caracteres):")
                print(f"'{CARACTERES}'")
                print("\nNota: 'esp' representa el espacio en blanco")
                
                n = len(CARACTERES)
                print(f"\nSe usará n = {n} (tamaño del alfabeto)")
                
                a = leer_entero("Ingrese el coeficiente a: ", permitir_negativos=True)
                b = leer_entero("Ingrese el término independiente b: ", permitir_negativos=True)
                
                mensaje = input("Ingrese el mensaje a encriptar: ")
                
                try:
                    mensaje_encriptado = encriptar(mensaje, a, b, n)
                    print(f"\nMensaje original:   '{mensaje}'")
                    print(f"Mensaje encriptado: '{mensaje_encriptado}'")
                except ValueError as e:
                    print(f"\nError: {e}")
            
            elif opcion == "9":  # Desencriptar
                print("\n--- DESENCRIPTACIÓN MODULAR ---")
                print(f"Alfabeto usado ({len(CARACTERES)} caracteres):")
                print(f"'{CARACTERES}'")
                
                n = len(CARACTERES)
                print(f"\nSe usará n = {n} (tamaño del alfabeto)")
                
                a = leer_entero("Ingrese el coeficiente a original: ", permitir_negativos=True)
                b = leer_entero("Ingrese el término independiente b original: ", permitir_negativos=True)
                
                mensaje_encriptado = input("Ingrese el mensaje encriptado: ")
                
                try:
                    mensaje_desencriptado = desencriptar(mensaje_encriptado, a, b, n)
                    print(f"\nMensaje encriptado:   '{mensaje_encriptado}'")
                    print(f"Mensaje desencriptado: '{mensaje_desencriptado}'")
                except ValueError as e:
                    print(f"\nError: {e}")
            
            else:
                print("\nOpción inválida. Por favor seleccione un número entre 0 y 9.")
        
        except KeyboardInterrupt:
            print("\n\n¡Programa interrumpido! Hasta luego.")
            break
        except Exception as e:
            print(f"\nError inesperado: {e}")
            print("Por favor, intente nuevamente.")

if __name__ == "__main__":
    main()