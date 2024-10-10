funciones_programacion = {
    "print": {
        "significado": "Imprimir",
        "explicacion": "Muestra información en la consola o salida estándar."
    },
    "input": {
        "significado": "Entrada",
        "explicacion": "Permite al usuario ingresar datos desde el teclado."
    },
    "len": {
        "significado": "Longitud",
        "explicacion": "Retorna la cantidad de elementos en una lista, cadena o colección."
    },
    "int": {
        "significado": "Entero",
        "explicacion": "Convierte un valor a un número entero."
    },
    "str": {
        "significado": "Cadena",
        "explicacion": "Convierte un valor a una cadena de texto."
    },
    "float": {
        "significado": "Decimal",
        "explicacion": "Convierte un valor a un número decimal."
    },
    "range": {
        "significado": "Rango",
        "explicacion": "Genera una secuencia de números en un rango dado."
    },
    "sum": {
        "significado": "Suma",
        "explicacion": "Suma los elementos de una lista o colección."
    },
    "max": {
        "significado": "Máximo",
        "explicacion": "Retorna el valor máximo de una lista o colección."
    },
    "min": {
        "significado": "Mínimo",
        "explicacion": "Retorna el valor mínimo de una lista o colección."
    },
    "append": {
        "significado": "Agregar",
        "explicacion": "Añade un elemento al final de una lista."
    },
    "pop": {
        "significado": "Eliminar",
        "explicacion": "Elimina y retorna el último elemento de una lista."
    },
    "remove": {
        "significado": "Quitar",
        "explicacion": "Elimina el primer elemento que coincida con el valor dado en una lista."
    },
    "split": {
        "significado": "Dividir",
        "explicacion": "Divide una cadena en una lista según un delimitador."
    },
    "join": {
        "significado": "Unir",
        "explicacion": "Une los elementos de una lista en una cadena de texto."
    },
    "def": {
        "significado": "Definir",
        "explicacion": "Se usa para definir una nueva función en Python."
    },
    "return": {
        "significado": "Retornar",
        "explicacion": "Devuelve un valor desde una función."
    },
    "if": {
        "significado": "Si",
        "explicacion": "Define una condición para ejecutar un bloque de código."
    },
    "elif": {
        "significado": "Si no",
        "explicacion": "Define una condición adicional si la primera no se cumple."
    },
    "else": {
        "significado": "De lo contrario",
        "explicacion": "Ejecuta un bloque de código si ninguna condición previa se cumple."
    },
    "for": {
        "significado": "Para",
        "explicacion": "Bucle que itera sobre una secuencia (lista, cadena, etc.)."
    },
    "while": {
        "significado": "Mientras",
        "explicacion": "Bucle que se ejecuta mientras una condición sea verdadera."
    },
    "break": {
        "significado": "Romper",
        "explicacion": "Termina un bucle de manera anticipada."
    },
    "continue": {
        "significado": "Continuar",
        "explicacion": "Salta la iteración actual y continúa con la siguiente."
    },
    "try": {
        "significado": "Intentar",
        "explicacion": "Ejecuta un bloque de código y captura errores si ocurren."
    },
    "except": {
        "significado": "Excepto",
        "explicacion": "Define lo que sucede si ocurre un error en el bloque `try`."
    },
    "finally": {
        "significado": "Finalmente",
        "explicacion": "Código que se ejecuta siempre, sin importar si hubo errores o no."
    },
    "class": {
        "significado": "Clase",
        "explicacion": "Define una nueva clase para crear objetos (POO)."
    },
    "import": {
        "significado": "Importar",
        "explicacion": "Se usa para importar módulos externos o funciones."
    },
    "lambda": {
        "significado": "Función anónima",
        "explicacion": "Define una pequeña función en una sola línea."
    }
}


print("Funciones de Python:")
print("--------------------")
for funcion, detalles in funciones_programacion.items():
    print(f"{funcion}:")
    print(f"  Significado: {detalles['significado']}")
    print(f"  Explicación: {detalles['explicacion']}")

