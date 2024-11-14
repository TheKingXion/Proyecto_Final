#pablo
diccionario_es = {
    "a": {
        "any": {
            "significado": ": Devuelve True si al menos uno de los elementos de un iterable es verdadero.",
            "uso": "Verificar si alguna condición en un iterable es verdadera.",
            "ejemplo": '''valores = [0, False, 2]
            print(any(valores))  # True'''
        },
        "all": {
            "significado": "Devuelve True si todos los elementos de un iterable son verdaderos.",
            "uso": "Verificar si todas las condiciones en un iterable son verdaderas.",
            "ejemplo": '''valores = [1, 2, 3]
            print(all(valores))  # True'''
        },
         "abs": {
            "significado":" Devuelve el valor absoluto de un número.",
            "uso": " sirve para obtener el valor absoluto de un número.",
            "ejemplo": '''abs(-5)  # 5'''
    },
    },
    "b": {
       "break": {
            "significado":" Termina un bucle de forma anticipada.",
            "uso": "Para salir de un bucle antes de que termine de iterar todos los elementos.",
            "ejemplo":'''while True:
            numero = int(input("Introduce un número (ingresa 0 para salir): "))
            if numero == 0:
            break  # Salir del bucle si el número es 0
            print(f"El número ingresado es {numero}")'''
        },
    },
    "c": {
        "_constains_": {
            "significado": " Define cómo se verifica si un objeto contiene otro (para el operador in).",
            "uso": " Personalizar el comportamiento del operador in cuando se usa con un objeto de una clase definida por el usuario.",
            "ejemplo": '''class Caja:
            def __init__(self, elementos):
            self.elementos = elementos
            def __contains__(self, item):
            return item in self.elementos
            caja = Caja([1, 2, 3])
            print(2 in caja)  # True'''
        },
        "count": {
            "significado":" Devuelve el número de veces que un elemento aparece en una lista o cadena.",
            "uso": " Contar las apariciones de un valor en una colección.",
            "ejemplo": '''lista = [1, 2, 2, 3, 2, 4]
            print(lista.count(2))  # 3'''
        },
     },
     "clear": {
            "significado":" Elimina todos los elementos de una lista o un diccionario.",
            "uso": " Vaciar el contenido de una colección.",
            "ejemplo": '''lista = [1, 2, 3]
            lista.clear()
            print(lista)  # []'''
    },
    "d": {
        "del": {
            "significado": "Elimina un objeto o variable.",
            "uso": "Borrar un objeto, variable o elemento de una colección.",
            "ejemplo": '''lista = [1, 2, 3]
            del lista[0]
            print(lista)  # [2, 3]'''
        },
        "datetime": {
            "significado":" El módulo datetime permite trabajar con fechas y horas.",
            "uso": "Se usa para manipular, comparar y formatear fechas y horas.",
            "ejemplo": '''import datetime
            ahora = datetime.datetime.now()
            print(ahora)  # 2024-11-14 12:30:45.123456
            fecha_formateada = ahora.strftime("%d/%m/%Y %H:%M")
            print(fecha_formateada)  # 14/11/2024 12:30'''
    },
    },
    "e": {
        "enumerate": {
            "significado":" Devuelve un objeto enumerado, es decir, un índice y su valor.",
            "uso": " sirve para obtener tanto el índice como el valor de un iterable en un bucle.",
            "ejemplo": '''for idx, val in enumerate(["a", "b", "c"]):
            print(idx, val)'''
    },
    },
    "f": {
         "format": {
            "significado": "Permite insertar valores dentro de una cadena de texto de manera más legible y flexible.",
            "uso": " Sirve para formatear cadenas de manera dinámica, insertando valores en lugares específicos.",
            "ejemplo": '''nombre = "Juan"
            edad = 30
            mensaje = "Hola, mi nombre es {} y tengo {} años.".format(nombre, edad)
            print(mensaje)  # "Hola, mi nombre es Juan y tengo 30 años."'''
        },
        "float": {
            "significado":"  Convierte una cadena a un número real .",
            "uso": " sirve para convertir cadenas numéricas en valores de tipo float.",
            "ejemplo": '''float("10.5")  # 10.5'''
    },
        "filter": {
            "significado":"  filter() permite filtrar elementos de un iterable utilizando una función que retorna True o False.",
            "uso": " Se utiliza para obtener elementos de una lista o secuencia que cumplan con una condición específica.",
            "ejemplo": '''# Función para verificar si un número es par
            def es_par(num):
            return num % 2 == 0
            numeros = [1, 2, 3, 4, 5, 6]
            pares = filter(es_par, numeros)
            print(list(pares))  # [2, 4, 6]'''
    },
    },
    "g": {
        # Aquí puedes agregar funciones que comiencen con la letra G
    },
    "h": {
        # Aquí puedes agregar funciones que comiencen con la letra H
    },
    "i": {
        "if": {
            "significado": "Condición que se evalúa como verdadera o falsa.",
            "uso": "Usado para tomar decisiones en el flujo de un programa.",
            "ejemplo": "si x > 10: print('Mayor que 10')"
        },
        "input": {
            "significado":"Lee los datos ingresados por el usuario en la consola",
            "uso": "Sirve para interactuar con el usuario y obtener información.",
            "ejemplo": "input('ingrese un número')"
        },
        "_init_": {
            "significado": "Es un método especial en las clases de Python que se llama cuando se crea una nueva instancia de la clase.",
            "uso": " Para inicializar los atributos del objeto.",
            "ejemplo": '''class Persona:
            def __init__(self, nombre, edad):
            self.nombre = nombre
            self.edad = edad'''
        },
        "index": {
            "significado":"Devuelve el índice de la primera aparición de un valor en una lista o cadena.",
            "uso": " Buscar la posición de un elemento dentro de un iterable.",
            " ejemplo": '''lista = [10, 20, 30, 40]
            print(lista.index(30))  # 2'''
        },
        "int": {
            "significado":" Convierte una cadena a un entero.",
            "uso": " sirve para convertir cadenas numéricas en valores enteros.",
            "ejemplo": '''int("10")  # 10'''
    },
    },
    "j": {
        "join": {
            "significado": "Une los elementos de un iterable en una cadena, utilizando un delimitador específico.",
            "uso": "Combinar elementos de una lista o tupla en una sola cadena.",
            "ejemplo": '''palabras = ["Hola", "mundo"]
            resultado = " ".join(palabras)
            print(resultado)  '''
        },
    },
    "k": {
        # Aquí puedes agregar funciones que comiencen con la letra K
    },
    "l": {
        "len()": {
            "significado": "Devuelve la longitud de un objeto (como una lista o cadena).",
            "usage": "Usado para contar elementos en una secuencia.",
            "ejemplo": '''lista = [1, 2, 3, 4]
            print(len(lista))  # 4'''
        },

    },
    "m": {
        "max": {
            "significado": "Devuelve el valor más grande de un iterable.",
            "usage": "Encontrar el valor máximo.",
            "ejemplo": '''max([1, 2, 3])  # 3'''
        },
        "map": {
            "significado":"  Aplica una función a cada elemento de un iterable.",
            "uso": "  sirve para  aplicar una operación a todos los elementos de un iterable..",
            "ejemplo": '''map(lambda x: x * 2, [1, 2, 3])  # [2, 4, 6]'''
    },
        "namedtuple": {
            "significado":"   namedtuple es una clase de collections que permite crear tuplas con nombres de campos, mejorando la legibilidad del código.",
            "uso": " Se utiliza para almacenar datos que pueden ser tratados como una tupla pero con un acceso más legible a sus elementos por nombre.",
            "ejemplo": '''from collections import namedtuple
            Punto = namedtuple('Punto', ['x', 'y'])
            p = Punto(x=10, y=20)
            print(p.x, p.y)  # 10 20'''
    },
    },
    "n": {
        # Aquí puedes agregar funciones que comiencen con la letra N
    },
    "o": { 
         "os": {
            "significado":"   El módulo os permite interactuar con el sistema operativo, como manipular archivos, directorios, obtener información sobre el sistema, etc.",
            "uso": "Es útil para realizar operaciones de bajo nivel en el sistema, como navegar por directorios o eliminar archivos.",
            "ejemplo": '''import os
            directorio_actual = os.getcwd()
            print(f"Directorio actual: {directorio_actual}")
            os.mkdir("nuevo_directorio")
            archivos = os.listdir(directorio_actual)
            print(f"Archivos en el directorio: {archivos}")
            os.rmdir("nuevo_directorio")'''
        }, 
    },
    "p": {
        "pop": {
            "significado":"Elimina y devuelve un elemento de una lista en un índice específico.",
            "uso": "Sirve Para quitar un valor específico de una lista.",
            "ejemplo": '''frutas = ["manzana", "banana", "naranja", "pera"]
            ultima_fruta = frutas.pop()
            print("Última fruta eliminada:", ultima_fruta)  # Salida: pera
            print("Lista después del pop:", frutas)  # Salida: ['manzana', 'banana', 'naranja']'''
        },
         "parseInt": {
            "significado":"   Convierte una cadena en un número entero.",
            "uso": " Usado para convertir cadenas de texto que representan números en valores enteros.",
            "ejemplo": '''parseInt("10");  // 10'''
        }, 
         "pathlib": {
            "significado":" pathlib es un módulo que facilita el manejo de rutas de archivos y directorios de manera más legible y moderna.",
            "uso": "  Se utiliza para manejar las rutas de manera más sencilla y para realizar operaciones de archivo de forma eficiente.",
            "ejemplo": '''from pathlib import Path
            ruta = Path("mi_directorio/mi_archivo.txt")
            if ruta.exists():
            print(f"El archivo {ruta} existe.")
            else:
            print(f"El archivo {ruta} no existe.")
            Path("nuevo_directorio").mkdir(parents=True, exist_ok=True)
            contenido = ruta.read_text()
            print(contenido)'''
    },
    },
    "q": {
        # Aquí puedes agregar funciones que comiencen con la letra Q
    },
    "r": {
        "range": {
            "significado": "Devuelve una secuencia de números, generalmente usada en bucles.",
            "uso": " Sirve Para crear un rango de números que se puede iterar",
            "ejemplo": '''for i in range(5):
            print(i)'''
        },
        "reversed": {
            "significado": "Devuelve el iterable invertido.",
            "uso": " Sirve Para invertir el orden de los elementos de un iterable.",
            "ejemplo": '''reversed([1, 2, 3])  # [3, 2, 1]'''
        },
        "ramdon": {
            "significado": "El módulo random permite generar números aleatorios o elegir elementos aleatorios de una secuencia.",
            "uso": " Es útil para simulaciones, juegos, y cuando necesitas valores aleatorios.",
            "ejemplo": '''import random
            numero = random.randint(1, 10)
            print(f"Número aleatorio: {numero}")
            colores = ["rojo", "azul", "verde", "amarillo"]
            color_elegido = random.choice(colores)
            print(f"Color elegido: {color_elegido}")
            random.shuffle(colores)
            print(f"Colores barajados: {colores}")'''
         },
    },
    "s": {
         "str": {
            "significado": " Convierte un valor en una cadena de texto.",
            "uso": " Sirve para separar una cadena usando un delimitador.",
            "ejemplo":''' # Número entero
            numero = 123
            numero_como_str = str(numero)
            print(type(numero_como_str))  # Salida: <class 'str'>
            print(numero_como_str)        # Salida: '123'''
        },
        "split": {
            "significado":"Divide una cadena en una lista de subcadenas..",
            "uso": " Es el primer parámetro de cualquier método de instancia de una clase.",
            "ejemplo": '''texto = "Hola Mundo Python"
            palabras = texto.split()
            print(palabras)'''
    },
        "sorted": {
            "significado":"Devuelve una lista nueva con los elementos de un iterable ordenados.",
            "uso": "  Ordenar una lista o tupla de manera ascendente o descendente.",
            "ejemplo": '''lista = [4, 1, 3, 2]
            print(sorted(lista))  # [1, 2, 3, 4]'''
    },
        "sum ": {
            "significado":" Devuelve la suma de los elementos de un iterable.",
            "uso": " Sumar los elementos de una lista o tupla.",
            "ejemplo": '''sum([1, 2, 3])  # 6'''
    },
      " shutil": {
            "significado":"   shutil es un módulo que proporciona una manera de copiar, mover o eliminar archivos y directorios.",
            "uso": "Se utiliza para operaciones de alto nivel con archivos y directorios, como copiar un archivo o mover un directorio completo.",
            "ejemplo": '''pimport shutil
            shutil.copy("origen.txt", "destino.txt")
            shutil.move("origen.txt", "nuevo_directorio/origen.txt")
            shutil.remove("destino.txt")'''
        },
    },
    "t": {
         
        "type": {
            "significado":" Devuelve el tipo de un objeto.",
            "uso": "  sirve para verificar el tipo de una variable.",
            "ejemplo": '''type(10)  # <class 'int'>'''
    },
        "time": {
            "significado":" El módulo time permite trabajar con el tiempo y medir el tiempo de ejecución de bloques de código.",
            "uso": "  Se utiliza para realizar mediciones de rendimiento o simplemente para trabajar con tiempos.",
            "ejemplo": '''import time
            inicio = time.time()
            suma = sum(range(1, 1000000))
            fin = time.time()
            print(f"Tiempo de ejecución: {fin - inicio} segundos.")'''
    },
    },
    "u": {
        # Aquí puedes agregar funciones que comiencen con la letra U
    },
    "v": {
        # Aquí puedes agregar funciones que comiencen con la letra V
    },
    "w": {
        # Aquí puedes agregar funciones que comiencen con la letra W
    },
    "x": {
        # Aquí puedes agregar funciones que comiencen con la letra X
    },
    "y": {
        # Aquí puedes agregar funciones que comiencen con la letra Y
    },
    "z": {
         "zip": {
            "significado":" Une varios iterables en una sola secuencia de tuplas.   ",
            "uso": " Combina listas o tuplas de manera que sus elementos estén emparejados.",
            "ejemplo": '''zip([1, 2], ["a", "b"])  # [(1, "a"), (2, "b")]'''
        },
    }, 
}