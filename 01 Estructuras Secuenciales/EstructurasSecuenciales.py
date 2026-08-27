# Actividad 1: Estructuras secuenciales
print("Hola Mundo!")
# Actividad 2: Pedir al usuario su nombre e imprima un saludo por pantalla un saludo usando el nombre ingresado
nombre = input("Ingrese su nombre:")
print(f"Hola {nombre}!")
# Actividad 3: Pedir al usuario su nombre, apellido, edad y lugar donde recide e imprima por pantalla una oracion con los datos ingresados
nombre = input("Ingrese su nombre:")
apellido = input("Ingrese su apellido:")
edad = input("Ingrese su edad:")
LugarDeResidencia = input("Ingrese su lugar de residencia:")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {LugarDeResidencia}.")
# Actividad 4: Crear un programa que pida al uduario el radio de un circulo e imprima por pantalla su area y su perimetro
import math
radio = float(input("Ingrese el radio del circulo:"))
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio
print(f"El area del circulo es: {area}")
print(f"El perimetro del circulo es: {perimetro}")
# Actividad 5: Crea un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuantas horas equivale
segundos = int(input("Ingrese una cantidad de segundos:"))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas} horas.")
# Actividad 6: Crea un programa que pida al usuario un numero e imprima por pantalla la tabla de multiplicar de dicho numero
numero = int(input("Ingrese un numero:"))
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
# Actividad 7: Crear un programa que pida al usuario dos numeros enteros distintos del 0 y muestre por pantalla el resultado al sumarlos, dividirlos, multiplicarlos y restarlos
num1 = int(input("Ingrese el primer numero entero distinto de 0:"))
num2 = int(input("Ingrese el segundo numero entero distinto de o:"))
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
print(f"La suma de {num1} y {num2} es: {suma}")
print(f"La resta de {num1} y {num2} es: {resta}")
print(f"La multiplicacion de {num1} y {num2} es: {multiplicacion}")
print(f"La division de {num1} y {num2} es: {division}")
# Actividad 8: Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su indice de masa corporal (IMC)
altura = float(input("Ingrese su altura en metros:"))
peso = float(input("Ingrese su peso en kilogramos:"))
imc = peso / (altura ** 2)
print(f"Su indice de masa corporal (IMC) es: {imc}")
# Actividad 9: Crear un programa que pida al usuario un temperatura en grados celsius e imprima por pantalla su equivalente en grados fahrenheit
celsius = float(input("Ingrese una temperatura en grados Celsius:"))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} grados Celsius equivalen a {fahrenheit} grados Fahrenheit.")
# Actividad 10: Crear un programa que pida al usuario 3 numeros e imprima por pantalla el promedio de dichos numeros
num1 = float(input("Ingrese el primer numero:"))
num2 = float(input("Ingrese el segundo numero:"))
num3 = float(input("Ingrese eltercer numero:"))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio de los numeros ingresados es: {promedio}")
