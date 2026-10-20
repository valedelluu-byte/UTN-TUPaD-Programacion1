
# TRABAJO PRÁCTICO N° 11 (TP7): APLICACIÓN DE LA RECURSIVIDAD

# EJERCICIO 1: Factorial de un número

def factorial(n: int) -> int:
    """Calcula el factorial de un número entero positivo de forma recursiva."""
    # Caso base: El factorial de 0 y 1 es 1
    if n <= 1:
        return 1
    # Caso recursivo: n * factorial(n - 1)
    else:
        return n * factorial(n - 1)
    
def resolver_ejercicio_1():
    print("--- EJERCICIO 1: Factorial ---")
    limite = int(input("Ingrese un número entero positivo: "))
    print(f"\nFactoriales del 1 al {limite}:")
    for i in range(1, limite + 1):
        print(f"El factorial de {i} es: {factorial(i)}")

# EJERCICIO 2: Serie de Fibonacci

def fibonacci(posicion: int) -> int:
    """Calcula el valor de la serie de Fibonacci en la posición indicada."""
    # Casos base: Posición 0 es 0, posición 1 es 1
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    # Caso recursivo: Suma de las dos posiciones anteriores
    else:
        return fibonacci(posicion - 1) + fibonacci(posicion - 2)

def resolver_ejercicio_2():
    print("\n--- EJERCICIO 2: Serie de Fibonacci ---")
    pos_limite = int(input("Ingrese la posición límite de la serie de Fibonacci: "))
    print(f"\nSerie completa de Fibonacci hasta la posición {pos_limite}:")
    for i in range(pos_limite + 1):
        print(f"Posición {i}: {fibonacci(i)}")


# EJERCICIO 3: Potencia de un número

def potencia(base: int, exponente: int) -> int:
    """Calcula la potencia de un número elevado a un exponente (n^m = n * n^(m-1))."""
    # Caso base: Todo número elevado a 0 es 1
    if exponente == 0:
        return 1
    # Caso recursivo: base * potencia(base, exponente - 1)
    else:
        return base * potencia(base, exponente - 1)


def resolver_ejercicio_3():
    print("\n--- EJERCICIO 3: Potencia de un número ---")
    base = int(input("Ingrese el número base: "))
    exponente = int(input("Ingrese el exponente (>= 0): "))
    resultado = potencia(base, exponente)
    print(f"Resultado: {base}^{exponente} = {resultado}")


# EJERCICIO 4: Decimal a Binario

def decimal_a_binario(n: int) -> str:
    """Convierte un número decimal entero positivo a su representación binaria (str)."""
    # Casos base: 0 o 1
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    # Caso recursivo: División entera de 2 y todos los restos del ultimo al primero
    else:
        resto = n % 2
        cociente = n // 2
        return decimal_a_binario(cociente) + str(resto)


def resolver_ejercicio_4():
    print("\n--- EJERCICIO 4: Decimal a Binario ---")
    num = int(input("Ingrese un número entero positivo en decimal: "))
    print(f"El número {num} en binario es: {decimal_a_binario(num)}")


# EJERCICIO 5: Es Palíndromo

def es_palindromo(palabra: str) -> bool:
    """Verifica si una palabra es palíndromo sin usar [::-1] ni reversed()."""
    # Caso base: Cadena vacía o de 1 carácter siempre es palíndromo
    if len(palabra) <= 1:
        return True
    
    # Caso recursivo: Comparar primer y último carácter
    if palabra[0] == palabra[-1]:
        return es_palindromo(palabra[1:-1])
    else:
        return False

def resolver_ejercicio_5():
    print("\n--- EJERCICIO 5: Palíndromo ---")
    texto = input("Ingrese una palabra (sin espacios ni tildes): ").lower()
    if es_palindromo(texto):
        print(f"'{texto}' ES un palíndromo.")
    else:
        print(f"'{texto}' NO es un palíndromo.")


# EJERCICIO 6: Suma de Dígitos

def suma_digitos(n: int) -> int:
    """Suma todos los dígitos de un número entero sin convertirlo a str."""
    # Caso base: Número de un solo dígito
    if n < 10:
        return n
    # Caso recursivo: Último dígito + suma_digitos(resto del número)
    else:
        ultimo_digito = n % 10
        resto_numero = n // 10
        return ultimo_digito + suma_digitos(resto_numero)


def resolver_ejercicio_6():
    print("\n--- EJERCICIO 6: Suma de Dígitos ---")
    num = int(input("Ingrese un número entero positivo: "))
    print(f"La suma de los dígitos de {num} es: {suma_digitos(num)}")


# EJERCICIO 7: Contar Bloques de la Pirámide

def contar_bloques(n: int) -> int:
    """Suma los bloques necesarios para construir una pirámide de n niveles."""
    # Caso base: El nivel más bajo de 1 bloque requiere 1 bloque
    if n <= 1:
        return 1
    # Caso recursivo: Bloques del nivel actual + bloques de los niveles superiores
    else:
        return n + contar_bloques(n - 1)

def resolver_ejercicio_7():
    print("\n--- EJERCICIO 7: Pirámide de Bloques ---")
    n = int(input("Ingrese la cantidad de bloques en el nivel más bajo: "))
    print(f"El total de bloques necesarios es: {contar_bloques(n)}")


# EJERCICIO 8: Contar Ocurrencias de un Dígito

def contar_digito(numero: int, digito: int) -> int:
    """Cuenta cuántas veces aparece un dígito específico dentro de un número."""
    # Caso base: Si el número quedó en 0
    if numero == 0:
        return 0
    
    ultimo = numero % 10
    resto_numero = numero // 10
    
    # Caso recursivo: Verificar si el último dígito coincide con el buscado
    if ultimo == digito:
        return 1 + contar_digito(resto_numero, digito)
    else:
        return 0 + contar_digito(resto_numero, digito)


def resolver_ejercicio_8():
    print("\n--- EJERCICIO 8: Contar Ocurrencias de un Dígito ---")
    num = int(input("Ingrese el número entero: "))
    dig = int(input("Ingrese el dígito a buscar (0 al 9): "))
    cantidad = contar_digito(num, dig)
    print(f"El dígito {dig} aparece {cantidad} veces en {num}.")


# MENÚ PRINCIPAL
def main():
    while True:
        print("\n==============================================")
        print("    MENÚ DE EJERCICIOS - TP11 (RECURSIVIDAD)   ")
        print("==============================================")
        print("1. Calcular Factorial")
        print("2. Serie de Fibonacci")
        print("3. Potencia de un número")
        print("4. Convertir Decimal a Binario")
        print("5. Verificar Palíndromo")
        print("6. Suma de dígitos")
        print("7. Contar bloques de una pirámide")
        print("8. Contar apariciones de un dígito")
        print("9. Salir")
        
        opcion = input("\nSeleccione una opción (1-9): ")
        
        if opcion == "1":
            resolver_ejercicio_1()
        elif opcion == "2":
            resolver_ejercicio_2()
        elif opcion == "3":
            resolver_ejercicio_3()
        elif opcion == "4":
            resolver_ejercicio_4()
        elif opcion == "5":
            resolver_ejercicio_5()
        elif opcion == "6":
            resolver_ejercicio_6()
        elif opcion == "7":
            resolver_ejercicio_7()
        elif opcion == "8":
            resolver_ejercicio_8()
        elif opcion == "9":
            print("\n¡Gracias por usar el programa! Éxitos en el examen.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


# Ejecución del programa
if __name__ == "__main__":
    main()