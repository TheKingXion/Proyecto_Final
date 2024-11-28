#cona
diccionario_ita ={
    "a": {
        "abs": {
            "significado": "Restituisce il valore assoluto di un numero.",
            "uso": "Viene utilizzato per ottenere la magnitudine di un numero senza considerare il suo segno.",
            "ejemplo": '''
                numero1 = -10
                print(abs(numero1))  # Uscita: 10
                '''
        },
        "absolute_import": {
            "significado": "Direttiva utilizzata per abilitare le importazioni assolute in Python 2.x e versioni successive.",
            "uso": "Viene utilizzato per evitare conflitti tra moduli locali e globali.",
            "ejemplo": '''
                from __future__ import absolute_import

                # Importa sempre il modulo globale, non un locale con lo stesso nome
                import math
                '''
        },
        "add": {
            "significado": "Metodo utilizzato per aggiungere un elemento a un insieme o eseguire una somma tra matrici (a seconda del contesto).",
            "uso": "Viene utilizzato negli insiemi per aggiungere elementi o in NumPy per eseguire operazioni matematiche.",
            "ejemplo": '''
                # Insiemi
                insieme = {1, 2, 3}
                insieme.add(4)
                print(insieme)  # Uscita: {1, 2, 3, 4}

                # NumPy
                import numpy as np
                risultato = np.add(2, 3)
                print(risultato)  # Uscita: 5
                '''
        },
        "all": {
            "significado": "Restituisce True se tutti gli elementi di un iterabile sono veri (o se l'iterabile è vuoto).",
            "uso": "Viene utilizzato per verificare se tutti i valori di un iterabile soddisfano una condizione.",
            "ejemplo": '''
                lista = [True, True, True]
                print(all(lista))  # Uscita: True

                numeri = [1, 2, 0]
                print(all(numeri))  # Uscita: False (0 è valutato come False)
                '''
        },
        "allclose": {
            "significado": "Verifica se tutti gli elementi di due array sono approssimativamente uguali.",
            "uso": "Viene utilizzato in NumPy per verificare l'uguaglianza degli elementi con tolleranza per piccole differenze.",
            "ejemplo": '''
                import numpy as np

                a = [1.0, 2.001]
                b = [1.0, 2.0009]
                print(np.allclose(a, b, atol=0.01))  # Uscita: True
                '''
        },
        "allexcept": {
            "significado": "Non è un termine nativo di Python. Può riferirsi a un approccio logico che applica operazioni su tutti gli elementi, tranne alcuni specifici.",
            "uso": "Generalmente implementato manualmente.",
            "ejemplo": '''
                lista = [1, 2, 3, 4]
                risultato = [x for x in lista if x != 2]  # Filtra tutti, tranne il 2
                print(risultato)  # Uscita: [1, 3, 4]
                '''
        },
        "any": {
            "significado": "Restituisce True se almeno un elemento di un iterabile è vero (o se l'iterabile è vuoto).",
            "uso": "Viene utilizzato per verificare se almeno un valore di un iterabile soddisfa una condizione.",
            "ejemplo": '''
                lista = [False, False, True]
                print(any(lista))  # Uscita: True

                numeri = [0, 0, 0]
                print(any(numeri))  # Uscita: False
            '''
        },
        "append": {
            "significado": "Aggiunge un elemento alla fine di una lista.",
            "uso": "Viene utilizzato per aggiungere nuovi elementi a una lista esistente.",
            "ejemplo": '''
                lista = [1, 2, 3]
                lista.append(4)
                print(lista)  # Uscita: [1, 2, 3, 4]
            '''
        },
        "apply": {
            "significado": "Metodo usato in pandas per applicare una funzione a righe o colonne di un DataFrame.",
            "uso": "Viene utilizzato per eseguire operazioni personalizzate su righe o colonne.",
            "ejemplo": '''
                import pandas as pd

                dati = pd.DataFrame({'A': [1, 2, 3]})
                dati['B'] = dati['A'].apply(lambda x: x * 2)
                print(dati)
                # Uscita:
                #    A  B
                # 0  1  2
                # 1  2  4
                # 2  3  6
                '''
        },
        "argmin": {
            "significado": "Restituisce l'indice del valore minimo in un array o iterabile.",
            "uso": "Viene utilizzato in librerie come NumPy per localizzare l'indice del valore minimo in strutture dati.",
            "ejemplo": '''
                import numpy as np

                numeri = [1, 5, 2, 9, 3]
                print(np.argmin(numeri))  # Uscita: 0 (indice del valore 1)
                '''
        },
        "array": {
            "significado": "È una struttura dati che contiene più elementi dello stesso tipo, comunemente utilizzata in librerie come NumPy.",
            "uso": "Viene utilizzato per memorizzare e operare in modo efficiente con grandi quantità di dati omogenei.",
            "ejemplo": '''
                import numpy as np

                numeri = np.array([1, 2, 3, 4])
                print(numeri)  # Uscita: [1 2 3 4]
                '''
        },
        "args": {
            "significado": "È un parametro che permette di ricevere un numero variabile di argomenti posizionali in una funzione.",
            "uso": "Viene utilizzato per gestire più argomenti in una funzione senza specificarli singolarmente.",
            "ejemplo": '''
                def somma(*args):
                    return sum(args)

                print(somma(1, 2, 3))  # Uscita: 6
                '''
        },
        "arccos": {
            "significado": "Restituisce l'arco coseno (in radianti) di un valore.",
            "uso": "Viene utilizzato nei calcoli trigonometrico con NumPy.",
            "ejemplo": '''
                import numpy as np

                risultato = np.arccos(0.5)
                print(risultato)  # Uscita: 1.0471975511965976 (equivalente a π/3)
                '''
        },
        "arcsin": {
            "significado": "Restituisce l'arco seno (in radianti) di un valore.",
            "uso": "Viene utilizzato nei calcoli trigonometrico con NumPy.",
            "ejemplo": '''
                import numpy as np

                risultato = np.arcsin(0.5)
                print(risultato)  # Uscita: 0.5235987755982988 (equivalente a π/6)
                '''
        },
        "arctan": {
            "significado": "Restituisce l'arco tangente (in radianti) di un valore.",
            "uso": "Viene utilizzato nei calcoli trigonometrico con NumPy.",
            "ejemplo": '''
                import numpy as np

                risultato = np.arctan(1)
                print(risultato)  # Uscita: 0.7853981633974483 (equivalente a π/4)
                '''
        },
        "argparse": {
            "significado": "Modulo di Python utilizzato per gestire gli argomenti e le opzioni della linea di comando.",
            "uso": "Viene utilizzato per creare interfacce di linea di comando facili da usare.",
            "ejemplo": '''
                import argparse

                parser = argparse.ArgumentParser(description='esempio di argparse')
                parser.add_argument('--nome', type=str, help='Il tuo nome')
                args = parser.parse_args()
                print(f'Ciao, {args.nome}')
                '''
        },
        "array_like": {
            "significado": "Si riferisce a qualsiasi oggetto che può essere trattato come un array, come liste, tuple o array di NumPy.",
            "uso": "Viene utilizzato come input in funzioni di NumPy o simili per operazioni sui dati.",
            "ejemplo": '''
                import numpy as np

                lista = [1, 2, 3]
                array = np.array(lista)  # lista è array_like
                print(array)  # Uscita: [1 2 3]
                '''
        },
        "arange": {
            "significado": "Genera un array con valori equamente distribuiti all'interno di un intervallo.",
            "uso": "Viene utilizzato in NumPy per creare sequenze numeriche.",
            "ejemplo": '''
                import numpy as np

                risultato = np.arange(0, 10, 2)
                print(risultato)  # Uscita: [0 2 4 6 8]
                '''
        },
        "argmax": {
            "significado": "Restituisce l'indice del valore massimo in un array o iterabile.",
            "uso": "Viene utilizzato in librerie come NumPy per localizzare l'indice del valore più grande in strutture dati.",
            "ejemplo": '''
                import numpy as np

                numeri = [1, 5, 2, 9, 3]
                print(np.argmax(numeri))  # Uscita: 3 (indice del valore 9)
                '''
        },
        "as": {
            "significado": "Parola chiave utilizzata per assegnare un alias a moduli o in dichiarazioni `with`.",
            "uso": "Facilita il riferimento a nomi lunghi o specifici nel codice.",
            "ejemplo": '''
                import numpy as np

                with open('file.txt', 'r') as file:
                    contenuto = file.read()
                '''
        },
        "assert": {
            "significado": "Valuta un'espressione e genera un'eccezione `AssertionError` se l'espressione è falsa.",
            "uso": "Viene utilizzato per verificare condizioni che devono essere soddisfatte durante l'esecuzione del programma.",
            "ejemplo": '''
                x = 5
                assert x > 0, 'x deve essere maggiore di 0'  # Non genera errore
                assert x < 0, 'x deve essere minore di 0'  # Genera AssertionError
                '''
        },
        "async": {
            "significado": "Definisce una funzione asincrona che può essere usata con `await`.",
            "uso": "Viene utilizzato per implementare la programmazione asincrona in Python.",
            "ejemplo": '''
                import asyncio

                async def saluto():
                    print('Ciao')
                    await asyncio.sleep(1)
                    print('Addio')

                asyncio.run(saluto())
                '''
        },
        "assertEqual": {
            "significado": "Verifica se due valori sono uguali in un test unitario.",
            "uso": "Viene utilizzato nei test unitari per validare l'uguaglianza tra valori attesi e reali.",
            "ejemplo": '''
                import unittest

                class Test(unittest.TestCase):
                    def test_somma(self):
                        self.assertEqual(1 + 1, 2)  # Il test passa
                '''
        }, 
        "as_tuple": {
            "significado": "Metodo che converte un oggetto in una tupla (comune in librerie come SymPy).",
            "uso": "Viene utilizzato per trasformare oggetti in rappresentazioni di tuple.",
            "ejemplo": '''
                from sympy import Point

                p = Point(2, 3)
                print(p.as_tuple())  # Uscita: (2, 3)
                '''
        },
        "ascii": {
            "significado": "Restituisce una rappresentazione leggibile di un oggetto usando caratteri ASCII.",
            "uso": "Viene utilizzato per rappresentare stringhe o caratteri in un formato sicuro in ASCII, sostituendo i caratteri non ASCII con sequenze di escape.",
            "ejemplo": '''
                testo = "Ciao, come stai?"
                print(ascii(testo))  # Uscita: 'Ol\\xe0, come v\\xf2 stai?'
                '''
        },
        "at": {
            "significado": "Metodo utilizzato per accedere a elementi specifici in strutture come DataFrame o array (generalmente in pandas).",
            "uso": "Viene utilizzato per accedere rapidamente a un valore individuale in una posizione specifica.",
            "ejemplo": '''
                import pandas as pd

                dati = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
                print(dati.at[0, 'A'])  # Uscita: 1
                '''
        },
        "attribute": {
            "significado": "Si riferisce a una proprietà o caratteristica associata a un oggetto in Python.",
            "uso": "Viene utilizzato per accedere o modificare le proprietà degli oggetti creati da classi.",
            "ejemplo": '''
                class Persona:
                    def __init__(self, nome, eta):
                        self.nome = nome
                        self.eta = eta

                p = Persona('Giovanni', 30)
                print(p.nome)  # Uscita: Giovanni
                p.eta = 31
                print(p.eta)  # Uscita: 31
                '''
        },
        "attributeError": {
            "significado": "È un'eccezione che si verifica quando si tenta di accedere o assegnare un attributo che non esiste.",
            "uso": "Viene utilizzato per catturare e trattare errori relativi ad attributi non validi.",
            "ejemplo": '''
                try:
                    oggetto = 5
                    oggetto.atributo = 10
                except AttributeError as e:
                    print('Errore:', e)
                # Uscita: Errore: 'int' object has no attribute 'atributo'
                '''
        },
        "atleast_1d": {
            "significado": "Converte gli input in array con almeno una dimensione.",
            "uso": "Viene utilizzato in NumPy per garantire che i dati abbiano una dimensione minima.",
            "ejemplo": '''
                import numpy as np

                risultato = np.atleast_1d(5)
                print(risultato)  # Uscita: [5]
                '''
        },
        "atleast_2d": {
            "significado": "Converte gli input in array con almeno due dimensioni.",
            "uso": "Viene utilizzato in NumPy per lavorare con i dati nel formato matrice.",
            "ejemplo": '''
                import numpy as np

                risultato = np.atleast_2d([1, 2, 3])
                print(risultato)
                # Uscita:
                # [[1 2 3]]
                '''
        },
        "average": {
            "significado": "Calcola la media degli elementi di un array o di una lista.",
            "uso": "Viene utilizzato in NumPy per calcolare medie, con la possibilità di ponderare i valori.",
            "ejemplo": '''
                import numpy as np

                valori = [1, 2, 3, 4]
                print(np.average(valori))  # Uscita: 2.5
                '''
        },
        "await": {
            "significado": "Viene utilizzato per aspettare il risultato di una funzione asincrona.",
            "uso": "Viene usato all'interno di funzioni definite con `async` per sospendere l'esecuzione finché un compito asincrono non è completato.",
            "ejemplo": '''
                import asyncio

                async def compito():
                    await asyncio.sleep(1)
                    return 'Compito completato'

                async def main():
                    risultato = await compito()
                    print(risultato)

                asyncio.run(main())
                '''
        },
    },

    "b": {
        "bin": {
            "significado": "Converte un numero nella sua rappresentazione binaria come una stringa.",
            "uso": "Viene utilizzato per ottenere la rappresentazione binaria di un numero intero.",
            "ejemplo": '''
                numero = 10
                print(bin(numero))  # Uscita: '0b1010'
                '''
        },
        "bool": {
            "significado": "Tipo di dato che rappresenta valori booleani: True o False.",
            "uso": "Viene utilizzato per rappresentare e operare con valori di verità.",
            "ejemplo": '''
                valore = bool(1)
                print(valore)  # Uscita: True
                '''
        },
        "break": {
            "significado": "Parola chiave che termina l'esecuzione di un ciclo.",
            "uso": "Viene utilizzato per uscire da un ciclo in modo anticipato.",
            "ejemplo": '''
                for i in range(5):
                    if i == 3:
                        break
                    print(i)  # Uscita: 0 1 2
                '''
        },
        "bytes": {
            "significado": "Tipo di dato immutabile che rappresenta una sequenza di byte.",
            "uso": "Viene utilizzato per lavorare con dati binari.",
            "ejemplo": '''
                b = bytes([65, 66, 67])
                print(b)  # Uscita: b'ABC'
                '''
        },
        "bytearray": {
            "significado": "Tipo di dato mutabile che rappresenta una sequenza di byte.",
            "uso": "Viene utilizzato per modificare sequenze di byte.",
            "ejemplo": '''
                b = bytearray([65, 66, 67])
                b[0] = 90
                print(b)  # Uscita: bytearray(b'ZBC')
                '''
        },
        "byteswap": {
            "significado": "Metodo che inverte l'ordine dei byte in un oggetto.",
            "uso": "Viene utilizzato per cambiare l'ordine dei byte in un tipo di dato numerico.",
            "ejemplo": '''
                import numpy as np

                a = np.array([1, 256], dtype=np.int16)
                a = a.byteswap()
                print(a)  # Uscita: [256 1]
                '''
        },
        "buffer": {
            "significado": "Una classe in Python che fornisce una vista di accesso a una zona di memoria di un oggetto.",
            "uso": "Viene utilizzato per accedere alla memoria in modo efficiente, specialmente in operazioni con grandi quantità di dati.",
            "ejemplo": '''
                buffer = memoryview(b'abc')
                print(buffer[0])  # Uscita: 97 (equivalente a 'a')
                '''
        },
            },
            "base64": {
            "significado": "Modulo che fornisce funzioni per codificare e decodificare dati in base64.",
            "uso": "Viene utilizzato per rappresentare dati binari in una stringa di caratteri ASCII.",
            "ejemplo": '''
                import base64

                encoded = base64.b64encode(b'abc')
                print(encoded)  # Uscita: b'YWJj'
                '''
        },
        "bitwise_and": {
            "significado": "Operatore che esegue un'operazione AND bit a bit tra due numeri.",
            "uso": "Viene utilizzato per confrontare i bit corrispondenti di due numeri e restituire 1 solo se entrambi i bit sono 1.",
            "ejemplo": '''
                x = 5  # binario: 0101
                y = 3  # binario: 0011
                print(x & y)  # Uscita: 1 (binario: 0001)
                '''
        },
        "bitwise_or": {
            "significado": "Operatore che esegue un'operazione OR bit a bit tra due numeri.",
            "uso": "Viene utilizzato per confrontare i bit corrispondenti di due numeri e restituire 1 se almeno uno dei bit è 1.",
            "ejemplo": '''
                x = 5  # binario: 0101
                y = 3  # binario: 0011
                print(x | y)  # Uscita: 7 (binario: 0111)
                '''
        },
        "bitwise_xor": {
            "significado": "Operatore che esegue un'operazione XOR bit a bit tra due numeri.",
            "uso": "Viene utilizzato per confrontare i bit corrispondenti di due numeri e restituire 1 se i bit sono diversi.",
            "ejemplo": '''
                x = 5  # binario: 0101
                y = 3  # binario: 0011
                print(x ^ y)  # Uscita: 6 (binario: 0110)
                '''
        },
        "bitwise_not": {
            "significado": "Operatore che esegue un'operazione NOT bit a bit su un numero.",
            "uso": "Viene utilizzato per invertire tutti i bit di un numero.",
            "ejemplo": '''
                x = 5  # binario: 0101
                print(~x)  # Uscita: -6 (binario: 1010)
                '''
        },
        "binomial": {
            "significado": "Funzione che calcola il coefficiente binomiale (n su k).",
            "uso": "Viene utilizzato per calcolare il numero di modi per selezionare k elementi da un insieme di n elementi.",
            "ejemplo": '''
                from scipy.special import comb

                risultato = comb(5, 2)
                print(risultato)  # Uscita: 10.0
                '''
        },
        "binascii": {
            "significado": "Modulo che contiene funzioni per convertire tra binario e diverse rappresentazioni di testo.",
            "uso": "Viene utilizzato per effettuare conversioni tra stringhe di testo e dati binari.",
            "ejemplo": '''
                import binascii

                encoded = binascii.hexlify(b'abc')
                print(encoded)  # Uscita: b'616263'
                '''
        },"byteorder": {
            "significado": "Indica l'ordine dei byte per rappresentare i numeri in memoria.",
            "uso": "Viene utilizzato per manipolare la rappresentazione dei numeri su sistemi con architetture diverse.",
            "ejemplo": '''
                import sys

                print(sys.byteorder)  # Uscita: 'little' o 'big'
                '''
        },
        "bit_length": {
            "significado": "Restituisce il numero di bit necessari per rappresentare un numero in binario.",
            "uso": "Viene utilizzato per ottenere la lunghezza in bit di un numero intero.",
            "ejemplo": '''
                numero = 10
                print(numero.bit_length())  # Uscita: 4
                '''
        },
        "breakpoint": {
            "significado": "Una funzione che stabilisce un punto di interruzione nel codice, attivando il debugger.",
            "uso": "Viene utilizzato per fermare l'esecuzione e entrare nel debugger interattivo.",
            "ejemplo": '''
                def funzione():
                    breakpoint()  # Interruzione qui
                    print('Ciao')
                funzione()
                '''
        },
        "binhex": {
            "significado": "Funzione per convertire un file binario in formato esadecimale.",
            "uso": "Viene utilizzato per rappresentare i dati binari in un formato leggibile esadecimale.",
            "ejemplo": '''
                import binhex

                with open('file.bin', 'rb') as f:
                    binhex.binhex(f, 'file.hex')
                '''
        },
        "bitset": {
            "significado": "Struttura dati che consente di memorizzare una raccolta di bit.",
            "uso": "Viene utilizzato per rappresentare insiemi di bit e per eseguire operazioni efficienti su di essi.",
            "ejemplo": '''
                # esempio non standard in Python, ma si può usare il modulo `bitarray` per creare bitset
                from bitarray import bitarray

                bitset = bitarray('10101')
                print(bitset)  # Uscita: bitarray('10101')
                '''
        },
        "broadcast": {
            "significado": "Tecnica che permette ad array di forme diverse di essere allineati per eseguire operazioni elemento per elemento.",
            "uso": "Viene utilizzato principalmente in NumPy per operazioni con array di dimensioni diverse.",
            "ejemplo": '''
                import numpy as np

                a = np.array([1, 2, 3])
                b = np.array([[1], [2], [3]])
                risultato = a + b
                print(risultato)
                # Uscita:
                # [[2 3 4]
                #  [3 4 5]
                #  [4 5 6]]
                '''
        },"bitarray": {
            "significado": "Modulo che implementa un tipo di dato efficiente per lavorare con array di bit.",
            "uso": "Viene utilizzato per manipolare e gestire array di bit in modo efficiente.",
            "ejemplo": '''
                from bitarray import bitarray

                a = bitarray('10101')
                a.append('1')
                print(a)  # Uscita: bitarray('101011')
                '''
        },
        "buffer": {
            "significado": "Una classe in Python che fornisce una vista di accesso a un'area di memoria di un oggetto.",
            "uso": "Viene utilizzato per accedere alla memoria in modo efficiente, specialmente nelle operazioni con grandi quantità di dati.",
            "ejemplo": '''
                buffer = memoryview(b'abc')
                print(buffer[0])  # Uscita: 97 (equivalente a 'a')
                '''
        },
        "bitwise_left_shift": {
            "significado": "Operatore che esegue uno spostamento di bit a sinistra.",
            "uso": "Viene utilizzato per spostare i bit di un numero a sinistra, moltiplicando il valore per potenze di due.",
            "ejemplo": '''
                x = 5  # binario: 0101
                print(x << 1)  # Uscita: 10 (binario: 1010)
                '''
        },
        "bitwise_right_shift": {
            "significado": "Operatore che esegue uno spostamento di bit a destra.",
            "uso": "Viene utilizzato per spostare i bit di un numero a destra, dividendo il valore per potenze di due.",
            "ejemplo": '''
                x = 5  # binario: 0101
                print(x >> 1)  # Uscita: 2 (binario: 0010)
                '''
        },
        "bz2": {
            "significado": "Modulo che fornisce compressione e decompressione utilizzando l'algoritmo bzip2.",
            "uso": "Viene utilizzato per manipolare file compressi nel formato bzip2.",
            "ejemplo": '''
                import bz2

                with bz2.open('file.bz2', 'rb') as file:
                    contenuto = file.read()
                    print(contenuto)
                '''
        },
        "bool_": {
            "significado": "Tipo di dato di NumPy per valori booleani, simile a `bool` di Python.",
            "uso": "Viene utilizzato in operazioni con array di NumPy per rappresentare valori booleani.",
            "ejemplo": '''
                import numpy as np

                valore = np.bool_(True)
                print(valore)  # Uscita: True
                '''
        },
    },
    "c": {
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
        "clear": {
            "significado":" Elimina tutti gli elementi da un elenco o da un dizionario.",
            "uso": "Scegliere il contenuto di una raccolta.",
            "ejemplo": '''lista = [1, 2, 3]
            lista.clear()
            print(lista)  # []'''
        },
        "callable": {
            "significado": "Verifica se un oggetto è invocabile (come una funzione o una classe).",
            "uso": "Viene utilizzato per determinare se un oggetto può essere chiamato.",
            "ejemplo": '''
                def funzione():
                    return "Ciao"

                print(callable(funzione))  # Uscita: True
                print(callable(42))  # Uscita: False
                '''
        },
        "chr": {
            "significado": "Ritorna il carattere Unicode corrispondente a un numero intero.",
            "uso": "Viene utilizzato per convertire un codice Unicode nella sua rappresentazione di carattere.",
            "ejemplo": '''
                print(chr(65))  # Uscita: 'A'
                print(chr(8364))  # Uscita: '€'
                '''
        },
        "class": {
            "significado": "Parola chiave per definire una classe in Python.",
            "uso": "Viene utilizzato per creare oggetti personalizzati con attributi e metodi.",
            "ejemplo": '''
                class Persona:
                    def __init__(self, nome):
                        self.nome = nome

                    def salutare(self):
                        print(f"Ciao, mi chiamo {self.nome}")

                p = Persona("Giovanni")
                p.salutare()  # Uscita: Ciao, mi chiamo Giovanni
                '''
        },
        "classmethod": {
            "significado": "Definisce un metodo di classe, che riceve la classe come primo argomento anziché un'istanza.",
            "uso": "Viene utilizzato per creare metodi che influenzano l'intera classe.",
            "ejemplo": '''
                class MiaClasse:
                    contatore = 0

                    @classmethod
                    def incrementare(cls):
                        cls.contatore += 1

                MiaClasse.incrementare()
                print(MiaClasse.contatore)  # Uscita: 1
                '''
        },
        "compile": {
            "significado": "Compila una stringa di codice in un oggetto eseguibile Python.",
            "uso": "Viene utilizzato per compilare codice dinamico da testo o file.",
            "ejemplo": '''
                codice = "print('Ciao Mondo')"
                compilato = compile(codice, '<string>', 'exec')
                exec(compilato)  # Uscita: Ciao Mondo
                '''
        },
        "complex": {
            "significado": "Crea un numero complesso in Python.",
            "uso": "Viene utilizzato per rappresentare numeri complessi con parte reale e immaginaria.",
            "ejemplo": '''
                c = complex(2, 3)
                print(c)  # Uscita: (2+3j)
                print(c.real, c.imag)  # Uscita: 2.0 3.0
                '''
        },
        "continue": {
            "significado": "Parola chiave che salta alla prossima iterazione di un ciclo.",
            "uso": "Viene utilizzato per ignorare il resto del codice nell'iterazione corrente.",
            "ejemplo": '''
                for i in range(5):
                    if i == 2:
                        continue
                    print(i)  # Uscita: 0 1 3 4
                '''
        },
        "copy": {
            "significado": "Crea una copia superficiale di un oggetto.",
            "uso": "Viene utilizzato per duplicare strutture di dati senza duplicare oggetti annidati.",
            "ejemplo": '''
                import copy

                lista = [1, 2, [3, 4]]
                copia = copy.copy(lista)
                print(copia)  # Uscita: [1, 2, [3, 4]]
                '''
        },
        "coroutine": {
            "significado": "Oggetto che rappresenta una funzione asincrona sospesa.",
            "uso": "Viene utilizzato per gestire compiti asincroni usando `async` e `await`.",
            "ejemplo": '''
                async def compito():
                    print("Inizio")
                    await asyncio.sleep(1)
                    print("Fine")

                import asyncio
                asyncio.run(compito())  # Uscita: Inizio... Fine
                '''
        },
        "count": {
            "significado": "Ritorna il numero di occorrenze di un elemento in una collezione.",
            "uso": "Viene utilizzato per contare quante volte un elemento appare in una lista o stringa.",
            "ejemplo": '''
                lista = [1, 2, 2, 3]
                print(lista.count(2))  # Uscita: 2
                '''
        },
}
   
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