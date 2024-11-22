import diccionario
# Funciones
def agregar_termino():
    palabra_ingles = input("Ingrese la palabra en inglés: ").lower()
    if palabra_ingles in diccionario:
        print("El término ya existe en el diccionario.")
    else:
        traduccion = input("Ingrese la traducción al español: ")
        categoria = input("Ingrese la categoría (Estructuras de Datos, Funciones, Condicionales, Ciclos, General): ")
        diccionario[palabra_ingles] = {
            "traduccion": traduccion,
            "categoria": categoria
        }
        print(f"Término '{palabra_ingles}' agregado con éxito.")

def eliminar_termino():
    palabra_ingles = input("Ingrese la palabra en inglés a eliminar: ").lower()
    if palabra_ingles in diccionario:
        del diccionario[palabra_ingles]
        print(f"Término '{palabra_ingles}' eliminado.")
    else:
        print("El término no existe en el diccionario.")

def buscar_termino():
    palabra_ingles = input("Ingrese la palabra en inglés a buscar: ").lower()
    if palabra_ingles in diccionario:
        print(f"Traducción: {diccionario[palabra_ingles]['traduccion']}")
        print(f"Categoría: {diccionario[palabra_ingles]['categoria']}")
    else:
        print("El término no existe en el diccionario.")

def mostrar_terminos():
    for palabra_ingles, detalles in diccionario.items():
        print(f"{palabra_ingles.capitalize()}: {detalles['traduccion']} (Categoría: {detalles['categoria']})")

def menu():
    while True:
        print("\n--- Menú del Diccionario del Programador ---")
        print("1. Agregar un término")
        print("2. Eliminar un término")
        print("3. Buscar la traducción de un término")
        print("4. Mostrar todos los términos")
        print("5. Acerca del programa")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_termino()
        elif opcion == "2":
            eliminar_termino()
        elif opcion == "3":
            buscar_termino()
        elif opcion == "4":
            mostrar_terminos()
        elif opcion == "5":
            print("Este programa fue desarrollado por [Nombre del equipo] usando Python.")
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

menu()
