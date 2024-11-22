diccionario_por = {
    "a": {
        "abs": {
            "significado": "Retorna o valor absoluto de um número.",
            "uso": "É usado para obter a magnitude de um número sem considerar o seu sinal.",
            "ejemplo": '''
                numero1 = -10
                print(abs(numero1))  # Saída: 10
                '''
        },
        "absolute_import": {
            "significado": "Diretiva usada para habilitar importações absolutas no Python 2.x e versões posteriores.",
            "uso": "É usado para evitar conflitos entre módulos locais e globais.",
            "ejemplo": '''
                from __future__ import absolute_import

                # Sempre importa o módulo global, não um local com o mesmo nome
                import math
                '''
        },
        "add": {
            "significado": "Método usado para adicionar um elemento a um conjunto ou realizar uma soma entre matrizes (dependendo do contexto).",
            "uso": "É usado em conjuntos para adicionar elementos ou no NumPy para realizar operações matemáticas.",
            "ejemplo": '''
                # Conjuntos
                conjunto = {1, 2, 3}
                conjunto.add(4)
                print(conjunto)  # Saída: {1, 2, 3, 4}

                # NumPy
                import numpy as np
                resultado = np.add(2, 3)
                print(resultado)  # Saída: 5
                '''
        },
        "all": {
            "significado": "Retorna True se todos os elementos de um iterável forem verdadeiros (ou se o iterável estiver vazio).",
            "uso": "É usado para verificar se todos os valores de um iterável atendem a uma condição.",
            "ejemplo": '''
                lista = [True, True, True]
                print(all(lista))  # Saída: True

                numeros = [1, 2, 0]
                print(all(numeros))  # Saída: False (0 é avaliado como False)
                '''
        },
        "allclose": {
            "significado": "Verifica se todos os elementos de dois arrays são aproximadamente iguais.",
            "uso": "É usado no NumPy para verificar a igualdade de elementos com tolerância a pequenas diferenças.",
            "ejemplo": '''
                import numpy as np

                a = [1.0, 2.001]
                b = [1.0, 2.0009]
                print(np.allclose(a, b, atol=0.01))  # Saída: True
                '''
        },
        "allexcept": {
            "significado": "Não é um termo nativo do Python. Pode se referir a uma abordagem lógica que aplica operações a todos os elementos, exceto alguns específicos.",
            "uso": "Geralmente implementado manualmente.",
            "ejemplo": '''
                lista = [1, 2, 3, 4]
                resultado = [x for x in lista if x != 2]  # Filtra todos, exceto o 2
                print(resultado)  # Saída: [1, 3, 4]
                '''
        },
        "any": {
            "significado": "Retorna True se pelo menos um elemento de um iterável for verdadeiro (ou se o iterável estiver vazio).",
            "uso": "É usado para verificar se pelo menos um valor de um iterável atende a uma condição.",
            "ejemplo": '''
                lista = [False, False, True]
                print(any(lista))  # Saída: True

                numeros = [0, 0, 0]
                print(any(numeros))  # Saída: False
            '''
        },
        "append": {
            "significado": "Adiciona um elemento ao final de uma lista.",
            "uso": "É usado para adicionar novos elementos a uma lista existente.",
            "ejemplo": '''
                lista = [1, 2, 3]
                lista.append(4)
                print(lista)  # Saída: [1, 2, 3, 4]
            '''
        },
        "apply": {
            "significado": "Método usado no pandas para aplicar uma função a linhas ou colunas de um DataFrame.",
            "uso": "É usado para realizar operações personalizadas em linhas ou colunas.",
            "ejemplo": '''
                import pandas as pd

                dados = pd.DataFrame({'A': [1, 2, 3]})
                dados['B'] = dados['A'].apply(lambda x: x * 2)
                print(dados)
                # Saída:
                #    A  B
                # 0  1  2
                # 1  2  4
                # 2  3  6
                '''
        },
        "argmin": {
            "significado": "Retorna o índice do valor mínimo em um array ou iterável.",
            "uso": "É usado em bibliotecas como NumPy para localizar o índice do menor valor em estruturas de dados.",
            "ejemplo": '''
                import numpy as np

                numeros = [1, 5, 2, 9, 3]
                print(np.argmin(numeros))  # Saída: 0 (índice do valor 1)
            '''
        },
        "array": {
            "significado": "É uma estrutura de dados que contém múltiplos elementos do mesmo tipo, comumente utilizada em bibliotecas como NumPy.",
            "uso": "É usada para armazenar e operar eficientemente com grandes quantidades de dados homogêneos.",
            "ejemplo": '''
                import numpy as np

                numeros = np.array([1, 2, 3, 4])
                print(numeros)  # Saída: [1 2 3 4]
            '''
        },
        "args": {
            "significado": "É um parâmetro que permite receber um número variável de argumentos posicionais em uma função.",
            "uso": "É usado para lidar com múltiplos argumentos em uma função sem especificar cada um individualmente.",
            "ejemplo": '''
                def soma(*args):
                    return sum(args)

                print(soma(1, 2, 3))  # Saída: 6
                '''
        },
        "arccos": {
            "significado": "Retorna o arco cosseno (em radianos) de um valor.",
            "uso": "É usado em cálculos trigonométricos com o NumPy.",
            "ejemplo": '''
                import numpy as np

                resultado = np.arccos(0.5)
                print(resultado)  # Saída: 1.0471975511965976 (equivalente a π/3)
                '''
        },
        "arcsin": {
            "significado": "Retorna o arco seno (em radianos) de um valor.",
            "uso": "É usado em cálculos trigonométricos com o NumPy.",
            "ejemplo": '''
                import numpy as np

                resultado = np.arcsin(0.5)
                print(resultado)  # Saída: 0.5235987755982988 (equivalente a π/6)
                '''
        },
        "arctan": {
            "significado": "Retorna o arco tangente (em radianos) de um valor.",
            "uso": "É usado em cálculos trigonométricos com o NumPy.",
            "ejemplo": '''
                import numpy as np

                resultado = np.arctan(1)
                print(resultado)  # Saída: 0.7853981633974483 (equivalente a π/4)
                '''
        },
        "argparse": {
            "significado": "Módulo do Python usado para gerenciar argumentos e opções de linha de comando.",
            "uso": "É usado para criar interfaces de linha de comando fáceis de usar.",
            "ejemplo": '''
                import argparse

                parser = argparse.ArgumentParser(description='ejemplo de argparse')
                parser.add_argument('--nome', type=str, help='Seu nome')
                args = parser.parse_args()
                print(f'Olá, {args.nome}')
                '''
        },
        "array_like": {
            "significado": "Refere-se a qualquer objeto que possa ser tratado como um array, como listas, tuplas ou arrays do NumPy.",
            "uso": "É usado como entrada em funções do NumPy ou similares para operações com dados.",
            "ejemplo": '''
                import numpy as np

                lista = [1, 2, 3]
                array = np.array(lista)  # lista é array_like
                print(array)  # Saída: [1 2 3]
                '''
        },
        "arange": {
            "significado": "Gera um array com valores igualmente espaçados dentro de um intervalo.",
            "uso": "É usado no NumPy para criar sequências numéricas.",
            "ejemplo": '''
                import numpy as np

                resultado = np.arange(0, 10, 2)
                print(resultado)  # Saída: [0 2 4 6 8]
                '''
        },
        "argmax": {
            "significado": "Retorna o índice do valor máximo em um array ou iterável.",
            "uso": "É usado em bibliotecas como NumPy para localizar o índice do maior valor em estruturas de dados.",
            "ejemplo": '''
                import numpy as np

                numeros = [1, 5, 2, 9, 3]
                print(np.argmax(numeros))  # Saída: 3 (índice do valor 9)
            '''
        },
        "as": {
            "significado": "Palavra-chave usada para atribuir um alias a módulos ou em declarações `with`.",
            "uso": "Facilita a referência de nomes longos ou específicos no código.",
            "ejemplo": '''
                import numpy as np

                with open('arquivo.txt', 'r') as arquivo:
                    conteudo = arquivo.read()
                '''
        },
        "assert": {
            "significado": "Avalia uma expressão e gera uma exceção `AssertionError` se a expressão for falsa.",
            "uso": "É usado para verificar condições que devem ser atendidas durante a execução do programa.",
            "ejemplo": '''
                x = 5
                assert x > 0, 'x deve ser maior que 0'  # Não gera erro
                assert x < 0, 'x deve ser menor que 0'  # Gera AssertionError
                '''
        },
        "async": {
            "significado": "Define uma função assíncrona que pode ser usada com `await`.",
            "uso": "É usado para implementar programação assíncrona em Python.",
            "ejemplo": '''
                import asyncio

                async def saudacao():
                    print('Olá')
                    await asyncio.sleep(1)
                    print('Adeus')

                asyncio.run(saudacao())
                '''
        },
        "assertEqual": {
            "significado": "Verifica se dois valores são iguais em um teste unitário.",
            "uso": "É usado em testes unitários para validar a igualdade de valores esperados e reais.",
            "ejemplo": '''
                import unittest

                class Teste(unittest.TestCase):
                    def test_soma(self):
                        self.assertEqual(1 + 1, 2)  # O teste passa
                '''
        },
        "assertIsNone": {
            "significado": "Verifica se um valor é None em um teste unitário.",
            "uso": "É usado em testes unitários para validar que um valor seja None.",
            "ejemplo": '''
                import unittest

                class Teste(unittest.TestCase):
                    def test_valor_none(self):
                        self.assertIsNone(None)  # O teste passa
                '''
        },
        "assertAlmostEqual": {
            "significado": "Verifica se dois valores são aproximadamente iguais até um número específico de casas decimais em um teste unitário.",
            "uso": "É usado em testes unitários para validar valores com tolerância a diferenças pequenas.",
            "ejemplo": '''
                import unittest

                class Teste(unittest.TestCase):
                    def test_aproximacao(self):
                        self.assertAlmostEqual(3.14159, 3.14, places=2)  # O teste passa
                '''
        },
        "as_tuple": {
            "significado": "Método que converte um objeto em uma tupla (comum em bibliotecas como o SymPy).",
            "uso": "É usado para transformar objetos em representações de tuplas.",
            "ejemplo": '''
                from sympy import Point

                p = Point(2, 3)
                print(p.as_tuple())  # Saída: (2, 3)
                '''
        },
        "ascii": {
            "significado": "Retorna uma representação legível de um objeto usando caracteres ASCII.",
            "uso": "É usado para representar strings ou caracteres em um formato seguro em ASCII, substituindo caracteres não ASCII por sequências de escape.",
            "ejemplo": '''
                texto = "Olá, como você está?"
                print(ascii(texto))  # Saída: 'Ol\\xe1, como voc\\xea est\\xe1?'
            '''
        },
        "at": {
            "significado": "Método usado para acessar elementos específicos em estruturas como DataFrames ou arrays (geralmente no pandas).",
            "uso": "É usado para acessar rapidamente um valor individual em uma posição específica.",
            "ejemplo": '''
                import pandas as pd

                dados = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
                print(dados.at[0, 'A'])  # Saída: 1
                '''
        },
        "attribute": {
            "significado": "Refere-se a uma propriedade ou característica associada a um objeto em Python.",
            "uso": "É usado para acessar ou modificar propriedades de objetos criados a partir de classes.",
            "ejemplo": '''
                class Pessoa:
                    def __init__(self, nome, idade):
                        self.nome = nome
                        self.idade = idade

                p = Pessoa('João', 30)
                print(p.nome)  # Saída: João
                p.idade = 31
                print(p.idade)  # Saída: 31
                '''
        },
        "attributeError": {
            "significado": "É uma exceção que ocorre quando se tenta acessar ou atribuir um atributo que não existe.",
            "uso": "É usado para capturar e tratar erros relacionados a atributos inválidos.",
            "ejemplo": '''
                try:
                    objeto = 5
                    objeto.atributo = 10
                except AttributeError as e:
                    print('Erro:', e)
                # Saída: Erro: 'int' object has no attribute 'atributo'
                '''
        },
        "atleast_1d": {
            "significado": "Converte entradas em arrays com pelo menos uma dimensão.",
            "uso": "É usado no NumPy para garantir que os dados tenham uma dimensão mínima.",
            "ejemplo": '''
                import numpy as np

                resultado = np.atleast_1d(5)
                print(resultado)  # Saída: [5]
                '''
        },
        "atleast_2d": {
            "significado": "Converte entradas em arrays com pelo menos duas dimensões.",
            "uso": "É usado no NumPy para trabalhar com dados no formato de matriz.",
            "ejemplo": '''
                import numpy as np

                resultado = np.atleast_2d([1, 2, 3])
                print(resultado)
                # Saída:
                # [[1 2 3]]
                '''
        },
        "average": {
            "significado": "Calcula a média dos elementos de um array ou lista.",
            "uso": "É usado no NumPy para calcular médias, com possibilidade de ponderar valores.",
            "ejemplo": '''
                import numpy as np

                valores = [1, 2, 3, 4]
                print(np.average(valores))  # Saída: 2.5
                '''
        },
        "await": {
            "significado": "É usado para aguardar o resultado de uma função assíncrona.",
            "uso": "É utilizado dentro de funções definidas com `async` para pausar sua execução até que uma tarefa assíncrona seja concluída.",
            "ejemplo": '''
                import asyncio

                async def tarefa():
                    await asyncio.sleep(1)
                    return 'Tarefa concluída'

                async def main():
                    resultado = await tarefa()
                    print(resultado)

                asyncio.run(main())
                '''
        },
    },
    "b": {
        "bin": {
            "significado": "Converte um número em sua representação binária como uma string.",
            "uso": "É utilizado para obter a representação binária de um número inteiro.",
            "ejemplo": '''
                numero = 10
                print(bin(numero))  # Saída: '0b1010'
                '''
        },
        "bool": {
            "significado": "Tipo de dado que representa valores booleanos: True ou False.",
            "uso": "É utilizado para representar e operar com valores de verdade.",
            "ejemplo": '''
                valor = bool(1)
                print(valor)  # Saída: True
                '''
        },
        "break": {
            "significado": "Palavra-chave que termina a execução de um loop.",
            "uso": "É utilizado para sair de um loop de forma antecipada.",
            "ejemplo": '''
                for i in range(5):
                    if i == 3:
                        break
                    print(i)  # Saída: 0 1 2
                '''
        },
        "bytes": {
            "significado": "Tipo de dado imutável que representa uma sequência de bytes.",
            "uso": "É utilizado para trabalhar com dados binários.",
            "ejemplo": '''
                b = bytes([65, 66, 67])
                print(b)  # Saída: b'ABC'
                '''
        },
        "bytearray": {
            "significado": "Tipo de dado mutável que representa uma sequência de bytes.",
            "uso": "É utilizado para modificar sequências de bytes.",
            "ejemplo": '''
                b = bytearray([65, 66, 67])
                b[0] = 90
                print(b)  # Saída: bytearray(b'ZBC')
                '''
        },
        "byteswap": {
            "significado": "Método que troca a ordem dos bytes em um objeto.",
            "uso": "É utilizado para alterar a ordem dos bytes em um tipo de dado numérico.",
            "ejemplo": '''
                import numpy as np

                a = np.array([1, 256], dtype=np.int16)
                a = a.byteswap()
                print(a)  # Saída: [256 1]
                '''
        },
        "buffer": {
            "significado": "Uma classe em Python que fornece uma visão de acesso a uma área de memória de um objeto.",
            "uso": "É utilizado para acessar a memória de forma eficiente, especialmente em operações com grandes quantidades de dados.",
            "ejemplo": '''
                buffer = memoryview(b'abc')
                print(buffer[0])  # Saída: 97 (equivalente a 'a')
                '''
        },
        "base64": {
            "significado": "Módulo que fornece funções para codificar e decodificar dados em base64.",
            "uso": "É utilizado para representar dados binários em uma string de caracteres ASCII.",
            "ejemplo": '''
                import base64

                encoded = base64.b64encode(b'abc')
                print(encoded)  # Saída: b'YWJj'
                '''
        },
        "bitwise_and": {
            "significado": "Operador que realiza uma operação AND bit a bit entre dois números.",
            "uso": "É utilizado para comparar os bits correspondentes de dois números e devolver 1 somente se ambos os bits forem 1.",
            "ejemplo": '''
                x = 5  # binário: 0101
                y = 3  # binário: 0011
                print(x & y)  # Saída: 1 (binário: 0001)
                '''
        },
        "bitwise_or": {
            "significado": "Operador que realiza uma operação OR bit a bit entre dois números.",
            "uso": "É utilizado para comparar os bits correspondentes de dois números e devolver 1 se pelo menos um dos bits for 1.",
            "ejemplo": '''
                x = 5  # binário: 0101
                y = 3  # binário: 0011
                print(x | y)  # Saída: 7 (binário: 0111)
                '''
        },
        "bitwise_xor": {
            "significado": "Operador que realiza uma operação XOR bit a bit entre dois números.",
            "uso": "É utilizado para comparar os bits correspondentes de dois números e devolver 1 se os bits forem diferentes.",
            "ejemplo": '''
                x = 5  # binário: 0101
                y = 3  # binário: 0011
                print(x ^ y)  # Saída: 6 (binário: 0110)
                '''
        },
        "bitwise_not": {
        "significado": "Operador que realiza uma operação NOT bit a bit sobre um número.",
        "uso": "É utilizado para inverter todos os bits de um número.",
        "ejemplo": '''
            x = 5  # binário: 0101
            print(~x)  # Saída: -6 (binário: 1010)
            '''
        },
        "binomial": {
            "significado": "Função que calcula o coeficiente binomial (n sobre k).",
            "uso": "É utilizado para calcular o número de formas de selecionar k elementos de um conjunto de n elementos.",
            "ejemplo": '''
                from scipy.special import comb

                resultado = comb(5, 2)
                print(resultado)  # Saída: 10.0
                '''
        },
        "binascii": {
            "significado": "Módulo que contém funções para converter entre binário e diferentes representações de texto.",
            "uso": "É utilizado para realizar conversões entre strings de texto e dados binários.",
            "ejemplo": '''
                import binascii

                encoded = binascii.hexlify(b'abc')
                print(encoded)  # Saída: b'616263'
                '''
        },
        "byteorder": {
            "significado": "Indica a ordem dos bytes para representar números na memória.",
            "uso": "É utilizado para manipular a representação de números em sistemas com diferentes arquiteturas.",
            "ejemplo": '''
                import sys

                print(sys.byteorder)  # Saída: 'little' ou 'big'
                '''
        },
        "bit_length": {
            "significado": "Retorna o número de bits necessários para representar um número em binário.",
            "uso": "É utilizado para obter o comprimento em bits de um número inteiro.",
            "ejemplo": '''
                numero = 10
                print(numero.bit_length())  # Saída: 4
                '''
        },
        "breakpoint": {
            "significado": "Uma função que estabelece um ponto de interrupção no código, ativando o depurador.",
            "uso": "É utilizado para pausar a execução e entrar no depurador interativo.",
            "ejemplo": '''
                def funcao():
                    breakpoint()  # Interrupção aqui
                    print('Olá')
                funcao()
                '''
        },
        "binhex": {
            "significado": "Função para converter um arquivo binário em formato hexadecimal.",
            "uso": "É utilizado para representar dados binários em formato legível em hexadecimal.",
            "ejemplo": '''
                import binhex

                with open('arquivo.bin', 'rb') as f:
                    binhex.binhex(f, 'arquivo.hex')
                '''
        },
        "bitset": {
            "significado": "Estrutura de dados que permite armazenar uma coleção de bits.",
            "uso": "É utilizado para representar conjuntos de bits e realizar operações eficientes sobre eles.",
            "ejemplo": '''
                # ejemplo não padrão em Python, mas pode-se usar o módulo `bitarray` para criar bitsets
                from bitarray import bitarray

                bitset = bitarray('10101')
                print(bitset)  # Saída: bitarray('10101')
                '''
        },
        "broadcast": {
            "significado": "Técnica que permite que arrays de formas diferentes sejam alinhados para realizar operações element-wise.",
            "uso": "É utilizado principalmente no NumPy para operações com arrays de tamanhos diferentes.",
            "ejemplo": '''
                import numpy as np

                a = np.array([1, 2, 3])
                b = np.array([[1], [2], [3]])
                resultado = a + b
                print(resultado)
                # Saída:
                # [[2 3 4]
                #  [3 4 5]
                #  [4 5 6]]
                '''
        },
        "bitarray": {
            "significado": "Módulo que implementa um tipo de dado eficiente para trabalhar com arrays de bits.",
            "uso": "É utilizado para manipular e gerenciar arrays de bits de forma eficiente.",
            "ejemplo": '''
                from bitarray import bitarray

                a = bitarray('10101')
                a.append('1')
                print(a)  # Saída: bitarray('101011')
                '''
        },
        "buffer": {
            "significado": "Uma classe em Python que fornece uma visão de acesso a uma área de memória de um objeto.",
            "uso": "É utilizado para acessar a memória de maneira eficiente, especialmente em operações com grandes quantidades de dados.",
            "ejemplo": '''
                buffer = memoryview(b'abc')
                print(buffer[0])  # Saída: 97 (equivalente a 'a')
                '''
        },
        "bitwise_left_shift": {
            "significado": "Operador que realiza um deslocamento de bits para a esquerda.",
            "uso": "É utilizado para deslocar os bits de um número para a esquerda, multiplicando o valor por potências de dois.",
            "ejemplo": '''
                x = 5  # binário: 0101
                print(x << 1)  # Saída: 10 (binário: 1010)
                '''
        },
        "bitwise_right_shift": {
            "significado": "Operador que realiza um deslocamento de bits para a direita.",
            "uso": "É utilizado para deslocar os bits de um número para a direita, dividindo o valor por potências de dois.",
            "ejemplo": '''
                x = 5  # binário: 0101
                print(x >> 1)  # Saída: 2 (binário: 0010)
                '''
        },
        "bz2": {
            "significado": "Módulo que fornece compressão e descompressão usando o algoritmo bzip2.",
            "uso": "É utilizado para manipular arquivos comprimidos no formato bzip2.",
            "ejemplo": '''
                import bz2

                with bz2.open('arquivo.bz2', 'rb') as arquivo:
                    conteudo = arquivo.read()
                    print(conteudo)
                '''
        },
        "bool_": {
            "significado": "Tipo de dado do NumPy para valores booleanos, similar ao `bool` do Python.",
            "uso": "É utilizado em operações com arrays do NumPy para representar valores booleanos.",
            "ejemplo": '''
                import numpy as np

                valor = np.bool_(True)
                print(valor)  # Saída: True
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

                print(callable(funcion))  # Saída: True
                print(callable(42))  # Saída: False
                '''
        },
        "chr": {
            "significado": "Devuelve el carácter Unicode correspondiente a un número entero.",
            "uso": "Se utiliza para convertir un código Unicode en su representación de carácter.",
            "ejemplo": '''
                print(chr(65))  # Saída: 'A'
                print(chr(8364))  # Saída: '€'
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
                        print(f"Hola, me llamo {self.nombre}")

                p = Persona("Juan")
                p.saludar()  # Saída: Hola, me llamo Juan
                '''
        },
        "classmethod": {
            "significado": "Define un método de clase, que recibe la clase como primer argumento en lugar de una instancia.",
            "uso": "Se utiliza para crear métodos que afectan a la clase en general.",
            "ejemplo": '''
                class MiClase:
                    contador = 0

                    @classmethod
                    def incrementar(cls):
                        cls.contador += 1

                MiClase.incrementar()
                print(MiClase.contador)  # Saída: 1
                '''
        },
        "compile": {
            "significado": "Compila una cadena de código en un objeto ejecutable de Python.",
            "uso": "Se utiliza para compilar código dinámico desde texto o archivos.",
            "ejemplo": '''
                codigo = "print('Hola Mundo')"
                compilado = compile(codigo, '<string>', 'exec')
                exec(compilado)  # Saída: Hola Mundo
                '''
        },
        "complex": {
            "significado": "Crea un número complejo en Python.",
            "uso": "Se utiliza para representar números complejos con parte real e imaginaria.",
            "ejemplo": '''
                c = complex(2, 3)
                print(c)  # Saída: (2+3j)
                print(c.real, c.imag)  # Saída: 2.0 3.0
                '''
        },
        "continue": {
            "significado": "Palabra clave que salta a la siguiente iteración de un bucle.",
            "uso": "Se utiliza para omitir el resto del código en la iteración actual.",
            "ejemplo": '''
                for i in range(5):
                    if i == 2:
                        continue
                    print(i)  # Saída: 0 1 3 4
                '''
        },
        "copy": {
            "significado": "Crea una copia superficial de un objeto.",
            "uso": "Se utiliza para duplicar estructuras de datos sin duplicar objetos anidados.",
            "ejemplo": '''
                import copy

                lista = [1, 2, [3, 4]]
                copia = copy.copy(lista)
                print(copia)  # Saída: [1, 2, [3, 4]]
                '''
        },
        "coroutine": {
            "significado": "Objeto que representa una función asincrónica suspendida.",
            "uso": "Se utiliza para manejar tareas asincrónicas con `async` y `await`.",
            "ejemplo": '''
                async def tarea():
                    print("Inicio")
                    await asyncio.sleep(1)
                    print("Fin")

                import asyncio
                asyncio.run(tarea())  # Saída: Inicio... Fin
                '''
        },
        "count": {
            "significado": "Devuelve el número de ocurrencias de un elemento en una colección.",
            "uso": "Se utiliza para contar la cantidad de veces que aparece un elemento en una lista o cadena.",
            "ejemplo": '''
                lista = [1, 2, 2, 3]
                print(lista.count(2))  # Saída: 2
                '''
        },
        "clear": {
            "significado": "Elimina todos los elementos de una lista o un diccionario.",
            "uso": "Se utiliza para vaciar el contenido de una lista o un diccionario.",
            "exemplo": """
                lista = [1, 2, 3]
                lista.clear()
                print(lista)  # Saída: []
                """
        },
        "cmath": {
            "significado": "Módulo que proporciona funciones matemáticas para trabajar con números complejos.",
            "uso": "Se utiliza para realizar operaciones matemáticas en números complejos.",
            "exemplo": """
                import cmath

                numero = cmath.sqrt(-1)
                print(numero)  # Saída: 1j
                """
        },
        "chain": {
            "significado": "Función que combina varios iteradores en uno solo.",
            "uso": "Se utiliza para concatenar múltiples iteradores.",
            "exemplo": """
                import itertools

                a = [1, 2, 3]
                b = [4, 5, 6]
                resultado = list(itertools.chain(a, b))
                print(resultado)  # Saída: [1, 2, 3, 4, 5, 6]
                """
        },
        "csv": {
            "significado": "Módulo para leer y escribir archivos en formato CSV (Comma Separated Values).",
            "uso": "Se utiliza para manejar archivos CSV.",
            "exemplo": """
                import csv

                with open('archivo.csv', mode='w', newline='') as archivo:
                    writer = csv.writer(archivo)
                    writer.writerow(['Nombre', 'Edad'])
                    writer.writerow(['Ana', 30])
                """
        },
        "copyreg": {
            "significado": "Módulo que proporciona funciones para registrar objetos para la copia y el desacoplamiento.",
            "uso": "Se utiliza para personalizar el comportamiento de copiado y almacenamiento de objetos.",
            "exemplo": """
                import copyreg

                def crear_persona(nombre, edad):
                    return {'nombre': nombre, 'edad': edad}

                copyreg.pickle(dict, crear_persona)
                """
        },
        "counter": {
            "significado": "Clase en el módulo `collections` que cuenta elementos hashables en una secuencia.",
            "uso": "Se utiliza para contar la frecuencia de elementos en un iterable.",
            "exemplo": """
                from collections import Counter

                contador = Counter([1, 2, 2, 3, 3, 3])
                print(contador)  # Saída: Counter({3: 3, 2: 2, 1: 1})
                """
        },
        "cProfile": {
            "significado": "Módulo para la medición del rendimiento de los programas en Python.",
            "uso": "Se utiliza para hacer perfiles de código y analizar la eficiencia del programa.",
            "exemplo": """
                import cProfile

                def funcion():
                    for i in range(1000):
                        pass

                cProfile.run('funcion()')
                """
        },
        "capitalize": {
            "significado": "Método de cadena que convierte la primera letra en mayúscula y el resto en minúsculas.",
            "uso": "Se utiliza para capitalizar la primera letra de una cadena.",
            "exemplo": """
                texto = 'hola mundo'
                print(texto.capitalize())  # Saída: 'Hola mundo'
                """
        },
        "center": {
            "significado": "Método de cadena que centra una cadena dentro de un campo de longitud especificada.",
            "uso": "Se utiliza para alinear texto en el centro de una cadena con un relleno.",
            "exemplo": """
                texto = 'hola'
                print(texto.center(10, '*'))  # Saída: '**hola****'
                """
        },
        "ceil": {
            "significado": "Función del módulo `math` que devuelve el entero más cercano mayor o igual a un número dado.",
            "uso": "Se utiliza para redondear un número hacia arriba.",
            "exemplo": """
                import math

                numero = 3.4
                print(math.ceil(numero))  # Saída: 4
                """
        },
        "call": {
            "significado": "Método utilizado para invocar un objeto que es callable, como funciones o clases.",
            "uso": "Se utiliza para llamar a un objeto que se puede ejecutar.",
            "exemplo": """
                def saludo():
                    return 'Hola'

                print(callable(saludo))  # Saída: True
                """
        },
        "clamp": {
            "significado": "Función que restringe un valor dentro de un rango especificado.",
            "uso": "Se utiliza para garantizar que un valor se mantenga dentro de un rango dado.",
            "exemplo": """
                def clamp(valor, minimo, maximo):
                    return max(minimo, min(valor, maximo))

                print(clamp(5, 1, 10))  # Saída: 5
                """
        },
        "choice": {
            "significado": "Función del módulo `random` que selecciona un elemento aleatorio de una secuencia.",
            "uso": "Se utiliza para elegir un valor aleatorio de una lista o secuencia.",
            "exemplo": """
                import random

                lista = [1, 2, 3, 4, 5]
                print(random.choice(lista))  # Saída: un valor aleatorio de la lista
                """
        },
        "collections": {
            "significado": "Módulo que implementa tipos de datos especializados como `Counter`, `deque`, `OrderedDict`, entre otros.",
            "uso": "Se utiliza para trabajar con colecciones de datos de manera eficiente.",
            "exemplo": """
                from collections import deque

                cola = deque([1, 2, 3])
                cola.append(4)
                print(cola)  # Saída: deque([1, 2, 3, 4])
                """
        },
        "compress": {
            "significado": "Función en el módulo `itertools` que permite comprimir elementos de un iterable.",
            "uso": "Se utiliza para filtrar los elementos de un iterable basándose en una condición booleana.",
            "exemplo": """
                import itertools

                datos = [1, 2, 3, 4, 5]
                condiciones = [True, False, True, False, True]
                resultado = list(itertools.compress(datos, condiciones))
                print(resultado)  # Saída: [1, 3, 5]
                """
        },
        "complex_conjugate": {
            "significado": "Método de los números complejos en Python que devuelve el conjugado complejo de un número.",
            "uso": "Se utiliza para obtener el conjugado de un número complejo.",
            "exemplo": """
                numero_complejo = 3 + 4j
                print(numero_complejo.conjugate())  # Saída: (3-4j)
                """
        },
        "ctypes": {
            "significado": "Módulo en Python que permite interactuar con bibliotecas de C y realizar llamadas a funciones de bajo nivel.",
            "uso": "Se utiliza para trabajar con tipos de datos y funciones de bibliotecas externas escritas en C.",
            "exemplo": """
                import ctypes

                # Crear una variable de tipo entero
                valor = ctypes.c_int(5)
                print(valor.value)  # Saída: 5
                """
        },
        "clear_screen": {
            "significado": "Función utilizada para limpiar la pantalla de la consola.",
            "uso": "Se utiliza para eliminar el contenido visible de la terminal o consola.",
            "exemplo": """
                import os

                def clear_screen():
                    os.system('cls' if os.name == 'nt' else 'clear')

                clear_screen()
                """
        },
        "call_later": {
            "significado": "Método utilizado para programar la ejecución de una función después de un cierto tiempo.",
            "uso": "Se utiliza en programación asíncrona para ejecutar tareas después de un retraso.",
            "exemplo": """
                import asyncio

                async def tarea():
                    print('Tarea ejecutada')

                asyncio.get_event_loop().call_later(2, asyncio.create_task, tarea())
                """
        },
        "chunk": {
            "significado": "Técnica que divide un iterable en partes más pequeñas o trozos.",
            "uso": "Se utiliza para dividir grandes volúmenes de datos en partes manejables.",
            "exemplo": """
                def chunk(iterable, tamaño):
                    for i in range(0, len(iterable), tamaño):
                        yield iterable[i:i + tamaño]

                lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                for trozo in chunk(lista, 3):
                    print(trozo)  # Saída: [1, 2, 3], [4, 5, 6], [7, 8, 9]
                """
        },
        "cycle": {
            "significado": "Función en el módulo `itertools` que crea un iterador que repite indefinidamente una secuencia.",
            "uso": "Se utiliza para recorrer un iterable en bucle sin fin.",
            "exemplo": """
                import itertools

                ciclo = itertools.cycle([1, 2, 3])
                for i in range(6):
                    print(next(ciclo))  # Saída: 1, 2, 3, 1, 2, 3
                """
        },
        "coerce": {
            "significado": "Función que intenta convertir un valor en un tipo compatible.",
            "uso": "Se utiliza para forzar la conversión de un valor a un tipo de datos específico.",
            "exemplo": """
                # La función coerce fue removida en versiones modernas de Python
                """
        },
        "current_thread": {
            "significado": "Método del módulo `threading` que devuelve el hilo actual de ejecución.",
            "uso": "Se utiliza para obtener el hilo de ejecución en el que se está ejecutando el código.",
            "exemplo": """
                import threading

                def mostrar_hilo():
                    print(threading.current_thread())

                mostrar_hilo()
                """
        },
        "configparser": {
            "significado": "Módulo que permite manejar archivos de configuración, como los archivos INI.",
            "uso": "Se utiliza para leer, escribir y modificar archivos de configuración.",
            "exemplo": """
                import configparser

                config = configparser.ConfigParser()
                config.read('config.ini')

                print(config['DEFAULT']['color'])  # Saída: rojo
                """
        },
        "compileall": {
            "significado": "Módulo en Python que compila todos los archivos `.py` en un directorio y sus subdirectorios.",
            "uso": "Se utiliza para compilar código Python a bytecode, lo que puede mejorar el rendimiento de la ejecución.",
            "exemplo": """
                import compileall

                compileall.compile_dir('mi_carpeta')
                """
        },
        "copytree": {
            "significado": "Función en el módulo `shutil` que copia un directorio completo, incluyendo su contenido, a otro destino.",
            "uso": "Se utiliza para copiar un directorio y todo su contenido a una nueva ubicación.",
            "exemplo": """
                import shutil

                shutil.copytree('origen', 'destino')
                """
        },
    },
    "d": {
        "def": {
        "significado": "Palabra clave en Python utilizada para definir una función.",
        "uso": "Se utiliza para crear una nueva función con un nombre y un bloque de código.",
        "exemplo": """
            def saludo():
                print('Hola Mundo')

            saludo()  # Saída: Hola Mundo
            """
        },
        "delattr": {
            "significado": "Función que elimina un atributo de un objeto en Python.",
            "uso": "Se utiliza para eliminar un atributo específico de un objeto.",
            "exemplo": """
                class Persona:
                    def __init__(self, nombre):
                        self.nombre = nombre

                p = Persona('Juan')
                delattr(p, 'nombre')
                print(hasattr(p, 'nombre'))  # Saída: False
                """
        },
        "dataframe": {
            "significado": "Estructura de datos bidimensional en la librería Pandas, similar a una tabla, que permite almacenar datos de diferentes tipos.",
            "uso": "Se utiliza para manejar grandes volúmenes de datos tabulares en Python.",
            "exemplo": """
                import pandas as pd

                data = {'Nombre': ['Juan', 'Ana'], 'Edad': [28, 22]}
                df = pd.DataFrame(data)
                print(df)
                """
        },
        "decode": {
            "significado": "Método utilizado para decodificar datos binarios a un formato de texto, generalmente en una codificación como UTF-8.",
            "uso": "Se utiliza para convertir datos binarios en cadenas de texto legibles.",
            "exemplo": """
                encoded = b'Hola Mundo'
                decoded = encoded.decode('utf-8')
                print(decoded)  # Saída: Hola Mundo
                """
        },
        "decimal": {
            "significado": "Módulo en Python que proporciona soporte para realizar cálculos con decimales de precisión arbitraria.",
            "uso": "Se utiliza para realizar operaciones aritméticas precisas sin los errores de redondeo típicos de los números de punto flotante.",
            "exemplo": """
                from decimal import Decimal

                x = Decimal('0.1')
                y = Decimal('0.2')
                print(x + y)  # Saída: 0.3
                """
        },
        "device": {
            "significado": "Término general para referirse a cualquier dispositivo de hardware o sistema en el que se ejecuta un programa.",
            "uso": "Se utiliza para referirse a dispositivos como computadoras, teléfonos móviles, etc.",
            "exemplo": "No es un término específico de Python, pero se puede usar en bibliotecas como TensorFlow para referirse a dispositivos de procesamiento como CPU o GPU."
        },
        "dict.get": {
            "significado": "Método de los diccionarios en Python que devuelve el valor de una clave especificada, o un valor por defecto si la clave no existe.",
            "uso": "Se utiliza para obtener el valor asociado a una clave sin generar un error si la clave no existe.",
            "exemplo": """
                d = {'a': 1, 'b': 2}
                print(d.get('a'))  # Saída: 1
                print(d.get('c', 'No encontrado'))  # Saída: No encontrado
                """
        },
        "dropna": {
            "significado": "Método en Pandas utilizado para eliminar los valores faltantes (NaN) en un DataFrame o Serie.",
            "uso": "Se utiliza para limpiar los datos eliminando las filas o columnas que contienen valores nulos.",
            "exemplo": """
                import pandas as pd

                df = pd.DataFrame({'A': [1, 2, None], 'B': [None, 3, 4]})
                print(df.dropna())
                """
        },
        "dtype": {
            "significado": "Propiedad de los arrays en Numpy o de las columnas en un DataFrame de Pandas que indica el tipo de dato de los elementos.",
            "uso": "Se utiliza para obtener o especificar el tipo de datos de un array o columna.",
            "exemplo": """
                import numpy as np

                arr = np.array([1, 2, 3])
                print(arr.dtype)  # Saída: int64
                """
        },
        "deque.appendleft": {
            "significado": "Método del tipo de dato `deque` en el módulo `collections` que agrega un elemento al principio de la deque.",
            "uso": "Se utiliza para insertar un nuevo elemento en la parte izquierda de una deque.",
            "exemplo": """
                from collections import deque

                d = deque([2, 3, 4])
                d.appendleft(1)
                print(d)  # Saída: deque([1, 2, 3, 4])
                """
        },
        "dict.update": {
            "significado": "Método de los diccionarios en Python que actualiza un diccionario con los elementos de otro diccionario o iterable.",
            "uso": "Se utiliza para agregar o modificar elementos en un diccionario utilizando otro diccionario o iterable.",
            "exemplo": """
                d1 = {'a': 1, 'b': 2}
                d2 = {'b': 3, 'c': 4}
                d1.update(d2)
                print(d1)  # Saída: {'a': 1, 'b': 3, 'c': 4}
                """
        },
        "del": {
            "significado": "Palabra clave en Python que elimina un atributo o un elemento de una colección.",
            "uso": "Se utiliza para eliminar elementos de una lista, atributo de un objeto o una variable.",
            "exemplo": """
                lista = [1, 2, 3]
                del lista[1]
                print(lista)  # Saída: [1, 3]
                """
        },
        "dict": {
            "significado": "Tipo de datos en Python que representa un diccionario, una colección de pares clave-valor.",
            "uso": "Se utiliza para almacenar y manipular datos de forma eficiente, asociando claves únicas a valores.",
            "exemplo": """
                d = {'a': 1, 'b': 2}
                print(d['a'])  # Saída: 1
                """
        },
        "dir": {
            "significado": "Función que devuelve una lista de los atributos y métodos de un objeto.",
            "uso": "Se utiliza para obtener información sobre los métodos y atributos disponibles para un objeto o módulo.",
            "exemplo": """
                x = [1, 2, 3]
                print(dir(x))
                """
        },
        "divmod": {
            "significado": "Función que recibe dos números y devuelve una tupla con el cociente y el residuo de su división.",
            "uso": "Se utiliza para obtener tanto el cociente como el residuo de una división en una sola operación.",
            "exemplo": """
                resultado = divmod(9, 4)
                print(resultado)  # Saída: (2, 1)
                """
        },
        "deque": {
            "significado": "Tipo de datos en el módulo `collections` de Python que representa una cola doblemente terminada, que permite añadir y eliminar elementos de ambos extremos de manera eficiente.",
            "uso": "Se utiliza para implementar colas y pilas de manera eficiente.",
            "exemplo": """
                from collections import deque

                d = deque([1, 2, 3])
                d.append(4)
                print(d)  # Saída: deque([1, 2, 3, 4])
                """
        },
        "defaultdict": {
            "significado": "Clase en el módulo `collections` que extiende el diccionario estándar y permite establecer un valor por defecto para claves inexistentes.",
            "uso": "Se utiliza para evitar la generación de errores al acceder a claves no existentes, proporcionando un valor por defecto.",
            "exemplo": """
                from collections import defaultdict

                d = defaultdict(int)
                d['a'] += 1
                print(d)  # Saída: defaultdict(<class 'int'>, {'a': 1})
                """
        },
        "decode": {
            "significado": "Método utilizado para convertir datos binarios en texto en una codificación específica.",
            "uso": "Se utiliza para decodificar una secuencia de bytes en una cadena de texto en una codificación dada.",
            "exemplo": """
                encoded = b'Hola Mundo'
                decoded = encoded.decode('utf-8')
                print(decoded)  # Saída: Hola Mundo
                """
        },
        "deflate": {
            "significado": "Algoritmo de compresión de datos sin pérdida, utilizado para reducir el tamaño de los archivos.",
            "uso": "Se utiliza para comprimir datos en un formato más eficiente.",
            "exemplo": """
                import zlib

                data = b'Hola Mundo'*100
                compressed = zlib.deflate(data)
                print(compressed)
                """
        },
        "deepcopy": {
            "significado": "Función del módulo `copy` que crea una copia profunda de un objeto, es decir, copia todos los elementos del objeto original, incluso los objetos dentro de objetos.",
            "uso": "Se utiliza cuando se necesita hacer una copia completa e independiente de un objeto.",
            "exemplo": """
                import copy

                original = {'a': [1, 2, 3]}
                copia = copy.deepcopy(original)
                copia['a'][0] = 100
                print(original)  # Saída: {'a': [1, 2, 3]}
                print(copia)     # Saída: {'a': [100, 2, 3]}
                """
        },
        "detach": {
            "significado": "Método de objetos en Python, utilizado para separar un objeto de su contexto o de su flujo de datos.",
            "uso": "Se utiliza para liberar recursos o desvincular un objeto de su entorno de ejecución.",
            "exemplo": """
                import torch

                tensor = torch.tensor([1, 2, 3])
                detached_tensor = tensor.detach()
                print(detached_tensor)  # Saída: tensor([1, 2, 3])
                """
        },
        "dump": {
            "significado": "Método de la biblioteca `pickle` que serializa un objeto y lo escribe en un archivo.",
            "uso": "Se utiliza para guardar un objeto en un archivo de forma serializada.",
            "exemplo": """
                import pickle

                data = {'a': 1, 'b': 2}
                with open('data.pkl', 'wb') as f:
                    pickle.dump(data, f)
                """
        },
        "dumps": {
            "significado": "Método de la biblioteca `pickle` que serializa un objeto y lo devuelve como una cadena de bytes.",
            "uso": "Se utiliza para convertir un objeto en un formato de cadena para su almacenamiento o transmisión.",
            "exemplo": """
                import pickle

                data = {'a': 1, 'b': 2}
                serialized = pickle.dumps(data)
                print(serialized)
                """
        },
        "difference": {
            "significado": "Método de conjuntos en Python que devuelve la diferencia entre dos o más conjuntos.",
            "uso": "Se utiliza para encontrar los elementos que están en un conjunto pero no en los otros.",
            "exemplo": """
                a = {1, 2, 3}
                b = {2, 3, 4}
                print(a.difference(b))  # Saída: {1}
                """
        },
        "difference_update": {
            "significado": "Método de conjuntos en Python que elimina los elementos de un conjunto que están presentes en otro conjunto.",
            "uso": "Se utiliza para modificar un conjunto eliminando sus elementos que se encuentran en otro conjunto.",
            "exemplo": """
                a = {1, 2, 3}
                b = {2, 3, 4}
                a.difference_update(b)
                print(a)  # Saída: {1}
                """
        },
        "decode_header": {
            "significado": "Función del módulo `email.header` que decodifica una cabecera de correo electrónico.",
            "uso": "Se utiliza para decodificar una cabecera de correo electrónico que puede estar en diferentes codificaciones.",
            "exemplo": """
                from email.header import decode_header

                header = '=?utf-8?B?SG9sYSBNdW5kbyA8MTIzNDU+?='
                decoded, encoding = decode_header(header)[0]
                print(decoded.decode(encoding))  # Saída: Hola Mundo <12345>
                """
        },
        "disk_usage": {
            "significado": "Función del módulo `shutil` que devuelve el uso del disco de una ruta o directorio.",
            "uso": "Se utiliza para obtener información sobre el espacio utilizado y disponible en un sistema de archivos.",
            "exemplo": """
                import shutil

                usage = shutil.disk_usage('/')
                print(usage)  # Saída: usage(total=500000000, used=200000000, free=300000000)
                """
        },
        "datetime": {
            "significado": "Módulo de Python que proporciona clases para trabajar con fechas y horas.",
            "uso": "Se utiliza para manipular y trabajar con fechas, horas y tiempos en general.",
            "exemplo": """
                import datetime

                ahora = datetime.datetime.now()
                print(ahora)  # Saída: 2024-11-22 12:00:00.123456
                """
        },
        "difference": {
            "significado": "Método de conjuntos en Python que devuelve la diferencia entre dos o más conjuntos.",
            "uso": "Se utiliza para obtener los elementos de un conjunto que no están presentes en los demás.",
            "exemplo": """
                a = {1, 2, 3, 4}
                b = {2, 3, 5}
                print(a.difference(b))  # Saída: {1, 4}
                """
        },
        "disk_cache": {
            "significado": "Almacenamiento en caché en disco para mejorar la velocidad de acceso a datos o resultados computacionales.",
            "uso": "Se utiliza para almacenar temporalmente resultados o datos en el disco para evitar tener que recalcular o volver a obtener los datos.",
            "exemplo": """
                import joblib

                result = joblib.Memory('cache_dir').cache(some_function)
                """
        },
    },
    "e": {
        "": {
            "significado": "",
            "uso": "",
            "ejemplo": ''''''
        },
        "enumerate": {
            "significado": "Función incorporada de Python que agrega un contador a un iterable y lo devuelve como un objeto iterable de tuplas.",
            "uso": "Se utiliza para obtener tanto el índice como el valor de los elementos en un iterable.",
            "exemplo": """
                lista = ['a', 'b', 'c']
                for indice, valor in enumerate(lista):
                    print(indice, valor)
                # Saída:
                # 0 a
                # 1 b
                # 2 c
                """
        },
        "eval": {
            "significado": "Función incorporada en Python que evalúa una cadena de código como una expresión de Python.",
            "uso": "Se utiliza para ejecutar expresiones Python contenidas en una cadena y devolver el resultado.",
            "exemplo": """
                x = 2
                resultado = eval('x + 1')
                print(resultado)  # Saída: 3
                """
        },
        "exec": {
            "significado": "Función incorporada en Python que ejecuta una cadena de código como un bloque de código completo.",
            "uso": "Se utiliza para ejecutar código Python dinámicamente.",
            "exemplo": """
                codigo = 'for i in range(3): print(i)'
                exec(codigo)
                # Saída:
                # 0
                # 1
                # 2
                """
        },
        "except": {
            "significado": "Palabra clave en Python utilizada para manejar excepciones dentro de un bloque try-except.",
            "uso": "Se utiliza para capturar y manejar excepciones que ocurren en el bloque try.",
            "exemplo": """
                try:
                    x = 1 / 0
                except ZeroDivisionError:
                    print('Error: División por cero')
                # Saída: Error: División por cero
                """
        },
        "else": {
            "significado": "Palabra clave en Python utilizada en estructuras de control condicional (if, try) para ejecutar un bloque de código si la condición no se cumple o no ocurre una excepción.",
            "uso": "Se utiliza para ejecutar un bloque de código cuando no se cumple la condición o no ocurre ninguna excepción.",
            "exemplo": """
                if 3 > 1:
                    print('Condición verdadera')
                else:
                    print('Condición falsa')
                # Saída: Condición verdadera
                """
        },
        "elif": {
            "significado": "Palabra clave en Python que se utiliza en estructuras condicionales para comprobar una condición adicional si las anteriores no se cumplen.",
            "uso": "Se utiliza para manejar múltiples condiciones en una estructura if-elif-else.",
            "exemplo": """
                x = 3
                if x > 5:
                    print('Mayor que 5')
                elif x == 3:
                    print('Igual a 3')
                else:
                    print('Menor que 3')
                # Saída: Igual a 3
                """
        },
        "exit": {
            "significado": "Función incorporada en Python que finaliza la ejecución del programa.",
            "uso": "Se utiliza para salir de un programa o cerrar un entorno de ejecución.",
            "exemplo": """
                import sys
                sys.exit('Terminando el programa')
                # El programa se termina con el mensaje 'Terminando el programa'
                """
        },
        "end": {
            "significado": "Palabra clave utilizada en Python para especificar el final de un bloque o la terminación de una cadena de caracteres.",
            "uso": "Se utiliza principalmente en las funciones de impresión para controlar el final de la salida.",
            "exemplo": """
                print('Hola', end=' ')
                print('Mundo')
                # Saída: Hola Mundo
                """
        },
        "expandtabs": {
            "significado": "Método de cadenas de texto en Python que reemplaza los caracteres de tabulación por espacios.",
            "uso": "Se utiliza para alinear texto reemplazando las tabulaciones por un número determinado de espacios.",
            "exemplo": """
                texto = 'Hola\tMundo'
                print(texto.expandtabs(4))
                # Saída: Hola   Mundo
                """
        },
        "encode": {
            "significado": "Método de cadenas de texto en Python que codifica una cadena en una secuencia de bytes usando un codificador específico.",
            "uso": "Se utiliza para convertir una cadena en una secuencia de bytes para ser almacenada o transmitida en formatos específicos.",
            "exemplo": """
                texto = 'Hola Mundo'
                encoded = texto.encode('utf-8')
                print(encoded)
                # Saída: b'Hola Mundo'
                """
        },
        "element": {
            "significado": "Un ítem individual dentro de una colección o estructura de datos.",
            "uso": "Se utiliza para referirse a un objeto dentro de una lista, conjunto, diccionario, etc.",
            "exemplo": """
                lista = [1, 2, 3]
                print(lista[0])  # Saída: 1
                """
        },
        "error": {
            "significado": "Condición anómala en la ejecución de un programa que interrumpe su flujo normal.",
            "uso": "Se utiliza para indicar que algo ha ido mal durante la ejecución del código.",
            "exemplo": """
                try:
                    1 / 0
                except ZeroDivisionError as e:
                    print(f'Error: {e}')
                # Saída: Error: division by zero
                """
        },
        "exception": {
            "significado": "Evento que altera el flujo normal de ejecución del programa, generalmente debido a un error.",
            "uso": "Se utiliza para manejar errores en el código y ejecutar acciones específicas cuando ocurren.",
            "exemplo": """
                try:
                    int('a')
                except ValueError:
                    print('Error: no se puede convertir a entero')
                # Saída: Error: no se puede convertir a entero
                """
        },
        "evaluate": {
            "significado": "Ejecutar o calcular el valor de una expresión o función.",
            "uso": "Se utiliza para obtener el resultado de una expresión.",
            "exemplo": """
                x = 5
                resultado = eval('x + 2')
                print(resultado)  # Saída: 7
                """
        },
        "elements": {
            "significado": "Ítems o componentes individuales dentro de un conjunto o colección.",
            "uso": "Se utiliza para referirse a las partes de una estructura de datos.",
            "exemplo": """
                conjunto = {1, 2, 3}
                for elemento in conjunto:
                    print(elemento)
                # Saída:
                # 1
                # 2
                # 3
                """
        },
        "exponential": {
            "significado": "Relacionado con la operación matemática de exponente, que calcula el valor de una base elevada a un exponente.",
            "uso": "Se utiliza para realizar cálculos exponenciales.",
            "exemplo": """
                import math
                resultado = math.exp(2)
                print(resultado)  # Saída: 7.3890560989306495
                """
        },
        "enumerations": {
            "significado": "Una lista o conjunto de elementos, a menudo con un valor asociado o un identificador.",
            "uso": "Se utiliza para representar un conjunto de valores posibles de una variable.",
            "exemplo": """
                from enum import Enum

                class Color(Enum):
                    RED = 1
                    GREEN = 2
                    BLUE = 3

                print(Color.RED)  # Saída: Color.RED
                """
        },
        "encode_utf8": {
            "significado": "Método de codificación que convierte una cadena de caracteres en una secuencia de bytes utilizando el formato UTF-8.",
            "uso": "Se utiliza para convertir texto a una representación binaria utilizando UTF-8.",
            "exemplo": """
                texto = 'Hola Mundo'
                encoded = texto.encode('utf-8')
                print(encoded)  # Saída: b'Hola Mundo'
                """
        },
        "execfile": {
            "significado": "Función que ejecuta un archivo de Python como si fuera un script.",
            "uso": "Se utiliza para ejecutar un archivo Python externo.",
            "exemplo": """
                # Este comando está disponible solo en Python 2
                execfile('script.py')
                """
        },
        "edit_distance": {
            "significado": "Medida que calcula la diferencia entre dos cadenas de texto basándose en las operaciones necesarias para convertir una en otra.",
            "uso": "Se utiliza para comparar cuán similares son dos cadenas y determinar cuántos cambios son necesarios para hacerlas idénticas.",
            "exemplo": """
                from nltk.metrics import edit_distance

                distancia = edit_distance('kitten', 'sitting')
                print(distancia)  # Saída: 3
                """
        },
        "eval_input": {
            "significado": "Función que evalúa una entrada de usuario, normalmente a través de la función `input()`.",
            "uso": "Se utiliza para obtener y evaluar una entrada proporcionada por el usuario.",
            "exemplo": """
                entrada = input('Ingresa un número: ')
                resultado = eval(entrada)
                print(resultado)
                """
        },
        "xceed": {
            "significado": "Término utilizado para describir algo que supera o excede un límite o expectativa.",
            "uso": "Se utiliza para indicar que algo ha superado un estándar o límite.",
            "exemplo": "La nueva actualización excede nuestras expectativas en términos de rendimiento."
        },
        "expected": {
            "significado": "Algo anticipado o previsto, basado en expectativas o predicciones.",
            "uso": "Se utiliza para describir lo que se espera que ocurra en una situación.",
            "exemplo": "El resultado esperado era un incremento en la velocidad de procesamiento."
        },
        "encode_base64": {
            "significado": "Método de codificación que convierte datos binarios en una representación de texto en base 64.",
            "uso": "Se utiliza para codificar datos binarios en una cadena de texto legible en base 64.",
            "exemplo": """
                import base64
                encoded = base64.b64encode(b'hello')
                print(encoded)  # Saída: b'aGVsbG8='
                """
        },
        "execute": {
            "significado": "Realizar o llevar a cabo un conjunto de instrucciones o un programa.",
            "uso": "Se utiliza para poner en práctica una acción o ejecutar código.",
            "exemplo": """
                def funcion():
                    print('Ejecutando...')
                funcion()  # Saída: Ejecutando...
                """
        },
        "exit_code": {
            "significado": "Valor retornado por un programa o script al finalizar, indicando si se ejecutó correctamente o si ocurrió un error.",
            "uso": "Se utiliza para verificar si un programa finalizó con éxito o con error.",
            "exemplo": """
                import sys
                sys.exit(0)  # Saída: 0 indica éxito, otro número indica error.
                """
        },
        "evaluate_expression": {
            "significado": "Evaluar una expresión para obtener su resultado.",
            "uso": "Se utiliza para calcular o obtener el valor de una expresión matemática o lógica.",
            "exemplo": """
                resultado = eval('3 + 5')
                print(resultado)  # Saída: 8
                """
        },
        "environment": {
            "significado": "El contexto o conjunto de condiciones en el que se ejecuta un programa o aplicación.",
            "uso": "Se utiliza para referirse al conjunto de variables, configuraciones y recursos disponibles para un programa.",
            "exemplo": """
                import os
                print(os.environ)  # Saída: Muestra las variables de entorno del sistema.
                """
        },
        "environment_variable": {
            "significado": "Variable que almacena información sobre el entorno del sistema o aplicación.",
            "uso": "Se utiliza para almacenar configuraciones específicas que afectan el comportamiento de los programas.",
            "exemplo": """
                import os
                print(os.getenv('PATH'))  # Saída: Muestra la variable de entorno PATH.
                """
        },
        "exp": {
            "significado": "Función matemática que calcula la exponencial de un número, es decir, e elevado a la potencia de ese número.",
            "uso": "Se utiliza para realizar cálculos exponenciales.",
            "exemplo": """
                import math
                resultado = math.exp(1)
                print(resultado)  # Saída: 2.718281828459045
                """
        },
        "exception_handling": {
            "significado": "Proceso de gestionar y responder a errores o excepciones que ocurren durante la ejecución de un programa.",
            "uso": "Se utiliza para capturar y manejar errores, asegurando que el programa no se detenga inesperadamente.",
            "exemplo": """
                try:
                    valor = 1 / 0
                except ZeroDivisionError as e:
                    print(f'Error: {e}')  # Saída: Error: division by zero
                """
        },
        "expand": {
            "significado": "Ampliar o aumentar el tamaño o el alcance de algo.",
            "uso": "Se utiliza para hacer algo más grande o para incluir más información.",
            "exemplo": """
                texto = "Hola"
                print(texto.expandtabs(4))  # Saída: 'Hola' con tabulaciones ampliadas
                """
        },
        "environment_config": {
            "significado": "Configuración relacionada con el entorno de ejecución de un programa o sistema.",
            "uso": "Se utiliza para especificar o ajustar parámetros que afectan el funcionamiento de un programa o aplicación.",
            "exemplo": """
                config = {
                    'host': 'localhost',
                    'port': 8080
                }
                print(config)  # Saída: {'host': 'localhost', 'port': 8080}
                """
        },
        "equal": {
            "significado": "Indica que dos elementos son idénticos en valor.",
            "uso": "Se utiliza para comparar dos valores o expresiones para verificar si son iguales.",
            "exemplo": """
                a = 5
                b = 5
                print(a == b)  # Saída: True
                """
        },
        "error_handling": {
            "significado": "Proceso de manejar errores y excepciones que ocurren durante la ejecución de un programa.",
            "uso": "Se utiliza para capturar y gestionar errores de manera controlada para evitar que el programa termine inesperadamente.",
            "exemplo": """
                try:
                    valor = 10 / 0
                except ZeroDivisionError:
                    print('Error de división por cero')  # Saída: Error de división por cero
                """
        },
        "event": {
            "significado": "Acción o suceso que puede ser detectado y gestionado en un programa.",
            "uso": "Se utiliza para manejar y responder a actividades o cambios en un sistema o programa.",
            "exemplo": """
                import tkinter as tk
                def click():
                    print('Botón presionado')
                root = tk.Tk()
                button = tk.Button(root, text="Click me", command=click)
                button.pack()
                root.mainloop()  # Saída: Muestra un botón que al presionar, ejecuta el evento click
                """
        },
        "event_loop": {
            "significado": "Ciclo continuo que espera y maneja eventos o tareas asíncronas en un programa.",
            "uso": "Se utiliza para ejecutar tareas o responder a eventos en orden, sin bloquear el flujo principal de ejecución.",
            "exemplo": """
                import asyncio
                async def hello():
                    print("Hola")
                asyncio.run(hello())  # Saída: Hola
                """
        },
        "exception_type": {
            "significado": "El tipo específico de una excepción o error que ocurre en un programa.",
            "uso": "Se utiliza para identificar qué tipo de error ha ocurrido y tomar acciones adecuadas.",
            "exemplo": """
                try:
                    valor = 10 / 0
                except ZeroDivisionError as e:
                    print(f"Tipo de error: {type(e)}")  # Saída: Tipo de error: <class 'ZeroDivisionError'>
                """
        },
        "error_message": {
            "significado": "Mensaje que describe el error o problema ocurrido durante la ejecución de un programa.",
            "uso": "Se utiliza para proporcionar detalles sobre lo que ha fallado o causado una excepción.",
            "exemplo": """
                try:
                    x = int("abc")
                except ValueError as e:
                    print(f"Mensaje de error: {e}")  # Saída: Mensaje de error: invalid literal for int() with base 10: 'abc'
                """
        },
        "extract": {
            "significado": "Obtener una parte específica de un conjunto de datos o información.",
            "uso": "Se utiliza para sacar o extraer un componente específico de un conjunto mayor de datos.",
            "exemplo": """
                texto = 'Hola Mundo'
                print(texto[0:4])  # Saída: Hola
                """
        },
        "exit_status": {
            "significado": "Código de salida que indica si un programa o proceso terminó correctamente o con un error.",
            "uso": "Se utiliza para verificar si un proceso o comando terminó con éxito o si ocurrió algún error.",
            "exemplo": """
                import sys
                sys.exit(0)  # Saída: 0 indica éxito, cualquier otro número indica error.
                """
        },


    },
    "f": {
        "": {
            "significado": "",
            "uso": "",
            "ejemplo": ''''''
        },
        "filemode": {
            "significado": "Modo de apertura de un archivo que determina las operaciones que se pueden realizar en él.",
            "uso": "Se utiliza para especificar el tipo de acceso que se desea para un archivo (lectura, escritura, etc.).",
            "exemplo": """
                archivo = open('archivo.txt', 'r')  # 'r' indica modo de solo lectura
                print(archivo.mode)  # Saída: 'r'
                """
        },
        "frozen_set": {
            "significado": "Conjunto inmutable en Python, similar a un conjunto estándar pero sin la posibilidad de modificarlo después de su creación.",
            "uso": "Se utiliza para crear conjuntos que no deben ser modificados después de su creación.",
            "exemplo": """
                conjunto = frozenset([1, 2, 3])
                print(conjunto)  # Saída: frozenset({1, 2, 3})
                """
        },
        "format_map": {
            "significado": "Método que devuelve una cadena formateada utilizando un diccionario u objeto similar.",
            "uso": "Se utiliza para realizar sustituciones de valores en una cadena usando un mapa (como un diccionario).",
            "exemplo": """
                datos = {'nombre': 'Juan', 'edad': 30}
                texto = 'Nombre: {nombre}, Edad: {edad}'.format_map(datos)
                print(texto)  # Saída: Nombre: Juan, Edad: 30
                """
        },
        "find": {
            "significado": "Método que busca una subcadena dentro de una cadena y devuelve el índice de la primera aparición.",
            "uso": "Se utiliza para encontrar la posición de un texto dentro de otro.",
            "exemplo": """
                texto = 'Hola Mundo'
                print(texto.find('Mundo'))  # Saída: 5
                """
        },
        "float32": {
            "significado": "Tipo de datos en NumPy que representa un número de punto flotante de 32 bits.",
            "uso": "Se utiliza para almacenar números con decimales en un formato más eficiente en términos de memoria.",
            "exemplo": """
                import numpy as np
                numero = np.float32(3.1415)
                print(numero)  # Saída: 3.1415
                """
        },
        "float64": {
            "significado": "Tipo de datos en NumPy que representa un número de punto flotante de 64 bits.",
            "uso": "Se utiliza para almacenar números con decimales con mayor precisión que el tipo float32.",
            "exemplo": """
                import numpy as np
                numero = np.float64(3.141592653589793)
                print(numero)  # Saída: 3.141592653589793
                """
        },
        "formatting": {
            "significado": "El proceso de aplicar un formato a datos o cadenas, como la alineación, los anchos y los tipos de datos.",
            "uso": "Se utiliza para organizar o mostrar datos de manera más legible o específica.",
            "exemplo": """
                texto = 'Nombre: {0:10}, Edad: {1:5}'.format('Juan', 30)
                print(texto)  # Saída: Nombre: Juan      , Edad: 30
                """
        },
        "flush_output": {
            "significado": "Método utilizado para vaciar el búfer de salida, forzando que los datos se escriban de inmediato.",
            "uso": "Se utiliza cuando se quiere asegurarse de que todos los datos pendientes en el búfer de salida se escriban al destino.",
            "exemplo": """
                import sys
                sys.stdout.write('Hola Mundo')
                sys.stdout.flush()  # Saída: 'Hola Mundo' inmediatamente
                """
        },
        "function_definition": {
            "significado": "El proceso de crear una función en Python utilizando la palabra clave 'def'.",
            "uso": "Se utiliza para declarar funciones reutilizables que ejecutan un bloque de código específico.",
            "exemplo": """
                def saludar(nombre):
                    return f'Hola {nombre}'
                print(saludar('Juan'))  # Saída: Hola Juan
                """
        },
        "filepath": {
            "significado": "Ruta o dirección de un archivo en el sistema de archivos.",
            "uso": "Se utiliza para especificar la ubicación de un archivo en el sistema de archivos.",
            "exemplo": """
                import os
                ruta = os.path.join('carpeta', 'archivo.txt')
                print(ruta)  # Saída: carpeta/archivo.txt
                """
        },
        "flask": {
            "significado": "Un micro-framework de Python para el desarrollo de aplicaciones web.",
            "uso": "Se utiliza para crear aplicaciones web de manera sencilla y rápida con rutas, formularios y otras funcionalidades.",
            "exemplo": """
                from flask import Flask
                app = Flask(__name__)

                @app.route('/')
                def hello():
                    return 'Hola Mundo'

                app.run()  # Saída: 'Hola Mundo' en una aplicación web
                """
        },
        "filtering": {
            "significado": "Proceso de seleccionar elementos de una colección que cumplen con una condición específica.",
            "uso": "Se utiliza para extraer elementos de una lista, conjunto o cualquier iterable basado en una condición.",
            "exemplo": """
                lista = [1, 2, 3, 4, 5]
                resultado = filter(lambda x: x > 2, lista)
                print(list(resultado))  # Saída: [3, 4, 5]
                """
        },
        "futures": {
            "significado": "Módulo que proporciona una interfaz para ejecutar tareas asincrónicas y paralelizadas.",
            "uso": "Se utiliza para ejecutar funciones de manera concurrente utilizando hilos o procesos.",
            "exemplo": """
                from concurrent.futures import ThreadPoolExecutor

                def tarea(x):
                    return x * x

                with ThreadPoolExecutor() as executor:
                    resultados = executor.map(tarea, [1, 2, 3])
                    print(list(resultados))  # Saída: [1, 4, 9]
                """
        },
        "fold": {
            "significado": "Función que aplica una operación acumulativa sobre los elementos de una secuencia.",
            "uso": "Se utiliza para reducir una secuencia de elementos a un solo valor aplicando una operación binaria.",
            "exemplo": """
                from functools import reduce
                lista = [1, 2, 3, 4]
                resultado = reduce(lambda x, y: x + y, lista)
                print(resultado)  # Saída: 10
                """
        },
        "fromkeys": {
            "significado": "Método de diccionario que crea un nuevo diccionario con claves especificadas y valores predeterminados.",
            "uso": "Se utiliza para crear diccionarios a partir de una lista de claves con un valor predeterminado.",
            "exemplo": """
                diccionario = dict.fromkeys(['a', 'b', 'c'], 0)
                print(diccionario)  # Saída: {'a': 0, 'b': 0, 'c': 0}
                """
        },
        "flask_restful": {
            "significado": "Extensión para Flask que simplifica la creación de APIs RESTful.",
            "uso": "Se utiliza para desarrollar aplicaciones web que siguen la arquitectura REST utilizando recursos.",
            "exemplo": """
                from flask import Flask
                from flask_restful import Api, Resource

                app = Flask(__name__)
                api = Api(app)

                class HelloWorld(Resource):
                    def get(self):
                        return {'mensaje': 'Hola Mundo'}

                api.add_resource(HelloWorld, '/')
                app.run()  # Saída: 'Hola Mundo' como respuesta de la API
                """
        },
        "fix": {
            "significado": "Término general para corregir o ajustar algo que no funciona correctamente.",
            "uso": "Se utiliza cuando se realiza un ajuste o corrección en el código o en la configuración de algo.",
            "exemplo": """
                # Ejemplo en el contexto de código: corrección de un error de sintaxis
                def corregir_error():
                    print('Este es el mensaje corregido')
                corregir_error()
                """
        },
        "float_conversion": {
            "significado": "Proceso de convertir datos de otros tipos a tipo flotante.",
            "uso": "Se utiliza para convertir valores a números de punto flotante (decimales).",
            "exemplo": """
                numero = '3.14'
                resultado = float(numero)
                print(resultado)  # Saída: 3.14
                """
        },
        "full_path": {
            "significado": "Ruta completa a un archivo o directorio en el sistema de archivos.",
            "uso": "Se utiliza para especificar la ubicación exacta de un archivo o directorio desde la raíz del sistema de archivos.",
            "exemplo": """
                import os
                ruta_completa = os.path.abspath('archivo.txt')
                print(ruta_completa)  # Saída: /home/usuario/archivo.txt
                """
        },
        "filter": {
            "significado": "Función que aplica una condición a cada elemento de un iterable y devuelve los elementos que cumplen la condición.",
            "uso": "Se utiliza para seleccionar solo aquellos elementos que cumplen con una condición específica.",
            "exemplo": """
                lista = [1, 2, 3, 4, 5]
                resultado = filter(lambda x: x % 2 == 0, lista)
                print(list(resultado))  # Saída: [2, 4]
                """
        },
        "float": {
            "significado": "Tipo de dato en Python para representar números de punto flotante (números con decimales).",
            "uso": "Se utiliza para representar números que requieren decimales.",
            "exemplo": """
                numero = 3.14
                print(type(numero))  # Saída: <class 'float'>
                """
        },
        "for": {
            "significado": "Palabra clave en Python utilizada para iterar sobre los elementos de un iterable.",
            "uso": "Se utiliza para ejecutar un bloque de código repetidamente para cada elemento en un iterable.",
            "exemplo": """
                for i in range(5):
                    print(i)
                # Saída:
                # 0
                # 1
                # 2
                # 3
                # 4
                """
        },
        "format": {
            "significado": "Método utilizado para formatear cadenas de texto, insertando valores dentro de ellas.",
            "uso": "Se utiliza para crear cadenas de texto más legibles y dinámicas con valores variables.",
            "exemplo": """
                nombre = 'Juan'
                edad = 30
                print('Mi nombre es {} y tengo {} años'.format(nombre, edad))
                # Saída: Mi nombre es Juan y tengo 30 años
                """
        },
        "from": {
            "significado": "Palabra clave en Python que se utiliza para importar módulos o funciones específicas de módulos.",
            "uso": "Se utiliza para traer funcionalidades específicas desde un módulo hacia el espacio de nombres actual.",
            "exemplo": """
                from math import sqrt
                print(sqrt(16))  # Saída: 4.0
                """
        },
        "function": {
            "significado": "Bloque de código diseñado para realizar una tarea específica y que puede ser reutilizado.",
            "uso": "Se utiliza para agrupar código relacionado que realiza una tarea común, permitiendo reutilización y modularidad.",
            "exemplo": """
                def saludo(nombre):
                    return f'Hola, {nombre}'
                
                print(saludo('Juan'))  # Saída: Hola, Juan
                """
        },
        "fibonacci": {
            "significado": "Secuencia matemática en la que cada número es la suma de los dos anteriores.",
            "uso": "Se utiliza para generar la secuencia de Fibonacci, frecuentemente en ejercicios de programación o algoritmos.",
            "exemplo": """
                def fibonacci(n):
                    if n <= 1:
                        return n
                    else:
                        return fibonacci(n-1) + fibonacci(n-2)
                
                print(fibonacci(5))  # Saída: 5
                """
        },
        "file": {
            "significado": "Objeto en Python que permite interactuar con archivos en el sistema de archivos.",
            "uso": "Se utiliza para abrir, leer, escribir y manipular archivos.",
            "exemplo": """
                with open('archivo.txt', 'r') as f:
                    contenido = f.read()
                print(contenido)
                """
        },
        "fwrite": {
            "significado": "Función utilizada para escribir datos en un archivo.",
            "uso": "Se utiliza para escribir datos binarios en un archivo abierto en modo de escritura.",
            "exemplo": """
                with open('archivo.bin', 'wb') as f:
                    f.write(b'Hello, World!')
                """
        },
        "fread": {
            "significado": "Función utilizada para leer datos de un archivo.",
            "uso": "Se utiliza para leer datos binarios de un archivo abierto en modo de lectura.",
            "exemplo": """
                with open('archivo.bin', 'rb') as f:
                    data = f.read()
                print(data)  # Saída: b'Hello, World!'
                """
        },
        "finally": {
            "significado": "Palabra clave en Python que define un bloque de código que se ejecutará siempre, independientemente de si ocurrió una excepción o no.",
            "uso": "Se utiliza en estructuras try-except para asegurar que se ejecute un bloque de código final, incluso si ocurre un error.",
            "exemplo": """
                try:
                    x = 1 / 0
                except ZeroDivisionError:
                    print('División por cero')
                finally:
                    print('Este bloque siempre se ejecuta')
                """
        },
        "freeze": {
            "significado": "Proceso de convertir un objeto mutable en uno inmutable.",
            "uso": "Se utiliza para evitar que un objeto sea modificado después de haber sido creado.",
            "exemplo": """
                # No hay una función explícita llamada freeze, pero en algunos casos como con `frozenset` se puede lograr lo mismo
                a = frozenset([1, 2, 3])
                print(a)  # Saída: frozenset({1, 2, 3})
                """
        },
        "flush": {
            "significado": "Método utilizado para vaciar los búferes de un archivo, asegurando que todos los datos se escriban en el disco.",
            "uso": "Se utiliza cuando es necesario asegurarse de que los datos almacenados en un búfer se escriban inmediatamente en el archivo.",
            "exemplo": """
                with open('archivo.txt', 'w') as f:
                    f.write('Hola')
                    f.flush()  # Asegura que los datos se escriban en el archivo
                """
        },
        "fstring": {
            "significado": "Cadena de texto que permite insertar expresiones dentro de la cadena de forma más legible y eficiente.",
            "uso": "Se utiliza para crear cadenas de texto interpoladas, donde se pueden insertar variables directamente dentro de la cadena.",
            "exemplo": """
                nombre = 'Juan'
                edad = 30
                print(f'Mi nombre es {nombre} y tengo {edad} años')  # Saída: Mi nombre es Juan y tengo 30 años
                """
        },
        "factorial": {
            "significado": "Función matemática que calcula el producto de todos los números enteros positivos hasta un número dado.",
            "uso": "Se utiliza para calcular el factorial de un número, frecuentemente en algoritmos de combinatoria y probabilidad.",
            "exemplo": """
                import math
                print(math.factorial(5))  # Saída: 120
                """
        },
        "frozen": {
            "significado": "Objeto inmutable que no puede ser modificado después de su creación.",
            "uso": "Se utiliza para crear objetos que no pueden ser alterados, como un `frozenset` en Python.",
            "exemplo": """
                a = frozenset([1, 2, 3])
                print(a)  # Saída: frozenset({1, 2, 3})
                """
        },
        "filterfalse": {
            "significado": "Función que devuelve un iterador que filtra los elementos de un iterable, excluyendo los que devuelven `True` en la función proporcionada.",
            "uso": "Se utiliza para obtener los elementos de un iterable para los cuales la función retorna `False`.",
            "exemplo": """
                from itertools import filterfalse
                result = filterfalse(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])
                print(list(result))  # Saída: [1, 3, 5]
                """
        },
        "fuzzy": {
            "significado": "Relacionado con la lógica difusa, que permite manejar información imprecisa o incierta.",
            "uso": "Se utiliza en sistemas que necesitan procesar datos aproximados o inciertos.",
            "exemplo": """
                # Ejemplo de una biblioteca de lógica difusa como `fuzzywuzzy` (para coincidencia difusa de texto)
                from fuzzywuzzy import fuzz
                print(fuzz.ratio('hola', 'Hola'))  # Saída: 100
                """
        },
        "fibonacci_sequence": {
            "significado": "Secuencia matemática en la que cada número es la suma de los dos anteriores.",
            "uso": "Se utiliza para generar la secuencia de Fibonacci.",
            "exemplo": """
                def fibonacci(n):
                    sequence = [0, 1]
                    while len(sequence) < n:
                        sequence.append(sequence[-1] + sequence[-2])
                    return sequence
                
                print(fibonacci(10))  # Saída: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
                """
        },
        "format_spec": {
            "significado": "Cadena utilizada para definir cómo se deben presentar los valores dentro de un formato de cadena.",
            "uso": "Se utiliza para especificar el formato de los valores dentro de una cadena, como precisión decimal, alineación, entre otros.",
            "exemplo": """
                pi = 3.14159
                print(f'{pi:.2f}')  # Saída: 3.14
                """
        },
        "fork": {
            "significado": "Proceso de crear un nuevo proceso, copiado del proceso original.",
            "uso": "Se utiliza en programación de sistemas para crear procesos secundarios.",
            "exemplo": """
                import os
                pid = os.fork()
                if pid > 0:
                    print(f'Proceso padre, PID: {pid}')
                else:
                    print(f'Proceso hijo, PID: {os.getpid()}')
                """
        },
        "forking": {
            "significado": "Acción de crear un nuevo proceso o subproceso desde un proceso principal.",
            "uso": "Se utiliza en sistemas operativos para crear procesos adicionales que ejecuten tareas de manera concurrente.",
            "exemplo": """
                import os
                pid = os.fork()
                # Similar al ejemplo de 'fork', pero abarcando el concepto de 'forking'
                """
        },
        "first": {
            "significado": "Acción de obtener el primer elemento de una secuencia o iterable.",
            "uso": "Se utiliza para acceder al primer valor de un iterable como una lista o conjunto.",
            "exemplo": """
                lista = [1, 2, 3, 4]
                print(lista[0])  # Saída: 1
                """
        },
        "float_format": {
            "significado": "Formato que define cómo se deben presentar los números flotantes en una cadena.",
            "uso": "Se utiliza para especificar la cantidad de decimales a mostrar en un número flotante.",
            "exemplo": """
                pi = 3.14159
                print(f'{pi:.2f}')  # Saída: 3.14
                """
        },
        "filter_none": {
            "significado": "Función que filtra elementos de un iterable, eliminando los valores `None`.",
            "uso": "Se utiliza para excluir valores `None` de una secuencia.",
            "exemplo": """
                lista = [1, None, 2, None, 3]
                result = filter(None, lista)
                print(list(result))  # Saída: [1, 2, 3]
                """
        },
        "func_code": {
            "significado": "Atributo que contiene el bytecode de la función en Python.",
            "uso": "Se utiliza para acceder al código de la función, generalmente en contextos de depuración o análisis.",
            "exemplo": """
                def ejemplo():
                    pass
                
                print(ejemplo.__code__)  # Saída: <code object ejemplo at 0x...>
                """
        },
        "float_power": {
            "significado": "Función que calcula un número elevado a una potencia flotante.",
            "uso": "Se utiliza para realizar exponentiación con números flotantes.",
            "exemplo": """
                print(pow(2, 3.5))  # Saída: 11.313708498984761
                """
        },
        "format_string": {
            "significado": "Cadena que define la estructura de un valor que se desea mostrar, utilizando especificadores de formato.",
            "uso": "Se utiliza para definir cómo deben mostrarse los valores en una cadena, como el número de decimales o la alineación.",
            "exemplo": """
                nombre = 'Juan'
                edad = 25
                print(f'Nombre: {nombre}, Edad: {edad}')  # Saída: Nombre: Juan, Edad: 25
                """
        },
        "filename": {
            "significado": "Cadena que representa el nombre de un archivo en el sistema de archivos.",
            "uso": "Se utiliza para especificar el nombre y la ubicación de un archivo que se desea manipular.",
            "exemplo": """
                archivo = 'documento.txt'
                with open(archivo, 'r') as f:
                    print(f.read())
                """
        },
        "file_object": {
            "significado": "Objeto que representa un archivo abierto en Python, a través del cual se puede leer, escribir o manipular el archivo.",
            "uso": "Se utiliza para interactuar con archivos abiertos en Python, accediendo a sus contenidos o modificándolos.",
            "exemplo": """
                with open('documento.txt', 'r') as f:
                    contenido = f.read()
                    print(contenido)
                """
        },
        "finally_clause": {
            "significado": "Parte de un bloque de código que siempre se ejecuta después de una instrucción `try`, independientemente de si se generó una excepción.",
            "uso": "Se utiliza para ejecutar código de limpieza o finalización, como el cierre de archivos o liberación de recursos.",
            "exemplo": """
                try:
                    archivo = open('documento.txt', 'r')
                    contenido = archivo.read()
                finally:
                    archivo.close()
                    print('Archivo cerrado')
                """
        },
        "file_read": {
            "significado": "Operación que permite leer los contenidos de un archivo en Python.",
            "uso": "Se utiliza para obtener los datos almacenados en un archivo para su procesamiento o visualización.",
            "exemplo": """
                with open('documento.txt', 'r') as archivo:
                    contenido = archivo.read()
                    print(contenido)
                """
        },
        "form": {
            "significado": "Estructura o plantilla utilizada para organizar datos de manera específica.",
            "uso": "Se utiliza en interfaces de usuario o aplicaciones web para capturar y organizar datos del usuario.",
            "exemplo": """
                formulario = {'nombre': 'Juan', 'edad': 25}
                print(formulario)
                """
        },
        "function_call": {
            "significado": "Acción de invocar una función en el código, pasándole los parámetros necesarios para ejecutar su tarea.",
            "uso": "Se utiliza para ejecutar una función y obtener su resultado.",
            "exemplo": """
                def suma(a, b):
                    return a + b
                resultado = suma(3, 4)
                print(resultado)  # Saída: 7
                """
        },
        "force": {
            "significado": "Acción de imponer o forzar la ejecución de algo, generalmente en el contexto de programación o manipulación de objetos.",
            "uso": "Se utiliza para forzar un comportamiento específico en un programa, como evitar errores o realizar una acción sin importar las condiciones.",
            "exemplo": """
                # No existe un 'force' directo en Python, pero se puede usar 'assert' para forzar condiciones
                assert 1 == 1, 'Condición falsa'
                """
        },
        "function_pointer": {
            "significado": "Referencia a una función que puede ser pasada y ejecutada como un argumento.",
            "uso": "Se utiliza en lenguajes como C o C++ para referenciar funciones y pasarlas como parámetros.",
            "exemplo": """
                # En Python no existe un puntero de función directo, pero las funciones se pueden pasar como objetos
                def saludar():
                    print('Hola')
                funcion = saludar
                funcion()  # Saída: Hola
                """
        },
        "float_precision": {
            "significado": "Número de dígitos que se usan para representar un número flotante con precisión.",
            "uso": "Se utiliza para especificar la cantidad de decimales que deben considerarse al realizar operaciones con números flotantes.",
            "exemplo": """
                numero = 3.14159265359
                print(f'{numero:.2f}')  # Saída: 3.14
                """
        },
        "format_error": {
            "significado": "Error que ocurre cuando hay un problema al formatear datos, como una cadena mal estructurada.",
            "uso": "Se utiliza para manejar errores relacionados con la conversión o formateo incorrecto de datos.",
            "exemplo": """
                try:
                    int('abc')
                except ValueError as e:
                    print(f'Error de formato: {e}')
                """
        },
        "file_write": {
            "significado": "Operación que permite escribir datos en un archivo en Python.",
            "uso": "Se utiliza para almacenar información en un archivo, sobrescribiéndolo o agregando nuevos datos.",
            "exemplo": """
                with open('documento.txt', 'w') as archivo:
                    archivo.write('Hola, mundo!')
                """
        },
        "fibonacci_search": {
            "significado": "Método de búsqueda que utiliza los números de Fibonacci para dividir el espacio de búsqueda de manera eficiente.",
            "uso": "Se utiliza como una alternativa al algoritmo de búsqueda binaria para encontrar un elemento en un array.",
            "exemplo": """
                # Implementación de Fibonacci Search no estándar, pero puede utilizarse como alternativa a la búsqueda binaria
                def fibonacci_search(arr, x):
                    fib_m_minus_2 = 0
                    fib_m_minus_1 = 1
                    fib_m = fib_m_minus_1 + fib_m_minus_2
                    while(fib_m < len(arr)):
                        fib_m_minus_2 = fib_m_minus_1
                        fib_m_minus_1 = fib_m
                        fib_m = fib_m_minus_1 + fib_m_minus_2
                    """
        },
        "filter_map": {
            "significado": "Función que filtra los elementos de un iterable y luego aplica una función de mapeo a los elementos restantes.",
            "uso": "Se utiliza para realizar transformaciones y filtrados de manera eficiente en secuencias de datos.",
            "exemplo": """
                from itertools import filterfalse
                data = [1, 2, 3, 4, 5]
                result = map(lambda x: x * 2, filter(lambda x: x % 2 == 0, data))
                print(list(result))  # Saída: [4, 8]
                """
        },

    },
    "g": {
        "": {
            "significado": "",
            "uso": "",
            "ejemplo": ''''''
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
            "ejemplo": '''
                def mostrar_informacion(**kwargs):
                    for clave, valor in kwargs.items():
                        print(f'{clave}: {valor}')

                mostrar_informacion(nombre='Juan', edad=30)
                # Salida:
                # nombre: Juan
                # edad: 30
                '''
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
