"""
ARCHIVO DE PRUEBAS - CALCULADORA MODULAR
=========================================
Este archivo prueba todas las funcionalidades de la calculadora modular
"""

from calculadora import (
    suma_modular, 
    producto_modular, 
    inverso_modular, 
    division_modular,
    raices_cuadradas, 
    cuadrados_perfectos, 
    potencia_modular,
    encriptar, 
    desencriptar,
    CARACTERES
)

def separador(titulo):
    """Imprime un separador visual con título"""
    print("\n" + "="*70)
    print(f"  {titulo}")
    print("="*70)

def prueba_1_suma_modular():
    """Prueba la suma modular"""
    separador("PRUEBA 1: SUMA MODULAR")
    
    # Ejemplo 1: (5 + 3) mod 7
    resultado = suma_modular(5, 3, 7)
    print(f"(5 + 3) mod 7 = {resultado}")
    print(f"[OK] Esperado: 1, Obtenido: {resultado}, {'CORRECTO' if resultado == 1 else 'ERROR'}")
    
    # Ejemplo 2: (10 + 8) mod 12
    resultado = suma_modular(10, 8, 12)
    print(f"\n(10 + 8) mod 12 = {resultado}")
    print(f"[OK] Esperado: 6, Obtenido: {resultado}, {'CORRECTO' if resultado == 6 else 'ERROR'}")

def prueba_2_producto_modular():
    """Prueba el producto modular"""
    separador("PRUEBA 2: PRODUCTO MODULAR")
    
    # Ejemplo 1: (5 * 3) mod 7
    resultado = producto_modular(5, 3, 7)
    print(f"(5 * 3) mod 7 = {resultado}")
    print(f"[OK] Esperado: 1, Obtenido: {resultado}, {'CORRECTO' if resultado == 1 else 'ERROR'}")
    
    # Ejemplo 2: (4 * 6) mod 10
    resultado = producto_modular(4, 6, 10)
    print(f"\n(4 * 6) mod 10 = {resultado}")
    print(f"[OK] Esperado: 4, Obtenido: {resultado}, {'CORRECTO' if resultado == 4 else 'ERROR'}")

def prueba_3_inverso_modular():
    """Prueba el inverso modular"""
    separador("PRUEBA 3: INVERSO MODULAR")
    
    # Ejemplo 1: inverso de 3 en Z_7
    resultado = inverso_modular(3, 7)
    print(f"Inverso de 3 en Z_7 = {resultado}")
    print(f"Verificacion: (3 * {resultado}) mod 7 = {(3 * resultado) % 7 if resultado else 'N/A'}")
    print(f"[OK] Esperado: 5, Obtenido: {resultado}, {'CORRECTO' if resultado == 5 else 'ERROR'}")
    
    # Ejemplo 2: inverso de 4 en Z_6 (no existe, porque gcd(4,6)=2)
    resultado = inverso_modular(4, 6)
    print(f"\nInverso de 4 en Z_6 = {resultado}")
    print(f"[OK] Esperado: None (no existe), Obtenido: {resultado}, {'CORRECTO' if resultado is None else 'ERROR'}")
    
    # Ejemplo 3: inverso de 5 en Z_6
    resultado = inverso_modular(5, 6)
    print(f"\nInverso de 5 en Z_6 = {resultado}")
    print(f"Verificacion: (5 * {resultado}) mod 6 = {(5 * resultado) % 6 if resultado else 'N/A'}")
    print(f"[OK] Esperado: 5, Obtenido: {resultado}, {'CORRECTO' if resultado == 5 else 'ERROR'}")

def prueba_4_division_modular():
    """Prueba la division modular"""
    separador("PRUEBA 4: DIVISION MODULAR")
    
    # Ejemplo 1: (8 / 3) mod 7
    # (8 / 3) mod 7 = (8 * inverso(3)) mod 7 = (8 * 5) mod 7 = 40 mod 7 = 5
    try:
        resultado = division_modular(8, 3, 7)
        print(f"(8 / 3) mod 7 = {resultado}")
        verificacion = (3 * resultado) % 7
        print(f"Verificacion: (3 * {resultado}) mod 7 = {verificacion}")
        print(f"[OK] Esperado: 5, Obtenido: {resultado}, {'CORRECTO' if resultado == 5 else 'ERROR'}")
    except ValueError as e:
        print(f"Error: {e}")
    
    # Ejemplo 2: (5 / 2) mod 6 (no debe funcionar porque 2 no tiene inverso en Z_6)
    print("\n(5 / 2) mod 6 (no debe funcionar):")
    try:
        resultado = division_modular(5, 2, 6)
        print(f"Resultado: {resultado} - ERROR, no deberia existir")
    except ValueError as e:
        print(f"[OK] CORRECTO: Se detecto el error -> {e}")

def prueba_5_raices_cuadradas():
    """Prueba las raíces cuadradas modulares"""
    separador("PRUEBA 5: RAICES CUADRADAS MODULARES")
    
    # Ejemplo 1: raíces de 4 en Z_5
    resultado = raices_cuadradas(4, 5)
    print(f"Raices cuadradas de 4 en Z_5: {resultado}")
    for r in resultado:
        print(f"  {r}² mod 5 = {(r*r) % 5}")
    print(f"[OK] Esperado: [2, 3], Obtenido: {resultado}, {'CORRECTO' if resultado == [2, 3] else 'ERROR'}")
    
    # Ejemplo 2: raíces de 1 en Z_8
    resultado = raices_cuadradas(1, 8)
    print(f"\nRaices cuadradas de 1 en Z_8: {resultado}")
    for r in resultado:
        print(f"  {r}² mod 8 = {(r*r) % 8}")
    print(f"[OK] Esperado: [1, 3, 5, 7], Obtenido: {resultado}, {'CORRECTO' if resultado == [1, 3, 5, 7] else 'ERROR'}")

def prueba_6_cuadrados_perfectos():
    """Prueba los cuadrados perfectos en Zn"""
    separador("PRUEBA 6: CUADRADOS PERFECTOS EN Zn")
    
    # Ejemplo 1: cuadrados perfectos en Z_5
    resultado = cuadrados_perfectos(5)
    print(f"Cuadrados perfectos en Z_5: {resultado}")
    print("Verificacion:")
    for i in range(5):
        print(f"  {i}² mod 5 = {(i*i) % 5}")
    print(f"[OK] Esperado: [0, 1, 4], Obtenido: {resultado}, {'CORRECTO' if resultado == [0, 1, 4] else 'ERROR'}")
    
    # Ejemplo 2: cuadrados perfectos en Z_8
    resultado = cuadrados_perfectos(8)
    print(f"\nCuadrados perfectos en Z_8: {resultado}")
    print("Verificacion:")
    for i in range(8):
        print(f"  {i}² mod 8 = {(i*i) % 8}")
    print(f"[OK] Esperado: [0, 1, 4], Obtenido: {resultado}, {'CORRECTO' if resultado == [0, 1, 4] else 'ERROR'}")

def prueba_7_potencia_modular():
    """Prueba la potencia modular"""
    separador("PRUEBA 7: POTENCIA MODULAR")
    
    # Ejemplo 1: 2^3 mod 5
    resultado = potencia_modular(2, 3, 5)
    print(f"2^3 mod 5 = {resultado}")
    print(f"Verificacion manual: 2^3 = 8, 8 mod 5 = 3")
    print(f"[OK] Esperado: 3, Obtenido: {resultado}, {'CORRECTO' if resultado == 3 else 'ERROR'}")
    
    # Ejemplo 2: 3^4 mod 7
    resultado = potencia_modular(3, 4, 7)
    print(f"\n3^4 mod 7 = {resultado}")
    print(f"Verificacion manual: 3^4 = 81, 81 mod 7 = 4")
    print(f"[OK] Esperado: 4, Obtenido: {resultado}, {'CORRECTO' if resultado == 4 else 'ERROR'}")
    
    # Ejemplo 3: 5^0 mod 7 (cualquier número elevado a 0 es 1)
    resultado = potencia_modular(5, 0, 7)
    print(f"\n5^0 mod 7 = {resultado}")
    print(f"[OK] Esperado: 1, Obtenido: {resultado}, {'CORRECTO' if resultado == 1 else 'ERROR'}")
    
    # Ejemplo 4: 2^10 mod 13
    resultado = potencia_modular(2, 10, 13)
    print(f"\n2^10 mod 13 = {resultado}")
    print(f"Verificacion manual: 2^10 = 1024, 1024 mod 13 = 10")
    print(f"[OK] Esperado: 10, Obtenido: {resultado}, {'CORRECTO' if resultado == 10 else 'ERROR'}")

def prueba_8_encriptar():
    """Prueba la encriptación modular"""
    separador("PRUEBA 8: ENCRIPTACION MODULAR")
    
    n = len(CARACTERES)  # 67 caracteres
    print(f"Alfabeto ({n} caracteres): '{CARACTERES}'")
    
    # Ejemplo 1: Encriptar "hola"
    mensaje1 = "hola"
    a1, b1 = 5, 8
    try:
        encriptado1 = encriptar(mensaje1, a1, b1, n)
        print(f"\nMensaje: '{mensaje1}'")
        print(f"Parámetros: a={a1}, b={b1}, n={n}")
        print(f"Encriptado: '{encriptado1}'")
        print("[OK] Encriptacion exitosa")
    except ValueError as e:
        print(f"Error: {e}")
    
    # Ejemplo 2: Encriptar "Cuál es la yegüita?" (del enunciado)
    mensaje2 = "Cuál es la yegüita?"
    a2, b2 = 3, 7
    try:
        encriptado2 = encriptar(mensaje2, a2, b2, n)
        print(f"\nMensaje: '{mensaje2}'")
        print(f"Parámetros: a={a2}, b={b2}, n={n}")
        print(f"Encriptado: '{encriptado2}'")
        print("[OK] Encriptacion exitosa")
    except ValueError as e:
        print(f"Error: {e}")
    
    # Ejemplo 3: Encriptar con mayúsculas "CUÁL ES LA YEGÜITA?" (del enunciado)
    mensaje3 = "CUÁL ES LA YEGÜITA?"
    a3, b3 = 9, 5
    try:
        encriptado3 = encriptar(mensaje3, a3, b3, n)
        print(f"\nMensaje: '{mensaje3}'")
        print(f"Parámetros: a={a3}, b={b3}, n={n}")
        print(f"Encriptado: '{encriptado3}'")
        print("[OK] Encriptacion exitosa")
    except ValueError as e:
        print(f"Error: {e}")

def prueba_9_desencriptar():
    """Prueba la desencriptación modular"""
    separador("PRUEBA 9: DESENCRIPTACION MODULAR")
    
    n = len(CARACTERES)
    
    # Ejemplo 1: Encriptar y desencriptar "hola"
    mensaje_original = "hola"
    a, b = 5, 8
    
    try:
        print(f"Mensaje original: '{mensaje_original}'")
        print(f"Parámetros: a={a}, b={b}, n={n}")
        
        mensaje_encriptado = encriptar(mensaje_original, a, b, n)
        print(f"Mensaje encriptado: '{mensaje_encriptado}'")
        
        mensaje_desencriptado = desencriptar(mensaje_encriptado, a, b, n)
        print(f"Mensaje desencriptado: '{mensaje_desencriptado}'")
        
        if mensaje_original == mensaje_desencriptado:
            print("[OK] CORRECTO: El mensaje se encripto y desencripto correctamente")
        else:
            print("[ERROR] ERROR: El mensaje desencriptado no coincide con el original")
    except ValueError as e:
        print(f"Error: {e}")
    
    # Ejemplo 2: Encriptar y desencriptar "Cuál es la yegüita?"
    mensaje_original2 = "Cuál es la yegüita?"
    a2, b2 = 3, 7
    
    try:
        print(f"\nMensaje original: '{mensaje_original2}'")
        print(f"Parámetros: a={a2}, b={b2}, n={n}")
        
        mensaje_encriptado2 = encriptar(mensaje_original2, a2, b2, n)
        print(f"Mensaje encriptado: '{mensaje_encriptado2}'")
        
        mensaje_desencriptado2 = desencriptar(mensaje_encriptado2, a2, b2, n)
        print(f"Mensaje desencriptado: '{mensaje_desencriptado2}'")
        
        if mensaje_original2 == mensaje_desencriptado2:
            print("[OK] CORRECTO: El mensaje se encripto y desencripto correctamente")
        else:
            print("[ERROR] ERROR: El mensaje desencriptado no coincide con el original")
    except ValueError as e:
        print(f"Error: {e}")
    
    # Ejemplo 3: Con mayúsculas
    mensaje_original3 = "CUÁL ES LA YEGÜITA?"
    a3, b3 = 9, 5
    
    try:
        print(f"\nMensaje original: '{mensaje_original3}'")
        print(f"Parámetros: a={a3}, b={b3}, n={n}")
        
        mensaje_encriptado3 = encriptar(mensaje_original3, a3, b3, n)
        print(f"Mensaje encriptado: '{mensaje_encriptado3}'")
        
        mensaje_desencriptado3 = desencriptar(mensaje_encriptado3, a3, b3, n)
        print(f"Mensaje desencriptado: '{mensaje_desencriptado3}'")
        
        if mensaje_original3 == mensaje_desencriptado3:
            print("[OK] CORRECTO: El mensaje se encripto y desencripto correctamente")
        else:
            print("[ERROR] ERROR: El mensaje desencriptado no coincide con el original")
    except ValueError as e:
        print(f"Error: {e}")

def prueba_manejo_errores():
    """Prueba el manejo de errores"""
    separador("PRUEBA ADICIONAL: MANEJO DE ERRORES")
    
    print("1. Probando modulo invalido (n=1):")
    try:
        suma_modular(5, 3, 1)
        print("   [ERROR] ERROR: Deberia haber lanzado una excepcion")
    except ValueError as e:
        print(f"   [OK] CORRECTO: {e}")
    
    print("\n2. Probando encriptacion con caracter invalido:")
    try:
        encriptar("hola@mundo", 5, 8, 67)
        print("   [ERROR] ERROR: Deberia haber lanzado una excepcion")
    except ValueError as e:
        print(f"   [OK] CORRECTO: {e}")
    
    print("\n3. Probando encriptacion con a y n no coprimos:")
    try:
        encriptar("hola", 2, 8, 10)  # gcd(2, 10) = 2
        print("   [ERROR] ERROR: Deberia haber lanzado una excepcion")
    except ValueError as e:
        print(f"   [OK] CORRECTO: {e}")

def ejecutar_todas_las_pruebas():
    """Ejecuta todas las pruebas"""
    print("\n")
    print("=" + "="*68 + "=")
    print("|" + " "*15 + "CALCULADORA MODULAR - PRUEBAS" + " "*24 + "|")
    print("|" + " "*20 + "Matematicas Discretas" + " "*26 + "|")
    print("=" + "="*68 + "=")
    
    prueba_1_suma_modular()
    prueba_2_producto_modular()
    prueba_3_inverso_modular()
    prueba_4_division_modular()
    prueba_5_raices_cuadradas()
    prueba_6_cuadrados_perfectos()
    prueba_7_potencia_modular()
    prueba_8_encriptar()
    prueba_9_desencriptar()
    prueba_manejo_errores()
    
    separador("PRUEBAS COMPLETADAS")
    print("\n[OK] Todas las pruebas han sido ejecutadas.")
    print("  Revisa los resultados arriba para verificar que todo este correcto.")
    print("\n")

if __name__ == "__main__":
    ejecutar_todas_las_pruebas()

