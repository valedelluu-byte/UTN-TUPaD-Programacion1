#Actividad 1: imprimir numeros del 0 al 100
def imprimir_numeros():
    for i in range(101):
        print(i)
imprimir_numeros()
#Actividad 2: contar digitos de un numero
numero = int(input("Ingrese un numero entero:"))
cantidad_digitos = len(str(abs(numero)))
print(f"El numero ingresado es: {numero}")
print(f"Cantidad de digitos: {cantidad_digitos}")
#Actividad 3: sumar numeros entre dos valores dados por el usuario
valor1 = int(input("Ingrese el primer valor:"))
valor2 = int(input("Ingrese el segundo valor:"))
suma = sum(range(min(valor1, valor2) + 1, max(valor1, valor2)))
print(f"La suma de los numeros entre {valor1} y {valor2} es: {suma}")
#Actividad 4: sumar numeros ingresados por el usuario hasta que ingrese 0
total = 0
while True:
    n = int(input("Ingrese un numero entero (0 para terminar):"))
    if n == 0:
        break
    total += n
    print(f"Total acumulado: {total}")
    print(f"Total acumulado: {total}")
#Actividad 5: juego de adivinar un numero entre 0 y 9 
import random
numero_aleatorio = random.randint(0, 9)
intentos = 0
while True:
    intento = int(input("Adivina el numero entre 0 y 9:"))
    intentos += 1
    if intento == numero_aleatorio:
        print(f"¡Correcto! El numero era {numero_aleatorio}. Intentos: {intentos}")
        break
    else:
        print("Incorrecto, intenta de nuevo.")
#Actividad 6: imprimir numeros pares entre 0 y 100 en orden decreciente
for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)
#Actividad 7: sumar numeros entre 0 y un numero entero positivo indicado por el usuario
limite = int(input("Ingrese un numero entero positivo:"))
suma = sum(range(limite + 1))
print(f"La suma de los numeros entre 0 y {limite} es: {suma}")
#Actividad 8: contar pares, impares, negativos y positivos entre 100 numeros ingresados por el usuario
pares = impares = negativos = positivos = 0
for i in range(100):
    n = int(input(f"Ingrese el numero {i + 1}:"))
    if n < 0:
        negativos += 1
    elif n > 0:
        positivos += 1
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1
        print(f"Pares: {pares}, Impares: {impares}, Negativos: {negativos}, Positivos: {positivos}")
#Actividad 9: calcular la media de 100 numeros ingresados por el usuario
suma = 0
for i in range(100):
    n = int(input(f"Ingrese el numero {i + 1}:"))
    suma += n
    media = suma / (i + 1)
    print(f"Media actual: {media}")
#Actividad 10: invertir el orden de los digitos de un numero ingresado por el usuario
numero = input("Ingrese un numero entero:")
numero_invertido = numero[::-1]
print(f"Numero invertido: {numero_invertido}") 
