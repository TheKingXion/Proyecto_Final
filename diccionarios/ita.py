#cona
diccionario_ita ={
    "a": {
        # Aquí puedes agregar funciones que comiencen con la letra A
    },
      "any": {
            "significado": ":Restituisce True se almeno uno degli elementi in un iterabile è vero",
            "uso": "Verifica se una condizione è un vero iterabile",
            "ejemplo": '''values = [0, False, 2]
            print(any(values))  # True'''
        },
        "all": {
            "significado": "Restituisce True se tutti gli elementi sono true iterabili",
            "uso": "Verifi è che tutte le condizioni sono vere iterabili",
            "ejemplo": '''values = [1, 2, 3]
            print(all(values))  # True'''
        },
        # Aquí puedes agregar funciones que comiencen con la letra b
    "b": {
       "break": {
            "significado":" Termina un ciclo in anticipo.",
            "uso": "Per uscire da un ciclo prima che termini l'iterazione di tutti gli elementi.",
            "ejemplo":'''while True:
            numero = int(input("Introduce un número (ingresa 0 para salir): "))
            if numero == 0:
            break  # Salir del bucle si el número es 0
            print(f"El número ingresado es {numero}")'''
        },
    },
   
        # Aquí puedes agregar funciones que comiencen con la letra C
    },
        "_constains_": {
            "significado":"Definire come verificare se un oggetto contiene altro (per l'operatore in).",
            "uso": " Personalizzare il comportamento dell'operatore quando viene utilizzato con un oggetto di una classe definita dall'utente.",
            "ejemplo": '''class Caja:
            def __init__(self, elementos):
            self.elementos = elementos
            def __contains__(self, item):
            return item in self.elementos
            caja = Caja([1, 2, 3])
            print(2 in caja)  # True'''
        },
        "count": {
            "significado":" Personalizzare il comportamento dell'operatore quando viene utilizzato con un oggetto di una classe definita dall'utente.",
            "uso": " Conta le apparizioni di un valore in una collezione.",
            "ejemplo": '''lista = [1, 2, 2, 3, 2, 4]
            print(lista.count(2))  # 3'''
        },
     },
        "clear": {
            "significado":" Elimina tutti gli elementi da un elenco o da un dizionario.",
            "uso": "Scegliere il contenuto di una raccolta.",
            "ejemplo": '''lista = [1, 2, 3]
            lista.clear()
            print(lista)  # []'''
    "d": {
        # Aquí puedes agregar funciones que comiencen con la letra D
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
            "significado": "Condizione che restituisce vero o falso.",
            "uso": "Utilizzato per prendere decisioni nel flusso di un programma.",
            "ejemplo": "si x > 10: print('Mayor que 10')"
        },
        "input": {
            "significado":"Leggere i dati inseriti dall'utente nella console",
            "uso": "Viene utilizzato per interagire con l'utente e ottenere informazioni.",
            "ejemplo": "input('ingrese un número')"
        },
        "_init_": {
            "significado": "È un metodo speciale nelle classi Python che viene chiamato quando viene creata una nuova istanza della classe.",
            "uso": " Per inizializzare gli attributi dell'oggetto.",
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
            "significado": "Restituisce la lunghezza di un oggetto (come una lista o una stringa).",
            "uso": "Utilizzato per contare gli elementi in una sequenza.",
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
        # Aquí puedes agregar funciones que comiencen con la letra P
    },
    "q": {
        # Aquí puedes agregar funciones que comiencen con la letra Q
    },
    "r": {
        "range": {
        "significado": "Restituisce una sequenza di numeri, solitamente utilizzata nei cicli.",
        "uso": " Utilizzato per creare un intervallo di numeri che può essere ripetuto",
        "ejemplo": '''for i in range(5):
                        print(i)'''
        },
    },
    "s": {
       "str": {
        "significado": " Converte un valore in una stringa di testo.",
        "uso": " Viene utilizzato per separare una stringa utilizzando un delimitatore.",
        "ejemplo":''' # Número entero
        numero = 123
        numero_como_str = str(numero)
        print(type(numero_como_str))  # Salida: <class 'str'>
        print(numero_como_str)        # Salida: '123'''
        },
     "split": {
        "significado":"Divide una stringa in un elenco di sottostringhe..",
        "uso": " È il primo parametro di qualsiasi metodo di istanza di una classe.",
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