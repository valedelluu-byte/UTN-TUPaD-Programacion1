# TRABAJO PRÁCTICO: LECTURA Y ESCRITURA DE ARCHIVOS
# Gestión de Alumnos y Notas

# 1. FUNCIÓN PARA LEER EL ARCHIVO Y CREAR DICCIONARIO E STRUCTURA DE MEMORIA
def leer_alumnos(nombre_archivo="alumnos.txt"):
    """ Lee 'alumnos.txt'. Si no existe, lo crea vacío. Retorna la lista de alumnos y el diccionario con el legajo como clave. """
    lista_alumnos = []
    dicc_legajos = {}
    try:
        with open(nombre_archivo, "r") as archivo:
            for linea in archivo:
                linea_limpia = linea.strip()
                if linea_limpia != "":
                    partes = linea_limpia.split(";")
                    if len(partes) == 4:
                        nombre = partes[0].strip()
                        apellido = partes[1].strip()
                        legajo = partes[2].strip()
                        nota = float(partes[3].strip())
                        alumno = { "nombre": nombre, "apellido": apellido, "legajo": legajo, "nota": nota }
                        lista_alumnos.append(alumno)
                        dicc_legajos[legajo] = alumno
    except FileNotFoundError:
        # Si el archivo no existe, se crea vacío
        with open(nombre_archivo, "w") as archivo:
            pass
    return lista_alumnos, dicc_legajos

# 2. FUNCIÓN PARA VALIDAR EXISTENCIA DEL LEGAJO
def validar_existe_alumno(legajo, dicc_legajos):
    """ Valida si el legajo ingresado ya existe en el diccionario. """
    return legajo in dicc_legajos

# 3. FUNCIÓN PARA AGREGAR UN NUEVO ALUMNO
def agregar_alumno(lista_alumnos, dicc_legajos, nombre_archivo="alumnos.txt"):
    print("\n--- AGREGAR NUEVO ALUMNO ---")
    nombre = input("Ingrese Nombre: ").strip()
    apellido = input("Ingrese Apellido: ").strip()
    # Validar Legajo (que sea numérico y de 5 dígitos)
    legajo = input("Ingrese Legajo (5 dígitos): ").strip()
    while not (legajo.isdigit() and len(legajo) == 5):
        print("Error: El legajo debe tener exactamente 5 dígitos numéricos.")
        legajo = input("Ingrese Legajo (5 dígitos): ").strip()
    # Validar si el legajo ya existe en el diccionario
    if validar_existe_alumno(legajo, dicc_legajos):
        print(f"El legajo {legajo} ya existe en el archivo alumnos.txt, no se permite su escritura")
        return
    # Validar Nota Promedio (número entre 1 y 10)
    nota_valida = False
    nota = 0.0
    while not nota_valida:
        try:
            nota_input = float(input("Ingrese Nota Promedio (1 a 10): "))
            if 1 <= nota_input <= 10:
                nota = nota_input
                nota_valida = True
            else:
                print("Error: La nota debe estar comprendida entre 1 y 10.")
        except ValueError:
            print("Error: Debe ingresar un valor numérico válido para la nota.")
    # Guardar en las estructuras en memoria RAM
    nuevo_alumno = { "nombre": nombre, "apellido": apellido, "legajo": legajo, "nota": nota }
    lista_alumnos.append(nuevo_alumno)
    dicc_legajos[legajo] = nuevo_alumno
    # Escribir al final del archivo con modo "a" (append)
    try:
        with open(nombre_archivo, "a") as archivo:
            # Si la nota es un entero (ej: 8.0), la guarda limpia como "8"
            nota_str = str(int(nota)) if nota.is_integer() else str(nota)
            linea = f"{nombre}; {apellido}; {legajo}; {nota_str}\n"
            archivo.write(linea)
        print("¡Alumno agregado y guardado con éxito en alumnos.txt!")
    except Exception as e:
        print(f"Error al escribir en el archivo: {e}")


# 4. FUNCIÓN PARA GENERAR Y MOSTRAR ARCHIVO DE APROBADOS
def guardar_aprobados(lista_alumnos, nombre_salida="aprobados.txt"):
    """ Filtra los alumnos con nota >= 6, genera 'aprobados.txt' y muestra el archivo. """
    print("\n--- GENERANDO ARCHIVO DE APROBADOS ---")
    try:
        # Generar o sobrescribir aprobados.txt
        with open(nombre_salida, "w") as archivo:
            for alu in lista_alumnos:
                if alu["nota"] >= 6:
                    nota_str = str(int(alu["nota"])) if alu["nota"].is_integer() else str(alu["nota"])
                    linea = f"{alu['nombre']}; {alu['apellido']}; {alu['legajo']}; {nota_str}\n"
                    archivo.write(linea)
        print(f"Archivo '{nombre_salida}' generado correctamente.\n")
        # Mostrar el contenido por pantalla
        print(f"=== CONTENIDO DE {nombre_salida} ===")
        with open(nombre_salida, "r") as archivo_aprobados:
            contenido = archivo_aprobados.read()
            if contenido.strip() == "":
                print("No hay alumnos aprobados registrados.")
            else:
                print(contenido)
    except Exception as e:
        print(f"Error al procesar el archivo de aprobados: {e}")

# 5. MENÚ PRINCIPAL
def menu():
    lista_alumnos, dicc_legajos = leer_alumnos("alumnos.txt")
    opcion = ""
    while opcion != "4":
        print("\n==================================")
        print("      GESTOR DE ALUMNOS (UTN)")
        print("==================================")
        print("1. Ver alumnos")
        print("2. Agregar alumno")
        print("3. Generar y mostrar archivo de aprobados")
        print("4. Salir")
        opcion = input("Seleccione una opción (1-4): ").strip()
        if opcion == "1":
            print("\n--- LISTADO DE ALUMNOS (alumnos.txt) ---")
            if len(lista_alumnos) == 0:
                print("El registro está vacío.")
            else:
                for alu in lista_alumnos:
                    print(f"Nombre: {alu['nombre']} {alu['apellido']} | Legajo: {alu['legajo']} | Nota Promedio: {alu['nota']}")
        elif opcion == "2":
            agregar_alumno(lista_alumnos, dicc_legajos, "alumnos.txt")
        elif opcion == "3":
            guardar_aprobados(lista_alumnos, "aprobados.txt")
        elif opcion == "4":
            print("Saliendo del programa... ¡Hasta luego!")
        else:
            print("Opción no válida. Ingrese un número del 1 al 4.")

# Punto de ejecución principal
if __name__ == "__main__":
    menu()
