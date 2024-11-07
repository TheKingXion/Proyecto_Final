#pablo
diccionario_es = {
    "a": {
        "all": {
            "significado": "Devuelve True si todos los elementos de un iterable son verdaderos.",
            "uso": "Borrar un objeto, variable o elemento de una colección.",
            "ejemplo": '''lista = [1, 2, 3]
            del lista[0]
            print(lista)  # [2, 3]'''
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
        "constains": {
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
        # Aquí puedes agregar funciones que comiencen con la letra E
    },
    "f": {
        # Aquí puedes agregar funciones que comiencen con la letra F
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

    },
    "j": {
        # Aquí puedes agregar funciones que comiencen con la letra J
    },
    "k": {
        # Aquí puedes agregar funciones que comiencen con la letra K
    },
    "l": {
        "len()": {
            "significado": "Devuelve la longitud de un objeto (como una lista o cadena).",
            "usage": "Usado para contar elementos en una secuencia.",
            "ejemplo": '''text = "Hola mundo"
            longitud = longitud (texto)
            print(f"La longitud de la cadena es: {longitud}")'''
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
        "input": {
            "significado":"Elimina y devuelve un elemento de una lista en un índice específico.",
            "uso": "Sirve Para quitar un valor específico de una lista.",
            "ejemplo": '''frutas = ["manzana", "banana", "naranja", "pera"]
            ultima_fruta = frutas.pop()
            print("Última fruta eliminada:", ultima_fruta)  # Salida: pera
            print("Lista después del pop:", frutas)  # Salida: ['manzana', 'banana', 'naranja']'''
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
        # Aquí puedes agregar funciones que comiencen con la letra Z    }
    }, 
}