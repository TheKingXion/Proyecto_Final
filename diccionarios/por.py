diccionario_por = {
    "a": {
        "abs": {
            "significado": "Devuelve el valor absoluto de un número.",
            "uso": "Se utiliza para obtener la magnitud de un número sin considerar su signo.",
            "ejemplo": """
                numero1 = -10
                print(abs(numero1))  # Salida: 10
                """
        },
        "all": {
            "significado": "Devuelve True si todos los elementos de un iterable son verdaderos (o si el iterable está vacío).",
            "uso": "Se utiliza para verificar que todos los valores de un iterable cumplan una condición.",
            "ejemplo": """
                lista = [True, True, True]
                print(all(lista))  # Salida: True

                numeros = [1, 2, 0]
                print(all(numeros))  # Salida: False (0 es evaluado como False)
                """
        },
        "any": {
            "significado": "Devuelve True si al menos un elemento de un iterable es verdadero (o si el iterable está vacío).",
            "uso": "Se utiliza para verificar si al menos un valor de un iterable cumple una condición.",
            "ejemplo": """
                lista = [False, False, True]
                print(any(lista))  # Salida: True

                numeros = [0, 0, 0]
                print(any(numeros))  # Salida: False
                """
        },
        "ascii": {
            "significado": "Devuelve una representación legible de un objeto utilizando caracteres ASCII.",
            "uso": "Se utiliza para representar cadenas o caracteres en un formato seguro en ASCII, reemplazando caracteres no ASCII con secuencias de escape.",
            "ejemplo": """
                texto = "Hola, ¿cómo estás?"
                print(ascii(texto))  # Salida: 'Hola, \\xbfcomo est\\xe1s?'
                """
        },
        "append": {
            "significado": "Agrega un elemento al final de una lista.",
            "uso": "Se utiliza para añadir nuevos elementos a una lista existente.",
            "ejemplo": """
                lista = [1, 2, 3]
                lista.append(4)
                print(lista)  # Salida: [1, 2, 3, 4]
                """
        },
        "argmax": {
            "significado": "Devuelve el índice del valor máximo en un array o iterable.",
            "uso": "Se utiliza en bibliotecas como NumPy para localizar el índice del mayor valor en estructuras de datos.",
            "ejemplo": """
                import numpy as np

                numeros = [1, 5, 2, 9, 3]
                print(np.argmax(numeros))  # Salida: 3 (índice del valor 9)
                """
        },
        "argmin": {
            "significado": "Devuelve el índice del valor mínimo en un array o iterable.",
            "uso": "Se utiliza en bibliotecas como NumPy para localizar el índice del menor valor en estructuras de datos.",
            "ejemplo": """
                import numpy as np

                numeros = [1, 5, 2, 9, 3]
                print(np.argmin(numeros))  # Salida: 0 (índice del valor 1)
                """
        },
        "array": {
            "significado": "Es una estructura de datos que contiene múltiples elementos del mismo tipo, comúnmente utilizada en bibliotecas como NumPy.",
            "uso": "Se utiliza para almacenar y operar eficientemente con grandes cantidades de datos homogéneos.",
            "ejemplo": """
                import numpy as np

                numeros = np.array([1, 2, 3, 4])
                print(numeros)  # Salida: [1 2 3 4]
                """
        },
        "as": {
            "significado": "Palabra clave utilizada para asignar un alias a módulos o en declaraciones `with`.",
            "uso": "Facilita la referenciación de nombres largos o específicos en el código.",
            "ejemplo": """
                import numpy as np

                with open('archivo.txt', 'r') as archivo:
                contenido = archivo.read()
                """
        },
        "assert": {
        "significado": "Evalúa una expresión y genera una excepción `AssertionError` si la expresión es falsa.",
        "uso": "Se utiliza para verificar condiciones que deben cumplirse durante la ejecución del programa.",
        "ejemplo": """
            x = 5
            assert x > 0, 'x debe ser mayor que 0'  # No genera error
            assert x < 0, 'x debe ser menor que 0'  # Genera AssertionError
            """
        },
        "async": {
            "significado": "Define una función asíncrona que puede ser utilizada con `await`.",
            "uso": "Se utiliza para implementar programación asíncrona en Python.",
            "ejemplo": """
                import asyncio

                async def saludo():
                    print('Hola')
                    await asyncio.sleep(1)
                    print('Adiós')

                asyncio.run(saludo())
                """
        },
        "await": {
            "significado": "Se utiliza para esperar el resultado de una función asíncrona.",
            "uso": "Se utiliza dentro de funciones definidas con `async` para pausar su ejecución hasta que una tarea asíncrona se complete.",
            "ejemplo": """
                import asyncio

                async def tarea():
                    await asyncio.sleep(1)
                    return 'Tarea completada'

                async def main():
                    resultado = await tarea()
                    print(resultado)

                asyncio.run(main())
                """
        },
        "attribute": {
            "significado": "Se refiere a una propiedad o característica asociada a un objeto en Python.",
            "uso": "Se utiliza para acceder o modificar propiedades de objetos creados a partir de clases.",
            "ejemplo": """
                class Persona:
                    def __init__(self, nombre, edad):
                        self.nombre = nombre
                        self.edad = edad

                p = Persona('Juan', 30)
                print(p.nombre)  # Salida: Juan
                p.edad = 31
                print(p.edad)  # Salida: 31
                """
        },
        "at": {
            "significado": "Método utilizado para acceder a elementos específicos en estructuras como DataFrames o arrays (usualmente en pandas).",
            "uso": "Se utiliza para acceder rápidamente a un valor individual en una posición específica.",
            "ejemplo": """
                import pandas as pd

                datos = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
                print(datos.at[0, 'A'])  # Salida: 1
                """
        },
        "args": {
        "significado": "Es un parámetro que permite recibir un número variable de argumentos posicionales en una función.",
        "uso": "Se utiliza para manejar múltiples argumentos en una función sin especificar cada uno individualmente.",
        "ejemplo": """
            def suma(*args):
                return sum(args)

            print(suma(1, 2, 3))  # Salida: 6
            """
        },
        "apply": {
            "significado": "Método utilizado en pandas para aplicar una función a filas o columnas de un DataFrame.",
            "uso": "Se utiliza para realizar operaciones personalizadas en filas o columnas.",
            "ejemplo": """
                import pandas as pd

                datos = pd.DataFrame({'A': [1, 2, 3]})
                datos['B'] = datos['A'].apply(lambda x: x * 2)
                print(datos)
                # Salida:
                #    A  B
                # 0  1  2
                # 1  2  4
                # 2  3  6
                """
        },
        "assertEqual": {
            "significado": "Comprueba si dos valores son iguales en una prueba unitaria.",
            "uso": "Se utiliza en pruebas unitarias para validar la igualdad de valores esperados y reales.",
            "ejemplo": """
                import unittest

                class Prueba(unittest.TestCase):
                    def test_suma(self):
                        self.assertEqual(1 + 1, 2)  # La prueba pasa
                """
        },
        "assertIsNone": {
            "significado": "Comprueba si un valor es None en una prueba unitaria.",
            "uso": "Se utiliza en pruebas unitarias para validar que un valor sea None.",
            "ejemplo": """
                import unittest

                class Prueba(unittest.TestCase):
                    def test_valor_none(self):
                        self.assertIsNone(None)  # La prueba pasa
                """
        },
        "attributeError": {
            "significado": "Es una excepción que ocurre cuando se intenta acceder o asignar un atributo que no existe.",
            "uso": "Se utiliza para capturar y manejar errores relacionados con atributos no válidos.",
            "ejemplo": """
                try:
                    objeto = 5
                    objeto.atributo = 10
                except AttributeError as e:
                    print('Error:', e)
                # Salida: Error: 'int' object has no attribute 'atributo'
                """
        },
        "add": {
            "significado": "Método utilizado para añadir un elemento a un conjunto o realizar una suma entre matrices (dependiendo del contexto).",
            "uso": "Se utiliza en conjuntos para agregar elementos o en NumPy para realizar operaciones matemáticas.",
            "ejemplo": """
                # Conjuntos
                conjunto = {1, 2, 3}
                conjunto.add(4)
                print(conjunto)  # Salida: {1, 2, 3, 4}

                # NumPy
                import numpy as np
                resultado = np.add(2, 3)
                print(resultado)  # Salida: 5
                """
        },
        "allclose": {
            "significado": "Comprueba si todos los elementos de dos arrays son aproximadamente iguales.",
            "uso": "Se utiliza en NumPy para verificar la igualdad de elementos con tolerancia a pequeñas diferencias.",
            "ejemplo": """
                import numpy as np

                a = [1.0, 2.001]
                b = [1.0, 2.0009]
                print(np.allclose(a, b, atol=0.01))  # Salida: True
                """
        },
    },
    "b": {
        "": {
            "significado": "",
            "uso": "",
            "ejemplo": """"""
        },
    },
    "c": {
        "": {
            "significado": "",
            "uso": "",
            "ejemplo": """"""
        },
    },
    "d": {
        "": {
            "significado": "",
            "uso": "",
            "ejemplo": """"""
        },
    },
    "e": {
        "": {
            "significado": "",
            "uso": "",
            "ejemplo": """"""
        },
    },
    "f": {
        "": {
            "significado": "",
            "uso": "",
            "ejemplo": """"""
        },
    },
    "g": {
        "": {
            "significado": "",
            "uso": "",
            "ejemplo": """"""
        },
    },
    "h": {
        # Aquí puedes agregar funciones que comiencen con la letra H
    },
    "i": {
        "if": {
            "significado": "Condição que é avaliada como verdadeira ou falsa.",
            "uso": "Usado para tomar decisões no fluxo de um programa.",
            "ejemplo": "if x > 10: print('Maior que 10')"
        },
        "input": {
            "significado": "Lê dados inseridos pelo usuário no console",
            "uso": "Serve para interagir com o usuário e obter informações.",
            "ejemplo": "input('insira um número')"
        },
    },
    "j": {
        # Aquí puedes agregar funciones que comiencen con la letra J
    },
    "k": {
        "kwargs": {
            "significado": "Es un parámetro que permite recibir un número variable de argumentos con nombre en una función.",
            "uso": "Se utiliza para manejar argumentos nombrados dinámicos en una función.",
            "ejemplo": """
                def mostrar_informacion(**kwargs):
                    for clave, valor in kwargs.items():
                        print(f'{clave}: {valor}')

                mostrar_informacion(nombre='Juan', edad=30)
                # Salida:
                # nombre: Juan
                # edad: 30
                """
        },
    },
    "l": {
        "len()": {
            "significado": "Retorna o comprimento de um objeto (como uma lista ou string).",
            "uso": "Usado para contar elementos em uma sequência.",
            "ejemplo": '''texto = "Olá, Mundo"
            comprimento = len(texto)
        print(f"O comprimento da string é: {comprimento}")'''
        },

    },
    "m": {
        # Aquí puedes agregar funciones que comiencen con la letra M
    },
    "n": {
        # Aquí puedes agregar funciones que comiencen con la letra N
    },
    "o": {
        # Aquí puedes agregar funciones que comiencen con la letra O
    },
    "p": {
        # Aquí puedes agregar funciones que comiencen con la letra P
    },
    "q": {
        # Aquí puedes agregar funciones que comiencen con la letra Q
    },
    "r": {
        # Aquí puedes agregar funciones que comiencen con la letra R
    },
    "s": {
        # Aquí puedes agregar funciones que comiencen con la letra S
    },
    "t": {
        # Aquí puedes agregar funciones que comiencen con la letra T
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
        # Aquí puedes agregar funciones que comiencen con la letra Z
    },
}
