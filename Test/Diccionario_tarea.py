import diccionario

def agregar_termino():
    letra = input("Ingrese la letra del término (ejemplo: 'a'): ").lower()
    palabra_ingles = input("Ingrese la palabra en inglés: ").lower()
    
    # Si no existe la letra en el diccionario, la creamos
    if letra not in diccionario.diccionario:
        diccionario.diccionario[letra] = {}

    # Verificar si la palabra ya está en la letra correspondiente
    if palabra_ingles in diccionario.diccionario[letra]:
        print("El término ya existe en el diccionario.")
    else:
        traduccion = input("Ingrese la traducción al español: ")
        categoria = input("Ingrese la categoría (Estructuras de Datos, Funciones, Condicionales, Ciclos, General): ")
        definicion = input("Ingrese la definición del término: ")
        
        diccionario.diccionario[letra][palabra_ingles] = {
            "traduccion": traduccion,
            "categoria": categoria,
            "definicion": definicion
        }
        print(f"Término '{palabra_ingles}' agregado con éxito en la letra '{letra.upper()}'.")
        
def eliminar_termino():
    letra = input("Ingrese la letra del término (ejemplo: 'a'): ").lower()
    palabra_ingles = input("Ingrese la palabra en inglés a eliminar: ").lower()
    
    if letra in diccionario.diccionario and palabra_ingles in diccionario.diccionario[letra]:
        del diccionario.diccionario[letra][palabra_ingles]
        print(f"Término '{palabra_ingles}' eliminado de la letra '{letra.upper()}'.")
    else:
        print("El término no existe en el diccionario.")
        
def buscar_termino():
    letra = input("Ingrese la letra del término (ejemplo: 'a'): ").lower()
    palabra_ingles = input("Ingrese la palabra en inglés a buscar: ").lower()
    
    if letra in diccionario.diccionario and palabra_ingles in diccionario.diccionario[letra]:
        termino = diccionario.diccionario[letra][palabra_ingles]
        print(f"Traducción: {termino['traduccion']}")
        print(f"Categoría: {termino['categoria']}")
        print(f"Definición: {termino['definicion']}")
    else:
        print("El término no existe en el diccionario.")
        
def mostrar_terminos():
    for letra, terminos in diccionario.diccionario.items():
        print(f"\nTérminos de la letra '{letra.upper()}':")
        for palabra_ingles, detalles in terminos.items():
            print(f"Termino: {palabra_ingles.capitalize()}  -  Categoría: {detalles['categoria']}")

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
            print("Este programa fue desarrollado por Luis Gonzalez, Pablo Cocio, Vicente Soto, Benjamin Cona, Ambar Rojas usando Python.")
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente. (1-6)")

menu()
