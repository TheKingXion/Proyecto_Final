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
        "clear": {
            "significato": "Rimuove tutti gli elementi da una lista o dizionario.",
            "uso": "Viene utilizzato per svuotare il contenuto di una lista o dizionario.",
            "esempio": '''
                lista = [1, 2, 3]
                lista.clear()
                print(lista)  # Uscita: []
                '''
        },
        "cmath": {
            "significato": "Modulo che fornisce funzioni matematiche per lavorare con numeri complessi.",
            "uso": "Viene utilizzato per eseguire operazioni matematiche su numeri complessi.",
            "esempio": '''
                import cmath

                numero = cmath.sqrt(-1)
                print(numero)  # Uscita: 1j
                '''
        },
        "chain": {
            "significato": "Funzione che combina più iteratori in uno solo.",
            "uso": "Viene utilizzato per concatenare più iteratori.",
            "esempio": '''
                import itertools

                a = [1, 2, 3]
                b = [4, 5, 6]
                risultato = list(itertools.chain(a, b))
                print(risultato)  # Uscita: [1, 2, 3, 4, 5, 6]
                '''
        },
        "csv": {
            "significato": "Modulo per leggere e scrivere file in formato CSV (Comma Separated Values).",
            "uso": "Viene utilizzato per manipolare file CSV.",
            "esempio": '''
                import csv

                with open('file.csv', mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(['Nome', 'Età'])
                    writer.writerow(['Ana', 30])
                '''
        },
        "copyreg": {
            "significato": "Modulo che fornisce funzioni per registrare oggetti per la copia e il disaccoppiamento.",
            "uso": "Viene utilizzato per personalizzare il comportamento di copia e salvataggio degli oggetti.",
            "esempio": '''
                import copyreg

                def creare_persona(nome, eta):
                    return {'nome': nome, 'eta': eta}

                copyreg.pickle(dict, creare_persona)
                '''
        },
        "counter": {
            "significato": "Classe nel modulo `collections` che conta gli elementi hashabili in una sequenza.",
            "uso": "Viene utilizzato per contare la frequenza degli elementi in un iterabile.",
            "esempio": '''
                from collections import Counter

                contatore = Counter([1, 2, 2, 3, 3, 3])
                print(contatore)  # Uscita: Counter({3: 3, 2: 2, 1: 1})
                '''
        },
        "cProfile": {
            "significato": "Modulo per misurare le prestazioni dei programmi in Python.",
            "uso": "Viene utilizzato per fare il profiling del codice e analizzare l'efficienza del programma.",
            "esempio": '''
                import cProfile

                def funzione():
                    for i in range(1000):
                        pass

                cProfile.run('funzione()')
                '''
        },
        "capitalize": {
            "significato": "Metodo di stringa che converte la prima lettera in maiuscolo e il resto in minuscolo.",
            "uso": "Viene utilizzato per capitalizzare la prima lettera di una stringa.",
            "esempio": '''
                testo = 'ciao mondo'
                print(testo.capitalize())  # Uscita: 'Ciao mondo'
                '''
        },
        "center": {
            "significato": "Metodo di stringa che centra una stringa all'interno di un campo di lunghezza specificata.",
            "uso": "Viene utilizzato per allineare il testo al centro di una stringa con riempimento.",
            "esempio": '''
                testo = 'ciao'
                print(testo.center(10, '*'))  # Uscita: '**ciao****'
                '''
        },
        "ceil": {
            "significato": "Funzione del modulo `math` che restituisce l'intero più vicino maggiore o uguale a un numero dato.",
            "uso": "Viene utilizzato per arrotondare un numero per eccesso.",
            "esempio": '''
                import math

                numero = 3.4
                print(math.ceil(numero))  # Uscita: 4
                '''
        },
        "call": {
            "significato": "Metodo utilizzato per invocare un oggetto che è callable, come funzioni o classi.",
            "uso": "Viene utilizzato per chiamare un oggetto che può essere eseguito.",
            "esempio": '''
                def saluto():
                    return 'Ciao'

                print(callable(saluto))  # Uscita: True
                '''
        },
        "clamp": {
            "significato": "Funzione che restringe un valore all'interno di un intervallo specificato.",
            "uso": "Viene utilizzato per garantire che un valore rimanga all'interno di un intervallo definito.",
            "esempio": '''
                def clamp(valore, minimo, massimo):
                    return max(minimo, min(valore, massimo))

                print(clamp(5, 1, 10))  # Uscita: 5
                '''
        },
        "choice": {
            "significato": "Funzione del modulo `random` che seleziona un elemento casuale da una sequenza.",
            "uso": "Viene utilizzato per scegliere un valore casuale da una lista o sequenza.",
            "esempio": '''
                import random

                lista = [1, 2, 3, 4, 5]
                print(random.choice(lista))  # Uscita: un valore casuale dalla lista
                '''
        },
        "collections": {
            "significato": "Modulo che implementa tipi di dati specializzati come `Counter`, `deque`, `OrderedDict`, tra gli altri.",
            "uso": "Viene utilizzato per lavorare con collezioni di dati in modo efficiente.",
            "esempio": '''
                from collections import deque

                fila = deque([1, 2, 3])
                fila.append(4)
                print(fila)  # Uscita: deque([1, 2, 3, 4])
                '''
        },
        "compress": {
            "significato": "Funzione nel modulo `itertools` che permette di comprimere gli elementi di un iterabile.",
            "uso": "Viene utilizzato per filtrare gli elementi di un iterabile in base a una condizione booleana.",
            "esempio": '''
                import itertools

                dati = [1, 2, 3, 4, 5]
                condizioni = [True, False, True, False, True]
                risultato = list(itertools.compress(dati, condizioni))
                print(risultato)  # Uscita: [1, 3, 5]
                '''
        },
        "complex_conjugate": {
            "significato": "Metodo dei numeri complessi in Python che restituisce il coniugato complesso di un numero.",
            "uso": "Viene utilizzato per ottenere il coniugato di un numero complesso.",
            "esempio": '''
                numero_complesso = 3 + 4j
                print(numero_complesso.conjugate())  # Uscita: (3-4j)
                '''
        },
        "ctypes": {
            "significato": "Modulo in Python che permette di interagire con librerie C e fare chiamate a funzioni di basso livello.",
            "uso": "Viene utilizzato per lavorare con tipi di dati e funzioni di librerie esterne scritte in C.",
            "esempio": '''
                import ctypes

                # Creare una variabile di tipo intero
                valore = ctypes.c_int(5)
                print(valore.value)  # Uscita: 5
                '''
        },
        "clear_screen": {
            "significato": "Funzione utilizzata per pulire la schermata del terminale.",
            "uso": "Viene utilizzata per rimuovere il contenuto visibile del terminale o console.",
            "esempio": '''
                import os

                def clear_screen():
                    os.system('cls' if os.name == 'nt' else 'clear')

                clear_screen()
                '''
        },
        "call_later": {
            "significato": "Metodo utilizzato per pianificare l'esecuzione di una funzione dopo un certo periodo di tempo.",
            "uso": "Viene utilizzato nella programmazione asincrona per eseguire attività dopo un ritardo.",
            "esempio": '''
                import asyncio

                async def compito():
                    print('Compito eseguito')

                asyncio.get_event_loop().call_later(2, asyncio.create_task, compito())
                '''
        },
        "chunk": {
            "significato": "Tecnica che divide un iterabile in parti più piccole o blocchi.",
            "uso": "Viene utilizzata per dividere grandi volumi di dati in parti più gestibili.",
            "esempio": '''
                def chunk(iterabile, dimensione):
                    for i in range(0, len(iterabile), dimensione):
                        yield iterabile[i:i + dimensione]

                lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                for blocco in chunk(lista, 3):
                    print(blocco)  # Uscita: [1, 2, 3], [4, 5, 6], [7, 8, 9]
                '''
        },
                "cycle": {
            "significato": "Funzione nel modulo `itertools` che crea un iteratore che ripete indefinitamente una sequenza.",
            "uso": "Viene utilizzata per percorrere un iterabile in un ciclo infinito.",
            "esempio": '''
                import itertools

                ciclo = itertools.cycle([1, 2, 3])
                for i in range(6):
                    print(next(ciclo))  # Uscita: 1, 2, 3, 1, 2, 3
                '''
        },
        "coerce": {
            "significato": "Funzione che cerca di convertire un valore in un tipo compatibile.",
            "uso": "Viene utilizzata per forzare la conversione di un valore in un tipo di dati specifico.",
            "esempio": '''
                # La funzione coerce è stata rimossa nelle versioni moderne di Python.
                '''
        },
        "current_thread": {
            "significato": "Metodo del modulo `threading` che restituisce il thread attuale di esecuzione.",
            "uso": "Viene utilizzato per ottenere il thread di esecuzione in cui il codice sta venendo eseguito.",
            "esempio": '''
                import threading

                def mostra_thread():
                    print(threading.current_thread())

                mostra_thread()
                '''
        },
        "configparser": {
            "significato": "Modulo che permette di manipolare file di configurazione, come i file INI.",
            "uso": "Viene utilizzato per leggere, scrivere e modificare file di configurazione.",
            "esempio": '''
                import configparser

                config = configparser.ConfigParser()
                config.read('config.ini')

                print(config['DEFAULT']['color'])  # Uscita: rosso
                '''
        },
        "compileall": {
            "significato": "Modulo in Python che compila tutti i file `.py` in una directory e nelle sue sottodirectory.",
            "uso": "Viene utilizzato per compilare codice Python in bytecode, il che può migliorare le prestazioni dell'esecuzione.",
            "esempio": '''
                import compileall

                compileall.compile_dir('mia_directory')
                '''
        },
        "copytree": {
            "significato": "Funzione nel modulo `shutil` che copia una directory completa, inclusi i suoi contenuti, in un'altra destinazione.",
            "uso": "Viene utilizzato per copiare una directory e tutto il suo contenuto in una nuova posizione.",
            "esempio": '''
                import shutil

                shutil.copytree('origine', 'destinazione')
                '''
        },
    },
    "d": {
        # Aquí puedes agregar funciones que comiencen con la letra D
        "def": {
            "significato": "Parola chiave in Python utilizzata per definire una funzione.",
            "uso": "Viene utilizzata per creare una nuova funzione con un nome e un blocco di codice.",
            "esempio": '''
                def saluto():
                    print('Ciao Mondo')

                saluto()  # Uscita: Ciao Mondo
                '''
        },
        "delattr": {
            "significato": "Funzione che rimuove un attributo da un oggetto in Python.",
            "uso": "Viene utilizzata per eliminare un attributo specifico di un oggetto.",
            "esempio": '''
                class Persona:
                    def __init__(self, nome):
                        self.nome = nome

                p = Persona('Giovanni')
                delattr(p, 'nome')
                print(hasattr(p, 'nome'))  # Uscita: False
                '''
        },
        "dataframe": {
            "significato": "Struttura di dati bidimensionale nella libreria Pandas, simile a una tabella, che consente di memorizzare dati di tipi diversi.",
            "uso": "Viene utilizzata per manipolare grandi volumi di dati tabulari in Python.",
            "esempio": '''
                import pandas as pd

                dati = {'Nome': ['Giovanni', 'Anna'], 'Età': [28, 22]}
                df = pd.DataFrame(dati)
                print(df)
                '''
        },
        "decode": {
            "significato": "Metodo utilizzato per decodificare dati binari in un formato di testo, generalmente in una codifica come UTF-8.",
            "uso": "Viene utilizzato per convertire dati binari in stringhe di testo leggibili.",
            "esempio": '''
                codificato = b'Ciao Mondo'
                decodificato = codificato.decode('utf-8')
                print(decodificato)  # Uscita: Ciao Mondo
                '''
        },
        "decimal": {
            "significato": "Modulo in Python che fornisce supporto per eseguire calcoli con decimali a precisione arbitraria.",
            "uso": "Viene utilizzato per eseguire operazioni aritmetiche precise senza gli errori di arrotondamento tipici dei numeri a virgola mobile.",
            "esempio": '''
                from decimal import Decimal

                x = Decimal('0.1')
                y = Decimal('0.2')
                print(x + y)  # Uscita: 0.3
                '''
        },
        "device": {
            "significato": "Termine generico per riferirsi a qualsiasi dispositivo hardware o sistema su cui un programma è in esecuzione.",
            "uso": "Viene utilizzato per riferirsi a dispositivi come computer, telefoni cellulari, ecc.",
            "esempio": "Non è un termine specifico di Python, ma può essere utilizzato in librerie come TensorFlow per riferirsi a dispositivi di elaborazione come CPU o GPU."
        },
        "dict.get": {
            "significato": "Metodo dei dizionari in Python che restituisce il valore di una chiave specificata o un valore predefinito se la chiave non esiste.",
            "uso": "Viene utilizzato per ottenere il valore associato a una chiave senza generare un errore se la chiave non esiste.",
            "esempio": '''
                d = {'a': 1, 'b': 2}
                print(d.get('a'))  # Uscita: 1
                print(d.get('c', 'Non trovato'))  # Uscita: Non trovato
                '''
        },
        "dropna": {
            "significato": "Metodo in Pandas utilizzato per rimuovere i valori mancanti (NaN) in un DataFrame o Serie.",
            "uso": "Viene utilizzato per pulire i dati rimuovendo le righe o colonne che contengono valori nulli.",
            "esempio": '''
                import pandas as pd

                df = pd.DataFrame({'A': [1, 2, None], 'B': [None, 3, 4]})
                print(df.dropna())
                '''
        },
        "dtype": {
            "significato": "Proprietà degli array in Numpy o delle colonne in un DataFrame di Pandas che indica il tipo di dato degli elementi.",
            "uso": "Viene utilizzato per ottenere o specificare il tipo di dati di un array o di una colonna.",
            "esempio": '''
                import numpy as np

                arr = np.array([1, 2, 3])
                print(arr.dtype)  # Uscita: int64
                '''
        },
        "deque.appendleft": {
            "significato": "Metodo del tipo di dato `deque` nel modulo `collections` che aggiunge un elemento all'inizio della deque.",
            "uso": "Viene utilizzato per inserire un nuovo elemento nella parte sinistra di una deque.",
            "esempio": '''
                from collections import deque

                d = deque([2, 3, 4])
                d.appendleft(1)
                print(d)  # Uscita: deque([1, 2, 3, 4])
                '''
        },
        "dict.update": {
            "significato": "Metodo dei dizionari in Python che aggiorna un dizionario con gli elementi di un altro dizionario o iterabile.",
            "uso": "Viene utilizzato per aggiungere o modificare gli elementi di un dizionario utilizzando un altro dizionario o iterabile.",
            "esempio": '''
                d1 = {'a': 1, 'b': 2}
                d2 = {'b': 3, 'c': 4}
                d1.update(d2)
                print(d1)  # Uscita: {'a': 1, 'b': 3, 'c': 4}
                '''
        },
        "del": {
            "significato": "Parola chiave in Python che rimuove un attributo o un elemento di una collezione.",
            "uso": "Viene utilizzata per rimuovere elementi da una lista, attributo di un oggetto o una variabile.",
            "esempio": '''
                lista = [1, 2, 3]
                del lista[1]
                print(lista)  # Uscita: [1, 3]
                '''
        },
        "dict": {
            "significato": "Tipo di dato in Python che rappresenta un dizionario, una collezione di coppie chiave-valore.",
            "uso": "Viene utilizzato per memorizzare e manipolare i dati in modo efficiente, associando chiavi uniche ai valori.",
            "esempio": '''
                d = {'a': 1, 'b': 2}
                print(d['a'])  # Uscita: 1
                '''
        },
        "dir": {
            "significato": "Funzione che restituisce una lista degli attributi e dei metodi di un oggetto.",
            "uso": "Viene utilizzata per ottenere informazioni sui metodi e sugli attributi disponibili per un oggetto o modulo.",
            "esempio": '''
                x = [1, 2, 3]
                print(dir(x))
                '''
        },
        "divmod": {
            "significato": "Funzione che riceve due numeri e restituisce una tupla con il quoziente e il resto della loro divisione.",
            "uso": "Viene utilizzata per ottenere sia il quoziente che il resto di una divisione in un'unica operazione.",
            "esempio": '''
                risultato = divmod(9, 4)
                print(risultato)  # Uscita: (2, 1)
                '''
        },
        "deque": {
            "significato": "Tipo di dato nel modulo `collections` di Python che rappresenta una coda a doppia estremità, permettendo di aggiungere e rimuovere elementi da entrambe le estremità in modo efficiente.",
            "uso": "Viene utilizzato per implementare code e pile in modo efficiente.",
            "esempio": '''
                from collections import deque

                d = deque([1, 2, 3])
                d.append(4)
                print(d)  # Uscita: deque([1, 2, 3, 4])
                '''
        },
        "defaultdict": {
            "significato": "Classe nel modulo `collections` che estende il dizionario predefinito e consente di definire un valore predefinito per le chiavi inesistenti.",
            "uso": "Viene utilizzato per evitare errori nell'accesso a chiavi inesistenti, fornendo un valore predefinito.",
            "esempio": '''
                from collections import defaultdict

                d = defaultdict(int)
                d['a'] += 1
                print(d)  # Uscita: defaultdict(<class 'int'>, {'a': 1})
                '''
        },
        "decode": {
            "significato": "Metodo utilizzato per convertire i dati binari in testo in una codifica specifica.",
            "uso": "Viene utilizzato per decodificare una sequenza di byte in una stringa di testo in una codifica specifica.",
            "esempio": '''
                encoded = b'Olá Mundo'
                decoded = encoded.decode('utf-8')
                print(decoded)  # Uscita: Olá Mundo
                '''
        },
        "deflate": {
            "significato": "Algoritmo di compressione dei dati senza perdita, utilizzato per ridurre la dimensione dei file.",
            "uso": "Viene utilizzato per comprimere i dati in un formato più efficiente.",
            "esempio": '''
                import zlib

                data = b'Olá Mundo'*100
                compressed = zlib.compress(data)
                print(compressed)
                '''
        },
        "deepcopy": {
            "significato": "Funzione del modulo `copy` che crea una copia profonda di un oggetto, cioè copia tutti gli elementi dell'oggetto originale, inclusi gli oggetti dentro ad altri oggetti.",
            "uso": "Viene utilizzato quando è necessario fare una copia completa e indipendente di un oggetto.",
            "esempio": '''
                import copy

                original = {'a': [1, 2, 3]}
                copia = copy.deepcopy(original)
                copia['a'][0] = 100
                print(original)  # Uscita: {'a': [1, 2, 3]}
                print(copia)     # Uscita: {'a': [100, 2, 3]}
                '''
        },
        "detach": {
            "significato": "Metodo utilizzato negli oggetti Python per separare un oggetto dal suo contesto o flusso di dati.",
            "uso": "Viene utilizzato per liberare risorse o separare un oggetto dal suo ambiente di esecuzione.",
            "esempio": '''
                import torch

                tensor = torch.tensor([1, 2, 3])
                detached_tensor = tensor.detach()
                print(detached_tensor)  # Uscita: tensor([1, 2, 3])
                '''
        },
        "dump": {
            "significato": "Metodo della libreria `pickle` che serializza un oggetto e lo salva in un file.",
            "uso": "Viene utilizzato per salvare un oggetto in un file in formato serializzato.",
            "esempio": '''
                import pickle

                data = {'a': 1, 'b': 2}
                with open('data.pkl', 'wb') as f:
                    pickle.dump(data, f)
                '''
        },
        "dumps": {
            "significato": "Metodo della libreria `pickle` che serializza un oggetto e lo restituisce come una stringa di byte.",
            "uso": "Viene utilizzato per convertire un oggetto in una stringa per l'archiviazione o la trasmissione.",
            "esempio": '''
                import pickle

                data = {'a': 1, 'b': 2}
                serialized = pickle.dumps(data)
                print(serialized)
                '''
        },
        "difference": {
            "significato": "Metodo degli insiemi in Python che restituisce la differenza tra due o più insiemi.",
            "uso": "Viene utilizzato per trovare gli elementi che sono in un insieme, ma non negli altri.",
            "esempio": '''
                a = {1, 2, 3}
                b = {2, 3, 4}
                print(a.difference(b))  # Uscita: {1}
                '''
        },
        "difference_update": {
            "significato": "Metodo degli insiemi in Python che rimuove gli elementi di un insieme che sono presenti in un altro insieme.",
            "uso": "Viene utilizzato per modificare un insieme, rimuovendo gli elementi che si trovano in un altro insieme.",
            "esempio": '''
                a = {1, 2, 3}
                b = {2, 3, 4}
                a.difference_update(b)
                print(a)  # Uscita: {1}
                '''
        },
        "decode_header": {
            "significato": "Funzione del modulo `email.header` che decodifica un'intestazione di una e-mail.",
            "uso": "Viene utilizzata per decodificare un'intestazione di e-mail che può essere in diverse codifiche.",
            "esempio": '''
                from email.header import decode_header

                header = '=?utf-8?B?SG9sYSBNdW5kbyA8MTIzNDU+?='
                decoded, encoding = decode_header(header)[0]
                print(decoded.decode(encoding))  # Uscita: Olá Mundo <12345>
                '''
        },
        "disk_usage": {
            "significato": "Funzione del modulo `shutil` che restituisce l'uso del disco di un percorso o directory.",
            "uso": "Viene utilizzata per ottenere informazioni sullo spazio usato e disponibile in un file system.",
            "esempio": '''
                import shutil

                usage = shutil.disk_usage('/')
                print(usage)  # Uscita: usage(total=500000000, used=200000000, free=300000000)
                '''
        },
        "datetime": {
            "significato": "Modulo di Python che fornisce classi per lavorare con date e orari.",
            "uso": "Viene utilizzato per manipolare e lavorare con date, orari e tempi in generale.",
            "esempio": '''
                import datetime

                adesso = datetime.datetime.now()
                print(adesso)  # Uscita: 2024-11-22 12:00:00.123456
                '''
        },
        "disk_cache": {
            "significato": "Memoria cache su disco per migliorare la velocità di accesso a dati o risultati computazionali.",
            "uso": "Viene utilizzato per archiviare temporaneamente risultati o dati su disco per evitare la necessità di ricalcolare o recuperare nuovamente i dati.",
            "esempio": '''
                import joblib

                result = joblib.Memory('cache_dir').cache(some_function)
                '''
        },
    },
    "e": {
        # Aquí puedes agregar funciones que comiencen con la letra E

    "enumerate": {
        "significato": "Funzione incorporata di Python che aggiunge un contatore a un iterabile e lo restituisce come un oggetto iterabile di tuple.",
        "uso": "Viene utilizzato per ottenere sia l'indice che il valore degli elementi in un iterabile.",
        "esempio": '''
            lista = ['a', 'b', 'c']
            for indice, valore in enumerate(lista):
                print(indice, valore)
            # Uscita:
            # 0 a
            # 1 b
            # 2 c
            '''
    },
    "eval": {
        "significato": "Funzione incorporata di Python che valuta una stringa di codice come un'espressione Python.",
        "uso": "Viene utilizzato per eseguire espressioni Python contenute in una stringa e restituire il risultato.",
        "esempio": '''
            x = 2
            risultato = eval('x + 1')
            print(risultato)  # Uscita: 3
            '''
    },
    "exec": {
        "significato": "Funzione incorporata di Python che esegue una stringa di codice come un blocco di codice completo.",
        "uso": "Viene utilizzato per eseguire dinamicamente codice Python.",
        "esempio": '''
            codice = 'for i in range(3): print(i)'
            exec(codice)
            # Uscita:
            # 0
            # 1
            # 2
            '''
    },
    "except": {
        "significato": "Parola chiave in Python utilizzata per trattare le eccezioni all'interno di un blocco try-except.",
        "uso": "Viene utilizzata per catturare e trattare le eccezioni che si verificano nel blocco try.",
        "esempio": '''
            try:
                x = 1 / 0
            except ZeroDivisionError:
                print('Errore: Divisione per zero')
            # Uscita: Errore: Divisione per zero
            '''
    },
    "else": {
        "significato": "Parola chiave in Python utilizzata in strutture di controllo condizionale (if, try) per eseguire un blocco di codice se la condizione non è soddisfatta o se non si verificano eccezioni.",
        "uso": "Viene utilizzata per eseguire un blocco di codice quando la condizione non è soddisfatta o non si verificano eccezioni.",
        "esempio": '''
            if 3 > 1:
                print('Condizione vera')
            else:
                print('Condizione falsa')
            # Uscita: Condizione vera
            '''
    },
    "elif": {
        "significato": "Parola chiave in Python utilizzata in strutture condizionali per verificare una condizione aggiuntiva se le precedenti non sono soddisfatte.",
        "uso": "Viene utilizzata per gestire più condizioni in una struttura if-elif-else.",
        "esempio": '''
            x = 3
            if x > 5:
                print('Maggiore di 5')
            elif x == 3:
                print('Uguale a 3')
            else:
                print('Minore di 3')
            # Uscita: Uguale a 3
            '''
    },
    "exit": {
        "significato": "Funzione incorporata di Python che termina l'esecuzione del programma.",
        "uso": "Viene utilizzata per uscire da un programma o chiudere un ambiente di esecuzione.",
        "esempio": '''
            import sys
            sys.exit('Terminando il programma')
            # Il programma viene interrotto con il messaggio 'Terminando il programma'
            '''
    },
    "end": {
        "significato": "Parola chiave utilizzata in Python per specificare la fine di un blocco o la terminazione di una stringa.",
        "uso": "Viene utilizzata principalmente nelle funzioni di stampa per controllare la fine dell'output.",
        "esempio": '''
            print('Ciao', end=' ')
            print('Mondo')
            # Uscita: Ciao Mondo
            '''
    },
    "expandtabs": {
        "significato": "Metodo di stringhe in Python che sostituisce i caratteri di tabulazione con spazi.",
        "uso": "Viene utilizzato per allineare il testo sostituendo le tabulazioni con un numero specificato di spazi.",
        "esempio": '''
            testo = 'Ciao\tMondo'
            print(testo.expandtabs(4))
            # Uscita: Ciao   Mondo
            '''
    },
    "encode": {
        "significato": "Metodo di stringhe in Python che codifica una stringa in una sequenza di byte usando un codificatore specifico.",
        "uso": "Viene utilizzato per convertire una stringa in una sequenza di byte per essere memorizzata o trasmessa in formati specifici.",
        "esempio": '''
            testo = 'Ciao Mondo'
            encoded = testo.encode('utf-8')
            print(encoded)
            # Uscita: b'Ciao Mondo'
            '''
    },
    "element": {
        "significato": "Un elemento individuale all'interno di una collezione o struttura di dati.",
        "uso": "Viene utilizzato per riferirsi a un oggetto all'interno di una lista, set, dizionario, ecc.",
        "esempio": '''
            lista = [1, 2, 3]
            print(lista[0])  # Uscita: 1
            '''
    },
    "error": {
        "significato": "Condizione anomala nell'esecuzione di un programma che interrompe il flusso normale.",
        "uso": "Viene utilizzata per indicare che qualcosa è andato storto durante l'esecuzione del codice.",
        "esempio": '''
            try:
                1 / 0
            except ZeroDivisionError as e:
                print(f'Errore: {e}')
            # Uscita: Errore: division by zero
            '''
    },
    "exception": {
        "significato": "Evento che altera il flusso normale di esecuzione del programma, generalmente a causa di un errore.",
        "uso": "Viene utilizzato per gestire errori nel codice ed eseguire azioni specifiche quando si verificano.",
        "esempio": '''
            try:
                int('a')
            except ValueError:
                print('Errore: non è possibile convertire in intero')
            # Uscita: Errore: non è possibile convertire in intero
            '''
    },
    "evaluate": {
        "significato": "Eseguire o calcolare il valore di un'espressione o funzione.",
        "uso": "Viene utilizzato per ottenere il risultato di un'espressione.",
        "esempio": '''
            x = 5
            risultato = eval('x + 2')
            print(risultato)  # Uscita: 7
            '''
    },
    "elements": {
        "significato": "Elementi o componenti individuali all'interno di un set o collezione.",
        "uso": "Viene utilizzato per riferirsi alle parti di una struttura di dati.",
        "esempio": '''
            set = {1, 2, 3}
            for elemento in set:
                print(elemento)
            # Uscita:
            # 1
            # 2
            # 3
            '''
    },
    "exponential": {
        "significato": "Relativo all'operazione matematica di esponenziazione, che calcola il valore di una base elevata a un esponente.",
        "uso": "Viene utilizzato per eseguire calcoli esponenziali.",
        "esempio": '''
            import math
            risultato = math.exp(2)
            print(risultato)  # Uscita: 7.3890560989306495
            '''
    },
    "enumerations": {
        "significato": "Una lista o insieme di elementi, spesso con un valore associato o un identificatore.",
        "uso": "Viene utilizzato per rappresentare un insieme di valori possibili per una variabile.",
        "esempio": '''
            from enum import Enum

            class Colore(Enum):
                ROSSO = 1
                VERDE = 2
                BLU = 3

            print(Colore.ROSSO)  # Output: Colore.ROSSO
            '''
    },
    "encode_utf8": {
        "significato": "Metodo di codifica che converte una stringa di caratteri in una sequenza di byte utilizzando il formato UTF-8.",
        "uso": "Viene utilizzato per convertire il testo in una rappresentazione binaria utilizzando UTF-8.",
        "esempio": '''
            testo = 'Ciao Mondo'
            codificato = testo.encode('utf-8')
            print(codificato)  # Output: b'Ciao Mondo'
            '''
    },
    "execfile": {
        "significato": "Funzione che esegue un file Python come se fosse uno script.",
        "uso": "Viene utilizzato per eseguire un file Python esterno.",
        "esempio": '''
            # Questo comando è disponibile solo in Python 2
            execfile('script.py')
            '''
    },
    "edit_distance": {
        "significato": "Misura che calcola la differenza tra due stringhe in base alle operazioni necessarie per trasformarne una nell'altra.",
        "uso": "Viene utilizzato per confrontare quanto siano simili due stringhe e determinare quante modifiche sono necessarie per renderle identiche.",
        "esempio": '''
            from nltk.metrics import edit_distance

            distanza = edit_distance('kitten', 'sitting')
            print(distanza)  # Output: 3
            '''
    },
    "eval_input": {
        "significato": "Funzione che valuta un input dell'utente, normalmente tramite la funzione `input()`.",
        "uso": "Viene utilizzato per ottenere e valutare un input fornito dall'utente.",
        "esempio": '''
            input_utente = input('Inserisci un numero: ')
            risultato = eval(input_utente)
            print(risultato)
            '''
    },
    "xceed": {
        "significato": "Termine usato per descrivere qualcosa che supera o eccede un limite o una aspettativa.",
        "uso": "Viene utilizzato per indicare che qualcosa ha superato uno standard o limite.",
        "esempio": "Il nuovo aggiornamento supera le nostre aspettative in termini di prestazioni."
    },

      "expected": {
        "significato": "Qualcosa che è stato anticipato o previsto, basato su aspettative o previsioni.",            "uso": "Viene utilizzato per descrivere ciò che ci si aspetta che accada in una situazione.",
            "esempio": "Il risultato previsto era un aumento della velocità di elaborazione."
        },
        "encode_base64": {
            "significato": "Metodo di codifica che converte i dati binari in una rappresentazione testuale in base 64.",
            "uso": "Viene utilizzato per codificare dati binari in una stringa di testo leggibile in base 64.",
            "esempio": '''
                import base64
                codificato = base64.b64encode(b'ciao')
                print(codificato)  # Output: b'b2lhbw=='
                '''
        },
        "execute": {
            "significato": "Eseguire o mettere in pratica un insieme di istruzioni o un programma.",
            "uso": "Viene utilizzato per mettere in atto un'azione o eseguire un codice.",
            "esempio": '''
                def funzione():
                    print('Eseguendo...')
                funzione()  # Output: Eseguendo...
                '''
        },
        "exit_code": {
            "significato": "Valore restituito da un programma o script al termine, che indica se è stato eseguito correttamente o se si è verificato un errore.",
            "uso": "Viene utilizzato per verificare se un programma è stato completato con successo o se si è verificato un errore.",
            "esempio": '''
                import sys
                sys.exit(0)  # Output: 0 indica successo, un altro numero indica errore.
                '''
        },
        "evaluate_expression": {
            "significato": "Valutare un'espressione per ottenere il suo risultato.",
            "uso": "Viene utilizzato per calcolare o ottenere il valore di un'espressione matematica o logica.",
            "esempio": '''
                risultato = eval('3 + 5')
                print(risultato)  # Output: 8
                '''
        },
        "environment": {
            "significato": "Il contesto o insieme di condizioni in cui un programma o applicazione viene eseguito.",
            "uso": "Viene utilizzato per riferirsi all'insieme di variabili, configurazioni e risorse disponibili per un programma.",
            "esempio": '''
                import os
                print(os.environ)  # Output: Mostra le variabili di ambiente del sistema.
                '''
        },
        "environment_variable": {
            "significato": "Variabile che memorizza informazioni sull'ambiente del sistema o applicazione.",
            "uso": "Viene utilizzato per memorizzare configurazioni specifiche che influenzano il comportamento dei programmi.",
            "esempio": '''
                import os
                print(os.getenv('PATH'))  # Output: Mostra la variabile di ambiente PATH.
                '''
        },
        "exp": {
            "significato": "Funzione matematica che calcola l'esponenziale di un numero, ovvero e elevato alla potenza di quel numero.",
            "uso": "Viene utilizzato per eseguire calcoli esponenziali.",
            "esempio": '''
                import math
                risultato = math.exp(1)
                print(risultato)  # Output: 2.718281828459045
                '''
        },
        "exception_handling": {
            "significato": "Processo di gestione e risposta agli errori o eccezioni che si verificano durante l'esecuzione di un programma.",
            "uso": "Viene utilizzato per catturare e gestire gli errori, garantendo che il programma non si fermi in modo imprevisto.",
            "esempio": '''
                try:
                    valore = 1 / 0
                except ZeroDivisionError as e:
                    print(f'Errore: {e}')  # Output: Errore: divisione per zero
                '''
        },
        "expand": {
            "significato": "Ampliare o aumentare la dimensione o la portata di qualcosa.",
            "uso": "Viene utilizzato per rendere qualcosa più grande o includere più informazioni.",
            "esempio": '''
                testo = "Ciao"
                print(testo.expandtabs(4))  # Output: 'Ciao' con tabulazioni ampliate
                '''
        },
        "environment_config": {
            "significato": "Configurazione relativa all'ambiente di esecuzione di un programma o sistema.",
            "uso": "Viene utilizzato per specificare o regolare i parametri che influenzano il funzionamento di un programma o applicazione.",
            "esempio": '''
                config = {
                    'host': 'localhost',
                    'port': 8080
                }
                print(config)  # Output: {'host': 'localhost', 'port': 8080}
                '''
        },
        "equal": {
            "significato": "Indica che due elementi sono identici nel valore.",
            "uso": "Viene utilizzato per confrontare due valori o espressioni per verificare se sono uguali.",
            "esempio": '''
                a = 5
                b = 5
                print(a == b)  # Output: True
                '''
        },
        "error_handling": {
            "significato": "Processo di gestione degli errori e delle eccezioni che si verificano durante l'esecuzione di un programma.",
            "uso": "Viene utilizzato per catturare e gestire gli errori in modo controllato, per evitare che il programma termini in modo imprevisto.",
            "esempio": '''
                try:
                    valore = 10 / 0
                except ZeroDivisionError:
                    print('Errore di divisione per zero')  # Output: Errore di divisione per zero
                '''
        },
        "event": {
            "significato": "Azione o evento che può essere rilevato e gestito in un programma.",
            "uso": "Viene utilizzato per gestire e rispondere ad attività o cambiamenti in un sistema o programma.",
            "esempio": '''
                import tkinter as tk
                def clicca():
                    print('Pulsante premuto')
                root = tk.Tk()
                button = tk.Button(root, text="Clicca su di me", command=clicca)
                button.pack()
                root.mainloop()  # Output: Mostra un pulsante che, se premuto, esegue l'evento clicca
                '''
        },
        "event_loop": {
            "significato": "Ciclo continuo che attende e gestisce eventi o attività asincrone in un programma.",
            "uso": "Viene utilizzato per eseguire compiti o rispondere a eventi in ordine, senza bloccare il flusso principale di esecuzione.",
            "esempio": '''
                import asyncio
                async def ciao():
                    print("Ciao")
                asyncio.run(ciao())  # Output: Ciao
                '''
        },
        "exception_type": {
            "significato": "Il tipo specifico di un'eccezione o errore che si verifica in un programma.",
            "uso": "Viene utilizzato per identificare il tipo di errore che si è verificato e prendere le azioni appropriate.",
            "esempio": '''
                try:
                    valore = 10 / 0
                except ZeroDivisionError as e:
                    print(f"Tipo di errore: {type(e)}")  # Output: Tipo di errore: <class 'ZeroDivisionError'>
                '''
        },
        "error_message": {
            "significato": "Messaggio che descrive l'errore o il problema verificatosi durante l'esecuzione di un programma.",
            "uso": "Viene utilizzato per fornire dettagli su cosa ha fallito o ha causato un'eccezione.",
            "esempio": '''
                try:
                    x = int("abc")
                except ValueError as e:
                    print(f"Messaggio di errore: {e}")  # Output: Messaggio di errore: invalid literal for int() with base 10: 'abc'
                '''
        },
        "extract": {
            "significato": "Ottenere una parte specifica di un insieme di dati o informazioni.",
            "uso": "Viene utilizzato per prelevare o estrarre un componente specifico da un insieme più grande di dati.",
            "esempio": '''
                testo = 'Ciao Mondo'
                print(testo[0:4])  # Output: Ciao
                '''
        },
        "exit_status": {
            "significato": "Codice di uscita che indica se un programma o processo è terminato correttamente o con errore.",
            "uso": "Viene utilizzato per verificare se un processo o comando è terminato con successo o se si è verificato un errore.",
            "esempio": '''
                import sys
                sys.exit(0)  # Output: 0 indica successo, qualsiasi altro numero indica errore.
                '''
        },
    },
    "f": {
        # Aquí puedes agregar funciones que comiencen con la letra F
        "filemode": {
            "significato": "Modalità di apertura di un file che determina le operazioni che possono essere eseguite su di esso.",
            "uso": "Viene utilizzata per specificare il tipo di accesso desiderato per un file (lettura, scrittura, ecc.).",
            "esempio": '''
                file = open('file.txt', 'r')  # 'r' indica la modalità di sola lettura
                print(file.mode)  # Output: 'r'
                '''
        },
        "frozen_set": {
            "significato": "Set immutabile in Python, simile a un set standard, ma senza la possibilità di modificarlo dopo la creazione.",
            "uso": "Viene utilizzato per creare set che non devono essere modificati dopo la creazione.",
            "esempio": '''
                set = frozenset([1, 2, 3])
                print(set)  # Output: frozenset({1, 2, 3})
                '''
        },
        "format_map": {
            "significato": "Metodo che restituisce una stringa formattata utilizzando un dizionario o un oggetto simile.",
            "uso": "Viene utilizzato per effettuare sostituzioni di valori in una stringa usando una mappa (come un dizionario).",
            "esempio": '''
                dati = {'nome': 'Giovanni', 'età': 30}
                testo = 'Nome: {nome}, Età: {età}'.format_map(dati)
                print(testo)  # Output: Nome: Giovanni, Età: 30
                '''
        },
        "find": {
            "significato": "Metodo che cerca una sottostringa all'interno di una stringa e restituisce l'indice della prima occorrenza.",
            "uso": "Viene utilizzato per trovare la posizione di un testo all'interno di un altro.",
            "esempio": '''
                testo = 'Ciao Mondo'
                print(testo.find('Mondo'))  # Output: 5
                '''
        },
        "float32": {
            "significato": "Tipo di dato in NumPy che rappresenta un numero in virgola mobile a 32 bit.",
            "uso": "Viene utilizzato per memorizzare numeri decimali in modo più efficiente in termini di memoria.",
            "esempio": '''
                import numpy as np
                numero = np.float32(3.1415)
                print(numero)  # Output: 3.1415
                '''
        },
        "float64": {
            "significato": "Tipo di dato in NumPy che rappresenta un numero in virgola mobile a 64 bit.",
            "uso": "Viene utilizzato per memorizzare numeri decimali con maggiore precisione rispetto al tipo float32.",
            "esempio": '''
                import numpy as np
                numero = np.float64(3.141592653589793)
                print(numero)  # Output: 3.141592653589793
                '''
        },
        "formatting": {
            "significato": "Il processo di applicare un formato ai dati o alle stringhe, come l'allineamento, le larghezze e i tipi di dati.",
            "uso": "Viene utilizzato per organizzare o visualizzare i dati in modo più leggibile o specifico.",
            "esempio": '''
                testo = 'Nome: {0:10}, Età: {1:5}'.format('Giovanni', 30)
                print(testo)  # Output: Nome: Giovanni  , Età: 30
                '''
        },
        "flush_output": {
            "significato": "Metodo utilizzato per svuotare il buffer di uscita, forzando la scrittura immediata dei dati.",
            "uso": "Viene utilizzato quando si vuole garantire che tutti i dati in sospeso nel buffer di uscita vengano scritti nel destino.",
            "esempio": '''
                import sys
                sys.stdout.write('Ciao Mondo')
                sys.stdout.flush()  # Output: 'Ciao Mondo' immediatamente
                '''
        },
        "function_definition": {
            "significato": "Il processo di creazione di una funzione in Python utilizzando la parola chiave 'def'.",
            "uso": "Viene utilizzato per dichiarare funzioni riutilizzabili che eseguono un blocco di codice specifico.",
            "esempio": '''
                def saluta(nome):
                    return f'Ciao {nome}'
                print(saluta('Giovanni'))  # Output: Ciao Giovanni
                '''
        },
        "filepath": {
            "significato": "Percorso o indirizzo di un file nel sistema di file.",
            "uso": "Viene utilizzato per specificare la posizione di un file nel sistema di file.",
            "esempio": '''
                import os
                percorso = os.path.join('cartella', 'file.txt')
                print(percorso)  # Output: cartella/file.txt
                '''
        },
        "flask": {
            "significato": "Un micro-framework in Python per lo sviluppo di applicazioni web.",
            "uso": "Viene utilizzato per creare applicazioni web in modo semplice e veloce con rotte, moduli e altre funzionalità.",
            "esempio": '''
                from flask import Flask
                app = Flask(__name__)

                @app.route('/')
                def ciao():
                    return 'Ciao Mondo'

                app.run()  # Output: 'Ciao Mondo' in una applicazione web
                '''
        },
        "filtering": {
            "significato": "Processo di selezione degli elementi di una collezione che soddisfano una condizione specifica.",
            "uso": "Viene utilizzato per estrarre elementi da una lista, set o qualsiasi iterabile in base a una condizione.",
            "esempio": '''
                lista = [1, 2, 3, 4, 5]
                risultato = filter(lambda x: x > 2, lista)
                print(list(risultato))  # Output: [3, 4, 5]
                '''
        },
        "futures": {
            "significato": "Modulo che fornisce un'interfaccia per eseguire compiti asincroni e parallelizzati.",
            "uso": "Viene utilizzato per eseguire funzioni in modo concorrente utilizzando thread o processi.",
            "esempio": '''
                from concurrent.futures import ThreadPoolExecutor

                def compito(x):
                    return x * x

                with ThreadPoolExecutor() as executor:
                    risultati = executor.map(compito, [1, 2, 3])
                    print(list(risultati))  # Output: [1, 4, 9]
                '''
        },
        "fold": {
            "significato": "Funzione che applica un'operazione cumulativa sugli elementi di una sequenza.",
            "uso": "Viene utilizzata per ridurre una sequenza di elementi a un singolo valore applicando un'operazione binaria.",
            "esempio": '''
                from functools import reduce
                lista = [1, 2, 3, 4]
                risultato = reduce(lambda x, y: x + y, lista)
                print(risultato)  # Output: 10
                '''
        },
        "fromkeys": {
            "significato": "Metodo del dizionario che crea un nuovo dizionario con chiavi specificate e valori predefiniti.",
            "uso": "Viene utilizzato per creare dizionari a partire da una lista di chiavi con un valore predefinito.",
            "esempio": '''
                dizionario = dict.fromkeys(['a', 'b', 'c'], 0)
                print(dizionario)  # Output: {'a': 0, 'b': 0, 'c': 0}
                '''
        },
        "flask_restful": {
            "significato": "Estensione per Flask che semplifica la creazione di API RESTful.",
            "uso": "Viene utilizzato per sviluppare applicazioni web che seguono l'architettura REST utilizzando risorse.",
            "esempio": '''
                from flask import Flask
                from flask_restful import Api, Resource

                app = Flask(__name__)
                api = Api(app)

                class HelloWorld(Resource):
                    def get(self):
                        return {'messaggio': 'Ciao Mondo'}

                api.add_resource(HelloWorld, '/')
                app.run()  # Output: 'Ciao Mondo' come risposta dell'API
                '''
        },
        "fix": {
            "significato": "Termine generale per correggere o regolare qualcosa che non funziona correttamente.",
            "uso": "Viene utilizzato quando si fa un aggiustamento o una correzione nel codice o nella configurazione di qualcosa.",
            "esempio": '''
                # esempio nel contesto del codice: correzione di un errore di sintassi
                def correggere_errore():
                    print('Questo è il messaggio corretto')
                correggere_errore()
                '''
        },
        "float_conversion": {
            "significato": "Processo di conversione di dati da altri tipi al tipo fluttuante.",
            "uso": "Viene utilizzato per convertire valori in numeri decimali (float).",
            "esempio": '''
                numero = '3.14'
                risultato = float(numero)
                print(risultato)  # Output: 3.14
                '''
        },
        "full_path": {
            "significato": "Percorso completo per un file o una cartella nel sistema di file.",
            "uso": "Viene utilizzato per specificare la posizione esatta di un file o una cartella dalla radice del sistema di file.",
            "esempio": '''
                import os
                percorso_completo = os.path.abspath('file.txt')
                print(percorso_completo)  # Output: /home/utente/file.txt
                '''
        },
        "filter": {
            "significato": "Funzione che applica una condizione a ciascun elemento di un iterabile e restituisce gli elementi che soddisfano la condizione.",
            "uso": "Viene utilizzato per selezionare solo gli elementi che soddisfano una condizione specifica.",
            "esempio": '''
                lista = [1, 2, 3, 4, 5]
                risultato = filter(lambda x: x % 2 == 0, lista)
                print(list(risultato))  # Output: [2, 4]
                '''
        },
        "float": {
            "significato": "Tipo di dato in Python per rappresentare numeri in virgola mobile (numeri con decimali).",
            "uso": "Viene utilizzato per rappresentare numeri che richiedono decimali.",
            "esempio": '''
                numero = 3.14
                print(type(numero))  # Output: <class 'float'>
                '''
        },
        "for": {
            "significato": "Parola chiave in Python utilizzata per iterare sugli elementi di un iterabile.",
            "uso": "Viene utilizzata per eseguire un blocco di codice ripetutamente per ogni elemento di un iterabile.",
            "esempio": '''
                for i in range(5):
                    print(i)
                # Output:
                # 0
                # 1
                # 2
                # 3
                # 4
                '''
        },
        "format": {
            "significato": "Metodo utilizzato per formattare le stringhe, inserendo valori al loro interno.",
            "uso": "Viene utilizzato per creare stringhe più leggibili e dinamiche con valori variabili.",
            "esempio": '''
                nome = 'Juan'
                eta = 30
                print('Il mio nome è {} e ho {} anni'.format(nome, eta))
                # Output: Il mio nome è Juan e ho 30 anni
                '''
        },
        "from": {
            "significato": "Parola chiave in Python utilizzata per importare moduli o funzioni specifiche da un modulo.",
            "uso": "Viene utilizzata per portare funzionalità specifiche da un modulo nello spazio dei nomi corrente.",
            "esempio": '''
                from math import sqrt
                print(sqrt(16))  # Output: 4.0
                '''
        },
        "function": {
            "significato": "Blocco di codice progettato per eseguire un compito specifico e che può essere riutilizzato.",
            "uso": "Viene utilizzato per raggruppare codice correlato che esegue un compito comune, permettendo riutilizzo e modularità.",
            "esempio": '''
                def saluto(nome):
                    return f'Ciao, {nome}'
                
                print(saluto('Juan'))  # Output: Ciao, Juan
                '''
        },
        "fibonacci": {
            "significato": "Sequenza matematica in cui ogni numero è la somma dei due precedenti.",
            "uso": "Viene utilizzata per generare la sequenza di Fibonacci, spesso in esercizi di programmazione o algoritmi.",
            "esempio": '''
                def fibonacci(n):
                    if n <= 1:
                        return n
                    else:
                        return fibonacci(n-1) + fibonacci(n-2)
                
                print(fibonacci(5))  # Output: 5
                '''
        },
        "file": {
            "significato": "Oggetto in Python che permette di interagire con i file nel sistema di file.",
            "uso": "Viene utilizzato per aprire, leggere, scrivere e manipolare i file.",
            "esempio": '''
                with open('file.txt', 'r') as f:
                    contenuto = f.read()
                print(contenuto)
                '''
        },
        "fwrite": {
            "significato": "Funzione utilizzata per scrivere dati in un file.",
            "uso": "Viene utilizzata per scrivere dati binari in un file aperto in modalità scrittura.",
            "esempio": '''
                with open('file.bin', 'wb') as f:
                    f.write(b'Ciao, Mondo!')
                '''
        },
        "fread": {
            "significato": "Funzione utilizzata per leggere dati da un file.",
            "uso": "Viene utilizzata per leggere dati binari da un file aperto in modalità lettura.",
            "esempio": '''
                with open('file.bin', 'rb') as f:
                    dati = f.read()
                print(dati)  # Output: b'Ciao, Mondo!'
                '''
        },
        "finally": {
            "significato": "Parola chiave in Python che definisce un blocco di codice che verrà eseguito sempre, indipendentemente dal fatto che si verifichi o meno un'eccezione.",
            "uso": "Viene utilizzata nelle strutture try-except per garantire che un blocco di codice finale venga eseguito, anche se si verifica un errore.",
            "esempio": '''
                try:
                    x = 1 / 0
                except ZeroDivisionError:
                    print('Divisione per zero')
                finally:
                    print('Questo blocco viene sempre eseguito')
                '''
        },
        "freeze": {
            "significato": "Processo di conversione di un oggetto mutabile in un oggetto immutabile.",
            "uso": "Viene utilizzato per evitare che un oggetto venga modificato dopo essere stato creato.",
            "esempio": '''
                # Non esiste una funzione esplicita chiamata freeze, ma in alcuni casi come con `frozenset` si può ottenere lo stesso effetto
                a = frozenset([1, 2, 3])
                print(a)  # Output: frozenset({1, 2, 3})
                '''
        },
        "flush": {
            "significato": "Metodo utilizzato per svuotare i buffer di un file, garantendo che tutti i dati vengano scritti su disco.",
            "uso": "Viene utilizzato quando è necessario garantire che i dati memorizzati in un buffer vengano scritti immediatamente nel file.",
            "esempio": '''
                with open('file.txt', 'w') as f:
                    f.write('Ciao')
                    f.flush()  # Garantisce che i dati vengano scritti nel file
                '''
        },
        "fstring": {
            "significato": "Stringa che permette di inserire espressioni all'interno della stringa in modo più leggibile ed efficiente.",
            "uso": "Viene utilizzata per creare stringhe interpolate, dove le variabili possono essere inserite direttamente nella stringa.",
            "esempio": '''
                nome = 'Juan'
                eta = 30
                print(f'Il mio nome è {nome} e ho {eta} anni')  # Output: Il mio nome è Juan e ho 30 anni
                '''
        },
        "factorial": {
            "significato": "Funzione matematica che calcola il prodotto di tutti i numeri interi positivi fino a un numero dato.",
            "uso": "Viene utilizzata per calcolare il fattoriale di un numero, spesso in algoritmi di combinatoria e probabilità.",
            "esempio": '''
                import math
                print(math.factorial(5))  # Output: 120
                '''
        },
        "frozen": {
            "significato": "Oggetto immutabile che non può essere modificato dopo la sua creazione.",
            "uso": "Viene utilizzato per creare oggetti che non possono essere alterati, come un `frozenset` in Python.",
            "esempio": '''
                a = frozenset([1, 2, 3])
                print(a)  # Output: frozenset({1, 2, 3})
                '''
        },
        "filterfalse": {
            "significato": "Funzione che restituisce un iteratore che filtra gli elementi di un iterabile, escludendo quelli che restituiscono `True` nella funzione fornita.",
            "uso": "Viene utilizzato per ottenere gli elementi di un iterabile per i quali la funzione restituisce `False`.",
            "esempio": '''
                from itertools import filterfalse
                risultato = filterfalse(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])
                print(list(risultato))  # Output: [1, 3, 5]
                '''
        },
        "fuzzy": {
            "significato": "Relativo alla logica fuzzy, che consente di trattare informazioni imprecise o incerte.",
            "uso": "Viene utilizzato in sistemi che devono elaborare dati approssimativi o incerti.",
            "esempio": '''
                # esempio di una libreria di logica fuzzy come `fuzzywuzzy` (per la corrispondenza fuzzy di testo)
                from fuzzywuzzy import fuzz
                print(fuzz.ratio('hola', 'Hola'))  # Output: 100
                '''
        },
        "fibonacci_sequence": {
            "significato": "Sequenza matematica in cui ogni numero è la somma dei due precedenti.",
            "uso": "Viene utilizzato per generare la sequenza di Fibonacci.",
            "esempio": '''
                def fibonacci(n):
                    sequenza = [0, 1]
                    while len(sequenza) < n:
                        sequenza.append(sequenza[-1] + sequenza[-2])
                    return sequenza
                
                print(fibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
                '''
        },
        "format_spec": {
            "significato": "Stringa utilizzata per definire come i valori devono essere presentati all'interno di una stringa formattata.",
            "uso": "Viene utilizzato per specificare il formato dei valori all'interno di una stringa, come la precisione decimale, l'allineamento, ecc.",
            "esempio": '''
                pi = 3.14159
                print(f'{pi:.2f}')  # Output: 3.14
                '''
        },
        "fork": {
            "significato": "Processo di creare un nuovo processo, copiato dal processo originale.",
            "uso": "Viene utilizzato nella programmazione di sistemi per creare processi secondari.",
            "esempio": '''
                import os
                pid = os.fork()
                if pid > 0:
                    print(f'Processo padre, PID: {pid}')
                else:
                    print(f'Processo figlio, PID: {os.getpid()}')
                '''
        },
        "forking": {
            "significato": "Azione di creare un nuovo processo o sottoprocesso a partire da un processo principale.",
            "uso": "Viene utilizzato nei sistemi operativi per creare processi aggiuntivi che eseguono compiti in modo concorrente.",
            "esempio": '''
                import os
                pid = os.fork()
                # Simile all'esempio di 'fork', ma comprendendo il concetto di 'forking'
                '''
        },
        "first": {
            "significato": "Azione di ottenere il primo elemento di una sequenza o iterabile.",
            "uso": "Viene utilizzato per accedere al primo valore di un iterabile, come una lista o un insieme.",
            "esempio": '''
                lista = [1, 2, 3, 4]
                print(lista[0])  # Output: 1
                '''
        },
        "float_format": {
            "significato": "Formato che definisce come i numeri in virgola mobile devono essere presentati all'interno di una stringa.",
            "uso": "Viene utilizzato per specificare quante cifre decimali devono essere mostrate in un numero in virgola mobile.",
            "esempio": '''
                pi = 3.14159
                print(f'{pi:.2f}')  # Output: 3.14
                '''
        },
        
        "filter_none": {
            "significato": "Funzione che filtra gli elementi di un iterabile, escludendo i valori `None`.",
            "uso": "Viene utilizzato per escludere i valori `None` da una sequenza.",
            "esempio": '''
                lista = [1, None, 2, None, 3]
                risultato = filter(None, lista)
                print(list(risultato))  # Output: [1, 2, 3]
                '''
        },
        "func_code": {
            "significato": "Attributo che contiene il bytecode della funzione in Python.",
            "uso": "Viene utilizzato per accedere al codice della funzione, generalmente in contesti di debug o analisi.",
            "esempio": '''
                def esempio():
                    pass
                
                print(esempio.__code__)  # Output: <code object esempio at 0x...>
                '''
        },
        "float_power": {
            "significato": "Funzione che calcola un numero elevato a una potenza in virgola mobile.",
            "uso": "Viene utilizzato per eseguire esponenziazione con numeri in virgola mobile.",
            "esempio": '''
                print(pow(2, 3.5))  # Output: 11.313708498984761
                '''
        },
        "format_string": {
            "significato": "Stringa che definisce la struttura di un valore che si desidera mostrare, utilizzando specificatori di formato.",
            "uso": "Viene utilizzato per definire come i valori devono essere visualizzati in una stringa, come il numero di decimali o l'allineamento.",
            "esempio": '''
                nome = 'Juan'
                eta = 25
                print(f'Nome: {nome}, Età: {eta}')  # Output: Nome: Juan, Età: 25
                '''
        },
        "filename": {
            "significato": "Stringa che rappresenta il nome di un file nel sistema di file.",
            "uso": "Viene utilizzato per specificare il nome e la posizione di un file che si desidera manipolare.",
            "esempio": '''
                file = 'documento.txt'
                with open(file, 'r') as f:
                    print(f.read())
                '''
        },
        "file_object": {
            "significato": "Oggetto che rappresenta un file aperto in Python, tramite il quale è possibile leggere, scrivere o manipolare il file.",
            "uso": "Viene utilizzato per interagire con file aperti in Python, accedendo o modificando il loro contenuto.",
            "esempio": '''
                with open('documento.txt', 'r') as f:
                    contenuto = f.read()
                    print(contenuto)
                '''
        },
        "finally_clause": {
            "significato": "Parte di un blocco di codice che viene sempre eseguita dopo un'istruzione `try`, indipendentemente dal fatto che venga generata un'eccezione o meno.",
            "uso": "Viene utilizzata per eseguire codice di pulizia o finalizzazione, come la chiusura dei file o il rilascio di risorse.",
            "esempio": '''
                try:
                    file = open('documento.txt', 'r')
                    contenuto = file.read()
                finally:
                    file.close()
                    print('File chiuso')
                '''
        },
        "file_read": {
            "significato": "Operazione che consente di leggere il contenuto di un file in Python.",
            "uso": "Viene utilizzato per ottenere i dati memorizzati in un file per il processamento o la visualizzazione.",
            "esempio": '''
                with open('documento.txt', 'r') as file:
                    contenuto = file.read()
                    print(contenuto)
                '''
        },
        "form": {
            "significato": "Struttura o modello utilizzato per organizzare i dati in modo specifico.",
            "uso": "Viene utilizzato in interfacce utente o applicazioni web per acquisire e organizzare i dati dell'utente.",
            "esempio": '''
                modulo = {'nome': 'Juan', 'età': 25}
                print(modulo)
                '''
        },
        "function_call": {
            "significato": "Azione di invocare una funzione nel codice, passando i parametri necessari per eseguire il suo compito.",
            "uso": "Viene utilizzato per eseguire una funzione e ottenere il suo risultato.",
            "esempio": '''
                def somma(a, b):
                    return a + b
                risultato = somma(3, 4)
                print(risultato)  # Output: 7
                '''
        },
        "force": {
            "significato": "Azione di imporre o forzare l'esecuzione di qualcosa, generalmente nel contesto della programmazione o manipolazione degli oggetti.",
            "uso": "Viene utilizzato per forzare un comportamento specifico in un programma, come evitare errori o eseguire un'azione indipendentemente dalle condizioni.",
            "esempio": '''
                # Non esiste un 'force' diretto in Python, ma è possibile usare 'assert' per forzare condizioni
                assert 1 == 1, 'Condizione falsa'
                '''
        },
        "function_pointer": {
            "significato": "Riferimento a una funzione che può essere passato ed eseguito come argomento.",
            "uso": "Viene utilizzato in linguaggi come C o C++ per fare riferimento a funzioni e passarle come parametri.",
            "esempio": '''
                # In Python non esiste un puntatore di funzione diretto, ma le funzioni possono essere passate come oggetti
                def saluto():
                    print('Ciao')
                funzione = saluto
                funzione()  # Output: Ciao
                '''
        },
        "float_precision": {
            "significato": "Numero di cifre utilizzate per rappresentare un numero in virgola mobile con precisione.",
            "uso": "Viene utilizzato per specificare la quantità di decimali da considerare quando si effettuano operazioni con numeri in virgola mobile.",
            "esempio": '''
                numero = 3.14159265359
                print(f'{numero:.2f}')  # Output: 3.14
                '''
        },
        "format_error": {
            "significato": "Errore che si verifica quando c'è un problema nel formattare i dati, come una stringa mal strutturata.",
            "uso": "Viene utilizzato per gestire errori relativi alla conversione o formattazione errata dei dati.",
            "esempio": '''
                try:
                    int('abc')
                except ValueError as e:
                    print(f'Errore di formato: {e}')
                '''
        },
        "file_write": {
            "significato": "Operazione che permette di scrivere dati in un file in Python.",
            "uso": "Viene utilizzato per memorizzare informazioni in un file, sovrascrivendo o aggiungendo nuovi dati.",
            "esempio": '''
                with open('documento.txt', 'w') as file:
                    file.write('Ciao, mondo!')
                '''
        }

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