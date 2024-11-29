#pablo
diccionario_es = {
    "a": {
        "abs": {
            "significado": "Devuelve el valor absoluto de un número.",
            "uso": "Se usa para obtener la magnitud de un número sin considerar su signo.",
            "ejemplo": '''
                numero1 = -10
                print(abs(numero1))  # Salida: 10
                '''
        },
        "absolute_import": {
            "significado": "Directiva utilizada para habilitar importaciones absolutas en Python 2.x y versiones posteriores.",
            "uso": "Se usa para evitar conflictos entre módulos locales y globales.",
            "ejemplo": '''
                from __future__ import absolute_import

                # Siempre importa el módulo global, no uno local con el mismo nombre
                import math
                '''
        },
        "add": {
            "significado": "Método utilizado para agregar un elemento a un conjunto o realizar una suma entre matrices (dependiendo del contexto).",
            "uso": "Se usa en conjuntos para agregar elementos o en NumPy para realizar operaciones matemáticas.",
            "ejemplo": '''
                # Conjuntos
                conjunto = {1, 2, 3}
                conjunto.add(4)
                print(conjunto)  # Salida: {1, 2, 3, 4}

                # NumPy
                import numpy as np
                resultado = np.add(2, 3)
                print(resultado)  # Salida: 5
                '''
        },
        "all": {
            "significado": "Devuelve True si todos los elementos de un iterable son verdaderos (o si el iterable está vacío).",
            "uso": "Se usa para verificar si todos los valores de un iterable cumplen con una condición.",
            "ejemplo": '''
                lista = [True, True, True]
                print(all(lista))  # Salida: True

                numeros = [1, 2, 0]
                print(all(numeros))  # Salida: False (0 es evaluado como False)
                '''
        },
        "allclose": {
            "significado": "Verifica si todos los elementos de dos arrays son aproximadamente iguales.",
            "uso": "Se usa en NumPy para verificar la igualdad de elementos con tolerancia a pequeñas diferencias.",
            "ejemplo": '''
                import numpy as np

                a = [1.0, 2.001]
                b = [1.0, 2.0009]
                print(np.allclose(a, b, atol=0.01))  # Salida: True
                '''
        },
        "allexcept": {
            "significado": "No es un término nativo de Python. Puede referirse a un enfoque lógico que aplica operaciones a todos los elementos, excepto algunos específicos.",
            "uso": "Generalmente implementado manualmente.",
            "ejemplo": '''
                lista = [1, 2, 3, 4]
                resultado = [x for x in lista if x != 2]  # Filtra todos, excepto el 2
                print(resultado)  # Salida: [1, 3, 4]
                '''
        },
        "any": {
            "significado": "Devuelve True si al menos un elemento de un iterable es verdadero (o si el iterable está vacío).",
            "uso": "Se usa para verificar si al menos un valor de un iterable cumple con una condición.",
            "ejemplo": '''
                lista = [False, False, True]
                print(any(lista))  # Salida: True

                numeros = [0, 0, 0]
                print(any(numeros))  # Salida: False
            '''
        },
        "append": {
            "significado": "Agrega un elemento al final de una lista.",
            "uso": "Se usa para agregar nuevos elementos a una lista existente.",
            "ejemplo": '''
                lista = [1, 2, 3]
                lista.append(4)
                print(lista)  # Salida: [1, 2, 3, 4]
            '''
        },
        "apply": {
            "significado": "Método utilizado en pandas para aplicar una función a filas o columnas de un DataFrame.",
            "uso": "Se usa para realizar operaciones personalizadas en filas o columnas.",
            "ejemplo": '''
                import pandas as pd

                datos = pd.DataFrame({'A': [1, 2, 3]})
                datos['B'] = datos['A'].apply(lambda x: x * 2)
                print(datos)
                # Salida:
                #    A  B
                # 0  1  2
                # 1  2  4
                # 2  3  6
                '''
        },
        "argmin": {
            "significado": "Devuelve el índice del valor mínimo en un array o iterable.",
            "uso": "Se usa en bibliotecas como NumPy para localizar el índice del menor valor en estructuras de datos.",
            "ejemplo": '''
                import numpy as np

                numeros = [1, 5, 2, 9, 3]
                print(np.argmin(numeros))  # Salida: 0 (índice del valor 1)
            '''
        },
        "array": {
            "significado": "Es una estructura de datos que contiene múltiples elementos del mismo tipo, comúnmente utilizada en bibliotecas como NumPy.",
            "uso": "Se usa para almacenar y operar eficientemente con grandes cantidades de datos homogéneos.",
            "ejemplo": '''
                import numpy as np

                numeros = np.array([1, 2, 3, 4])
                print(numeros)  # Salida: [1 2 3 4]
            '''
        },
        "args": {
            "significado": "Es un parámetro que permite recibir un número variable de argumentos posicionales en una función.",
            "uso": "Se usa para manejar múltiples argumentos en una función sin especificar cada uno individualmente.",
            "ejemplo": '''
                def suma(*args):
                    return sum(args)

                print(suma(1, 2, 3))  # Salida: 6
            '''
        },
        "arccos": {
            "significado": "Devuelve el arco coseno (en radianes) de un valor.",
            "uso": "Se usa en cálculos trigonométricos con NumPy.",
            "ejemplo": '''
                import numpy as np

                resultado = np.arccos(0.5)
                print(resultado)  # Salida: 1.0471975511965976 (equivalente a π/3)
            '''
        },
        "arcsin": {
            "significado": "Devuelve el arco seno (en radianes) de un valor.",
            "uso": "Se usa en cálculos trigonométricos con NumPy.",
            "ejemplo": '''
                import numpy as np

                resultado = np.arcsin(0.5)
                print(resultado)  # Salida: 0.5235987755982988 (equivalente a π/6)
            '''
        },
        "arctan": {
            "significado": "Devuelve el arco tangente (en radianes) de un valor.",
            "uso": "Se usa en cálculos trigonométricos con NumPy.",
            "ejemplo": '''
                import numpy as np

                resultado = np.arctan(1)
                print(resultado)  # Salida: 0.7853981633974483 (equivalente a π/4)
            '''
        },
        "argparse": {
            "significado": "Módulo de Python usado para gestionar argumentos y opciones de línea de comandos.",
            "uso": "Se usa para crear interfaces de línea de comandos fáciles de usar.",
            "ejemplo": '''
                import argparse

                parser = argparse.ArgumentParser(description='ejemplo de argparse')
                parser.add_argument('--nombre', type=str, help='Tu nombre')
                args = parser.parse_args()
                print(f'Hola, {args.nombre}')
            '''
        },
        "array_like": {
            "significado": "Se refiere a cualquier objeto que pueda ser tratado como un array, como listas, tuplas o arrays de NumPy.",
            "uso": "Se usa como entrada en funciones de NumPy o similares para operaciones con datos.",
            "ejemplo": '''
                import numpy as np

                lista = [1, 2, 3]
                array = np.array(lista)  # lista es array_like
                print(array)  # Salida: [1 2 3]
            '''
        },
        "arange": {
        "significado": "Genera un array con valores igualmente espaciados dentro de un intervalo.",
        "uso": "Se usa en NumPy para crear secuencias numéricas.",
        "ejemplo": '''
            import numpy as np

            resultado = np.arange(0, 10, 2)
            print(resultado)  # Salida: [0 2 4 6 8]
            '''
        },
        "argmax": {
            "significado": "Devuelve el índice del valor máximo en un array o iterable.",
            "uso": "Se usa en bibliotecas como NumPy para localizar el índice del valor más alto en estructuras de datos.",
            "ejemplo": '''
                import numpy as np

                numeros = [1, 5, 2, 9, 3]
                print(np.argmax(numeros))  # Salida: 3 (índice del valor 9)
                '''
        },
        "as": {
            "significado": "Palabra clave usada para asignar un alias a módulos o en declaraciones `with`.",
            "uso": "Facilita la referencia a nombres largos o específicos en el código.",
            "ejemplo": '''
                import numpy as np

                with open('archivo.txt', 'r') as archivo:
                    contenido = archivo.read()
                '''
        },
        "assert": {
            "significado": "Evalúa una expresión y genera una excepción `AssertionError` si la expresión es falsa.",
            "uso": "Se usa para verificar condiciones que deben ser satisfechas durante la ejecución del programa.",
            "ejemplo": '''
                x = 5
                assert x > 0, 'x debe ser mayor que 0'  # No genera error
                assert x < 0, 'x debe ser menor que 0'  # Genera AssertionError
                '''
        },
        "async": {
            "significado": "Define una función asincrónica que puede ser usada con `await`.",
            "uso": "Se usa para implementar programación asincrónica en Python.",
            "ejemplo": '''
                import asyncio

                async def saludo():
                    print('Hola')
                    await asyncio.sleep(1)
                    print('Adiós')

                asyncio.run(saludo())
                '''
        },
        "assertEqual": {
            "significado": "Verifica si dos valores son iguales en una prueba unitaria.",
            "uso": "Se usa en pruebas unitarias para validar la igualdad de valores esperados y reales.",
            "ejemplo": '''
                import unittest

                class Teste(unittest.TestCase):
                    def test_suma(self):
                        self.assertEqual(1 + 1, 2)  # La prueba pasa
                '''
        },
        "assertIsNone": {
            "significado": "Verifica si un valor es None en una prueba unitaria.",
            "uso": "Se usa en pruebas unitarias para validar que un valor sea None.",
            "ejemplo": '''
                import unittest

                class Teste(unittest.TestCase):
                    def test_valor_none(self):
                        self.assertIsNone(None)  # La prueba pasa
                '''
        },
        "assertAlmostEqual": {
            "significado": "Verifica si dos valores son aproximadamente iguales hasta un número específico de decimales en una prueba unitaria.",
            "uso": "Se usa en pruebas unitarias para validar valores con tolerancia a pequeñas diferencias.",
            "ejemplo": '''
                import unittest

                class Teste(unittest.TestCase):
                    def test_aproximacion(self):
                        self.assertAlmostEqual(3.14159, 3.14, places=2)  # La prueba pasa
                '''
        },
        "as_tuple": {
            "significado": "Método que convierte un objeto en una tupla (común en bibliotecas como SymPy).",
            "uso": "Se usa para transformar objetos en representaciones de tuplas.",
            "ejemplo": '''
                from sympy import Point

                p = Point(2, 3)
                print(p.as_tuple())  # Salida: (2, 3)
                '''
        },
        "ascii": {
        "significado": "Devuelve una representación legible de un objeto usando caracteres ASCII.",
        "uso": "Se usa para representar cadenas o caracteres en un formato seguro en ASCII, reemplazando caracteres no ASCII por secuencias de escape.",
        "ejemplo": '''
            texto = "Hola, ¿cómo estás?"
            print(ascii(texto))  # Salida: 'Ol\\xe1, como voc\\xea est\\xe1?'
            '''
        },
        "at": {
            "significado": "Método usado para acceder a elementos específicos en estructuras como DataFrames o arrays (generalmente en pandas).",
            "uso": "Se usa para acceder rápidamente a un valor individual en una posición específica.",
            "ejemplo": '''
                import pandas as pd

                datos = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
                print(datos.at[0, 'A'])  # Salida: 1
                '''
        },
        "attribute": {
            "significado": "Se refiere a una propiedad o característica asociada a un objeto en Python.",
            "uso": "Se usa para acceder o modificar propiedades de objetos creados a partir de clases.",
            "ejemplo": '''
                class Persona:
                    def __init__(self, nombre, edad):
                        self.nombre = nombre
                        self.edad = edad

                p = Persona('Juan', 30)
                print(p.nombre)  # Salida: Juan
                p.edad = 31
                print(p.edad)  # Salida: 31
                '''
        },
        "attributeError": {
            "significado": "Es una excepción que ocurre cuando se intenta acceder o asignar un atributo que no existe.",
            "uso": "Se usa para capturar y manejar errores relacionados con atributos inválidos.",
            "ejemplo": '''
                try:
                    objeto = 5
                    objeto.atributo = 10
                except AttributeError as e:
                    print('Error:', e)
                # Salida: Error: 'int' object has no attribute 'atributo'
                '''
        },
        "atleast_1d": {
            "significado": "Convierte entradas en arrays con al menos una dimensión.",
            "uso": "Se usa en NumPy para garantizar que los datos tengan una dimensión mínima.",
            "ejemplo": '''
                import numpy as np

                resultado = np.atleast_1d(5)
                print(resultado)  # Salida: [5]
                '''
        },
        "atleast_2d": {
            "significado": "Convierte entradas en arrays con al menos dos dimensiones.",
            "uso": "Se usa en NumPy para trabajar con datos en formato de matriz.",
            "ejemplo": '''
                import numpy as np

                resultado = np.atleast_2d([1, 2, 3])
                print(resultado)
                # Salida:
                # [[1 2 3]]
                '''
        },
        "average": {
            "significado": "Calcula la media de los elementos de un array o lista.",
            "uso": "Se usa en NumPy para calcular medias, con la posibilidad de ponderar valores.",
            "ejemplo": '''
                import numpy as np

                valores = [1, 2, 3, 4]
                print(np.average(valores))  # Salida: 2.5
                '''
        },
        "await": {
            "significado": "Se usa para esperar el resultado de una función asincrónica.",
            "uso": "Se utiliza dentro de funciones definidas con `async` para pausar su ejecución hasta que una tarea asincrónica se complete.",
            "ejemplo": '''
                import asyncio

                async def tarea():
                    await asyncio.sleep(1)
                    return 'Tarea completada'

                async def principal():
                    resultado = await tarea()
                    print(resultado)

                asyncio.run(principal())
                '''
        },
    },
    "b": {
        "bin": {
            "significado": "Convierte un número en su representación binaria como una cadena.",
            "uso": "Se utiliza para obtener la representación binaria de un número entero.",
            "ejemplo": '''
                numero = 10
                print(bin(numero))  # Salida: '0b1010'
                '''
        },
        "bool": {
            "significado": "Tipo de dato que representa valores booleanos: True o False.",
            "uso": "Se utiliza para representar y operar con valores de verdad.",
            "ejemplo": '''
                valor = bool(1)
                print(valor)  # Salida: True
                '''
        },
        "break": {
            "significado": "Palabra clave que termina la ejecución de un bucle.",
            "uso": "Se utiliza para salir de un bucle de forma anticipada.",
            "ejemplo": '''
                for i in range(5):
                    if i == 3:
                        break
                    print(i)  # Salida: 0 1 2
                '''
        },
        "bytes": {
            "significado": "Tipo de dato inmutable que representa una secuencia de bytes.",
            "uso": "Se utiliza para trabajar con datos binarios.",
            "ejemplo": '''
                b = bytes([65, 66, 67])
                print(b)  # Salida: b'ABC'
                '''
        },
        "bytearray": {
            "significado": "Tipo de dato mutable que representa una secuencia de bytes.",
            "uso": "Se utiliza para modificar secuencias de bytes.",
            "ejemplo": '''
                b = bytearray([65, 66, 67])
                b[0] = 90
                print(b)  # Salida: bytearray(b'ZBC')
                '''
        },
        "byteswap": {
            "significado": "Método que intercambia el orden de los bytes en un objeto.",
            "uso": "Se utiliza para alterar el orden de los bytes en un tipo de dato numérico.",
            "ejemplo": '''
                import numpy as np

                a = np.array([1, 256], dtype=np.int16)
                a = a.byteswap()
                print(a)  # Salida: [256 1]
                '''
        },
        "buffer": {
            "significado": "Una clase en Python que proporciona una vista de acceso a un área de memoria de un objeto.",
            "uso": "Se utiliza para acceder a la memoria de manera eficiente, especialmente en operaciones con grandes cantidades de datos.",
            "ejemplo": '''
                buffer = memoryview(b'abc')
                print(buffer[0])  # Salida: 97 (equivalente a 'a')
                '''
        },
        "base64": {
            "significado": "Módulo que proporciona funciones para codificar y decodificar datos en base64.",
            "uso": "Se utiliza para representar datos binarios en una cadena de caracteres ASCII.",
            "ejemplo": '''
                import base64

                encoded = base64.b64encode(b'abc')
                print(encoded)  # Salida: b'YWJj'
                '''
        },
        "bitwise_and": {
        "significado": "Operador que realiza una operación AND bit a bit entre dos números.",
        "uso": "Se utiliza para comparar los bits correspondientes de dos números y devolver 1 solo si ambos bits son 1.",
        "ejemplo": '''
            x = 5  # binario: 0101
            y = 3  # binario: 0011
            print(x & y)  # Salida: 1 (binario: 0001)
            '''
        },
        "bitwise_or": {
            "significado": "Operador que realiza una operación OR bit a bit entre dos números.",
            "uso": "Se utiliza para comparar los bits correspondientes de dos números y devolver 1 si al menos uno de los bits es 1.",
            "ejemplo": '''
                x = 5  # binario: 0101
                y = 3  # binario: 0011
                print(x | y)  # Salida: 7 (binario: 0111)
                '''
        },
        "bitwise_xor": {
            "significado": "Operador que realiza una operación XOR bit a bit entre dos números.",
            "uso": "Se utiliza para comparar los bits correspondientes de dos números y devolver 1 si los bits son diferentes.",
            "ejemplo": '''
                x = 5  # binario: 0101
                y = 3  # binario: 0011
                print(x ^ y)  # Salida: 6 (binario: 0110)
                '''
        },
        "bitwise_not": {
            "significado": "Operador que realiza una operación NOT bit a bit sobre un número.",
            "uso": "Se utiliza para invertir todos los bits de un número.",
            "ejemplo": '''
                x = 5  # binario: 0101
                print(~x)  # Salida: -6 (binario: 1010)
                '''
        },
        "binomial": {
            "significado": "Función que calcula el coeficiente binomial (n sobre k).",
            "uso": "Se utiliza para calcular el número de formas de seleccionar k elementos de un conjunto de n elementos.",
            "ejemplo": '''
                from scipy.special import comb

                resultado = comb(5, 2)
                print(resultado)  # Salida: 10.0
                '''
        },
        "binascii": {
            "significado": "Módulo que contiene funciones para convertir entre binario y diferentes representaciones de texto.",
            "uso": "Se utiliza para realizar conversiones entre cadenas de texto y datos binarios.",
            "ejemplo": '''
                import binascii

                encoded = binascii.hexlify(b'abc')
                print(encoded)  # Salida: b'616263'
                '''
        },
        "byteorder": {
            "significado": "Indica el orden de los bytes para representar números en la memoria.",
            "uso": "Se utiliza para manipular la representación de números en sistemas con diferentes arquitecturas.",
            "ejemplo": '''
                import sys

                print(sys.byteorder)  # Salida: 'little' o 'big'
                '''
        },
        "bit_length": {
        "significado": "Devuelve el número de bits necesarios para representar un número en binario.",
        "uso": "Se utiliza para obtener la longitud en bits de un número entero.",
        "ejemplo": '''
            numero = 10
            print(numero.bit_length())  # Salida: 4
            '''
        },
        "breakpoint": {
            "significado": "Una función que establece un punto de interrupción en el código, activando el depurador.",
            "uso": "Se utiliza para pausar la ejecución y entrar en el depurador interactivo.",
            "ejemplo": '''
                def funcion():
                    breakpoint()  # Interrupción aquí
                    print('Hola')
                funcion()
                '''
        },
        "binhex": {
            "significado": "Función para convertir un archivo binario en formato hexadecimal.",
            "uso": "Se utiliza para representar datos binarios en formato legible en hexadecimal.",
            "ejemplo": '''
                import binhex

                with open('archivo.bin', 'rb') as f:
                    binhex.binhex(f, 'archivo.hex')
                '''
        },
        "bitset": {
            "significado": "Estructura de datos que permite almacenar una colección de bits.",
            "uso": "Se utiliza para representar conjuntos de bits y realizar operaciones eficientes sobre ellos.",
            "ejemplo": '''
                # ejemplo no estándar en Python, pero se puede usar el módulo `bitarray` para crear bitsets
                from bitarray import bitarray

                bitset = bitarray('10101')
                print(bitset)  # Salida: bitarray('10101')
                '''
        },
        "broadcast": {
            "significado": "Técnica que permite que arrays de formas diferentes se alineen para realizar operaciones element-wise.",
            "uso": "Se utiliza principalmente en NumPy para operaciones con arrays de tamaños diferentes.",
            "ejemplo": '''
                import numpy as np

                a = np.array([1, 2, 3])
                b = np.array([[1], [2], [3]])
                resultado = a + b
                print(resultado)
                # Salida:
                # [[2 3 4]
                #  [3 4 5]
                #  [4 5 6]]
                '''
        },
        "bitarray": {
            "significado": "Módulo que implementa un tipo de dato eficiente para trabajar con arrays de bits.",
            "uso": "Se utiliza para manipular y gestionar arrays de bits de manera eficiente.",
            "ejemplo": '''
                from bitarray import bitarray

                a = bitarray('10101')
                a.append('1')
                print(a)  # Salida: bitarray('101011')
                '''
        },
        "buffer": {
        "significado": "Una clase en Python que proporciona una vista de acceso a un área de memoria de un objeto.",
        "uso": "Se utiliza para acceder a la memoria de manera eficiente, especialmente en operaciones con grandes cantidades de datos.",
        "ejemplo": '''
            buffer = memoryview(b'abc')
            print(buffer[0])  # Salida: 97 (equivalente a 'a')
            '''
        },
        "bitwise_left_shift": {
            "significado": "Operador que realiza un desplazamiento de bits hacia la izquierda.",
            "uso": "Se utiliza para desplazar los bits de un número hacia la izquierda, multiplicando el valor por potencias de dos.",
            "ejemplo": '''
                x = 5  # binario: 0101
                print(x << 1)  # Salida: 10 (binario: 1010)
                '''
        },
        "bitwise_right_shift": {
            "significado": "Operador que realiza un desplazamiento de bits hacia la derecha.",
            "uso": "Se utiliza para desplazar los bits de un número hacia la derecha, dividiendo el valor por potencias de dos.",
            "ejemplo": '''
                x = 5  # binario: 0101
                print(x >> 1)  # Salida: 2 (binario: 0010)
                '''
        },
        "bz2": {
            "significado": "Módulo que proporciona compresión y descompresión usando el algoritmo bzip2.",
            "uso": "Se utiliza para manipular archivos comprimidos en formato bzip2.",
            "ejemplo": '''
                import bz2

                with bz2.open('archivo.bz2', 'rb') as archivo:
                    contenido = archivo.read()
                    print(contenido)
                '''
        },
        "bool_": {
            "significado": "Tipo de dato de NumPy para valores booleanos, similar a `bool` de Python.",
            "uso": "Se utiliza en operaciones con arrays de NumPy para representar valores booleanos.",
            "ejemplo": '''
                import numpy as np

                valor = np.bool_(True)
                print(valor)  # Salida: True
                '''
        },
    },
    "c": {
        "callable": {
        "significado": "Verifica si un objeto es invocable (como una función o una clase).",
        "uso": "Se utiliza para determinar si un objeto puede ser llamado.",
        "ejemplo": '''
            def funcion():
                return "Hola"

            print(callable(funcion))  # Salida: True
            print(callable(42))  # Salida: False
            '''
        },
        "chr": {
            "significado": "Devuelve el carácter Unicode correspondiente a un número entero.",
            "uso": "Se utiliza para convertir un código Unicode en su representación de carácter.",
            "ejemplo": '''
                print(chr(65))  # Salida: 'A'
                print(chr(8364))  # Salida: '€'
                '''
        },
        "class": {
            "significado": "Palabra clave para definir una clase en Python.",
            "uso": "Se utiliza para crear objetos personalizados con atributos y métodos.",
            "ejemplo": '''
                class Persona:
                    def __init__(self, nombre):
                        self.nombre = nombre

                    def saludar(self):
                        print(f"Hola, mi nombre es {self.nombre}")

                p = Persona("Juan")
                p.saludar()  # Salida: Hola, mi nombre es Juan
                '''
        },
        "classmethod": {
            "significado": "Define un método de clase, que recibe la clase como primer argumento en lugar de una instancia.",
            "uso": "Se utiliza para crear métodos que afectan a la clase en su totalidad.",
            "ejemplo": '''
                class MiClase:
                    contador = 0

                    @classmethod
                    def incrementar(cls):
                        cls.contador += 1

                MiClase.incrementar()
                print(MiClase.contador)  # Salida: 1
                '''
        },
        "compile": {
            "significado": "Compila una cadena de código en un objeto ejecutable de Python.",
            "uso": "Se utiliza para compilar código dinámico a partir de texto o archivos.",
            "ejemplo": '''
                codigo = "print('Hola Mundo')"
                compilado = compile(codigo, '<string>', 'exec')
                exec(compilado)  # Salida: Hola Mundo
                '''
        },
        "complex": {
            "significado": "Crea un número complejo en Python.",
            "uso": "Se utiliza para representar números complejos con parte real e imaginaria.",
            "ejemplo": '''
                c = complex(2, 3)
                print(c)  # Salida: (2+3j)
                print(c.real, c.imag)  # Salida: 2.0 3.0
                '''
        },
        "continue": {
            "significado": "Palabra clave que salta a la siguiente iteración de un bucle.",
            "uso": "Se utiliza para ignorar el resto del código en la iteración actual.",
            "ejemplo": '''
                for i in range(5):
                    if i == 2:
                        continue
                    print(i)  # Salida: 0 1 3 4
                '''
        },
        "copy": {
            "significado": "Crea una copia superficial de un objeto.",
            "uso": "Se utiliza para duplicar estructuras de datos sin duplicar objetos anidados.",
            "ejemplo": '''
                import copy

                lista = [1, 2, [3, 4]]
                copia = copy.copy(lista)
                print(copia)  # Salida: [1, 2, [3, 4]]
                '''
        },
        "coroutine": {
            "significado": "Objeto que representa una función asíncrona suspendida.",
            "uso": "Se utiliza para manejar tareas asíncronas usando `async` y `await`.",
            "ejemplo": '''
                async def tarea():
                    print("Inicio")
                    await asyncio.sleep(1)
                    print("Fin")

                import asyncio
                asyncio.run(tarea())  # Salida: Inicio... Fin
                '''
        },
        "count": {
            "significado": "Devuelve el número de ocurrencias de un elemento en una colección.",
            "uso": "Se utiliza para contar cuántas veces un elemento aparece en una lista o cadena.",
            "ejemplo": '''
                lista = [1, 2, 2, 3]
                print(lista.count(2))  # Salida: 2
                '''
        },
        "clear": {
            "significado": "Elimina todos los elementos de una lista o diccionario.",
            "uso": "Se utiliza para vaciar el contenido de una lista o diccionario.",
            "ejemplo": '''
                lista = [1, 2, 3]
                lista.clear()
                print(lista)  # Salida: []
                '''
        },
        "cmath": {
            "significado": "Módulo que proporciona funciones matemáticas para trabajar con números complejos.",
            "uso": "Se utiliza para realizar operaciones matemáticas en números complejos.",
            "ejemplo": '''
                import cmath

                numero = cmath.sqrt(-1)
                print(numero)  # Salida: 1j
                '''
        },
        "chain": {
            "significado": "Función que combina varios iteradores en uno solo.",
            "uso": "Se utiliza para concatenar múltiples iteradores.",
            "ejemplo": '''
                import itertools

                a = [1, 2, 3]
                b = [4, 5, 6]
                resultado = list(itertools.chain(a, b))
                print(resultado)  # Salida: [1, 2, 3, 4, 5, 6]
                '''
        },
        "csv": {
            "significado": "Módulo para leer y escribir archivos en formato CSV (Comma Separated Values).",
            "uso": "Se utiliza para manipular archivos CSV.",
            "ejemplo": '''
                import csv

                with open('archivo.csv', mode='w', newline='') as archivo:
                    writer = csv.writer(archivo)
                    writer.writerow(['Nombre', 'Edad'])
                    writer.writerow(['Ana', 30])
                '''
        },
        "copyreg": {
            "significado": "Módulo que proporciona funciones para registrar objetos para copias y desacoplamiento.",
            "uso": "Se utiliza para personalizar el comportamiento de copia y almacenamiento de objetos.",
            "ejemplo": '''
                import copyreg

                def crear_persona(nombre, edad):
                    return {'nombre': nombre, 'edad': edad}

                copyreg.pickle(dict, crear_persona)
                '''
        },
        "counter": {
        "significado": "Clase en el módulo `collections` que cuenta elementos hashables en una secuencia.",
        "uso": "Se utiliza para contar la frecuencia de elementos en un iterable.",
        "ejemplo": '''
            from collections import Counter

            contador = Counter([1, 2, 2, 3, 3, 3])
            print(contador)  # Salida: Counter({3: 3, 2: 2, 1: 1})
            '''
        },
        "cProfile": {
            "significado": "Módulo para la medición del rendimiento de programas en Python.",
            "uso": "Se utiliza para hacer perfiles de código y analizar la eficiencia del programa.",
            "ejemplo": '''
                import cProfile

                def funcion():
                    for i in range(1000):
                        pass

                cProfile.run('funcion()')
                '''
        },
        "capitalize": {
            "significado": "Método de cadena que convierte la primera letra en mayúscula y el resto en minúsculas.",
            "uso": "Se utiliza para capitalizar la primera letra de una cadena.",
            "ejemplo": '''
                texto = 'hola mundo'
                print(texto.capitalize())  # Salida: 'Hola mundo'
                '''
        },
        "center": {
            "significado": "Método de cadena que centraliza una cadena dentro de un campo de longitud especificada.",
            "uso": "Se utiliza para alinear texto en el centro de una cadena con relleno.",
            "ejemplo": '''
                texto = 'hola'
                print(texto.center(10, '*'))  # Salida: '**hola****'
                '''
        },
        "ceil": {
            "significado": "Función del módulo `math` que devuelve el entero más cercano mayor o igual a un número dado.",
            "uso": "Se utiliza para redondear un número hacia arriba.",
            "ejemplo": '''
                import math

                numero = 3.4
                print(math.ceil(numero))  # Salida: 4
                '''
        },
        "call": {
            "significado": "Método utilizado para invocar un objeto que es callable, como funciones o clases.",
            "uso": "Se utiliza para llamar un objeto que puede ser ejecutado.",
            "ejemplo": '''
                def saludo():
                    return 'Hola'

                print(callable(saludo))  # Salida: True
                '''
        },
        "clamp": {
            "significado": "Función que restringe un valor dentro de un intervalo especificado.",
            "uso": "Se utiliza para garantizar que un valor permanezca dentro de un intervalo definido.",
            "ejemplo": '''
                def clamp(valor, minimo, maximo):
                    return max(minimo, min(valor, maximo))

                print(clamp(5, 1, 10))  # Salida: 5
                '''
        },
        "choice": {
            "significado": "Función del módulo `random` que selecciona un elemento aleatorio de una secuencia.",
            "uso": "Se utiliza para elegir un valor aleatorio de una lista o secuencia.",
            "ejemplo": '''
                import random

                lista = [1, 2, 3, 4, 5]
                print(random.choice(lista))  # Salida: un valor aleatorio de la lista
                '''
        },
        "collections": {
            "significado": "Módulo que implementa tipos de datos especializados como `Counter`, `deque`, `OrderedDict`, entre otros.",
            "uso": "Se utiliza para trabajar con colecciones de datos de manera eficiente.",
            "ejemplo": '''
                from collections import deque

                cola = deque([1, 2, 3])
                cola.append(4)
                print(cola)  # Salida: deque([1, 2, 3, 4])
                '''
        },
        "compress": {
            "significado": "Función en el módulo `itertools` que permite comprimir elementos de un iterable.",
            "uso": "Se utiliza para filtrar los elementos de un iterable basándose en una condición booleana.",
            "ejemplo": '''
                import itertools

                datos = [1, 2, 3, 4, 5]
                condiciones = [True, False, True, False, True]
                resultado = list(itertools.compress(datos, condiciones))
                print(resultado)  # Salida: [1, 3, 5]
                '''
        },
        "complex_conjugate": {
            "significado": "Método de los números complejos en Python que devuelve el conjugado complejo de un número.",
            "uso": "Se utiliza para obtener el conjugado de un número complejo.",
            "ejemplo": '''
                numero_complejo = 3 + 4j
                print(numero_complejo.conjugate())  # Salida: (3-4j)
                '''
        },
        "ctypes": {
            "significado": "Módulo en Python que permite interactuar con bibliotecas de C y realizar llamadas de funciones de bajo nivel.",
            "uso": "Se utiliza para trabajar con tipos de datos y funciones de bibliotecas externas escritas en C.",
            "ejemplo": '''
                import ctypes

                # Crear una variable de tipo entero
                valor = ctypes.c_int(5)
                print(valor.value)  # Salida: 5
                '''
        },
        "clear_screen": {
        "significado": "Función utilizada para limpiar la pantalla de la consola.",
        "uso": "Se utiliza para remover el contenido visible del terminal o consola.",
        "ejemplo": '''
            import os

            def clear_screen():
                os.system('cls' if os.name == 'nt' else 'clear')

            clear_screen()
            '''
        },
        "call_later": {
            "significado": "Método utilizado para programar la ejecución de una función después de un cierto tiempo.",
            "uso": "Se utiliza en programación asíncrona para ejecutar tareas después de un retraso.",
            "ejemplo": '''
                import asyncio

                async def tarea():
                    print('Tarea ejecutada')

                asyncio.get_event_loop().call_later(2, asyncio.create_task, tarea())
                '''
        },
        "chunk": {
            "significado": "Técnica que divide un iterable en partes más pequeñas o bloques.",
            "uso": "Se utiliza para dividir grandes volúmenes de datos en partes más manejables.",
            "ejemplo": '''
                def chunk(iterable, tamaño):
                    for i in range(0, len(iterable), tamaño):
                        yield iterable[i:i + tamaño]

                lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                for bloque in chunk(lista, 3):
                    print(bloque)  # Salida: [1, 2, 3], [4, 5, 6], [7, 8, 9]
                '''
        },
        "cycle": {
            "significado": "Función en el módulo `itertools` que crea un iterador que repite indefinidamente una secuencia.",
            "uso": "Se utiliza para recorrer un iterable en bucle infinito.",
            "ejemplo": '''
                import itertools

                ciclo = itertools.cycle([1, 2, 3])
                for i in range(6):
                    print(next(ciclo))  # Salida: 1, 2, 3, 1, 2, 3
                '''
        },
        "coerce": {
            "significado": "Función que intenta convertir un valor en un tipo compatible.",
            "uso": "Se utilizaba para forzar la conversión de un valor a un tipo de dato específico.",
            "ejemplo": '''
                # La función coerce fue eliminada en versiones modernas de Python.
                '''
        },
        "current_thread": {
            "significado": "Método del módulo `threading` que devuelve el hilo actual de ejecución.",
            "uso": "Se utiliza para obtener el hilo de ejecución donde el código está siendo ejecutado.",
            "ejemplo": '''
                import threading

                def mostrar_thread():
                    print(threading.current_thread())

                mostrar_thread()
                '''
        },
        "configparser": {
            "significado": "Módulo que permite manipular archivos de configuración, como archivos INI.",
            "uso": "Se utiliza para leer, escribir y modificar archivos de configuración.",
            "ejemplo": '''
                import configparser

                config = configparser.ConfigParser()
                config.read('config.ini')

                print(config['DEFAULT']['color'])  # Salida: rojo
                '''
        },
        "compileall": {
            "significado": "Módulo en Python que compila todos los archivos `.py` en un directorio y sus subdirectorios.",
            "uso": "Se utiliza para compilar código Python a bytecode, lo que puede mejorar el rendimiento de la ejecución.",
            "ejemplo": '''
                import compileall

                compileall.compile_dir('mi_directorio')
                '''
        },
        "copytree": {
            "significado": "Función en el módulo `shutil` que copia un directorio completo, incluyendo su contenido, a otro destino.",
            "uso": "Se utiliza para copiar un directorio y todo su contenido a una nueva ubicación.",
            "ejemplo": '''
                import shutil

                shutil.copytree('origen', 'destino')
                '''
        },
     },
    "d": {
        "def": {
            "significado": "Palabra clave en Python utilizada para definir una función.",
            "uso": "Se utiliza para crear una nueva función con un nombre y un bloque de código.",
            "ejemplo": '''
                def saludo():
                    print('Hola Mundo')

                saludo()  # Salida: Hola Mundo
                '''
        },
        "delattr": {
            "significado": "Función que elimina un atributo de un objeto en Python.",
            "uso": "Se utiliza para eliminar un atributo específico de un objeto.",
            "ejemplo": '''
                class Persona:
                    def __init__(self, nombre):
                        self.nombre = nombre

                p = Persona('Juan')
                delattr(p, 'nombre')
                print(hasattr(p, 'nombre'))  # Salida: False
                '''
        },
        "dataframe": {
            "significado": "Estructura de datos bidimensional en la biblioteca Pandas, similar a una tabla, que permite almacenar datos de diferentes tipos.",
            "uso": "Se utiliza para manipular grandes volúmenes de datos tabulares en Python.",
            "ejemplo": '''
                import pandas as pd

                datos = {'Nombre': ['Juan', 'Ana'], 'Edad': [28, 22]}
                df = pd.DataFrame(datos)
                print(df)
                '''
        },
        "decode": {
            "significado": "Método utilizado para decodificar datos binarios a un formato de texto, generalmente en una codificación como UTF-8.",
            "uso": "Se utiliza para convertir datos binarios en cadenas de texto legibles.",
            "ejemplo": '''
                codificado = b'Hola Mundo'
                decodificado = codificado.decode('utf-8')
                print(decodificado)  # Salida: Hola Mundo
                '''
        },
        "decimal": {
            "significado": "Módulo en Python que proporciona soporte para realizar cálculos con decimales de precisión arbitraria.",
            "uso": "Se utiliza para realizar operaciones aritméticas precisas sin los errores de redondeo típicos de los números de punto flotante.",
            "ejemplo": '''
                from decimal import Decimal

                x = Decimal('0.1')
                y = Decimal('0.2')
                print(x + y)  # Salida: 0.3
                '''
        },
        "device": {
            "significado": "Término general para referirse a cualquier dispositivo de hardware o sistema donde un programa se ejecuta.",
            "uso": "Se utiliza para referirse a dispositivos como computadoras, teléfonos móviles, etc.",
            "ejemplo": "No es un término específico de Python, pero puede ser utilizado en bibliotecas como TensorFlow para referirse a dispositivos de procesamiento como CPU o GPU."
        },
        "dict.get": {
            "significado": "Método de los diccionarios en Python que devuelve el valor de una clave especificada o un valor por defecto si la clave no existe.",
            "uso": "Se utiliza para obtener el valor asociado a una clave sin generar un error si la clave no existe.",
            "ejemplo": '''
                d = {'a': 1, 'b': 2}
                print(d.get('a'))  # Salida: 1
                print(d.get('c', 'No encontrado'))  # Salida: No encontrado
                '''
        },
        "dropna": {
            "significado": "Método en Pandas utilizado para eliminar valores ausentes (NaN) en un DataFrame o Serie.",
            "uso": "Se utiliza para limpiar los datos eliminando las filas o columnas que contienen valores nulos.",
            "ejemplo": '''
                import pandas as pd

                df = pd.DataFrame({'A': [1, 2, None], 'B': [None, 3, 4]})
                print(df.dropna())
                '''
        },
        "dtype": {
            "significado": "Propiedad de los arrays en Numpy o de las columnas en un DataFrame de Pandas que indica el tipo de datos de los elementos.",
            "uso": "Se utiliza para obtener o especificar el tipo de datos de un array o columna.",
            "ejemplo": '''
                import numpy as np

                arr = np.array([1, 2, 3])
                print(arr.dtype)  # Salida: int64
                '''
        },
        "deque.appendleft": {
            "significado": "Método del tipo de dato `deque` en el módulo `collections` que agrega un elemento al inicio de la deque.",
            "uso": "Se utiliza para insertar un nuevo elemento en la parte izquierda de una deque.",
            "ejemplo": '''
                from collections import deque

                d = deque([2, 3, 4])
                d.appendleft(1)
                print(d)  # Salida: deque([1, 2, 3, 4])
                '''
        },
        "dict.update": {
            "significado": "Método de los diccionarios en Python que actualiza un diccionario con los elementos de otro diccionario o iterable.",
            "uso": "Se utiliza para agregar o modificar elementos en un diccionario usando otro diccionario o iterable.",
            "ejemplo": '''
                d1 = {'a': 1, 'b': 2}
                d2 = {'b': 3, 'c': 4}
                d1.update(d2)
                print(d1)  # Salida: {'a': 1, 'b': 3, 'c': 4}
                '''
        },
        "del": {
            "significado": "Palabra clave en Python que elimina un atributo o un elemento de una colección.",
            "uso": "Se utiliza para eliminar elementos de una lista, atributo de un objeto o una variable.",
            "ejemplo": '''
                lista = [1, 2, 3]
                del lista[1]
                print(lista)  # Salida: [1, 3]
                '''
        },
        "dict": {
            "significado": "Tipo de dato en Python que representa un diccionario, una colección de pares clave-valor.",
            "uso": "Se utiliza para almacenar y manipular datos de forma eficiente, asociando claves únicas a valores.",
            "ejemplo": '''
                d = {'a': 1, 'b': 2}
                print(d['a'])  # Salida: 1
                '''
        },
        "dir": {
            "significado": "Función que devuelve una lista de los atributos y métodos de un objeto.",
            "uso": "Se utiliza para obtener información sobre los métodos y atributos disponibles para un objeto o módulo.",
            "ejemplo": '''
                x = [1, 2, 3]
                print(dir(x))
                '''
        },
        "divmod": {
            "significado": "Función que recibe dos números y devuelve una tupla con el cociente y el resto de su división.",
            "uso": "Se utiliza para obtener tanto el cociente como el resto de una división en una única operación.",
            "ejemplo": '''
                resultado = divmod(9, 4)
                print(resultado)  # Salida: (2, 1)
                '''
        },
        "deque": {
            "significado": "Tipo de dato en el módulo `collections` de Python que representa una cola doblemente terminada, permitiendo agregar y eliminar elementos de ambos extremos de manera eficiente.",
            "uso": "Se usa para implementar colas y pilas de manera eficiente.",
            "ejemplo": '''
                from collections import deque

                d = deque([1, 2, 3])
                d.append(4)
                print(d)  # Salida: deque([1, 2, 3, 4])
                '''
        },
        "defaultdict": {
            "significado": "Clase en el módulo `collections` que extiende el diccionario estándar y permite definir un valor por defecto para claves inexistentes.",
            "uso": "Se usa para evitar errores al acceder a claves no existentes, proporcionando un valor por defecto.",
            "ejemplo": '''
                from collections import defaultdict

                d = defaultdict(int)
                d['a'] += 1
                print(d)  # Salida: defaultdict(<class 'int'>, {'a': 1})
                '''
        },
        "decode": {
            "significado": "Método utilizado para convertir datos binarios en texto con una codificación específica.",
            "uso": "Se usa para decodificar una secuencia de bytes en una cadena de texto con una codificación específica.",
            "ejemplo": '''
                codificado = b'Hola Mundo'
                decodificado = codificado.decode('utf-8')
                print(decodificado)  # Salida: Hola Mundo
                '''
        },
        "deflate": {
            "significado": "Algoritmo de compresión de datos sin pérdida, utilizado para reducir el tamaño de los archivos.",
            "uso": "Se usa para comprimir datos en un formato más eficiente.",
            "ejemplo": '''
                import zlib

                datos = b'Hola Mundo'*100
                comprimido = zlib.compress(datos)
                print(comprimido)
                '''
        },
        "deepcopy": {
            "significado": "Función del módulo `copy` que crea una copia profunda de un objeto, es decir, copia todos los elementos del objeto original, incluidos los objetos dentro de objetos.",
            "uso": "Se usa cuando es necesario hacer una copia completa e independiente de un objeto.",
            "ejemplo": '''
                import copy

                lista = [1, [2, 3]]
                copia = copy.deepcopy(lista)
                lista[1][0] = 99
                print(copia)  # Salida: [1, [2, 3]]
                '''
        },
    },
    "e": {
        "enumerate": {
            "significado": "Función incorporada de Python que agrega un contador a un iterable y lo devuelve como un objeto iterable de tuplas.",
            "uso": "Se usa para obtener tanto el índice como el valor de los elementos en un iterable.",
            "ejemplo": '''
                lista = ['a', 'b', 'c']
                for indice, valor in enumerate(lista):
                    print(indice, valor)
                # Salida:
                # 0 a
                # 1 b
                # 2 c
                '''
        },
        "eval": {
            "significado": "Función incorporada de Python que evalúa una cadena de código como una expresión Python.",
            "uso": "Se usa para ejecutar expresiones Python contenidas en una cadena y devolver el resultado.",
            "ejemplo": '''
                x = 2
                resultado = eval('x + 1')
                print(resultado)  # Salida: 3
                '''
        },
        "exec": {
            "significado": "Función incorporada de Python que ejecuta una cadena de código como un bloque de código completo.",
            "uso": "Se usa para ejecutar código Python dinámicamente.",
            "ejemplo": '''
                codigo = 'for i in range(3): print(i)'
                exec(codigo)
                # Salida:
                # 0
                # 1
                # 2
                '''
        },
        "except": {
            "significado": "Palabra clave en Python usada para manejar excepciones dentro de un bloque try-except.",
            "uso": "Se usa para capturar y manejar excepciones que ocurren en el bloque try.",
            "ejemplo": '''
                try:
                    x = 1 / 0
                except ZeroDivisionError:
                    print('Error: División por cero')
                # Salida: Error: División por cero
                '''
        },
        "else": {
            "significado": "Palabra clave en Python usada en estructuras de control condicional (if, try) para ejecutar un bloque de código si la condición no se cumple o no ocurre ninguna excepción.",
            "uso": "Se usa para ejecutar un bloque de código cuando la condición no se cumple o no ocurre ninguna excepción.",
            "ejemplo": '''
                if 3 > 1:
                    print('Condición verdadera')
                else:
                    print('Condición falsa')
                # Salida: Condición verdadera
                '''
        },
        "elif": {
            "significado": "Palabra clave en Python usada en estructuras condicionales para verificar una condición adicional si las anteriores no se cumplen.",
            "uso": "Se usa para manejar múltiples condiciones en una estructura if-elif-else.",
            "ejemplo": '''
                x = 3
                if x > 5:
                    print('Mayor que 5')
                elif x == 3:
                    print('Igual a 3')
                else:
                    print('Menor que 3')
                # Salida: Igual a 3
                '''
        },
        "exit": {
            "significado": "Función incorporada de Python que finaliza la ejecución del programa.",
            "uso": "Se usa para salir de un programa o cerrar un entorno de ejecución.",
            "ejemplo": '''
                import sys
                sys.exit('Finalizando el programa')
                # El programa se cierra con el mensaje 'Finalizando el programa'
                '''
        },
        "end": {
            "significado": "Palabra clave utilizada en Python para especificar el final de un bloque o la terminación de una cadena.",
            "uso": "Se usa principalmente en las funciones de impresión para controlar el final de la salida.",
            "ejemplo": '''
                print('Hola', end=' ')
                print('Mundo')
                # Salida: Hola Mundo
                '''
        },
        "expandtabs": {
            "significado": "Método de cadenas en Python que reemplaza los caracteres de tabulación por espacios.",
            "uso": "Se usa para alinear texto reemplazando las tabulaciones por un número determinado de espacios.",
            "ejemplo": '''
                texto = 'Hola\tMundo'
                print(texto.expandtabs(4))
                # Salida: Hola   Mundo
                '''
        },
        "encode": {
            "significado": "Método de cadenas en Python que codifica una cadena en una secuencia de bytes usando un codificador específico.",
            "uso": "Se usa para convertir una cadena en una secuencia de bytes para ser almacenada o transmitida en formatos específicos.",
            "ejemplo": '''
                texto = 'Hola Mundo'
                encoded = texto.encode('utf-8')
                print(encoded)
                # Salida: b'Hola Mundo'
                '''
        },
        "element": {
            "significado": "Un elemento individual dentro de una colección o estructura de datos.",
            "uso": "Se usa para referirse a un objeto dentro de una lista, conjunto, diccionario, etc.",
            "ejemplo": '''
                lista = [1, 2, 3]
                print(lista[0])  # Salida: 1
                '''
        },
        "error": {
            "significado": "Condición anómala en la ejecución de un programa que interrumpe su flujo normal.",
            "uso": "Se usa para indicar que algo salió mal durante la ejecución del código.",
            "ejemplo": '''
                try:
                    1 / 0
                except ZeroDivisionError as e:
                    print(f'Error: {e}')
                # Salida: Error: division by zero
                '''
        },
        "exception": {
            "significado": "Evento que altera el flujo normal de ejecución del programa, generalmente debido a un error.",
            "uso": "Se usa para manejar errores en el código y ejecutar acciones específicas cuando ocurren.",
            "ejemplo": '''
                try:
                    int('a')
                except ValueError:
                    print('Error: no se puede convertir a entero')
                # Salida: Error: no se puede convertir a entero
                '''
        },
        "evaluate": {
            "significado": "Ejecutar o calcular el valor de una expresión o función.",
            "uso": "Se usa para obtener el resultado de una expresión.",
            "ejemplo": '''
                x = 5
                resultado = eval('x + 2')
                print(resultado)  # Salida: 7
                '''
        },
        "elements": {
            "significado": "Elementos o componentes individuales dentro de un conjunto o colección.",
            "uso": "Se usa para referirse a las partes de una estructura de datos.",
            "ejemplo": '''
                conjunto = {1, 2, 3}
                for elemento in conjunto:
                    print(elemento)
                # Salida:
                # 1
                # 2
                # 3
                '''
        },
        "exponential": {
            "significado": "Relacionado con la operación matemática de exponenciación, que calcula el valor de una base elevada a un exponente.",
            "uso": "Se usa para realizar cálculos exponenciales.",
            "ejemplo": '''
                import math
                resultado = math.exp(2)
                print(resultado)  # Salida: 7.3890560989306495
                '''
        },
        "enumerations": {
            "significado": "Una lista o conjunto de elementos, muchas veces con un valor asociado o un identificador.",
            "uso": "Se usa para representar un conjunto de valores posibles de una variable.",
            "ejemplo": '''
                from enum import Enum

                class Color(Enum):
                    ROJO = 1
                    VERDE = 2
                    AZUL = 3

                print(Color.ROJO)  # Salida: Color.ROJO
                '''
        },
        "encode_utf8": {
            "significado": "Método de codificación que convierte una cadena de caracteres en una secuencia de bytes usando el formato UTF-8.",
            "uso": "Se usa para convertir texto en una representación binaria usando UTF-8.",
            "ejemplo": '''
                texto = 'Hola Mundo'
                encoded = texto.encode('utf-8')
                print(encoded)  # Salida: b'Hola Mundo'
                '''
        },
        "execfile": {
            "significado": "Función que ejecuta un archivo Python como si fuera un script.",
            "uso": "Se usa para ejecutar un archivo Python externo.",
            "ejemplo": '''
                # Este comando está disponible solo en Python 2
                execfile('script.py')
                '''
        },
        "edit_distance": {
            "significado": "Medida que calcula la diferencia entre dos cadenas basándose en las operaciones necesarias para convertir una en la otra.",
            "uso": "Se usa para comparar cuán similares son dos cadenas y determinar cuántos cambios son necesarios para hacerlas idénticas.",
            "ejemplo": '''
                from nltk.metrics import edit_distance

                distancia = edit_distance('kitten', 'sitting')
                print(distancia)  # Salida: 3
                '''
        },
        "eval_input": {
            "significado": "Función que evalúa una entrada del usuario, normalmente a través de la función `input()`.",
            "uso": "Se usa para obtener y evaluar una entrada proporcionada por el usuario.",
            "ejemplo": '''
                entrada = input('Digite un número: ')
                resultado = eval(entrada)
                print(resultado)
                '''
        },
        "xceed": {
            "significado": "Término usado para describir algo que supera o excede un límite.",
            "uso": "Se usa para describir el acto de ir más allá de un límite o expectativa.",
            "ejemplo": '''
                x = 10
                if x > 5:
                    print('Excedió el límite')
                '''
        },
    },
    "f": {
            "filemode": {
            "significado": "Modo de apertura de un archivo que determina las operaciones que se pueden realizar en él.",
            "uso": "Se utiliza para especificar el tipo de acceso deseado para un archivo (lectura, escritura, etc.).",
            "ejemplo": "archivo = open('archivo.txt', 'r')  # 'r' indica modo de solo lectura\nprint(archivo.mode)  # Salida: 'r'"
        },
        "frozen_set": {
            "significado": "Conjunto inmutable en Python, similar a un conjunto estándar, pero sin la posibilidad de modificarlo después de su creación.",
            "uso": "Se utiliza para crear conjuntos que no deben ser modificados después de su creación.",
            "ejemplo": "conjunto = frozenset([1, 2, 3])\nprint(conjunto)  # Salida: frozenset({1, 2, 3})"
        },
        "format_map": {
            "significado": "Método que devuelve una cadena formateada usando un diccionario u objeto similar.",
            "uso": "Se utiliza para realizar sustituciones de valores en una cadena usando un mapa (como un diccionario).",
            "ejemplo": "datos = {'nombre': 'Juan', 'edad': 30}\ntexto = 'Nombre: {nombre}, Edad: {edad}'.format_map(datos)\nprint(texto)  # Salida: Nombre: Juan, Edad: 30"
        },
        "find": {
            "significado": "Método que busca una subcadena dentro de una cadena y devuelve el índice de la primera ocurrencia.",
            "uso": "Se utiliza para encontrar la posición de un texto dentro de otro.",
            "ejemplo": "texto = 'Hola Mundo'\nprint(texto.find('Mundo'))  # Salida: 5"
        },
        "float32": {
            "significado": "Tipo de dato en NumPy que representa un número de punto flotante de 32 bits.",
            "uso": "Se utiliza para almacenar números con decimales de manera más eficiente en términos de memoria.",
            "ejemplo": "import numpy as np\nnumero = np.float32(3.1415)\nprint(numero)  # Salida: 3.1415"
        },
        "float64": {
            "significado": "Tipo de dato en NumPy que representa un número de punto flotante de 64 bits.",
            "uso": "Se utiliza para almacenar números con decimales con mayor precisión que el tipo float32.",
            "ejemplo": "import numpy as np\nnumero = np.float64(3.141592653589793)\nprint(numero)  # Salida: 3.141592653589793"
        },
        "formatting": {
            "significado": "El proceso de aplicar un formato a datos o cadenas, como alineación, anchos y tipos de datos.",
            "uso": "Se utiliza para organizar o mostrar datos de forma más legible o específica.",
            "ejemplo": "texto = 'Nombre: {0:10}, Edad: {1:5}'.format('Juan', 30)\nprint(texto)  # Salida: Nombre: Juan      , Edad: 30"
        },
        "flush_output": {
            "significado": "Método utilizado para vaciar el búfer de salida, forzando que los datos se escriban inmediatamente.",
            "uso": "Se utiliza cuando se quiere garantizar que todos los datos pendientes en el búfer de salida se escriban en el destino.",
            "ejemplo": "import sys\nsys.stdout.write('Hola Mundo')\nsys.stdout.flush()  # Salida: 'Hola Mundo' inmediatamente"
        },
        "function_definition": {
            "significado": "El proceso de crear una función en Python usando la palabra clave 'def'.",
            "uso": "Se utiliza para declarar funciones reutilizables que ejecutan un bloque de código específico.",
            "ejemplo": "def saludar(nombre):\n    return f'Hola {nombre}'\nprint(saludar('Juan'))  # Salida: Hola Juan"
        },
        "filepath": {
            "significado": "Ruta o dirección de un archivo en el sistema de archivos.",
            "uso": "Se utiliza para especificar la ubicación de un archivo en el sistema de archivos.",
            "ejemplo": "import os\ncamino = os.path.join('carpeta', 'archivo.txt')\nprint(camino)  # Salida: carpeta/archivo.txt"
        },
        "flask": {
            "significado": "Un micro-framework en Python para el desarrollo de aplicaciones web.",
            "uso": "Se utiliza para crear aplicaciones web de manera sencilla y rápida con rutas, formularios y otras funcionalidades.",
            "ejemplo": "from flask import Flask\napp = Flask(__name__)\n\n@app.route('/')\ndef hola():\n    return 'Hola Mundo'\n\napp.run()  # Salida: 'Hola Mundo' en una aplicación web"
        },
        "filtering": {
            "significado": "Proceso de seleccionar elementos de una colección que cumplen con una condición específica.",
            "uso": "Se utiliza para extraer elementos de una lista, conjunto o cualquier iterable basándose en una condición.",
            "ejemplo": "lista = [1, 2, 3, 4, 5]\nresultado = filter(lambda x: x > 2, lista)\nprint(list(resultado))  # Salida: [3, 4, 5]"
        },
        "futures": {
            "significado": "Módulo que proporciona una interfaz para ejecutar tareas asincrónicas y paralelizadas.",
            "uso": "Se utiliza para ejecutar funciones de manera concurrente usando hilos o procesos.",
            "ejemplo": "from concurrent.futures import ThreadPoolExecutor\n\ndef tarea(x):\n    return x * x\n\nwith ThreadPoolExecutor() as executor:\n    resultados = executor.map(tarea, [1, 2, 3])\n    print(list(resultados))  # Salida: [1, 4, 9]"
        },
        "fold": {
            "significado": "Función que aplica una operación acumulativa sobre los elementos de una secuencia.",
            "uso": "Se utiliza para reducir una secuencia de elementos a un único valor aplicando una operación binaria.",
            "ejemplo": "from functools import reduce\nlista = [1, 2, 3, 4]\nresultado = reduce(lambda x, y: x + y, lista)\nprint(resultado)  # Salida: 10"
        },
        "fromkeys": {
            "significado": "Método de diccionario que crea un nuevo diccionario con claves especificadas y valores predeterminados.",
            "uso": "Se utiliza para crear diccionarios a partir de una lista de claves con un valor predeterminado.",
            "ejemplo": "diccionario = dict.fromkeys(['a', 'b', 'c'], 0)\nprint(diccionario)  # Salida: {'a': 0, 'b': 0, 'c': 0}"
        },
        "flask_restful": {
            "significado": "Extensión para Flask que simplifica la creación de APIs RESTful.",
            "uso": "Se utiliza para desarrollar aplicaciones web que siguen la arquitectura REST usando recursos.",
            "ejemplo": "from flask import Flask\nfrom flask_restful import Api, Resource\n\napp = Flask(__name__)\napi = Api(app)\n\nclass HelloWorld(Resource):\n    def get(self):\n        return {'mensaje': 'Hola Mundo'}\n\napi.add_resource(HelloWorld, '/')\napp.run()  # Salida: 'Hola Mundo' como respuesta de la API"
        },
        "fix": {
            "significado": "Término general para corregir o ajustar algo que no funciona correctamente.",
            "uso": "Se utiliza cuando se hace un ajuste o corrección en el código o en la configuración de algo.",
            "ejemplo": "def corregir_error():\n    print('Esta es la mensaje corregida')\ncorregir_error()"
        },
        "float_conversion": {
            "significado": "Proceso de convertir datos de otros tipos a tipo flotante.",
            "uso": "Se utiliza para convertir valores en números de punto flotante (decimales).",
            "ejemplo": "numero = '3.14'\nresultado = float(numero)\nprint(resultado)  # Salida: 3.14"
        },
        "full_path": {
            "significado": "Ruta completa para un archivo o directorio en el sistema de archivos.",
            "uso": "Se utiliza para especificar la ubicación exacta de un archivo o directorio desde la raíz del sistema de archivos.",
            "ejemplo": "import os\ncamino_completo = os.path.abspath('archivo.txt')\nprint(camino_completo)  # Salida: /home/usuario/archivo.txt"
        },
        "filter": {
            "significado": "Función que aplica una condición a cada elemento de un iterable y devuelve los elementos que cumplen con la condición.",
            "uso": "Se utiliza para seleccionar solo los elementos que cumplen con una condición específica.",
            "ejemplo": "lista = [1, 2, 3, 4, 5]\nresultado = filter(lambda x: x % 2 == 0, lista)\nprint(list(resultado))  # Salida: [2, 4]"
        },
        "float": {
        "significado": "Tipo de dato en Python para representar números de punto flotante (números con decimales).",
        "uso": "Se usa para representar números que requieren decimales.",
        "ejemplo": '''
            numero = 3.14
            print(type(numero))  # Salida: <class 'float'>
            '''
        },
        "for": {
            "significado": "Palabra clave en Python usada para iterar sobre los elementos de un iterable.",
            "uso": "Se usa para ejecutar un bloque de código repetidamente para cada elemento de un iterable.",
            "ejemplo": '''
                for i in range(5):
                    print(i)
                # Salida:
                # 0
                # 1
                # 2
                # 3
                # 4
                '''
        },
        "format": {
            "significado": "Método utilizado para formatear cadenas de texto, insertando valores dentro de ellas.",
            "uso": "Se usa para crear cadenas de texto más legibles y dinámicas con valores variables.",
            "ejemplo": '''
                nombre = 'Juan'
                edad = 30
                print('Mi nombre es {} y tengo {} años'.format(nombre, edad))
                # Salida: Mi nombre es Juan y tengo 30 años
                '''
        },
        "from": {
            "significado": "Palabra clave en Python usada para importar módulos o funciones específicas de módulos.",
            "uso": "Se usa para traer funcionalidades específicas de un módulo al espacio de nombres actual.",
            "ejemplo": '''
                from math import sqrt
                print(sqrt(16))  # Salida: 4.0
                '''
        },
        "function": {
            "significado": "Bloque de código diseñado para realizar una tarea específica y que puede ser reutilizado.",
            "uso": "Se usa para agrupar código relacionado que realiza una tarea común, permitiendo reutilización y modularidad.",
            "ejemplo": '''
                def saludo(nombre):
                    return f'Hola, {nombre}'
                
                print(saludo('Juan'))  # Salida: Hola, Juan
                '''
        },
        "fibonacci": {
            "significado": "Secuencia matemática donde cada número es la suma de los dos anteriores.",
            "uso": "Se usa para generar la secuencia de Fibonacci, frecuentemente en ejercicios de programación o algoritmos.",
            "ejemplo": '''
                def fibonacci(n):
                    if n <= 1:
                        return n
                    else:
                        return fibonacci(n-1) + fibonacci(n-2)
                
                print(fibonacci(5))  # Salida: 5
                '''
        },
        "file": {
            "significado": "Objeto en Python que permite interactuar con archivos en el sistema de archivos.",
            "uso": "Se usa para abrir, leer, escribir y manipular archivos.",
            "ejemplo": '''
                with open('archivo.txt', 'r') as f:
                    contenido = f.read()
                print(contenido)
                '''
        },
        "fwrite": {
            "significado": "Función usada para escribir datos en un archivo.",
            "uso": "Se usa para escribir datos binarios en un archivo abierto en modo de escritura.",
            "ejemplo": '''
                with open('archivo.bin', 'wb') as f:
                    f.write(b'Hello, World!')
                '''
        },
        "fread": {
            "significado": "Función usada para leer datos de un archivo.",
            "uso": "Se usa para leer datos binarios de un archivo abierto en modo de lectura.",
            "ejemplo": '''
                with open('archivo.bin', 'rb') as f:
                    datos = f.read()
                print(datos)  # Salida: b'Hello, World!'
                '''
        },
        "finally": {
            "significado": "Palabra clave en Python que define un bloque de código que siempre se ejecutará, independientemente de si ocurre una excepción o no.",
            "uso": "Se usa en estructuras try-except para garantizar que un bloque de código final sea ejecutado, incluso si ocurre un error.",
            "ejemplo": '''
                try:
                    x = 1 / 0
                except ZeroDivisionError:
                    print('División por cero')
                finally:
                    print('Este bloque siempre se ejecuta')
                '''
        },
        "freeze": {
            "significado": "Proceso de convertir un objeto mutable en un objeto inmutable.",
            "uso": "Se usa para evitar que un objeto sea modificado después de haber sido creado.",
            "ejemplo": '''
                # No hay una función explícita llamada freeze, pero en algunos casos como con `frozenset` se puede lograr el mismo efecto
                a = frozenset([1, 2, 3])
                print(a)  # Salida: frozenset({1, 2, 3})
                '''
        },
        "flush": {
            "significado": "Método usado para vaciar los buffers de un archivo, garantizando que todos los datos sean escritos en el disco.",
            "uso": "Se usa cuando es necesario garantizar que los datos almacenados en un buffer sean inmediatamente escritos en el archivo.",
            "ejemplo": '''
                with open('archivo.txt', 'w') as f:
                    f.write('Hola')
                    f.flush()  # Garantiza que los datos sean escritos en el archivo
                '''
        },
        "fstring": {
            "significado": "Cadena de texto que permite insertar expresiones dentro de la cadena de forma más legible y eficiente.",
            "uso": "Se usa para crear cadenas de texto interpoladas, donde las variables pueden ser insertadas directamente dentro de la cadena.",
            "ejemplo": '''
                nombre = 'Juan'
                edad = 30
                print(f'Mi nombre es {nombre} y tengo {edad} años')  # Salida: Mi nombre es Juan y tengo 30 años
                '''
        },
        "factorial": {
            "significado": "Función matemática que calcula el producto de todos los números enteros positivos hasta un número dado.",
            "uso": "Se usa para calcular el factorial de un número, frecuentemente en algoritmos de combinatoria y probabilidad.",
            "ejemplo": '''
                import math
                print(math.factorial(5))  # Salida: 120
                '''
        },
        "frozen": {
            "significado": "Objeto inmutable que no puede ser modificado después de su creación.",
            "uso": "Se usa para crear objetos que no pueden ser alterados, como un `frozenset` en Python.",
            "ejemplo": '''
                a = frozenset([1, 2, 3])
                print(a)  # Salida: frozenset({1, 2, 3})
                '''
        },
        "filterfalse": {
            "significado": "Función que devuelve un iterador que filtra los elementos de un iterable, excluyendo los que devuelven `True` en la función proporcionada.",
            "uso": "Se usa para obtener los elementos de un iterable para los cuales la función devuelve `False`.",
            "ejemplo": '''
                from itertools import filterfalse
                resultado = filterfalse(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])
                print(list(resultado))  # Salida: [1, 3, 5]
                '''
        },
        "fuzzy": {
            "significado": "Relacionado con la lógica difusa, que permite lidiar con información imprecisa o incierta.",
            "uso": "Se usa en sistemas que necesitan procesar datos aproximados o inciertos.",
            "ejemplo": '''
                # ejemplo de una biblioteca de lógica difusa como `fuzzywuzzy` (para coincidencia difusa de texto)
                from fuzzywuzzy import fuzz
                print(fuzz.ratio('hola', 'Hola'))  # Salida: 100
                '''
        },
        "fibonacci_sequence": {
            "significado": "Secuencia matemática donde cada número es la suma de los dos anteriores.",
            "uso": "Se usa para generar la secuencia de Fibonacci.",
            "ejemplo": '''
                def fibonacci(n):
                    secuencia = [0, 1]
                    while len(secuencia) < n:
                        secuencia.append(secuencia[-1] + secuencia[-2])
                    return secuencia
                
                print(fibonacci(10))  # Salida: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
                '''
        },
        "format_spec": {
            "significado": "Cadena usada para definir cómo deben presentarse los valores dentro de un formato de cadena.",
            "uso": "Se usa para especificar el formato de los valores dentro de una cadena, como precisión decimal, alineación, entre otros.",
            "ejemplo": '''
                pi = 3.14159
                print(f'{pi:.2f}')  # Salida: 3.14
                '''
        },
        "fork": {
            "significado": "Proceso de crear un nuevo proceso, copiado del proceso original.",
            "uso": "Se usa en la programación de sistemas para crear procesos secundarios.",
            "ejemplo": '''
                import os
                pid = os.fork()
                if pid > 0:
                    print(f'Proceso padre, PID: {pid}')
                else:
                    print(f'Proceso hijo, PID: {os.getpid()}')
                '''
        },
        "function_annotation": {
            "significado": "Anotaciones en funciones que se usan para indicar el tipo de los parámetros y el valor de retorno.",
            "uso": "Se usa para mejorar la legibilidad y el análisis estático de código, sin afectar su ejecución.",
            "ejemplo": '''
                def suma(a: int, b: int) -> int:
                    return a + b
                
                print(suma(2, 3))  # Salida: 5
                '''
        },
        "freeze_support": {
            "significado": "Función que se usa en programas que usan el módulo `multiprocessing` para habilitar el soporte de procesos en Windows.",
            "uso": "Se usa para permitir que los programas que usan `multiprocessing` funcionen correctamente en sistemas Windows.",
            "ejemplo": '''
                from multiprocessing import freeze_support
                if __name__ == '__main__':
                    freeze_support()
                    # Código adicional aquí
                '''
        },
        "float_format": {
            "significado": "Formato que define cómo se deben presentar los números de punto flotante en una cadena.",
            "uso": "Se utiliza para especificar la cantidad de decimales a mostrar en un número de punto flotante.",
            "ejemplo": '''
                pi = 3.14159
                print(f'{pi:.2f}')  # Salida: 3.14
                '''
        },
        "filter_none": {
            "significado": "Función que filtra elementos de un iterable, excluyendo los valores None.",
            "uso": "Se usa para excluir los valores None de una secuencia.",
            "ejemplo": '''
                lista = [1, None, 2, None, 3]
                resultado = filter(None, lista)
                print(list(resultado))  # Salida: [1, 2, 3]
                '''
        },
        "func_code": {
            "significado": "Atributo que contiene el bytecode de la función en Python.",
            "uso": "Se usa para acceder al código de la función, generalmente en contextos de depuración o análisis.",
            "ejemplo": '''
                def ejemplo():
                    pass
                
                print(ejemplo.__code__)  # Salida: <code object ejemplo at 0x...>
                '''
        },
        "float_power": {
            "significado": "Función que calcula un número elevado a una potencia flotante.",
            "uso": "Se usa para realizar exponenciación con números flotantes.",
            "ejemplo": '''
                print(pow(2, 3.5))  # Salida: 11.313708498984761
                '''
        },
        "format_string": {
            "significado": "Cadena que define la estructura de un valor que se desea mostrar, utilizando especificadores de formato.",
            "uso": "Se usa para definir cómo deben mostrarse los valores en una cadena, como el número de decimales o la alineación.",
            "ejemplo": '''
                nombre = 'Juan'
                edad = 25
                print(f'Nombre: {nombre}, Edad: {edad}')  # Salida: Nombre: Juan, Edad: 25
                '''
        },
        "filename": {
            "significado": "Cadena que representa el nombre de un archivo en el sistema de archivos.",
            "uso": "Se usa para especificar el nombre y la ubicación de un archivo que se desea manipular.",
            "ejemplo": '''
                archivo = 'documento.txt'
                with open(archivo, 'r') as f:
                    print(f.read())
                '''
        },
        "file_object": {
            "significado": "Objeto que representa un archivo abierto en Python, mediante el cual es posible leer, escribir o manipular el archivo.",
            "uso": "Se usa para interactuar con archivos abiertos en Python, accediendo o modificando su contenido.",
            "ejemplo": '''
                with open('documento.txt', 'r') as f:
                    contenido = f.read()
                    print(contenido)
                '''
        },
        "finally_clause": {
            "significado": "Parte de un bloque de código que siempre se ejecuta después de una instrucción try, independientemente de si se genera una excepción o no.",
            "uso": "Se usa para ejecutar código de limpieza o finalización, como el cierre de archivos o la liberación de recursos.",
            "ejemplo": '''
                try:
                    archivo = open('documento.txt', 'r')
                    contenido = archivo.read()
                finally:
                    archivo.close()
                    print('Archivo cerrado')
                '''
        },
        "file_read": {
            "significado": "Operación que permite leer el contenido de un archivo en Python.",
            "uso": "Se usa para obtener los datos almacenados en un archivo para su procesamiento o visualización.",
            "ejemplo": '''
                with open('documento.txt', 'r') as archivo:
                    contenido = archivo.read()
                    print(contenido)
                '''
        },
        "form": {
            "significado": "Estructura o modelo utilizado para organizar datos de manera específica.",
            "uso": "Se usa en interfaces de usuario o aplicaciones web para capturar y organizar datos del usuario.",
            "ejemplo": '''
                formulario = {'nombre': 'Juan', 'edad': 25}
                print(formulario)
                '''
        },
        "function_call": {
            "significado": "Acción de invocar una función en el código, pasando los parámetros necesarios para ejecutar su tarea.",
            "uso": "Se usa para ejecutar una función y obtener su resultado.",
            "ejemplo": '''
                def suma(a, b):
                    return a + b
                resultado = suma(3, 4)
                print(resultado)  # Salida: 7
                '''
        },
        "force": {
            "significado": "Acción de imponer o forzar la ejecución de algo, generalmente en el contexto de programación o manipulación de objetos.",
            "uso": "Se usa para forzar un comportamiento específico en un programa, como evitar errores o realizar una acción independientemente de las condiciones.",
            "ejemplo": '''
                # No existe un 'force' directo en Python, pero es posible usar 'assert' para forzar condiciones
                assert 1 == 1, 'Condición falsa'
                '''
        },
        "function_pointer": {
            "significado": "Referencia a una función que puede ser pasada y ejecutada como un argumento.",
            "uso": "Se usa en lenguajes como C o C++ para referenciar funciones y pasarlas como parámetros.",
            "ejemplo": '''
                # En Python no existe un puntero de función directo, pero las funciones pueden ser pasadas como objetos
                def saludo():
                    print('Hola')
                funcion = saludo
                funcion()  # Salida: Hola
                '''
        },
        "float_precision": {
            "significado": "Número de dígitos usados para representar un número flotante con precisión.",
            "uso": "Se usa para especificar la cantidad de decimales a considerar al realizar operaciones con números flotantes.",
            "ejemplo": '''
                numero = 3.14159265359
                print(f'{numero:.2f}')  # Salida: 3.14
                '''
        },
        "format_error": {
            "significado": "Error que ocurre cuando hay un problema al formatear datos, como una cadena mal estructurada.",
            "uso": "Se usa para manejar errores relacionados con la conversión o el formateo incorrecto de datos.",
            "ejemplo": '''
                try:
                    int('abc')
                except ValueError as e:
                    print(f'Error de formato: {e}')
                '''
        },
        "file_write": {
            "significado": "Operación que permite escribir datos en un archivo en Python.",
            "uso": "Se usa para almacenar información en un archivo, sobrescribiéndolo o añadiendo nuevos datos.",
            "ejemplo": '''
                with open('documento.txt', 'w') as archivo:
                    archivo.write('¡Hola, mundo!')
                '''
        },
        "fibonacci_search": {
            "significado": "Método de búsqueda que utiliza los números de Fibonacci para dividir el espacio de búsqueda de manera eficiente.",
            "uso": "Se usa como una alternativa al algoritmo de búsqueda binaria para encontrar un elemento en un arreglo.",
            "ejemplo": '''
                # Implementación de Fibonacci Search no estándar, pero puede usarse como alternativa a la búsqueda binaria
                def fibonacci_search(arr, x):
                    fib_m_minus_2 = 0
                    fib_m_minus_1 = 1
                    fib_m = fib_m_minus_1 + fib_m_minus_2
                    while(fib_m < len(arr)):
                        fib_m_minus_2 = fib_m_minus_1
                        fib_m_minus_1 = fib_m
                        fib_m = fib_m_minus_1 + fib_m_minus_2
                '''
        },
        "filter_map": {
            "significado": "Función que filtra los elementos de un iterable y luego aplica una función de mapeo a los elementos restantes.",
            "uso": "Se usa para realizar transformaciones y filtrados de manera eficiente en secuencias de datos.",
            "ejemplo": '''
                from itertools import filterfalse
                datos = [1, 2, 3, 4, 5]
                resultado = map(lambda x: x * 2, filter(lambda x: x % 2 == 0, datos))
                print(list(resultado))  # Salida: [4, 8]
                '''
        },
    },
    "g": {
        "get": {
            "significado": "Método que obtiene el valor de una clave en un diccionario. Si la clave no existe, devuelve un valor por defecto.",
            "uso": "Se utiliza para obtener el valor asociado a una clave en un diccionario de manera segura.",
            "ejemplo": '''
                diccionario = {'a': 1, 'b': 2}
                print(diccionario.get('a'))  # Salida: 1
                print(diccionario.get('c', 'No encontrado'))  # Salida: No encontrado
                '''
        },
        "global": {
            "significado": "Palabra clave que se utiliza para declarar que una variable es global, es decir, que pertenece al ámbito global.",
            "uso": "Se utiliza para modificar variables globales dentro de una función.",
            "ejemplo": '''
                x = 10
                def cambiar_global():
                    global x
                    x = 20
                cambiar_global()
                print(x)  # Salida: 20
                '''
        },
        "generator": {
            "significado": "Función que devuelve un iterador, permitiendo generar elementos de uno en uno durante la ejecución.",
            "uso": "Se utiliza para crear secuencias de elementos de manera perezosa (evaluación diferida), sin tener que almacenarlos todos en memoria.",
            "ejemplo": '''
                def contar_hasta_tres():
                    yield 1
                    yield 2
                    yield 3
                for num in contar_hasta_tres():
                    print(num)  # Salida: 1, 2, 3
                '''
        },
        "globals": {
            "significado": "Función que devuelve un diccionario de todas las variables globales.",
            "uso": "Se utiliza para acceder y modificar el diccionario de variables globales.",
            "ejemplo": '''
                x = 10
                print(globals())  # Salida: {'x': 10, ...}
                '''
        },
        "getattr": {
            "significado": "Función que obtiene el valor de un atributo de un objeto.",
            "uso": "Se utiliza para acceder a un atributo de un objeto, incluso si no se conoce su nombre de antemano.",
            "ejemplo": '''
                class Persona:
                    def __init__(self, nombre):
                        self.nombre = nombre
                p = Persona('Juan')
                print(getattr(p, 'nombre'))  # Salida: Juan
                '''
        },
        "groupby": {
            "significado": "Función de `itertools` que agrupa los elementos de un iterable según una clave.",
            "uso": "Se utiliza para agrupar datos en función de un criterio, como en el caso de una lista de elementos.",
            "ejemplo": '''
                from itertools import groupby
                datos = [1, 2, 2, 3, 3, 3]
                grupos = groupby(datos, key=lambda x: x)
                for clave, grupo in grupos:
                    print(clave, list(grupo))  # Salida: 1 [1], 2 [2, 2], 3 [3, 3, 3]
                '''
        },
        "gc": {
            "significado": "Módulo de recolección de basura que permite interactuar con el recolector de basura de Python.",
            "uso": "Se utiliza para gestionar la memoria y liberar objetos no referenciados.",
            "ejemplo": '''
                import gc
                gc.collect()  # Forzar la recolección de basura
                '''
        },
        "git": {
            "significado": "Sistema de control de versiones distribuido para gestionar el código fuente.",
            "uso": "Se utiliza para manejar versiones de código, facilitando el trabajo en equipo y el control de cambios.",
            "ejemplo": '''
                # Usando Git en la terminal
                git clone https://github.com/usuario/repositorio.git
                '''
        },
        "generator_expression": {
            "significado": "Expresión que permite generar un generador de manera compacta, similar a una lista por comprensión.",
            "uso": "Se utiliza para crear generadores de manera eficiente y sin necesidad de almacenar todos los elementos.",
            "ejemplo": '''
                numeros = (x * 2 for x in range(5))
                for num in numeros:
                    print(num)  # Salida: 0, 2, 4, 6, 8
                '''
        },
        "gzip": {
            "significado": "Módulo que permite comprimir y descomprimir archivos en formato gzip.",
            "uso": "Se utiliza para trabajar con archivos comprimidos en el formato gzip, reduciendo su tamaño para almacenamiento o transmisión.",
            "ejemplo": '''
                import gzip
                with gzip.open('archivo.txt.gz', 'rb') as f:
                    contenido = f.read()
                    print(contenido)
                '''
        },
        "graph": {
            "significado": "Estructura de datos que representa relaciones entre objetos a través de nodos y aristas.",
            "uso": "Se utiliza para representar relaciones complejas entre objetos, como en redes sociales o rutas de transporte.",
            "ejemplo": '''
                # Ejemplo básico de grafo
                grafo = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A'], 'D': ['B']}
                print(grafo)
                '''
        },
        "grid": {
            "significado": "Estructura de datos o disposición de elementos en filas y columnas.",
            "uso": "Se utiliza para representar una cuadrícula, como en un tablero de ajedrez o una interfaz de usuario.",
            "ejemplo": '''
                grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
                for fila in grid:
                    print(fila)  # Salida: [1, 2, 3], [4, 5, 6], [7, 8, 9]
                '''
        },
        "getopt": {
            "significado": "Módulo que proporciona una forma de analizar argumentos de la línea de comandos.",
            "uso": "Se usa para gestionar opciones y parámetros pasados a un programa desde la línea de comandos.",
            "ejemplo": '''
                import getopt
                opciones, argumentos = getopt.getopt(['-f', 'archivo.txt'], 'f:')
                print(opciones)  # Salida: [('f', 'archivo.txt')]
                '''
        },
        "gcd": {
            "significado": "Función que calcula el mayor divisor común (MDC) de dos números.",
            "uso": "Se utiliza para encontrar el mayor número que divide dos números sin dejar resto.",
            "ejemplo": '''
                import math
                print(math.gcd(24, 36))  # Salida: 12
                '''
        },
        "getpass": {
            "significado": "Función que lee una contraseña de forma oculta (sin mostrar caracteres al escribir).",
            "uso": "Se utiliza para leer contraseñas o entradas sensibles de forma segura en la terminal.",
            "ejemplo": '''
                import getpass
                contraseña = getpass.getpass('Digite su contraseña: ')
                print(contraseña)  # La contraseña no se muestra mientras se escribe
                '''
        },
        "gradients": {
            "significado": "Cambio en el valor de una variable en relación con otra, comúnmente usado en cálculo y aprendizaje automático.",
            "uso": "Se utiliza para calcular la dirección y la tasa de variación de una función en relación con sus variables.",
            "ejemplo": '''
                # Ejemplo de gradiente en optimización
                def funcion(x):
                    return x**2
                gradiente = 2 * 3  # Gradiente de x^2 en x = 3
                print(gradiente)  # Salida: 6
                '''
        },
        "graphlib": {
            "significado": "Módulo en Python que proporciona estructuras de datos para trabajar con grafos.",
            "uso": "Se usa para representar y manipular grafos de manera eficiente.",
            "ejemplo": '''
                import graphlib
                grafo = graphlib.TopologicalSorter({'A': ['B'], 'B': ['C'], 'C': []})
                print(list(grafo.static_order()))  # Salida: ['A', 'B', 'C']
                '''
        },
        "get_event_loop": {
            "significado": "Función de la biblioteca `asyncio` que obtiene el loop de eventos de la aplicación.",
            "uso": "Se utiliza para obtener el loop de eventos principal en un programa asincrónico.",
            "ejemplo": '''
                import asyncio
                loop = asyncio.get_event_loop()
                print(loop)  # Salida: <_UnixSelectorEventLoop running=True closed=False pid=12345>
                '''
        },
        "get_terminal_size": {
            "significado": "Función que obtiene el tamaño del terminal en filas y columnas.",
            "uso": "Se utiliza para obtener la resolución del terminal y ajustar el diseño de la salida.",
            "ejemplo": '''
                import shutil
                tamaño = shutil.get_terminal_size()
                print(tamaño)  # Salida: os.terminal_size(columns=80, lines=24)
                '''
        },
        "getsizeof": {
            "significado": "Función del módulo `sys` que devuelve el tamaño de un objeto en bytes.",
            "uso": "Se utiliza para medir la memoria ocupada por un objeto en Python.",
            "ejemplo": '''
                import sys
                objeto = [1, 2, 3]
                print(sys.getsizeof(objeto))  # Salida: 72 (dependiendo del sistema)
                '''
        },
        "google": {
            "significado": "Motor de búsqueda de internet, también usado como nombre de la empresa.",
            "uso": "Se utiliza para buscar información en la web a través de un navegador o API.",
            "ejemplo": '''
                # Buscando algo en Google
                # Puede hacerse a través de la interfaz web en www.google.com
                '''
        },
        "getdefaultencoding": {
            "significado": "Método que devuelve el nombre de la codificación predeterminada utilizada por el sistema.",
            "uso": "Se usa para conocer la codificación predeterminada de texto en Python.",
            "ejemplo": '''
                import sys
                print(sys.getdefaultencoding())  # Salida: 'utf-8' (dependiendo del sistema)
                '''
        },
        "geometry": {
            "significado": "Área de las matemáticas que trata sobre las propiedades y relaciones de puntos, líneas, superficies y sólidos.",
            "uso": "Se usa en campos como la computación gráfica, ingeniería y arquitectura para describir formas y estructuras.",
            "ejemplo": '''
                # Ejemplo de geometría en programación
                import math
                area_circulo = math.pi * (5**2)  # Área de un círculo con radio 5
                print(area_circulo)  # Salida: 78.53981633974483
                '''
        },
        "greenlet": {
            "significado": "Módulo que proporciona primitivas para el control de flujo cooperativo de hilos (hilos ligeros).",
            "uso": "Se usa para ejecutar funciones de forma concurrente sin la sobrecarga de los hilos tradicionales.",
            "ejemplo": '''
                from greenlet import greenlet
                def funcao1():
                    print('En la función 1')
                    g2.switch()
                def funcao2():
                    print('En la función 2')
                    g1.switch()
                g1 = greenlet(funcao1)
                g2 = greenlet(funcao2)
                g1.switch()  # Salida: En la función 1, En la función 2
                '''
        },
        "gitignore": {
            "significado": "Archivo de configuración utilizado por Git para especificar qué archivos o directorios deben ser ignorados en el control de versiones.",
            "uso": "Se usa para evitar que ciertos archivos se incluyan en el repositorio Git, como archivos temporales o de configuración local.",
            "ejemplo": '''
                # Ejemplo de .gitignore
                *.log
                __pycache__/
                '''
        },
        "grammar": {
            "significado": "Conjunto de reglas que describen la estructura de un lenguaje.",
            "uso": "Se usa para definir cómo formar oraciones o expresiones válidas en un idioma o lenguaje.",
            "ejemplo": '''
                # Ejemplo de gramática en programación
                def sumar(a, b):
                    return a + b
                # La sintaxis es la gramática de la función sumar
                '''
        },
        "gettext": {
            "significado": "Función que traduce un texto a un idioma específico, generalmente utilizada en aplicaciones multilingües.",
            "uso": "Se usa para obtener una cadena traducida de acuerdo con el idioma actual del sistema.",
            "ejemplo": '''
                import gettext
                traduccion = gettext.translation('mi_app', localedir='locales', languages=['es'])
                print(traduccion.gettext('Hello'))  # Salida: Hola
                '''
        },
        "generate_tokens": {
            "significado": "Función que genera una secuencia de tokens a partir de un objeto de texto, utilizada para analizar y procesar código fuente.",
            "uso": "Se usa en la creación de analizadores léxicos para dividir un texto en unidades significativas.",
            "ejemplo": '''
                import token
                import tokenize
                codigo = 'print("Hola Mundo")'
                tokens = tokenize.generate_tokens(iter(codigo).__next__)
                for t in tokens:
                    print(t)
                '''
        },
        "gevent": {
            "significado": "Biblioteca de Python para trabajar con concurrencia basada en hilos ligeros, utilizando corutinas.",
            "uso": "Se usa para manejar tareas concurrentes de manera eficiente sin la necesidad de múltiples hilos.",
            "ejemplo": '''
                import gevent
                def tarea():
                    print('Tarea completada')
                gevent.spawn(tarea).join()
                '''
        },
        "gui": {
            "significado": "Interfaz gráfica de usuario, un sistema de interacción visual con programas de computadora.",
            "uso": "Se usa para crear aplicaciones con interfaces visuales, facilitando la interacción del usuario.",
            "ejemplo": '''
                import tkinter as tk
                ventana = tk.Tk()
                ventana.title('Mi GUI')
                ventana.mainloop()
                '''
        },
        "generator_function": {
            "significado": "Función que usa `yield` para retornar un generador.",
            "uso": "Se usa para crear funciones que devuelven un generador y permiten la iteración perezosa.",
            "ejemplo": '''
                def contar():
                    yield 1
                    yield 2
                    yield 3
                for numero in contar():
                    print(numero)  # Salida: 1, 2, 3
                '''
        },
        "get_data": {
            "significado": "Método o función que obtiene datos de una fuente externa o interna.",
            "uso": "Se usa para recuperar datos de bases de datos, APIs u otras fuentes.",
            "ejemplo": '''
                def obtener_datos():
                    return {'nombre': 'Juan', 'edad': 25}
                print(obtener_datos())  # Salida: {'nombre': 'Juan', 'edad': 25}
                '''
        },
        "git_branch": {
            "significado": "Comando de Git que permite trabajar con ramas dentro de un repositorio.",
            "uso": "Se usa para crear, listar y cambiar entre diferentes ramas de un proyecto en Git.",
            "ejemplo": '''
                git branch  # Muestra las ramas existentes
                git checkout -b nueva_rama  # Crea y cambia a la nueva rama
                '''
        },
        "governance": {
            "significado": "El proceso de toma de decisiones y gestión en una organización o sistema.",
            "uso": "Se usa para referirse a cómo un sistema o entidad es administrado y regulado.",
            "ejemplo": '''
                La gobernanza corporativa se refiere a las prácticas y estructuras organizacionales para la toma de decisiones.
                '''
        },
        "gtts": {
            "significado": "Biblioteca de Python para convertir texto a voz utilizando el servicio Google Text-to-Speech.",
            "uso": "Se usa para generar archivos de audio a partir de texto en varios idiomas.",
            "ejemplo": '''
                from gtts import gTTS
                tts = gTTS('Hola, ¿cómo estás?', lang='es')
                tts.save('hola.mp3')
                '''
        },
        "get_identity": {
            "significado": "Método o función que obtiene la identidad de un objeto o usuario.",
            "uso": "Se usa para obtener información sobre la identidad de un objeto o entidad, como un identificador único.",
            "ejemplo": '''
                def get_identity(usuario):
                    return usuario['id']
                usuario = {'id': 123, 'nombre': 'Juan'}
                print(get_identity(usuario))  # Salida: 123
                '''
        },
        "get_status": {
            "significado": "Método o función que obtiene el estado de una operación, proceso o entidad.",
            "uso": "Se usa para verificar o recuperar el estado actual de un sistema o proceso.",
            "ejemplo": '''
                def get_status(operacion):
                    return operacion['estado']
                operacion = {'estado': 'completada'}
                print(get_status(operacion))  # Salida: completada
                '''
        },
        "generator_instance": {
            "significado": "Instancia de un generador, que es un objeto que permite iterar sobre una secuencia de elementos.",
            "uso": "Se usa para gestionar iteraciones de manera eficiente usando la palabra clave `yield`.",
            "ejemplo": '''
                def contador():
                    yield 1
                    yield 2
                    yield 3
                generador = contador()
                for numero in generador:
                    print(numero)  # Salida: 1, 2, 3
                '''
        },
        "guess_encoding": {
            "significado": "Método que intenta adivinar la codificación de un archivo de texto en función de su contenido.",
            "uso": "Se usa para detectar la codificación de archivos de texto que no tienen una codificación especificada.",
            "ejemplo": '''
                import chardet
                with open('archivo.txt', 'rb') as f:
                    resultado = chardet.detect(f.read())
                print(resultado['encoding'])  # Salida: utf-8
                '''
        },
        "git_commit": {
            "significado": "Comando de Git usado para registrar cambios en el repositorio.",
            "uso": "Se usa para guardar un conjunto de cambios realizados en los archivos de un proyecto en el repositorio.",
            "ejemplo": '''
                git commit -m "Mensaje del commit"
                '''
        },
        "gradient_descent": {
            "significado": "Método de optimización utilizado para minimizar funciones de manera iterativa, ajustando los parámetros en la dirección del gradiente negativo.",
            "uso": "Es ampliamente utilizado en aprendizaje automático para encontrar los valores óptimos de los parámetros de un modelo.",
            "ejemplo": '''
                # Ejemplo simplificado de descenso de gradiente
                def gradiente_descendente(funcion, derivada, x_inicial, tasa_aprendizaje, iteraciones):
                    x = x_inicial
                    for _ in range(iteraciones):
                        x -= tasa_aprendizaje * derivada(x)
                    return x
                '''
        },
        "get_referrers": {
            "significado": "Función que obtiene una lista de objetos que hacen referencia a un objeto específico.",
            "uso": "Se usa para rastrear las referencias a un objeto, útil para análisis de memoria.",
            "ejemplo": '''
                import sys
                referencia = sys.get_referrers(objeto)
                print(referencia)
                '''
        },
        "get_window_extent": {
            "significado": "Método que obtiene las dimensiones de una ventana gráfica o área en la pantalla.",
            "uso": "Se usa para determinar el tamaño y las coordenadas de la ventana de una aplicación o gráfico.",
            "ejemplo": '''
                import matplotlib.pyplot as plt
                fig, ax = plt.subplots()
                extent = ax.get_window_extent()
                print(extent)
                '''
        },
        "group": {
            "significado": "Método que agrupa elementos en una colección o estructura según un criterio.",
            "uso": "Se usa para organizar datos en grupos o categorías.",
            "ejemplo": '''
                from itertools import groupby
                lista = [1, 1, 2, 2, 3]
                grupo = groupby(lista)
                for clave, valor in grupo:
                    print(clave, list(valor))  # Salida: 1 [1, 1], 2 [2, 2], 3 [3]
                '''
        },
        "get_history": {
            "significado": "Método que obtiene el historial de operaciones o acciones anteriores.",
            "uso": "Se usa para recuperar las acciones anteriores realizadas en un sistema o aplicación.",
            "ejemplo": '''
                # ejemplo de recuperación del historial en un sistema
                historico = get_history()
                print(historico)
                '''
        },
        "gradient": {
            "significado": "El vector que indica la dirección y la tasa de variación de una función en un punto específico.",
            "uso": "Es ampliamente utilizado en cálculo diferencial y en el entrenamiento de modelos de aprendizaje automático.",
            "ejemplo": '''
                # ejemplo de gradiente de una función
                import numpy as np
                def funcion(x):
                    return x**2
                gradiente = 2 * 3  # Gradiente de x^2 en x = 3
                print(gradiente)  # Salida: 6
                '''
        },
        "getfqdn": {
            "significado": "Función que obtiene el nombre de dominio completo (FQDN) de la máquina local.",
            "uso": "Se usa para obtener el nombre completo de dominio del computador en una red.",
            "ejemplo": '''
                import socket
                fqdn = socket.getfqdn()
                print(fqdn)  # Salida: ejemplo.local
                '''
        },
        "get_url": {
            "significado": "Función que obtiene una URL específica, generalmente para acceder a un recurso en línea.",
            "uso": "Se usa para recuperar una URL de una fuente externa o generar una URL para un recurso.",
            "ejemplo": '''
                import requests
                url = "http://example.com"
                respuesta = requests.get(url)
                print(respuesta.url)
                '''
        },
        "get_line": {
            "significado": "Método que obtiene una línea específica de un archivo o conjunto de datos.",
            "uso": "Se usa para acceder a una línea específica dentro de un archivo o texto.",
            "ejemplo": '''
                with open('archivo.txt', 'r') as f:
                    linea = f.readline()
                    print(linea)
                '''
        },
        "get_clock_info": {
            "significado": "Método que obtiene información sobre el reloj del sistema, como la frecuencia de actualización.",
            "uso": "Se usa para obtener detalles sobre el rendimiento y las características del reloj del sistema.",
            "ejemplo": '''
                import time
                info = time.get_clock_info('time')
                print(info)
                '''
        },
        "getmtime": {
            "significado": "Función que obtiene la fecha y hora de la última modificación de un archivo.",
            "uso": "Se usa para verificar cuándo fue la última modificación de un archivo o directorio.",
            "ejemplo": '''
                import os
                ultima_modificacion = os.path.getmtime('archivo.txt')
                print(ultima_modificacion)
                '''
        },
        "gettext_install": {
            "significado": "Comando o función que instala el paquete `gettext` para la internacionalización de aplicaciones.",
            "uso": "Se usa para instalar el paquete necesario para traducir cadenas de texto en aplicaciones Python.",
            "ejemplo": '''
                # ejemplo en la terminal
                pip install gettext
                '''
        },
        "geometry_manager": {
            "significado": "Método usado para gestionar el tamaño y la ubicación de los widgets en interfaces gráficas.",
            "uso": "Se usa en bibliotecas de interfaces gráficas como Tkinter para organizar la disposición de los elementos.",
            "ejemplo": '''
                import tkinter as tk
                root = tk.Tk()
                label = tk.Label(root, text="Hola Mundo")
                label.pack()  # Usa el geometry manager 'pack'
                root.mainloop()
                '''
        },
        "gcd_algorithm": {
            "significado": "Algoritmo para calcular el mayor divisor común (MCD) de dos números.",
            "uso": "Se usa para encontrar el mayor número que divide exactamente dos números.",
            "ejemplo": '''
                import math
                mcd = math.gcd(24, 36)
                print(mcd)  # Salida: 12
                '''
        },
        "googletrans": {
            "significado": "Biblioteca Python que usa la API de Google Translate para traducir texto entre diferentes idiomas.",
            "uso": "Se usa para traducir texto automáticamente usando los servicios de Google Translate.",
            "ejemplo": '''
                from googletrans import Translator
                translator = Translator()
                traduccion = translator.translate('Hola, ¿cómo estás?', src='es', dest='en')
                print(traduccion.text)  # Salida: Hello, how are you?
                '''
        },
        "get_dpi": {
            "significado": "Función que obtiene la densidad de píxeles por pulgada (DPI) de la pantalla.",
            "uso": "Se usa para obtener la resolución de la pantalla en términos de píxeles por pulgada.",
            "ejemplo": '''
                import tkinter as tk
                root = tk.Tk()
                dpi = root.winfo_fpixels('1i')  # Píxeles por pulgada
                print(dpi)
                '''
        },
        "geolocation": {
            "significado": "Proceso de determinar la ubicación geográfica de un dispositivo.",
            "uso": "Se usa para obtener la latitud, longitud y otros detalles sobre la ubicación de un dispositivo.",
            "ejemplo": '''
                # ejemplo usando geopy
                from geopy.geocoders import Nominatim
                geolocator = Nominatim(user_agent="mi_app")
                ubicacion = geolocator.geocode("1600 Pennsylvania Ave NW, Washington, DC 20500")
                print(ubicacion.address)
                '''
        },
        "git_merge": {
            "significado": "Comando de Git que combina cambios de diferentes ramas en una sola rama.",
            "uso": "Se usa para fusionar ramas de un repositorio en Git.",
            "ejemplo": '''
                git checkout master
                git merge branch-feature
                '''
        },
        "get_tick_params": {
            "significado": "Función que obtiene los parámetros de los 'ticks' en un gráfico.",
            "uso": "Se usa en bibliotecas gráficas como Matplotlib para ajustar los valores de los ejes en los gráficos.",
            "ejemplo": '''
                import matplotlib.pyplot as plt
                fig, ax = plt.subplots()
                ticks = ax.get_xticks()
                print(ticks)
                '''
        },
        "getrandbits": {
            "significado": "Método que retorna un número aleatorio con una cantidad específica de bits.",
            "uso": "Se usa para generar números aleatorios binarios con un número determinado de bits.",
            "ejemplo": '''
                import random
                numero = random.getrandbits(8)  # 8 bits
                print(numero)  # Salida: número aleatorio de 8 bits
                '''
        },
        "gui_toolkit": {
            "significado": "Conjunto de herramientas o bibliotecas utilizadas para desarrollar interfaces gráficas de usuario (GUI).",
            "uso": "Se usa para construir aplicaciones con interfaces visuales interactivas.",
            "ejemplo": '''
                # ejemplo con Tkinter
                import tkinter as tk
                root = tk.Tk()
                label = tk.Label(root, text="Hola Mundo")
                label.pack()
                root.mainloop()
                '''
        },
        "getpid": {
            "significado": "Función que obtiene el ID del proceso actual.",
            "uso": "Se usa para obtener el identificador único del proceso en ejecución.",
            "ejemplo": '''
                import os
                pid = os.getpid()
                print(pid)  # Salida: ID del proceso actual
                '''
        },
        "get_event": {
            "significado": "Método que obtiene un evento específico en el contexto de un sistema o aplicación.",
            "uso": "Se usa para recuperar un evento de un sistema de gestión de eventos.",
            "ejemplo": '''
                # ejemplo en un sistema de eventos
                evento = get_event("click")
                print(evento)
                '''
        },
        "gmm": {
            "significado": "Modelo de Mezcla Gaussiana (GMM), un modelo probabilístico para la distribución de datos.",
            "uso": "Se usa en aprendizaje automático para modelar datos como una mezcla de distribuciones gaussianas.",
            "ejemplo": '''
                from sklearn.mixture import GaussianMixture
                gmm = GaussianMixture(n_components=2)
                gmm.fit(datos)
                '''
        },
        "gather": {
            "significado": "Función usada para recolectar o agrupar elementos o resultados en una estructura.",
            "uso": "Se usa para reunir resultados de operaciones paralelas o de múltiples fuentes.",
            "ejemplo": '''
                import asyncio
                async def tarea():
                    return 1
                async def main():
                    resultados = await asyncio.gather(tarea(), tarea())
                    print(resultados)
                asyncio.run(main())
                '''
        },
        "get_statistics": {
            "significado": "Método que obtiene las estadísticas de un conjunto de datos.",
            "uso": "Se usa para calcular y recuperar métricas estadísticas como media, mediana, desviación estándar, etc.",
            "ejemplo": '''
                import statistics
                datos = [1, 2, 3, 4, 5]
                media = statistics.mean(datos)
                print(media)  # Salida: 3
                '''
        },
        "get_user": {
            "significado": "Método que obtiene información actual del usuario.",
            "uso": "Se utiliza para recuperar detalles del usuario en un sistema.",
            "ejemplo": '''
                print("¡Hola, bienvenido a nuestra aplicación!")
                '''
        },
        "get_unique": {
            "significado": "Función que obtiene los elementos únicos de un conjunto de datos.",
            "uso": "Se usa para recuperar los valores no repetidos de una lista o conjunto.",
            "ejemplo": '''
                import numpy as np
                datos = [1, 2, 2, 3, 4, 4]
                unicos = np.unique(datos)
                print(unicos)  # Salida: [1 2 3 4]
                '''
        },
        "git_rebase": {
            "significado": "Comando de Git que permite aplicar cambios de una rama a otra, reescribiendo el historial.",
            "uso": "Se usa para integrar los cambios de una rama a otra de manera más limpia, reorganizando los commits.",
            "ejemplo": '''
                git checkout feature-branch
                git rebase main
                '''
        },
        "get_score": {
            "significado": "Método para obtener una puntuación o clasificación basada en algún criterio o cálculo.",
            "uso": "Se usa en diversas aplicaciones para obtener la puntuación de un sistema, juego, examen, etc.",
            "ejemplo": '''
                score = game.get_score()
                print(score)  # Salida: puntuación actual
                '''
        },
        "graph_data": {
            "significado": "Proceso de representar datos en forma de gráficos.",
            "uso": "Se usa para visualizar información y patrones a través de gráficos como barras, líneas, etc.",
            "ejemplo": '''
                import matplotlib.pyplot as plt
                datos = [1, 2, 3, 4, 5]
                plt.plot(datos)
                plt.show()
                '''
        },
        "get_installed_distributions": {
            "significado": "Función que obtiene las distribuciones de paquetes instaladas en el entorno de Python.",
            "uso": "Se usa para obtener una lista de los paquetes instalados en un entorno de Python.",
            "ejemplo": '''
                from pkg_resources import get_distribution
                distribs = get_installed_distributions()
                for distrib in distribs:
                    print(distrib)
                '''
        },
        "geocode": {
            "significado": "Proceso de convertir una dirección en coordenadas geográficas (latitud y longitud).",
            "uso": "Se usa para obtener la localización geográfica de una dirección textual.",
            "ejemplo": '''
                from geopy.geocoders import Nominatim
                geolocator = Nominatim(user_agent="mi_app")
                local = geolocator.geocode("1600 Pennsylvania Ave NW, Washington, DC 20500")
                print(local.latitude, local.longitude)
                '''
        },
        "get_type_hints": {
            "significado": "Función que obtiene las sugerencias de tipo de los parámetros y valores de retorno de una función.",
            "uso": "Se usa para obtener las anotaciones de tipo de una función.",
            "ejemplo": '''
                from typing import get_type_hints
                def ejemplo(x: int, y: str) -> bool:
                    return True
                print(get_type_hints(ejemplo))
                '''
        },
        "genericpath": {
            "significado": "Módulo que proporciona funciones para trabajar con rutas de archivos y directorios de forma genérica.",
            "uso": "Se usa para manipular rutas de archivos y directorios.",
            "ejemplo": '''
                import genericpath
                archivo = "/ruta/a/archivo.txt"
                print(genericpath.exists(archivo))  # Salida: True o False
                '''
        },
        "get_resource_path": {
            "significado": "Método que obtiene la ruta de un recurso dentro de un paquete o aplicación.",
            "uso": "Se usa para localizar recursos dentro de un entorno empaquetado.",
            "ejemplo": '''
                import pkg_resources
                camino = pkg_resources.resource_filename('mi_paquete', 'recurso.txt')
                print(camino)
                '''
        },
        "git_pull": {
            "significado": "Comando de Git que actualiza el repositorio local con los cambios más recientes del repositorio remoto.",
            "uso": "Se usa para obtener los cambios más recientes del repositorio remoto y fusionarlos con la rama local.",
            "ejemplo": '''
                git pull origin master
                '''
        },
        "get_cached_properties": {
            "significado": "Método para obtener propiedades que han sido almacenadas en caché.",
            "uso": "Se usa para acceder a propiedades previamente calculadas y almacenadas en la memoria para mejorar la eficiencia.",
            "ejemplo": '''
                class MiClase:
                    @property
                    def propiedad(self):
                        if not hasattr(self, '_cached_property'):
                            self._cached_property = 42  # ejemplo de cálculo
                        return self._cached_property
                obj = MiClase()
                print(obj.propiedad)  # Salida: 42
                '''
        },
        "geopandas": {
            "significado": "Biblioteca de Python para la manipulación y análisis de datos geoespaciales.",
            "uso": "Se usa para trabajar con datos espaciales, como mapas y coordenadas geográficas.",
            "ejemplo": '''
                import geopandas as gpd
                gdf = gpd.read_file('mapa.shp')
                gdf.plot()
                '''
        },
        "get_open_files": {
            "significado": "Función que obtiene una lista de archivos abiertos en un sistema.",
            "uso": "Se usa para monitorear los archivos abiertos en un proceso o sistema.",
            "ejemplo": '''
                import psutil
                procesos = psutil.process_iter(['pid', 'name'])
                for proceso in procesos:
                    archivos = proceso.open_files()
                    for archivo in archivos:
                        print(archivo.path)
                '''
        },
        "get_active_connections": {
            "significado": "Método que obtiene las conexiones activas en un sistema o red.",
            "uso": "Se usa para obtener las conexiones activas en una aplicación o sistema operativo.",
            "ejemplo": '''
                import psutil
                conexiones = psutil.net_connections()
                for conexion in conexiones:
                    print(conexion)
                '''
        },
        "guess_language": {
            "significado": "Función que adivina el idioma de un texto dado.",
            "uso": "Se usa para determinar el idioma de una cadena de texto.",
            "ejemplo": '''
                from langdetect import detect
                idioma = detect("Hola, ¿cómo estás?")
                print(idioma)  # Salida: es
                '''
        },
        "get_doc": {
            "significado": "Método que obtiene la documentación asociada a un objeto o función.",
            "uso": "Se usa para obtener la cadena de documentación (docstring) de un objeto o función.",
            "ejemplo": '''
                def ejemplo():
                    """Esta es la documentación de la función"""
                    pass
                print(ejemplo.__doc__)
                '''
        },
    },
    "h": {
       "hash": {
        "meaning": "Función que genera un valor hash para un objeto, útil para un almacenamiento y comparación eficientes.",
        "uso": "Se utiliza para calcular el hash de un objeto inmutable.",
        "ejemplo": '''
            valor = hash("ejemplo")
            print(valor) # Salida: valor hash único
            '''
        },
        "help": {
            "significado": "Función que muestra documentación y ayuda para un objeto o módulo.",
            "uso": "Se utiliza para obtener información sobre el uso de funciones, clases o módulos.",
            "ejemplo": '''
                ayuda(imprimir) # Mostrar documentación para la función 'imprimir'
                '''
        },
        "head": {
            "significado": "Devuelve las primeras filas de un DataFrame en pandas.",
            "uso": " es utilizado en sistemas operativos tipo Unix (como Linux o macOS) para mostrar las primeras líneas de un archivo.",
            "ejemplo": '''# Lista de ejemplo
            mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            # Obtener los primeros 3 elementos de la lista (equivalente al 'head' de la lista)
            primeros_tres = mi_lista[:3]
            print(primeros_tres)  # Salida: [1, 2, 3]'''
        },
        "http": {
            "significado":"Proporciona soporte para el protocolo HTTP en Python..",
            "uso": " se utiliza principalmente para realizar solicitudes a un servidor web, ya sea para obtener datos de una API ",
            "ejemplo": '''import requests
            # URL del recurso o API
            url = "https://jsonplaceholder.typicode.com/posts/1"
            # Realizar una solicitud GET para obtener datos
            response = requests.get(url)
            # Verificar si la solicitud fue exitosa (código 200)
            if response.status_code == 200:
            # Mostrar el contenido de la respuesta (en formato JSON)
            print(response.json())
            else:
            print(f"Error: {response.status_code}")'''
        },
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
    },
    "l": {
        "len()": {
            "significado": "Devuelve la longitud de un objeto (como una lista o cadena).",
            "uso": "Usado para contar elementos en una secuencia.",
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
        "shutil": {
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
        "zscore": {
            "significado":" Función que calcula el valor z, que indica cuántas desviaciones estándar está un valor de la media.",
            "uso": "  indica cuántas desviaciones estándar se encuentra un valor respecto a la media de un conjunto de datos.",
            "ejemplo": '''# Estandarizar todo el conjunto de datos
            z_scores_datos = [(x - media) / desviacion_estandar for x in datos]
            print("Z-scores de todo el conjunto de datos:")
            print(z_scores_datos)'''
        },  
        "zoneinfo": {
            "significado":" Módulo que proporciona soporte para zonas horarias en Python.",
            "uso": "  permite trabajar con zonas horarias de forma más sencilla y precisa. ",
            "ejemplo": '''from zoneinfo import ZoneInfo
            from datetime import datetime
            # Obtener la hora local en la zona horaria del sistema
            fecha_local = datetime.now(ZoneInfo("America/Los_Angeles"))
            # Mostrar la fecha y hora en la zona horaria local
            print("Fecha y hora en Los Angeles:", fecha_local)'''
        },  
        "zipfile": {
            "significado":"Módulo para crear, leer y modificar archivos ZIP.",
            "uso": "  es un archivo comprimido que puede contener uno o más archivos y/o carpetas.",
            "ejemplo": '''import zipfile
            # Crear un nuevo archivo ZIP
            with zipfile.ZipFile('nuevo_archivo.zip', 'w') as zip_ref:
            # Agregar un archivo a la carpeta ZIP
            zip_ref.write('documento.txt')  # Asegúrate de que 'documento.txt' exista en tu carpeta actual
            # Agregar otro archivo
            zip_ref.write('imagen.png')
            print("Archivos agregados a 'nuevo_archivo.zip'.")'''
        },
    }, 
}