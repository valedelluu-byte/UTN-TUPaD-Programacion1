import sqlite3

# EJERCICIO 1: Modelado de Clases (POO)

class Autor:
    def __init__(self, id_autor: int, nombre: str, nacionalidad: str):
        self.id_autor = id_autor
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def __str__(self):
        return f"Autor #{self.id_autor}: {self.nombre} ({self.nacionalidad})"


class Libro:
    def __init__(self, id_libro: int, titulo: str, anio_publicacion: int, autor: Autor):
        self.id_libro = id_libro
        self.titulo = titulo
        self.anio_publicacion = anio_publicacion
        self.autor = autor  # Relación de agregación con la clase Autor

    def __str__(self):
        return f"Libro #{self.id_libro}: '{self.titulo}' ({self.anio_publicacion}) - {self.autor.nombre}"



# EJERCICIO 2: Creación del Esquema en Base de Datos

def inicializar_bd(nombre_bd="biblioteca.db"):
    """Crea la base de datos y las tablas 'autores' y 'libros' si no existen."""
    with sqlite3.connect(nombre_bd) as conexion:
        cursor = conexion.cursor()
        
        # Habilitar el soporte para Claves Foráneas (Foreign Keys)
        cursor.execute("PRAGMA foreign_keys = ON;")
        
        # Tabla 'autores'
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS autores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                nacionalidad TEXT
            )
        ''')
        
        # Tabla 'libros' (con clave foránea hacia autores.id)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS libros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                anio INTEGER,
                autor_id INTEGER,
                FOREIGN KEY (autor_id) REFERENCES autores(id) ON DELETE CASCADE
            )
        ''')
        conexion.commit()
    print("-> Base de datos inicializada correctamente.")


# EJERCICIO 3: Implementación del Repositorio CRUD

def registrar_autor(nombre: str, nacionalidad: str, nombre_bd="biblioteca.db") -> int:
    """Inserta un autor y retorna su ID generado."""
    with sqlite3.connect(nombre_bd) as conexion:
        cursor = conexion.cursor()
        cursor.execute('''
            INSERT INTO autores (nombre, nacionalidad)
            VALUES (?, ?)
        ''', (nombre, nacionalidad))
        conexion.commit()
        return cursor.lastrowid  # Devuelve el ID recién generado


def registrar_libro(titulo: str, anio: int, autor_id: int, nombre_bd="biblioteca.db"):
    """Inserta un libro vinculado a un autor mediante su autor_id."""
    with sqlite3.connect(nombre_bd) as conexion:
        cursor = conexion.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")
        cursor.execute('''
            INSERT INTO libros (titulo, anio, autor_id)
            VALUES (?, ?, ?)
        ''', (titulo, anio, autor_id))
        conexion.commit()


def listar_libros(nombre_bd="biblioteca.db"):
    """
    Realiza un SELECT con JOIN entre libros y autores para mostrar
    el título, año y nombre del autor. Devuelve una lista de instancias Libro.
    """
    libros = []
    with sqlite3.connect(nombre_bd) as conexion:
        cursor = conexion.cursor()
        query = '''
            SELECT L.id, L.titulo, L.anio, A.id, A.nombre, A.nacionalidad
            FROM libros L
            INNER JOIN autores A ON L.autor_id = A.id
        '''
        cursor.execute(query)
        filas = cursor.fetchall()
        
        for fila in filas:
            # Creamos primero el objeto Autor y luego el objeto Libro
            autor_obj = Autor(id_autor=fila[3], nombre=fila[4], nacionalidad=fila[5])
            libro_obj = Libro(id_libro=fila[0], titulo=fila[1], anio_publicacion=fila[2], autor=autor_obj)
            libros.append(libro_obj)
            
    return libros


def actualizar_titulo_libro(id_libro: int, nuevo_titulo: str, nombre_bd="biblioteca.db"):
    """Actualiza el título de un libro existente."""
    with sqlite3.connect(nombre_bd) as conexion:
        cursor = conexion.cursor()
        cursor.execute('''
            UPDATE libros
            SET titulo = ?
            WHERE id = ?
        ''', (nuevo_titulo, id_libro))
        conexion.commit()


def eliminar_libro(id_libro: int, nombre_bd="biblioteca.db"):
    """Elimina un libro de la base de datos según su ID."""
    with sqlite3.connect(nombre_bd) as conexion:
        cursor = conexion.cursor()
        cursor.execute('''
            DELETE FROM libros
            WHERE id = ?
        ''', (id_libro,))
        conexion.commit()



# EJERCICIO 4: Integración y Prueba Integral


if __name__ == '__main__':
    print("=== INICIANDO DEMOSTRACIÓN DEL SISTEMA DE BIBLIOTECA ===\n")
    
    # 1. Inicializar la base de datos
    inicializar_bd()

    # 2. Registrar al menos 2 autores y 3 libros
    id_autor1 = registrar_autor("Gabriel García Márquez", "Colombiana")
    id_autor2 = registrar_autor("Jorge Luis Borges", "Argentina")

    registrar_libro("Cien años de soledad", 1967, id_autor1)
    registrar_libro("El amor en los tiempos del cólera", 1985, id_autor1)
    registrar_libro("Ficciones", 1944, id_autor2)

    # 3. Listar todos los libros registrados en consola
    print("\n--- 📚 LISTADO DE LIBROS INICIAL ---")
    libros = listar_libros()
    for libro in libros:
        print(libro)

    # 4. Actualizar el título de uno de los libros y verificar el cambio
    if libros:
        id_libro_a_modificar = libros[0].id_libro
        nuevo_titulo = "Cien Años de Soledad (Edición Conmemorativa)"
        print(f"\n-> Actualizando el título del libro ID {id_libro_a_modificar}...")
        actualizar_titulo_libro(id_libro_a_modificar, nuevo_titulo)

        print("\n--- 📚 LISTADO TRAS LA ACTUALIZACIÓN ---")
        for libro in listar_libros():
            print(libro)

    # 5. Eliminar un libro y mostrar el listado resultante
    if len(libros) > 1:
        id_libro_a_eliminar = libros[1].id_libro
        print(f"\n-> Eliminando el libro con ID {id_libro_a_eliminar}...")
        eliminar_libro(id_libro_a_eliminar)

        print("\n--- 📚 LISTADO TRAS LA ELIMINACIÓN ---")
        for libro in listar_libros():
            print(libro)

    print("\n=== PRUEBA FINALIZADA CON ÉXITO ===")