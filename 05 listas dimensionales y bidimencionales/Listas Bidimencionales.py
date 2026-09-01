# Listas Bidimencionales

# Actividad 1: Crea una función que reciba dos parámetros: el número de filas y columnas. La función debe generar una matriz de ese tamaño, donde los valores son números enteros consecutivos empezando desde 1. 
# Crea una función que reciba dos parámetros: el número de filas y columnas. 
# La función debe generar una matriz de ese tamaño, donde los valores son números enteros consecutivos empezando desde 1
filas = int(input("Ingrese la cantidad de filas que desea agregar: "))
columnas = int(input("Ingrese la cantidad de columnas que desea agregar: "))
matriz_fila = []
contador = 1
for fila in range(filas):
    matriz_columna = []
    for columna in range(columnas):
        matriz_columna.append(contador)
        contador += 1
    matriz_fila.append(matriz_columna)
print(matriz_fila)

# Actividad 2: Escribe un programa que calcule la suma de todos los elementos en una lista bidimensional. 
# Escribe un programa que calcule la suma de todos los elementos en una lista bidimensional.
filas = int(input("Ingrese la cantidad de filas que desea agregar: "))
columnas = int(input("Ingrese la cantidad de columnas que desea agregar: "))
matriz_fila = []
contador = 1
for fila in range(filas):
    matriz_columna = []
    for columna in range(columnas):
        matriz_columna.append(contador)
        contador += 1
    matriz_fila.append(matriz_columna)
print(matriz_fila)
suma_total = sum(sum(fila) for fila in matriz_fila)
print(suma_total)

# Actividad 3: Modifica el programa anterior para que imprima la suma de cada fila de la lista bidimensional. 
# Modifica el programa anterior para que imprima la suma de cada fila de la lista bidimensional.
filas = int(input("Ingrese la cantidad de filas que desea agregar: "))
columnas = int(input("Ingrese la cantidad de columnas que desea agregar: "))
matriz = []
contador = 1
for fila in range(filas):
    matriz_fila = []
    for columna in range(columnas):
        matriz_fila.append(contador)
        contador += 1
    matriz.append(matriz_fila)
    suma = sum(matriz_fila)

    print(f"La suma de la fila {fila + 1} es {suma}")
print(matriz)

# Actividad 4: Escribe un programa que calcule la transpuesta de una matriz. La transpuesta de una matriz intercambia sus filas por columnas.
#--Definimos la matriz original (2 filas x 3 columnas)
matriz = [
    [1, 2, 3],
    [4, 5, 6]
]
#-- Obtenemos las dimensiones de la matriz original
filas = len(matriz)           # Numero de filas (2)
columnas = len(matriz[0])     # Numero de columnas (3)
# -- Creamos la matriz transpuesta vacia con dimensiones invertidas.
# La original era 2 x 3, la transpuesta sera de 3 filas x 2 columnas.
# La llenamos temporalmente con ceros.
transpuesta = []
for j in range(columnas):
    fila_nueva = []
    for i in range(filas):
        fila_nueva.append(0)
    transpuesta.append(fila_nueva)
#-- Recorremos la matriz original para copiar los valores invertidos
for i in range(filas):
    for j in range(columnas):
        # El elemento en la posicion [i][j] de la matriz original
        # pasa a la posición [j][i] en la matriz transpuesta.
        transpuesta[j][i] = matriz[i][j]
#--Mostramos el resultado en pantalla
print("Matriz original:")
for fila in matriz:
    print(fila)
print("Matriz transpuesta:")
for fila in transpuesta:
    print(fila)

# Actividad 5: Escribe un programa que encuentre el valor más grande en una lista bidimensional. 
#----Definimos la matriz con valores de prueba
matriz = [
    [11, 43, 74],
    [52, 85, 22],
    [64, 81, 12]
]
#-------Inicializamos el mayor con el primer elemento de la matriz (posicion [0][0])
mayor = matriz[0][0]
# -----Recorremos todas las filas y columnas mediante ciclos anidados
for fila in matriz:
    for elemento in fila:
        # Si el elemento actual es mas grande que el que teniamos guardado, actualizamos 'mayor'
        if elemento > mayor:
            mayor = elemento
# ------Mostramos la matriz y el resultado final
print("Matriz:")
for fila in matriz:
    print(fila)
print(f"El valor más grande en la lista bidimensional es: {mayor}")

# Actividad 6: Escribe un programa que multiplique cada elemento de una lista bidimensional por un valor escalar dado por el usuario. 
# -----------Definimos la matriz original
matriz = [
    [2, 4, 6],
    [1, 3, 5],
    [7, 8, 9]
]
#----------Pedimos al usuario el valor escalar y lo convertimos a entero o flotante
escalar = int(input("Ingrese el número escalar por el que desea multiplicar: "))
# -------------Obtenemos las dimensiones
filas = len(matriz)
columnas = len(matriz[0])
# ------------Creamos una nueva matriz vacía con el mismo tamaño para guardar el resultado
matriz_resultante = []
# -------------Recorremos la matriz original para realizar la multiplicacion
for i in range(filas):
    nueva_fila = []
    for j in range(columnas):
        # Multiplicamos el elemento actual por el escalar
        nuevo_valor = matriz[i][j] * escalar
        nueva_fila.append(nuevo_valor)
    # Agregamos la fila terminada a la matriz resultante
    matriz_resultante.append(nueva_fila)
# 6. Mostramos los resultados
print("Matriz Original:")
for fila in matriz:
    print(fila)
print(f"Matriz multiplicada por {escalar}:")
for fila in matriz_resultante:
    print(fila)


# Actividad 7: Escribe un programa que extraiga los elementos de la diagonal principal de una matriz cuadrada. 
# Creamos una matriz
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Recorremos las filas de la matriz
for i in range(len(matriz)):
    # Mostramos los elementos de la diagonal principal
    print(matriz[i][i])

# Actividad 8: Crea un programa que genere una matriz identidad de tamaño n. Una matriz identidad es una matriz cuadrada donde los elementos de la diagonal principal son 1 y el resto son 0.
# Pedimos al usuario el tamaño de la matriz
n = int(input("Ingrese el tamaño de la matriz: "))
# Creamos una lista vacía para guardar la matriz
matriz = []
# Recorremos las filas
for i in range(n):
    # Creamos una fila vacía
    fila = []
    # Recorremos las columnas
    for j in range(n):
        # Si la posición pertenece a la diagonal principal
        if i == j:
            fila.append(1)
        else:
            fila.append(0)
            # Agregamos la fila a la matriz
    matriz.append(fila)
# Mostramos la matriz
for fila in matriz:
    print(fila)

#Actividad 9: Crea un programa que genere una matriz identidad inversa de tamaño n. Una matriz identidad inversa es una matriz cuadrada donde los elementos de la diagonal inversa principal son 1 y el resto son 0. 
# Pedimos al usuario el tamaño de la matriz
n = int(input("Ingrese el tamaño de la matriz: "))
# Creamos una lista vacía para guardar la matriz
matriz = []
# Recorremos las filas
for i in range(n):
    # Creamos una fila vacía
    fila = []
    # Recorremos las columnas
    for j in range(n):
        # Si la posición pertenece a la diagonal inversa
        if i + j == n - 1:
            fila.append(1)
        else:
            fila.append(0)
    # Agregamos la fila a la matriz
    matriz.append(fila)
# Mostramos la matriz
for fila in matriz:
    print(fila)

# Actividad 10: Una matriz es simétrica si es igual a su transpuesta. Escribe un programa que verifique si una matriz es simétrica. 
import numpy as np
print("ejercicio 10")
matriz10=np.array([
    [1,2,3],
    [2,4,5],
    [3,5,6]
])
if np.array_equal(matriz10,matriz10.T):
    print("La matriz es simetrica")
else:
    print("La matriz es asimetrica")

# Actividad 11: Escribe un programa que gire una lista bidimensional (matriz) 90 grados en el sentido de las agujas del reloj. 
matriz11=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
rotado=[]
for i in range(len(matriz11)):
    row=[]
    for j in range(len(matriz11)-1,-1,-1):
        row.append(matriz11[j][i])
    rotado.append(row)
print(rotado)

# Actividad 12: En una asignatura universitaria se ha registrado una cadena de texto con las notas finales obtenidas por las estudiantes en un examen, separadas por comas (por ejemplo: "45, 88, -5, 92, 30, 110, 75, 60, 15"). Debido a un error en el sistema de carga, se incluyeron algunas notas inválidas (menores a 0 o mayores a 100). 
notasString="45, 88, -5, 92, 30, 110, 75, 60, 15"
notas=notasString.split(",")
aprobado=[]
reprobado=[]
notasValidas=[]
for notas in notas:
    notas=int(notas)
    if notas<0 or notas>100:
        continue
    notasValidas.append(notas)
    if notas>=60:
        aprobado.append(notas)
    else:
        reprobado.append(notas)
promedio=sum(notasValidas)/len(notasValidas)
print(f"Aprobados: {aprobado}")
print(f"Reprobados: {reprobado}")
print(f"Promedio: {promedio}")
print(f"Ultimos 2 aprobados: {aprobado[-2:]}")

# Actividad 13: Escribe un programa interactivo en Python que mantenga una lista de tareas (tareas = []) e incluya un menú ejecutado dentro de un bucle while con las siguientes opciones:  Agregar tarea: Pide el nombre de una tarea. Si la tarea ya existe en la lista (verificando con el operador in), muestra un mensaje indicando que ya está registrada. Si no existe, agrégala con .append(). 
# Eliminar tarea: Pide el nombre de la tarea. Si existe en la lista (usando in), elimínala con .remove(). Si no existe, muestra un mensaje de advertencia.
# Ver resumen: Muestra el total de tareas registradas y las primeras 3 tareas de la lista usando slicing ([:3]).  
#Salir: Utiliza la palabra clave break para terminar la ejecución del bucle while
tareas13=[]
while True:
    print("1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Ver resumen")
    print("4. Salir")
    opcion=input("Ingrese una opcion: ")
    if opcion=="1":
        tarea=input("Ingrese el nombre de la tarea: ")
        if tarea in tareas13:
            print("La tarea ya esta registrada")
        else:
            tareas13.append(tarea)
            print("Tarea agregada")
    elif opcion=="2":
        tarea=input("Ingrese el nombre de la tarea a eliminar: ")
        if tarea in tareas13:
            tareas13.remove(tarea)
            print("Tarea eliminada")
        else:
            print("La tarea no existe")
    elif opcion=="3":
        print(f"Total de tareas: {len(tareas13)}")
        print(f"Primeras 3 tareas: {tareas13[:3]}")
    elif opcion=="4":
        print("Programa finalizado")
        break
    else:
        print("Opcion invalida")