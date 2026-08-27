"""
Práctico 3: Estructuras condicionales

Objetivo:
Comprender y aplicar las estructuras condicionales en la programación,
desarrollando algoritmos que involucren tomas de decisiones.

Actividades (resumen):
1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
	debe mostrar un mensaje en pantalla que diga "Es mayor de edad".

2) Escribir un programa que solicite una nota al usuario. Si la nota es mayor o igual a 6,
	mostrar "Aprobado"; en caso contrario, mostrar "Desaprobado".

3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
	número par, imprimir por pantalla el mensaje "Ha ingresado un número par"; en caso
	contrario, imprimir "Por favor, ingrese un número par".

4) Escribir un programa que solicite la edad y muestre a cuál de las siguientes
	categorías pertenece: Niño/a (<12), Adolescente (>=12 y <18), Adulto/a joven (>=18 y <30),
	Adulto/a (>=30).

5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
	(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada,
	imprimir por pantalla "Ha ingresado una contraseña correcta"; en caso contrario,
	imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres".

6) Trabajar con una lista de números y calcular estadísticos (moda, media, mediana).
	Se propone usar el módulo `statistics` de Python para esas operaciones.

7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
	termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante;
	en caso contrario, dejar el string tal cual.

8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
	dependiendo de la acción que quiera realizar (por ejemplo: 1 = mayúsculas, 2 = minúsculas,
	3 = capitalizar). Aplicar la transformación elegida e imprimir el resultado.

9) Escribir un programa que pida al usuario la magnitud de un terremoto y lo clasifique
	según la escala de Richter en categorías como: "Muy leve", "Leve", "Moderado",
	"Fuerte", "Muy fuerte", "Extremo".

10) Usando información de períodos del año, preguntar en qué hemisferio está el usuario
	 (N/S) y en qué fecha está para determinar la estación (invierno, primavera, verano, otoño)
	 y mostrarla por pantalla.

Este script solo imprime el enunciado resumido para facilitar su lectura.
"""
#1.Solicitar la edad al usuario y determinar si es mayor de edad
edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")
    #2.Solicitar una nota al usuario y determinar si esta aprobado o desaprobado
    nota = float(input("Ingrese su nota:"))
    if nota >= 6:
        print("Aprobado")
    else:
        print("Desaprobado")
        #3.Solicitar un numero par al usuario
        numero = int(input("Ingrese un numero par:"))
        if numero % 2 == 0:
            print("Ha ingresado un numero par")
        else:
            print("Por favor, ingrese un numero par")
            #4.Solicitar la edad al usuario y determinar su categoria
            edad = int(input("Ingrese su edad:"))
            if edad < 12:
                print("Niño/a")
            elif edad >= 12 and edad < 18:
                print("Adolecente")
            elif edad >= 18 and edad < 30:
                print("Adulto/a joven")
            else:
                print("Adulto/a")
            #5.Solicitar una contraseña al usuario y determinar si es de longitud adecuada
contraseña = input("Ingrese una contraseña de entre 8 y 14 caracteres:")
if len(contraseña) >= 8 and len(contraseña) <= 14:
                     print("Ha ingresado una contraseña correcta")
else:
                    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
#6.Calcular estadisticos de una lista de numeros
import statistics
import random
numeros = [random.randint(1, 100) for _ in range(50)]
moda = statistics.mode(numeros)
media = statistics.mean(numeros)
mediana = statistics.median(numeros)
print(f"Lista: {numeros}")
print(f"Moda: {moda} | Media: {media} | Mediana: {mediana}")
if media > mediana:
       print("Resultado: sesgo positivo (a la derecha)")
elif media < mediana:
       print("Resultado: sesgo negativo (a la izquierda)")
else:
       print("Resultado: Sin sesgo")
#7.Solicitar una frase al usuario y determinar si termina con vocal
frase = input("Ingrese una frase o palabra:")
if len(frase) > 0:
       if frase[-1].lower() in "aeiou":
              frase += "!"
              print(frase)
else:
       print(frase)
#8.Solicitar el nombre al usuario y una opcion de transformacion
nombre = input("Ingrese su nombre:")
opcion = int(input("Ingrese el numero 1, 2 o 3 para elegir la transformacion (1=mayusculas, 2=minusculas, 3=capitalizar):"))
if opcion == 1:
       print(nombre.upper())
elif opcion == 2:
       print(nombre.lower())
elif opcion == 3:
       print(nombre.capitalize())
else:
       print("Opcion no valida")
#9.Solicitar la magnitud de un terremoto y clasificarlo
magnitud = float(input("Ingrese la magnitud del terremoto:"))
if magnitud < 2.0:
       print("Muy leve")
elif magnitud < 4.0:
       print("Leve")
elif magnitud < 6.0:
       print("Moderado")
elif magnitud < 7.0:
       print("Fuerte")
elif magnitud < 8.0:
       print("Muy fuerte")
else:
       print("Extremo")
#10.Solicitar el hemisferio y la fecha al usuario para determinar la estacion del año
hemisferio = input("Ingrese su hemisferio (N/S):").upper()
fecha = input("Ingrese la fecha (dd/mm):")
dia, mes = map(int, fecha.split("/"))
if hemisferio == "N":
       if (mes == 12 and dia >= 21) or (mes <= 3 and dia < 20):
              print("Invierno")
       elif (mes == 3 and dia >= 20) or (mes <= 6 and dia < 21):
              print("Primavera")
       elif (mes == 6 and dia >= 21) or (mes <= 9 and dia < 22):
              print("Verano")
       elif (mes == 9 and dia >= 22) or (mes <= 12 and dia < 21):
              print("Otoño")
       elif hemisferio == "S":
              if (mes == 12 and dia >= 21) or (mes <= 3 and dia < 20):
                     print("Verano")
              elif (mes == 3 and dia >= 20) or (mes <= 6 and dia < 21):
                     print("Otoño")
              elif (mes == 6 and dia >= 21) or (mes <= 9 and dia < 22):
                     print("Invierno")
              elif (mes == 9 and dia >= 22) or (mes <= 12 and dia < 21):
                     print("Primavera")
              else:
                     print("Fecha no valida")
else:
       print("Hemisferio no valido")
              

                    
                     

