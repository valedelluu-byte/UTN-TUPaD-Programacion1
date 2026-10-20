
# TRABAJO PRÁCTICO: ANÁLISIS Y NAVEGACIÓN DE SISTEMAS DE ARCHIVOS
# RECURSIVIDAD Y ESTRUCTURAS DE DATOS BASE


# 1. Estructura de Datos Base (Clases simplificadas)
class Archivo:
    def __init__(self, nombre: str, tamano_bytes: int):
        self.nombre = nombre
        self.tamano_bytes = tamano_bytes

class Directorio:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.archivos = []        # Lista de objetos de tipo Archivo
        self.subdirectorios = []   # Lista de objetos de tipo Directorio


# FUNCIÓN 1: Cálculo del Tamaño Total de un Directorio

def calcular_tamano_total(directorio: Directorio) -> int:
    """Calcula el tamaño acumulado de un directorio y sus subdirectorios."""
    # 1. Sumamos los tamaños de los archivos locales
    total_bytes = 0
    for archivo in directorio.archivos:
        total_bytes += archivo.tamano_bytes

    # 2. Paso recursivo: Invocamos la función sobre cada subdirectorio y acumulamos
    for subdirectorio in directorio.subdirectorios:
        total_bytes += calcular_tamano_total(subdirectorio)

    return total_bytes



# FUNCIÓN 2: Búsqueda de Archivos por Extensión

def buscar_por_extension(directorio: Directorio, extension: str) -> list[str]:
    """Retorna las rutas completas de todos los archivos con la extensión indicada."""
    resultados = []

    # 1. Inspeccionamos los archivos del directorio actual
    for archivo in directorio.archivos:
        if archivo.nombre.endswith(extension):
            resultados.append(directorio.nombre + "/" + archivo.nombre)

    # 2. Paso recursivo sobre cada subdirectorio
    for subdirectorio in directorio.subdirectorios:
        rutas_sub = buscar_por_extension(subdirectorio, extension)
        for ruta in rutas_sub:
            # Anteponemos el nombre del directorio actual a la ruta del subdirectorio
            resultados.append(directorio.nombre + "/" + ruta)

    return resultados


# FUNCIÓN 3: Eliminación Recursiva de Archivos Vacíos (Limpieza de Disco)

def limpiar_archivos_vacios(directorio: Directorio) -> int:
    """Elimina los objetos Archivo con tamano_bytes == 0 y devuelve la cantidad eliminada."""
    # 1. Conservamos solo los archivos que NO estén vacíos
    archivos_conservados = []
    eliminados_locales = 0

    for archivo in directorio.archivos:
        if archivo.tamano_bytes == 0:
            eliminados_locales += 1
        else:
            archivos_conservados.append(archivo)

    # Actualizamos la lista de archivos del directorio
    directorio.archivos = archivos_conservados

    # 2. Paso recursivo: Propagamos la limpieza a cada subdirectorio
    total_eliminados = eliminados_locales
    for subdirectorio in directorio.subdirectorios:
        total_eliminados += limpiar_archivos_vacios(subdirectorio)

    return total_eliminados



# EJERCICIO INTEGRADOR Y CASO DE PRUEBA (Validación)

if __name__ == "__main__":
    # --- Construcción del árbol 'root/' según el enunciado ---
    root = Directorio("root")

    # Archivos en root
    root.archivos.append(Archivo("documento.pdf", 1500))
    root.archivos.append(Archivo("config.txt", 0))

    # Subdirectorio 'imagenes'
    imagenes = Directorio("imagenes")
    imagenes.archivos.append(Archivo("foto1.png", 2000))
    imagenes.archivos.append(Archivo("foto2.png", 3500))
    root.subdirectorios.append(imagenes)

    # Subdirectorios 'proyectos' y 'temp'
    proyectos = Directorio("proyectos")
    proyectos.archivos.append(Archivo("avance.pdf", 800))

    temp = Directorio("temp")
    temp.archivos.append(Archivo("log.txt", 0))

    proyectos.subdirectorios.append(temp)
    root.subdirectorios.append(proyectos)

    # --- VALIDACIÓN DE RESULTADOS ESPERADOS ---
    print("==================================================")
    print("   PRUEBA DE VALIDACIÓN DEL TRABAJO PRÁCTICO")
    print("==================================================")
    
    # Pruebas
    tamano = calcular_tamano_total(root)
    print(f"1. Tamaño Total de root: {tamano} bytes")
    # Esperado: 7800

    pdfs = buscar_por_extension(root, ".pdf")
    print(f"2. Búsqueda de archivos .pdf: {pdfs}")
    # Esperado: ['root/documento.pdf', 'root/proyectos/avance.pdf']

    eliminados = limpiar_archivos_vacios(root)
    print(f"3. Archivos vacíos eliminados: {eliminados}")
    # Esperado: 2 (config.txt y log.txt)
    print("==================================================")