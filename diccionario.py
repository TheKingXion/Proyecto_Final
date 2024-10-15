# Diccionario de términos de programación
diccionario_programacion = {
    "if": {
        "traduccion": "si",
        "explicacion": "Se utiliza para tomar decisiones. Permite ejecutar un bloque de código solo si se cumple una condición.",
        "ejemplo": 'if numero == 1: print("Hola")'
    },
    "else": {
        "traduccion": "sino",
        "explicacion": "Se utiliza junto con 'if'. Ejecuta un bloque de código si la condición del 'if' no se cumple.",
        "ejemplo": 'if numero == 1: print("Uno") else: print("No es uno")'
    },
    "elif": {
        "traduccion": "sino si",
        "explicacion": "Se utiliza para evaluar múltiples condiciones. Permite agregar más de un caso a una estructura de control.",
        "ejemplo": 'if numero == 1: print("Uno") elif numero == 2: print("Dos")'
    },
    "for": {
        "traduccion": "para",
        "explicacion": "Se utiliza para iterar sobre una secuencia (como una lista, tupla o cadena) ejecutando un bloque de código por cada elemento.",
        "ejemplo": 'for i in range(5): print(i)'
    },
    "while": {
        "traduccion": "mientras",
        "explicacion": "Se utiliza para repetir un bloque de código mientras se cumpla una condición. Puede llevar a bucles infinitos si la condición nunca se vuelve falsa.",
        "ejemplo": 'while contador < 5: print(contador); contador += 1'
    },
    "function": {
        "traduccion": "función",
        "explicacion": "Es un bloque de código que se puede reutilizar. Se define una vez y se puede llamar en diferentes partes del programa.",
        "ejemplo": 'def saludo(): print("Hola")'
    },
    "variable": {
        "traduccion": "variable",
        "explicacion": "Es un espacio de almacenamiento que se utiliza para guardar datos. Las variables pueden cambiar su valor a lo largo del tiempo.",
        "ejemplo": 'numero = 10'
    },
    "list": {
        "traduccion": "lista",
        "explicacion": "Es una estructura de datos que almacena múltiples elementos en un solo objeto. Los elementos pueden ser de diferentes tipos y son accesibles mediante índices.",
        "ejemplo": 'mi_lista = [1, 2, 3, 4, 5]'
    },
    "array": {
        "traduccion": "arreglo",
        "explicacion": "Es una estructura de datos que almacena una colección de elementos del mismo tipo en un espacio contiguo de memoria, facilitando su acceso y manipulación.",
        "ejemplo": 'arreglo = [1, 2, 3, 4, 5]'
    },
    "dictionary": {
        "traduccion": "diccionario",
        "explicacion": "Es una estructura de datos que almacena pares clave-valor. Permite acceder a los valores mediante su clave correspondiente.",
        "ejemplo": 'mi_diccionario = {"clave": "valor"}'
    },
    "class": {
        "traduccion": "clase",
        "explicacion": "Es un plano para crear objetos. Define atributos y métodos que los objetos creados a partir de la clase tendrán.",
        "ejemplo": 'class Persona: pass'
    },
    "object": {
        "traduccion": "objeto",
        "explicacion": "Es una instancia de una clase. Los objetos pueden tener propiedades (atributos) y comportamientos (métodos).",
        "ejemplo": 'mi_objeto = Persona()'
    },
    "method": {
        "traduccion": "método",
        "explicacion": "Es una función que está asociada a un objeto. Se invoca usando el objeto al que pertenece.",
        "ejemplo": 'mi_lista.append(6)'  # Append es un método de las listas
    },
    "loop": {
        "traduccion": "bucle",
        "explicacion": "Es una estructura de control que repite un bloque de código mientras se cumpla una condición o para cada elemento de una colección.",
        "ejemplo": 'for i in range(5): print(i)'  # Bucle for
    },
    "conditional": {
        "traduccion": "condicional",
        "explicacion": "Es una estructura que permite tomar decisiones en el flujo de un programa, ejecutando diferentes bloques de código según se cumpla o no una condición.",
        "ejemplo": 'if x > 0: print("Positivo") else: print("No positivo")'
    },
    "import": {
        "traduccion": "importar",
        "explicacion": "Es una declaración que se utiliza para incluir módulos o bibliotecas en un programa, permitiendo acceder a funciones y variables definidas en otros archivos.",
        "ejemplo": 'import math  # Importa el módulo math'
    },
    "exception": {
        "traduccion": "excepción",
        "explicacion": "Es un error que ocurre durante la ejecución de un programa. Las excepciones pueden ser gestionadas mediante bloques try-except.",
        "ejemplo": 'try: print(1 / 0) except ZeroDivisionError: print("Error de división por cero")'
    },
    "string": {
        "traduccion": "cadena",
        "explicacion": "Es una secuencia de caracteres. En Python, se puede definir utilizando comillas simples o dobles.",
        "ejemplo": 'mi_cadena = "Hola, mundo!"'
    },
    "boolean": {
        "traduccion": "booleano",
        "explicacion": "Es un tipo de dato que puede ser verdadero (True) o falso (False). Se utiliza en condiciones y bucles.",
        "ejemplo": 'es_adulto = edad >= 18  # Retorna True o False'
    },
    "syntax": {
        "traduccion": "sintaxis",
        "explicacion": "Se refiere al conjunto de reglas que definen la estructura de un lenguaje de programación. Un código que no sigue la sintaxis correcta no se puede ejecutar.",
        "ejemplo": 'print("Hola")'  # Ejemplo de sintaxis correcta
    },
    "argument": {
        "traduccion": "argumento",
        "explicacion": "Es un valor que se pasa a una función cuando se llama. Los argumentos pueden ser requeridos o opcionales.",
        "ejemplo": 'def sumar(a, b): return a + b  # a y b son argumentos'
    },
    "parameter": {
        "traduccion": "parámetro",
        "explicacion": "Es una variable en la definición de una función que recibe un argumento. Los parámetros permiten a las funciones ser más flexibles.",
        "ejemplo": 'def multiplicar(x): return x * 2  # x es un parámetro'
    },
    "return": {
        "traduccion": "retornar",
        "explicacion": "Es una declaración que se utiliza en una función para devolver un valor al lugar donde fue llamada.",
        "ejemplo": 'def obtener_suma(a, b): return a + b'
    },
    "API": {
        "traduccion": "API (Interfaz de Programación de Aplicaciones)",
        "explicacion": "Es un conjunto de reglas y protocolos que permite que diferentes aplicaciones se comuniquen entre sí, facilitando el uso de servicios externos.",
        "ejemplo": 'requests.get("https://api.example.com/data")  # Llama a una API'
    },
    "IDE": {
        "traduccion": "IDE (Entorno de Desarrollo Integrado)",
        "explicacion": "Es una aplicación que proporciona herramientas para facilitar la programación, como editores de código, depuradores y herramientas de compilación.",
        "ejemplo": 'Ejemplos de IDE: PyCharm, Visual Studio Code'
    },
    "debugging": {
        "traduccion": "depuración",
        "explicacion": "Es el proceso de identificar y corregir errores en un programa. Los depuradores son herramientas que ayudan a este proceso.",
        "ejemplo": 'Uso de print() para verificar valores durante la depuración.'
    },
    "library": {
        "traduccion": "biblioteca",
        "explicacion": "Es una colección de funciones y procedimientos que pueden ser utilizadas en un programa. Facilita la reutilización de código.",
        "ejemplo": 'import numpy as np  # Importa la biblioteca NumPy'
    },
    "framework": {
        "traduccion": "marco de trabajo",
        "explicacion": "Es una plataforma que proporciona una estructura y herramientas para desarrollar aplicaciones, facilitando la creación de software.",
        "ejemplo": 'Django es un framework para desarrollar aplicaciones web en Python.'
    },
}
