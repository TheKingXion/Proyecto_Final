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
        
    },
    "e": {
        "": {
            "significado": "",
            "uso": "",
            "ejemplo": ''''''
        },
    },
    "f": {
        "": {
            "significado": "",
            "uso": "",
            "ejemplo": ''''''
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
