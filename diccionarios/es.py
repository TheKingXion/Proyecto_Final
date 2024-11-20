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
        "bytes": {
            "significado": "Devuelve un objeto bytes inmutable de secuencia de bytes.",
            "uso": " Trabajar con datos binarios inmutables.",
            "ejemplo": '''b = bytes([65, 66, 67])
            print(b)  # Resultado: b'ABC'''
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
        "clear": {
            "significado":" Elimina todos los elementos de una lista o un diccionario.",
            "uso": " Vaciar el contenido de una colección.",
            "ejemplo": '''lista = [1, 2, 3]
            lista.clear()
            print(lista)  # []'''
        },
     },
    "d": {
        "del": {
            "significado": "Elimina un objeto o variable.",
            "uso": "Borrar un objeto, variable o elemento de una colección.",
            "ejemplo": '''lista = [1, 2, 3]
            del lista[0]
            print(lista)  # [2, 3]'''
        },
    },
    "e": {
        "enumerate": {
            "significado":" Devuelve un objeto enumerado, es decir, un índice y su valor.",
            "uso": " sirve para obtener tanto el índice como el valor de un iterable en un bucle.",
            "ejemplo": '''for idx, val in enumerate(["a", "b", "c"]):
            print(idx, val)'''
        },
        "except": {
            "significado": "Error o evento inesperado que interrumpe el flujo normal del programa.",
            "uso": " Manejar errores y situaciones imprevistas.",
            "ejemplo": '''try:
            resultado = 10 / 0
            except ZeroDivisionError:
            print("No se puede dividir por cero")'''
        },
        "extend": {
            "significado": " Agrega los elementos de un iterable al final de una lista.",
            "uso": "  Ampliar una lista con los elementos de otra lista o iterable.",
            "ejemplo": '''lista = [1, 2]
            lista.extend([3, 4])
            print(lista)  # Resultado: [1, 2, 3, 4]'''
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
        "find": {
            "significado":"  se refiere a la definición o concepto de algo dentro del lenguaje de programación .",
            "uso": " se refiere a cómo se implementa o emplea un concepto dentro de un programa.",
            "ejemplo": '''def sumar(a, b):
            return a + b
            resultado = sumar(3, 4)
            print(resultado)  # Esto imprimirá 7'''
        },
        "formatting": {
            "significado":"  Proceso de dar formato a la salida de texto. .",
            "uso": " se utiliza principalmente para insertar variables o valores en cadenas de texto con un formato específico.",
            "ejemplo": '''nombre = "Juan"
            edad = 30
            print("Mi nombre es %s y tengo %d años." % (nombre, edad))
            # Resultado: Mi nombre es Juan y tengo 30 años.'''
        },
        "flush_output": {
            "significado":"  Forza la escritura de datos en la salida estándar.",
            "uso": "El uso de flush() es común cuando se trabaja con archivos, terminales o cualquier tipo de flujo de salida",
            "ejemplo": '''with open("mi_archivo.txt", "w") as archivo:
            archivo.write("Este es un mensaje importante.")
            archivo.flush()  # Asegura que se escriba de inmediato'''
        },
        "function_definition": {
            "significado":"  La forma en que se define una función en Python.",
            "uso": " implica declarar un bloque de código que realiza una tarea específica. ",
            "ejemplo": '''def sumar(a, b):
            return a + b
            # Llamada a la función
            resultado = sumar(3, 5)
            print(resultado)  # Resultado: 8'''
        },
        "filepath": {
            "significado":"Ruta que especifica la ubicación de un archivo en el sistema de archivos. ",
            "uso": "  es la dirección o localización de un archivo en el sistema de archivos.",
            "ejemplo": '''archivo = open("archivo.txt", "r")
            contenido = archivo.read()
            print(contenido)
            archivo.close()'''
        },
    },
    "g": {
       "global": {
            "significado":" Variable que se define fuera de todas las funciones y clases.",
            "uso": " Hacer que una variable sea accesible desde cualquier parte del código.",
            "ejemplo": '''x = 10
            def funcion():
            global x
            x = 20'''
        },
         "get": {
            "significado":" Devuelve el valor de una clave en un diccionario, o un valor predeterminado si la clave no existe.",
            "uso": " utilizado como un método o función que se utiliza para obtener el valor de un objeto,",
            "ejemplo": '''import requests
            # Realizar una solicitud GET a una API
            response = requests.get("https://jsonplaceholder.typicode.com/posts")

            # Verificar el código de estado de la respuesta
            if response.status_code == 200:
            # Convertir la respuesta en formato JSON
            data = response.json()
            print(data)  # Muestra los datos obtenidos de la API
            else:
            print("Error al hacer la solicitud.")'''
        },
         "generator": {
            "significado":" Función que devuelve un iterador que genera valores uno a uno usando yield..",
            "uso": "  es una función especial que permite crear un iterador de manera más eficiente. ",
            "ejemplo": '''def contar():
            yield 1
            yield 2
            yield 3
            # Crear un generador
            gen = contar()
            # Obtener valores del generador usando next()
            print(next(gen))  # Resultado: 1
            print(next(gen))  # Resultado: 2
            print(next(gen))  # Resultado: 3'''
        },
         "git": {
            "significado":"  Sistema de control de versiones utilizado para el seguimiento de cambios en el código.",
            "uso": " es un sistema de control de versiones distribuido que permite a los desarrolladores realizar un seguimiento de los cambios en el código fuente a lo largo del tiempo.",
            "ejemplo": '''git init
            git add .
            git commit -m "Primer commit"
            git push origin main'''
        },
         "gui": {
            "significado":"  Interfaz gráfica de usuario.",
            "uso": "se refiere a una forma de interacción con el software mediante elementos visuales como ventanas, botones, iconos, menús y otros controles gráficos,",
            "ejemplo": '''import tkinter as tk
            def saludar():
            label.config(text="¡Hola, Mundo!")
            ventana = tk.Tk()
            boton = tk.Button(ventana, text="Haz clic aquí", command=saludar)
            boton.pack()
            label = tk.Label(ventana, text="")
            label.pack()
            ventana.mainloop()'''
        },
         "guess_language": {
            "significado":" Intenta determinar el idioma de un texto.",
            "uso": " se refiere a una función o herramienta utilizada para adivinar o detectar el idioma de un texto o una cadena de caracteres.",
            "ejemplo": '''from langdetect import detect
            texto = "Hola, ¿cómo estás?"
            idioma = detect(texto)
            print(f"El idioma detectado es: {idioma}")  # Resultado: es'''
        },
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
        "issubclass": {
            "significado":" Verifica si una clase es una subclase de otra clase.",
            "uso": " Comprobar la relación de herencia entre clases.",
            "ejemplo": '''class Animal:
            pass
            class Perro(Animal):
            pass
            print(issubclass(Perro, Animal))  # Resultado: True'''
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
        "lambda": {
            "significado":"Función anónima (sin nombre) que se puede definir en una sola línea.",
            "uso": "  Definir funciones simples para usar en una sola expresión.",
            "ejemplo": '''cuadrado = lambda x: x**2
            print(cuadrado(4))  # Imprime 16'''
        },
        "locals()": {
            "significado": "Devuelve un diccionario que representa el espacio de nombres local actual.",
            "uso": "  Obtener el contexto local de las variables dentro de una función o módulo.",
            "ejemplo": '''def ejemplo():
            b = 20
            print(locals())  # Resultado: {'b': 20}
            ejemplo()'''
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
        "ord": {
            "significado": " Convierte un carácter a su código ASCII.",
            "usage": "Obtener el valor numérico de un carácter.",
            "ejemplo": '''ord('A')  # Resultado: 65'''
        },
         "open()": {
            "significado": "Abre un archivo y lo devuelve como un objeto de archivo.",
            "uso": " Leer o escribir archivos.",
            "ejemplo": '''archivo = open("ejemplo.txt", "w")
            archivo.write("Hola Mundo")
            archivo.close()'''
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
        "reduce()": {
            "significado":" La función reduce() aplica una función acumulativa a los elementos de un iterable, reduciéndolo a un solo valor.",
            "uso": " Se usa para realizar operaciones acumulativas, como sumar o multiplicar todos los elementos de una lista.",
            "ejemplo": '''from functools import reduce
            numeros = [1, 2, 3, 4]
            resultado = reduce(lambda x, y: x + y, numeros)
            print(resultado)  # 10'''
        },
        "return": {
            "significado": "Valor que una función devuelve a quien la invoca.",
            "uso": " Obtener el resultado de la ejecución de una función.",
            "ejemplo": '''def multiplicar(a, b):
            return a * b
            resultado = multiplicar(3, 4)'''
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
        "super() ": {
            "significado":" El uso de super() permite llamar a un método de la clase base desde una clase derivada..",
            "uso": " Se usa cuando una clase hija necesita extender o modificar el comportamiento de un método de la clase base.",
            "ejemplo": '''class Animal:
            def hablar(self):
            return "El animal hace un sonido."
            class Perro(Animal):
            def hablar(self):
            return super().hablar() + " y el perro ladra."
            mi_perro = Perro()
            print(mi_perro.hablar())  # El animal hace un sonido. y el perro ladra.'''
        },
        
    },
    "t": {
         
        "type": {
            "significado":" Devuelve el tipo de un objeto.",
            "uso": "  sirve para verificar el tipo de una variable.",
            "ejemplo": '''type(10)  # <class 'int'>'''
        },
    },
    "u": {
        # Aquí puedes agregar funciones que comiencen con la letra U
    },
    "v": {
        # Aquí puedes agregar funciones que comiencen con la letra V
    },
    "w": {
       "with": {
            "significado":"Usado para manejar recursos como archivos, bases de datos, conexiones de red, etc., de manera eficiente.",
            "uso": "  Se asegura de que los recursos sean cerrados correctamente, incluso si ocurre una excepción.",
            "ejemplo": '''try:
            with open("archivo.txt", "r") as archivo:
            contenido = archivo.read()
            print(contenido)
            except FileNotFoundError:
            print("El archivo no existe")'''
        },
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