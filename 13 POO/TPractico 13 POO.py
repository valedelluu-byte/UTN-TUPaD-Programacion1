
# EJERCICIO 1: CELDA Y MATRIZ

class Celda:
    def __init__(self, fila: int, columna: int, valor: str):
        self.fila = fila
        self.columna = columna
        self.valor = valor


class Matriz:
    def __init__(self):
        self.celdasMatriz: list[Celda] = []

    def existe_celda(self, fila: int, columna: int) -> bool:
        for celda in self.celdasMatriz:
            if celda.fila == fila and celda.columna == columna:
                return True
        return False

    def obtener_valor(self, fila: int, columna: int) -> str:
        for celda in self.celdasMatriz:
            if celda.fila == fila and celda.columna == columna:
                return celda.valor
        return "La fila y columna indicada no ha sido asignada en ninguna celda"


def ejecutar_ejercicio_1():
    print("\n==================================================")
    print("           EJERCICIO 1: CELDAS Y MATRIZ           ")
    print("==================================================")
    matriz = Matriz()

    while True:
        valor = input("Ingrese el valor para la celda (o 'FIN' para terminar): ")
        if valor.strip().upper() == "FIN":
            break

        fila = int(input("Ingrese el número de fila: "))
        columna = int(input("Ingrese el número de columna: "))

        if matriz.existe_celda(fila, columna):
            print("⚠️ Error: La celda en esa posición ya fue cargada anteriormente.")
        else:
            nueva_celda = Celda(fila, columna, valor)
            matriz.celdasMatriz.append(nueva_celda)
            print("✅ Celda cargada exitosamente.")

    print("\n--- CELDAS CARGADAS EN LA MATRIZ ---")
    for celda in matriz.celdasMatriz:
        print(f"Fila: {celda.fila} | Columna: {celda.columna} | Valor: {celda.valor}")

    print("\n--- BÚSQUEDA DE VALOR ---")
    f_buscar = int(input("Fila a consultar: "))
    c_buscar = int(input("Columna a consultar: "))
    print("Resultado:", matriz.obtener_valor(f_buscar, c_buscar))



# EJERCICIO 2: NOTA, ALUMNO Y CARGA DE NOTAS


class Nota:
    def __init__(self, catedra: str, notaExamen: float):
        self.catedra = catedra
        self.notaExamen = notaExamen


class Alumno:
    def __init__(self, nombreCompleto: str, legajo: int):
        self.nombreCompleto = nombreCompleto
        self.legajo = legajo
        self.notas: list[Nota] = []

    def agregar_nota(self, nota: Nota):
        self.notas.append(nota)

    def calcular_promedio(self) -> float:
        if not self.notas:
            return 0.0
        suma = sum(n.notaExamen for n in self.notas)
        return suma / len(self.notas)


def ejecutar_ejercicio_2():
    print("\n==================================================")
    print("        EJERCICIO 2: ALUMNOS Y NOTAS             ")
    print("==================================================")
    alumnos: list[Alumno] = []

    while True:
        print("\n--- INGRESO DE DATOS DEL ALUMNO ---")
        nombre = input("Nombre completo: ")
        legajo = int(input("Legajo: "))
        alumno = Alumno(nombre, legajo)

        while True:
            print("\n--- CARGA DE NOTA ---")
            catedra = input("Nombre de la cátedra: ")
            nota_examen = float(input("Nota del examen: "))
            alumno.agregar_nota(Nota(catedra, nota_examen))

            salir_notas = input("¿Desea salir de la carga de notas de este alumno? (SI/NO): ").strip().upper()
            if salir_notas == "SI":
                break

        alumnos.append(alumno)
        salir_alumno = input("¿Desea salir de la carga de alumnos? (SI/NO): ").strip().upper()
        if salir_alumno == "SI":
            break

    print("\n================ RESULTADOS ================")
    for alumno in alumnos:
        print(f"\nAlumno: {alumno.nombreCompleto} | Legajo: {alumno.legajo}")
        for nota in alumno.notas:
            print(f"  - Cátedra: {nota.catedra} | Nota: {nota.notaExamen}")
        print(f"  --> Promedio final: {alumno.calcular_promedio():.2f}")



# EJERCICIO 3: INGREDIENTE, PLATO Y MENÚ RESTAURANT


class Ingrediente:
    def __init__(self, nombre: str, cantidad: float, unidad_medida: str):
        self.nombre = nombre
        self.cantidad = cantidad
        self.unidad_medida = unidad_medida


class Plato:
    def __init__(self, nombreCompleto: str, precio: float, esBebida: bool):
        self.nombreCompleto = nombreCompleto
        self.precio = precio
        self.esBebida = esBebida
        self.ingredientes: list[Ingrediente] = []

    def agregar_ingrediente(self, ingrediente: Ingrediente):
        self.ingredientes.append(ingrediente)


def ejecutar_ejercicio_3():
    print("\n==================================================")
    print("        EJERCICIO 3: MENÚ DE RESTAURANT          ")
    print("==================================================")
    platosMenu: list[Plato] = []

    while True:
        nombre = input("\nNombre del plato o bebida: ")
        precio = float(input("Precio ($): "))
        es_bebida = input("¿Es bebida? (SI/NO): ").strip().upper() == "SI"

        plato = Plato(nombre, precio, es_bebida)

        if not es_bebida:
            print("Cargue los ingredientes obligatorios (al menos 1):")
            while True:
                ing_nombre = input("  Nombre del ingrediente: ")
                ing_cant = float(input("  Cantidad: "))
                ing_unidad = input("  Unidad de medida (gramos, unidad, etc.): ")
                
                plato.agregar_ingrediente(Ingrediente(ing_nombre, ing_cant, ing_unidad))

                if input("  ¿Desea agregar otro ingrediente? (SI/NO): ").strip().upper() != "SI":
                    break

        platosMenu.append(plato)

        if input("\n¿Desea agregar otro plato al menú? (SI/NO): ").strip().upper() != "SI":
            break

    print("\nMENÚ----------------------------------")
    for plato in platosMenu:
        print(f"\n{plato.nombreCompleto}")
        print(f"Precio: $ {plato.precio:.2f}")
        if not plato.esBebida and plato.ingredientes:
            print("Ingredientes:")
            print(f"{'Nombre':<20} | {'Cantidad':<10} | {'Unidad de Medida':<15}")
            print("-" * 50)
            for ing in plato.ingredientes:
                print(f"{ing.nombre:<20} | {ing.cantidad:<10} | {ing.unidad_medida:<15}")



# EJERCICIO 4: COMPONENTE CPU, COMPUTADORA Y COTIZACIÓN


class ComponenteCPU:
    def __init__(self, componente: str, marca: str, cantidad: int, precio: float):
        self.componente = componente
        self.marca = marca
        self.cantidad = cantidad
        self.precio = precio

    def subtotal(self) -> float:
        return self.cantidad * self.precio


class Computadora:
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo
        self.componentes: list[ComponenteCPU] = []

    def agregar_componente(self, componente: ComponenteCPU):
        self.componentes.append(componente)

    def costo_total(self) -> float:
        return sum(c.subtotal() for c in self.componentes)

    def precio_sugerido(self) -> float:
        costo = self.costo_total()
        if costo < 50000:
            return costo * 1.40
        else:
            return costo * 1.30


def ejecutar_ejercicio_4():
    print("\n==================================================")
    print("      EJERCICIO 4: COTIZACIÓN COMPUTADORAS       ")
    print("==================================================")
    while True:
        marca = input("\nMarca de la computadora: ")
        modelo = input("Modelo: ")
        comp = Computadora(marca, modelo)

        while True:
            nombre = input("\nNombre del componente (ej. Memoria RAM): ")
            marca_comp = input("Marca del componente: ")
            cant = int(input("Cantidad: "))
            precio = float(input("Precio unitario: "))

            comp.agregar_componente(ComponenteCPU(nombre, marca_comp, cant, precio))

            if input("¿Agregar otro componente? (SI/NO): ").strip().upper() != "SI":
                break

        print(f"\nComputadora")
        print(f"Marca: {comp.marca}")
        print(f"Modelo: {comp.modelo}")
        print("Componentes:")
        print("-" * 70)
        print(f"{'Componente':<20} | {'Marca':<10} | {'Cantidad':<8} | {'Precio X U.':<12} | {'SubTotal':<10}")
        print("-" * 70)
        for c in comp.componentes:
            print(f"{c.componente:<20} | {c.marca:<10} | {c.cantidad:<8} | {c.precio:<12.2f} | {c.subtotal():<10.2f}")
        print("-" * 70)
        
        costo = comp.costo_total()
        precio_venta = comp.precio_sugerido()
        print(f"{'':<58} Costo Total | ${costo:.2f}")
        print(f"\nEl precio sugerido de venta es: ${precio_venta:.2f}")

        if input("\n¿Desea cotizar una nueva computadora? (SI/NO): ").strip().upper() != "SI":
            break



# EJERCICIO 5: HABITACIÓN, VIVIENDA Y BARRIO


class Habitacion:
    def __init__(self, nombre: str, metrosCuadrados: float):
        self.nombre = nombre
        self.metrosCuadrados = metrosCuadrados


class Vivienda:
    def __init__(self, calle: str, numero: int, manzana: str, nroCasa: int, superficieTerreno: float):
        self.calle = calle
        self.numero = numero
        self.manzana = manzana
        self.nroCasa = nroCasa
        self.superficieTerreno = superficieTerreno
        self.habitaciones: list[Habitacion] = []

    def agregar_habitacion(self, habitacion: Habitacion):
        self.habitaciones.append(habitacion)

    def getMetrosCuadradosCubiertos(self) -> float:
        total_cubierto = sum(h.metrosCuadrados for h in self.habitaciones)
        if total_cubierto > self.superficieTerreno:
            raise Exception("La superficie cubierta no puede ser mayor a la superficie del terreno")
        return total_cubierto


class Barrio:
    def __init__(self, nombre: str, empresaConstructora: str):
        self.nombre = nombre
        self.empresaConstructora = empresaConstructora
        self.viviendas: list[Vivienda] = []

    def agregar_vivienda(self, vivienda: Vivienda):
        self.viviendas.append(vivienda)

    def getSuperficieTotalTerreno(self) -> float:
        return sum(v.superficieTerreno for v in self.viviendas)

    def getSuperficieTotalTerrenoXManzana(self, manzana: str) -> float:
        return sum(v.superficieTerreno for v in self.viviendas if v.manzana.upper() == manzana.upper())

    def getSuperficieTotalCubierta(self) -> float:
        return sum(v.getMetrosCuadradosCubiertos() for v in self.viviendas)


def ejecutar_ejercicio_5():
    print("\n==================================================")
    print("      EJERCICIO 5: BARRIO, VIVIENDA Y HABITACIÓN   ")
    print("==================================================")
    
    # Se crean los objetos y se prueban los métodos
    barrio = Barrio("Barrio Las Rosas", "Constructora Alfa")

    # Vivienda 1 (Manzana A)
    v1 = Vivienda("Av. San Martín", 123, "A", 1, 200.0)
    v1.agregar_habitacion(Habitacion("Dormitorio principal", 20.0))
    v1.agregar_habitacion(Habitacion("Cocina", 15.0))
    v1.agregar_habitacion(Habitacion("Living", 30.0))

    # Vivienda 2 (Manzana A)
    v2 = Vivienda("Calle Belgrano", 456, "A", 2, 250.0)
    v2.agregar_habitacion(Habitacion("Dormitorio 1", 25.0))
    v2.agregar_habitacion(Habitacion("Dormitorio 2", 20.0))
    v2.agregar_habitacion(Habitacion("Comedor", 40.0))

    # Vivienda 3 (Manzana B)
    v3 = Vivienda("Calle Mitre", 789, "B", 1, 180.0)
    v3.agregar_habitacion(Habitacion("Dormitorio", 15.0))
    v3.agregar_habitacion(Habitacion("Baño", 8.0))

    # Asociar viviendas al barrio
    barrio.agregar_vivienda(v1)
    barrio.agregar_vivienda(v2)
    barrio.agregar_vivienda(v3)

    # Mostrar resultados de los métodos pedidos
    print(f"Barrio: {barrio.nombre}")
    print(f"Empresa: {barrio.empresaConstructora}")
    print(f"- Superficie Total Terreno del Barrio: {barrio.getSuperficieTotalTerreno()} m²")
    print(f"- Superficie Total Terreno Manzana 'A': {barrio.getSuperficieTotalTerrenoXManzana('A')} m²")
    print(f"- Superficie Total Terreno Manzana 'B': {barrio.getSuperficieTotalTerrenoXManzana('B')} m²")
    
    try:
        print(f"- Superficie Total Cubierta del Barrio: {barrio.getSuperficieTotalCubierta()} m²")
    except Exception as e:
        print(f"Error: {e}")



# MENÚ PRINCIPAL INTERACTIVO PARA PROBAR CUALQUIER PUNTO


def main():
    while True:
        print("\n==================================================")
        print("    MENÚ TRABAJO PRÁCTICO POO - SELECCIONE OPCCIÓN ")
        print("==================================================")
        print("1. Ejercicio 1 (Matriz y Celdas)")
        print("2. Ejercicio 2 (Carga de Notas y Alumnos)")
        print("3. Ejercicio 3 (Menú de Restaurant)")
        print("4. Ejercicio 4 (Cotización de Computadoras)")
        print("5. Ejercicio 5 (Barrio, Viviendas y Habitaciones)")
        print("6. Salir")

        opcion = input("\nIngrese una opción (1-6): ").strip()

        if opcion == "1":
            ejecutar_ejercicio_1()
        elif opcion == "2":
            ejecutar_ejercicio_2()
        elif opcion == "3":
            ejecutar_ejercicio_3()
        elif opcion == "4":
            ejecutar_ejercicio_4()
        elif opcion == "5":
            ejecutar_ejercicio_5()
        elif opcion == "6":
            print("\n¡Programa finalizado!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


# Llamada obligatoria para arrancar la ejecución
if __name__ == "__main__":
    main()