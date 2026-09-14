# --- ESTRUCTURAS DE DATOS INICIALES ---

# 1. Lista bidimensional de golosinas [Código, Denominación, Stock]
golosinas = [
    [1, "KitKat", 20],
    [2, "Chicles", 50],
    [3, "Caramelos de Menta", 50],
    [4, "Huevo Kinder", 10],
    [5, "Chetoos", 10],
    [6, "Twix", 10],
    [7, "M&M'S", 10],
    [8, "Papas Lays", 2],
    [9, "Milkybar", 10],
    [10, "Alfajor Tofi", 15],
    [11, "Lata Coca", 20],
    [12, "Chitos", 10]
]

# 2. Diccionario de empleados {Legajo: Nombre}
empleados = {
    1100: "José Alonso",
    1200: "Federico Pacheco",
    1300: "Nelson Pereira",
    1400: "Osvaldo Tejada",
    1500: "Gastón Garcia"
}

# 3. Tupla inmutable de claves para el técnico
clavesTecnico = ("admin", "CCCDDD", "2020")

# 4. Historial de golosinas pedidas [Código, Denominación, Cantidad Pedida]
golosinasPedidas = []


# --- FUNCIONES DE LA MÁQUINA DE GOLOSINAS ---

def pedir_golosina():
    """Valida legajo, consulta stock, descuenta y registra en golosinasPedidas."""
    legajo = int(input("\nIngrese su número de legajo: "))
    
    if legajo not in empleados:
        print("Usted no es un empleado de la empresa")
        return

    print(f"\n¡Bienvenido/a {empleados[legajo]}!")
    
    mientras_pidiendo = True
    while mientras_pidiendo:
        codigo_str = input("Ingrese el código de la golosina que desea (o 'salir' si no desea nada): ")
        if codigo_str.lower() == 'salir':
            print("Operación cancelada. Volviendo al menú principal...")
            break
        
        if not codigo_str.isdigit():
            print("Código inválido. Intente nuevamente.")
            continue
            
        codigo = int(codigo_str)
        
        # Buscar golosina en la lista bidimensional
        golosina_encontrada = None
        for g in golosinas:
            if g[0] == codigo:
                golosina_encontrada = g
                break
        
        if golosina_encontrada is None:
            print("Código de golosina no existente. Intente con otro.")
            continue
            
        denominacion = golosina_encontrada[1]
        stock_actual = golosina_encontrada[2]
        
        if stock_actual <= 0:
          print(f"Lo sentimos la golosina {denominacion} no se encuentra disponible, seleccione otra golosina o ingresa salir si no desea otra golosina")
        else:
            # Descontar stock de la máquina
            golosina_encontrada[2] -= 1
            print(f"¡Disfrute su {denominacion}!")
            
            # Registrar / actualizar en golosinasPedidas
            registrada = False
            for item in golosinasPedidas:
                if item[0] == codigo:
                    item[2] += 1
                    registrada = True
                    break
            
            if not registrada:
                golosinasPedidas.append([codigo, denominacion, 1])
                
            mientras_pidiendo = False


def mostrar_golosinas():
    """Muestra todas las golosinas con su stock actual."""
    print("\n--- LISTA DE GOLOSINAS Y STOCK DISPONIBLE ---")
    print(f"{'Código':<8} | {'Golosina':<22} | {'Stock':<5}")
    print("-" * 40)
    for g in golosinas:
        print(f"{g[0]:<8} | {g[1]:<22} | {g[2]:<5}")


def rellenar_golosinas():
    """Valida la clave en 3 pasos y incrementa el stock de una golosina."""
    print("\n--- AUTENTICACIÓN TÉCNICO ---")
    pass1 = input("Paso 1 - Ingrese primera clave: ")
    pass2 = input("Paso 2 - Ingrese segunda clave: ")
    pass3 = input("Paso 3 - Ingrese tercera clave: ")
    
    if (pass1, pass2, pass3) != clavesTecnico:
        print("No tiene permiso para ejecutar la función de recarga")
        return

    print("\n¡Acceso concedido al menú de recarga!")
    codigo = int(input("Ingrese el código de la golosina a recargar: "))
    
    golosina_encontrada = None
    for g in golosinas:
        if g[0] == codigo:
            golosina_encontrada = g
            break
            
    if golosina_encontrada is None:
        print("Código de golosina no encontrado.")
        return

    cantidad = int(input("Ingrese la cantidad a recargar (debe ser mayor a 0): "))
    if cantidad <= 0:
        print("La cantidad a recargar debe ser mayor a cero.")
    else:
        golosina_encontrada[2] += cantidad
        print(f"Recarga exitosa. El nuevo stock de {golosina_encontrada[1]} es {golosina_encontrada[2]}.")


def apagar_maquina():
    """Muestra el historial de pedidos, calcula el total acumulado y finaliza."""
    print("\n--- APAGANDO MÁQUINA ---")
    print("HISTORIAL DE GOLOSINAS PEDIDAS:")
    print(f"{'Código':<8} | {'Denominación':<22} | {'Total Pedido':<12}")
    print("-" * 50)
    
    total_acumulado = 0
    for item in golosinasPedidas:
        print(f"{item[0]:<8} | {item[1]:<22} | {item[2]:<12}")
        total_acumulado += item[2]
        
    print("-" * 50)
    print(f"TOTAL GENERAL DE GOLOSINAS PEDIDAS: {total_acumulado}")
    print("¡Hasta luego!")


# --- MENÚ PRINCIPAL ---
def menu_maquina():
    opcion = ""
    while opcion != 'd':
        print("\n==========================================")
        print("     MÁQUINA EXPENDEDORA DE GOLOSINAS     ")
        print("==========================================")
        print("a. Pedir golosina")
        print("b. Mostrar golosinas")
        print("c. Rellenar golosinas")
        print("d. Apagar maquina")
        opcion = input("Seleccione una opción: ").strip().lower()
        
        if opcion == 'a':
            pedir_golosina()
        elif opcion == 'b':
            mostrar_golosinas()
        elif opcion == 'c':
            rellenar_golosinas()
        elif opcion == 'd':
            apagar_maquina()
        else:
            print("Opción inválida. Intente de nuevo.")

# Ejecutar programa de máquina de golosinas
# menu_maquina()


# --- ESTRUCTURAS INICIALES ---

# 1. Diccionario de alumnos {Legajo: Apellido y Nombre}
alumnos = {
    60902: "Rodolfo Fernandez",
    61654: "Luis Gomez",
    61852: "Andrea Pereira",
    61754: "Juan Cruz Gonzales"
}

# Lista de materias disponibles
nombres_materias = ["Ciencias", "Historia", "Geografia", "Matematicas", "Fisica"]

# Lista 2D final para promedios de cada alumno [Nombre Alumno, Promedio General]
notasFinales = []


def cargar_y_procesar_notas():
    # Iterar el diccionario de alumnos
    for legajo, nombre_completo in alumnos.items():
        print(f"\n==========================================")
        print(f"Alumno: {nombre_completo} (Legajo: {legajo})")
        print(f"==========================================")
        
        # Crear lista 2D de materias específica para el alumno actual
        # Columnas: [Materia, Nota 1, Nota 2, Nota Final]
        materias_alumno = []
        suma_promedios_materias = 0
        
        materia_mejor_nota = ""
        mejor_nota_materia = -1.0
        
        for m in nombres_materias:
            print(f"\nIngrese las notas para la materia {m}:")
            
            # Validación Nota 1
            while True:
                nota1 = float(input("  Nota 1: "))
                if 0 <= nota1 <= 10:
                    break
                print("  Error: La nota debe estar en el rango de 0 a 10.")
                
            # Validación Nota 2
            while True:
                nota2 = float(input("  Nota 2: "))
                if 0 <= nota2 <= 10:
                    break
                print("  Error: La nota debe estar en el rango de 0 a 10.")
                
            nota_final_materia = (nota1 + nota2) / 2
            print(f"  Nota Final {m}: {nota_final_materia:.2f}")
            
            # Guardar en la matriz de materias del alumno
            materias_alumno.append([m, nota1, nota2, nota_final_materia])
            suma_promedios_materias += nota_final_materia
            
            # Verificar cuál es la materia con la calificación más alta
            if nota_final_materia > mejor_nota_materia:
                mejor_nota_materia = nota_final_materia
                materia_mejor_nota = m

        # Mostrar lista de materias completa cargada para el alumno
        print(f"\n--- Resumen de materias cargadas para {nombre_completo} ---")
        print(f"{'Materia':<15} | {'Nota 1':<8} | {'Nota 2':<8} | {'Nota Final':<10}")
        print("-" * 50)
        for fila in materias_alumno:
            print(f"{fila[0]:<15} | {fila[1]:<8.2f} | {fila[2]:<8.2f} | {fila[3]:<10.2f}")
            
        print(f"\n>> Materia con la calificación más alta: {materia_mejor_nota} ({mejor_nota_materia:.2f})")
        
        # Calcular el promedio general del alumno
        promedio_general = suma_promedios_materias / len(nombres_materias)
        notasFinales.append([nombre_completo, promedio_general])

    # Terminado el proceso para todos los alumnos, determinar el mejor promedio general
    print("\n==========================================")
    print("      RESUMEN FINAL DE PROMEDIOS          ")
    print("==========================================")
    
    mejor_alumno = ""
    mejor_promedio_general = -1.0
    
    for registro in notasFinales:
        print(f"Alumno: {registro[0]:<22} | Promedio General: {registro[1]:.2f}")
        if registro[1] > mejor_promedio_general:
            mejor_promedio_general = registro[1]
            mejor_alumno = registro[0]
            
    print("-" * 50)
    print(f"🏆 El alumno con el MEJOR PROMEDIO GENERAL es: {mejor_alumno} con {mejor_promedio_general:.2f}")


# Ejecutar la gestión de notas
# cargar_y_procesar_notas()
