# Actividad 1: Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.
# Definir la funcion
def imprimir_hola_mundo():
    print("Hola Mundo!")
    # Ejecutar la funcion
imprimir_hola_mundo()

# Actividad 2: Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado.
# Definir la funcion
def saludar_usuario(nombre):
    return f"Hola, {nombre}!"
# Le pedimos el nombre al usuario
nombre_usuario = input("Ingrese su nombre: ")
# Llamamos a la funcion pasando el nombre enviado por el usuario
saludo = saludar_usuario(nombre_usuario)
# Mostramos el saludo
print(saludo)

# Actividad 3: Crear una función llamada informacion_personal(nombre, apellido edad, residencia) que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.
# Definimos la funcion
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")
# Pedimos los datos al usuario
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su residencia: ")
#Llamamos a la funcion pasando los 4 valores 
informacion_personal(nombre, apellido, edad, residencia)

# Actividad 4: Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.
import math
# Definimos la funcion para el area
def calcular_area_circulo(radio):
    return math.pi * radio ** 2
# Definimos la funcion del perimetro
def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio
# Solicitamos el radio al usuario
radio = float(input("Ingrese el radio del circulo: "))
# Llamamos a ambas funciones
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)
# Mostramos los resultados
print(f"El area del circulo es: {area:.2f}")
print(f"El perimetro del circulo es: {perimetro:.2f}")

# Actividad 5: Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.
# Definimos la funcion
def segundos_a_horas(segundos):
    return segundos / 3600
# Solicitamos los segundos al usuario
segundos_ingresados = int(input("Ingrese la cantidad de segundos:"))
# Llamamos a la funcion
horas = segundos_a_horas(segundos_ingresados)
# Mostramos el resultado
print(f"{segundos_ingresados} segundos son equivalentes a {horas:.2f} horas.")

# Actividad 6: Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la funcion.
# Definimos la funcion
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
# Solicitamos el numero al usuario 
numero_usuario = int(input("Ingrese un numero para mostrar su tabla de multiplicar: "))
# Llamamos a la funcion
tabla_multiplicar(numero_usuario)

# Actividad 7: Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultado de forma clara.
# Definicion de la funcion 
def operaciones_basicas(a, b):
    suma = a + b 
    resta = a - b 
    multiplicacion = a * b 
    division = a / b 
    return (suma, resta, multiplicacion, division)
# Pedimos los numeros al usuario
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
# Llamamos a la funcion 
s, r, m, d = operaciones_basicas(num1, num2)
# Mostramos los resultados
print("\n--- Resultados de las operaciones ---")
print(f"Suma: {s}")
print(f"Resta: {r}")
print(f"Multiplicacion: {m}")
print(f"Division: {d}")

# Actividad 8: Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.
# Definimos la funcion para calcular el IMC
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc
# Solicitamos los datos al usuario
peso_ingresado = float(input("Ingrese su peso en kilogramos: "))
altura_ingresada = float(input("Ingrese su altura en metros: "))
# Llamamos a la funcion
imc_resultado = calcular_imc(peso_ingresado, altura_ingresada)
# Mostramos el resultado
print(f"Su indice de masa corporal (IMC) es: {imc_resultado:.2f}")

# Actividad 9: Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.
# Definimos la funcion para convertir Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
# Solicitamos la temperatura al usuario
temperatura_celsius = float(input("Ingrese la temperatura en grados Celsius: "))
# Llamamos a la funcion
temperatura_fahrenheit = celsius_a_fahrenheit(temperatura_celsius)
# Mostramos el resultado
print(f"{temperatura_celsius} grados Celsius son equivalentes a {temperatura_fahrenheit:.2f} grados Fahrenheit.")

# Actividad 10: Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos.Solicitar los números al usuario y mostrar el resultado usando esta función.
# Definicion de la funcion
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio
# Pedimos los numeros al usuario
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
num3 = float(input("Ingrese el tercer numero: "))
#Llamamos a la funcion
promedio = calcular_promedio(num1, num2, num3)
# Mostramos el resultado
print(f"El promedio de los numeros ingresados es: {promedio:.2f}")
