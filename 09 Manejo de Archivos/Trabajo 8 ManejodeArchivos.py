# TRABAJO PRÁCTICO FINAL: MANEJO DE ARCHIVOS EN PYTHON

# Actividad 1: Crear archivo inicial con tres productos
def actividad_1_crear_archivo():
    """Crea el archivo productos.txt con 3 productos iniciales."""
    with open("productos.txt", "w") as archivo:
        archivo.write("Lapicera,120.5,30\n")
        archivo.write("Cuaderno,850.0,15\n")
        archivo.write("Mochila,4500.0,5\n")
    print("-> Actividad 1: Archivo 'productos.txt' creado con los productos iniciales.\n")


# Actividad 2: Leer y mostrar productos por pantalla
def actividad_2_mostrar_productos(lista_productos):
    """Abre el archivo y muestra los productos en pantalla con el formato pedido."""
    print("--- Actividad 2: LISTA DE PRODUCTOS ---")
    for p in lista_productos:
        print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")
    print()


# Actividad 3: Agregar productos desde el teclado (modo 'a')
def actividad_3_agregar_producto(lista_productos):
    """Pide un producto por teclado y lo agrega al archivo sin borrar lo anterior."""
    print("--- Actividad 3: AGREGAR NUEVO PRODUCTO ---")
    nombre = input("Ingrese el nombre del producto: ").strip()
    precio = float(input("Ingrese el precio: "))
    cantidad = int(input("Ingrese la cantidad: "))
    # A. Agregamos a la lista en memoria RAM
    nuevo_producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    lista_productos.append(nuevo_producto)
    # B. Anexamos al final del archivo usando el modo 'a'
    with open("productos.txt", "a") as archivo:
        archivo.write(f"{nombre},{precio},{cantidad}\n")
    print("-> Producto agregado al archivo con el modo 'a' exitosamente.\n")


# Actividad 4: Cargar productos en una lista de diccionarios
def actividad_4_cargar_productos():
    """Lee el archivo productos.txt y carga los datos en una lista de diccionarios."""
    lista_productos = []
    with open("productos.txt", "r") as archivo:
        for linea in archivo:
            linea_limpia = linea.strip()
            if linea_limpia != "":
                datos = linea_limpia.split(",")
                producto = { "nombre": datos[0], "precio": float(datos[1]), "cantidad": int(datos[2]) }
                lista_productos.append(producto)
    return lista_productos

# Actividad 5: Buscar producto por nombre
def actividad_5_buscar_producto(lista_productos):
    """Pide un nombre al usuario y busca el producto en la lista."""
    print("--- Actividad 5: BÚSQUEDA DE PRODUCTO ---")
    busqueda = input("Ingrese el nombre del producto a buscar: ").strip()
    encontrado = False
    for p in lista_productos:
        if p["nombre"].lower() == busqueda.lower():
            print(f"¡Encontrado! Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}\n")
            encontrado = True
            break
    if not encontrado:
        print(f"Error: El producto '{busqueda}' no existe en el registro.\n")


# Actividad 6: Guardar los productos actualizados (sobrescribir con modo 'w')
def actividad_6_guardar_actualizados(lista_productos):
    """Sobrescribe productos.txt escribiendo todos los productos desde la lista."""
    with open("productos.txt", "w") as archivo:
        for p in lista_productos:
            archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")
    print("-> Actividad 6: Archivo 'productos.txt' actualizado correctamente desde la lista.\n")


# EJECUCIÓN PASO A PASO (De la Actividad 1 a la 6)
# 1. Crear el archivo inicial
actividad_1_crear_archivo()
# 4. Cargar los datos del archivo en la lista de diccionarios
mis_productos = actividad_4_cargar_productos()
# 2. Mostrar los productos cargados
actividad_2_mostrar_productos(mis_productos)
# 3. Pedir al usuario un nuevo producto y agregarlo
actividad_3_agregar_producto(mis_productos)
# 5. Buscar un producto por su nombre
actividad_5_buscar_producto(mis_productos)
# 6. Guardar la lista actualizada sobrescribiendo el archivo
actividad_6_guardar_actualizados(mis_productos)