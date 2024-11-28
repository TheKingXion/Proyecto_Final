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
            "significado": "Verifica se um objeto é invocável (como uma função ou uma classe).",
            "uso": "É utilizado para determinar se um objeto pode ser chamado.",
            "ejemplo": '''
                def funcao():
                    return "Olá"

                print(callable(funcao))  # Saída: True
                print(callable(42))  # Saída: False
                '''
        },
        "chr": {
            "significado": "Retorna o caractere Unicode correspondente a um número inteiro.",
            "uso": "É utilizado para converter um código Unicode em sua representação de caractere.",
            "ejemplo": '''
                print(chr(65))  # Saída: 'A'
                print(chr(8364))  # Saída: '€'
                '''
        },
        "class": {
            "significado": "Palavra-chave para definir uma classe em Python.",
            "uso": "É utilizada para criar objetos personalizados com atributos e métodos.",
            "ejemplo": '''
                class Pessoa:
                    def __init__(self, nome):
                        self.nome = nome

                    def cumprimentar(self):
                        print(f"Olá, meu nome é {self.nome}")

                p = Pessoa("João")
                p.cumprimentar()  # Saída: Olá, meu nome é João
                '''
        },
        "classmethod": {
            "significado": "Define um método de classe, que recebe a classe como primeiro argumento em vez de uma instância.",
            "uso": "É utilizado para criar métodos que afetam a classe como um todo.",
            "ejemplo": '''
                class MinhaClasse:
                    contador = 0

                    @classmethod
                    def incrementar(cls):
                        cls.contador += 1

                MinhaClasse.incrementar()
                print(MinhaClasse.contador)  # Saída: 1
                '''
        },
        "compile": {
            "significado": "Compila uma string de código em um objeto executável de Python.",
            "uso": "É utilizado para compilar código dinâmico a partir de texto ou arquivos.",
            "ejemplo": '''
                codigo = "print('Olá Mundo')"
                compilado = compile(codigo, '<string>', 'exec')
                exec(compilado)  # Saída: Olá Mundo
                '''
        },
        "complex": {
            "significado": "Cria um número complexo em Python.",
            "uso": "É utilizado para representar números complexos com parte real e imaginária.",
            "ejemplo": '''
                c = complex(2, 3)
                print(c)  # Saída: (2+3j)
                print(c.real, c.imag)  # Saída: 2.0 3.0
                '''
        },
        "continue": {
            "significado": "Palavra-chave que salta para a próxima iteração de um loop.",
            "uso": "É utilizada para ignorar o restante do código na iteração atual.",
            "ejemplo": '''
                for i in range(5):
                    if i == 2:
                        continue
                    print(i)  # Saída: 0 1 3 4
                '''
        },
        "copy": {
            "significado": "Cria uma cópia superficial de um objeto.",
            "uso": "É utilizada para duplicar estruturas de dados sem duplicar objetos aninhados.",
            "ejemplo": '''
                import copy

                lista = [1, 2, [3, 4]]
                copia = copy.copy(lista)
                print(copia)  # Saída: [1, 2, [3, 4]]
                '''
        },
        "coroutine": {
            "significado": "Objeto que representa uma função assíncrona suspensa.",
            "uso": "É utilizada para lidar com tarefas assíncronas usando `async` e `await`.",
            "ejemplo": '''
                async def tarefa():
                    print("Início")
                    await asyncio.sleep(1)
                    print("Fim")

                import asyncio
                asyncio.run(tarefa())  # Saída: Início... Fim
                '''
        },
        "count": {
            "significado": "Retorna o número de ocorrências de um elemento em uma coleção.",
            "uso": "É utilizada para contar quantas vezes um elemento aparece em uma lista ou string.",
            "ejemplo": '''
                lista = [1, 2, 2, 3]
                print(lista.count(2))  # Saída: 2
                '''
        },
        "clear": {
            "significado": "Remove todos os elementos de uma lista ou dicionário.",
            "uso": "É utilizada para esvaziar o conteúdo de uma lista ou dicionário.",
            "ejemplo": '''
                lista = [1, 2, 3]
                lista.clear()
                print(lista)  # Saída: []
                '''
        },
        "cmath": {
            "significado": "Módulo que fornece funções matemáticas para trabalhar com números complexos.",
            "uso": "É utilizado para realizar operações matemáticas em números complexos.",
            "ejemplo": '''
                import cmath

                numero = cmath.sqrt(-1)
                print(numero)  # Saída: 1j
                '''
        },
        "chain": {
            "significado": "Função que combina vários iteradores em um só.",
            "uso": "É utilizada para concatenar múltiplos iteradores.",
            "ejemplo": '''
                import itertools

                a = [1, 2, 3]
                b = [4, 5, 6]
                resultado = list(itertools.chain(a, b))
                print(resultado)  # Saída: [1, 2, 3, 4, 5, 6]
                '''
        },
        "csv": {
            "significado": "Módulo para ler e escrever arquivos em formato CSV (Comma Separated Values).",
            "uso": "É utilizado para manipular arquivos CSV.",
            "ejemplo": '''
                import csv

                with open('arquivo.csv', mode='w', newline='') as arquivo:
                    writer = csv.writer(arquivo)
                    writer.writerow(['Nome', 'Idade'])
                    writer.writerow(['Ana', 30])
                '''
        },
        "copyreg": {
            "significado": "Módulo que fornece funções para registrar objetos para cópia e desacoplamento.",
            "uso": "É utilizado para personalizar o comportamento de cópia e armazenamento de objetos.",
            "ejemplo": '''
                import copyreg

                def criar_pessoa(nome, idade):
                    return {'nome': nome, 'idade': idade}

                copyreg.pickle(dict, criar_pessoa)
                '''
        },
        "counter": {
            "significado": "Classe no módulo `collections` que conta elementos hasháveis em uma sequência.",
            "uso": "É utilizada para contar a frequência de elementos em um iterável.",
            "ejemplo": '''
                from collections import Counter

                contador = Counter([1, 2, 2, 3, 3, 3])
                print(contador)  # Saída: Counter({3: 3, 2: 2, 1: 1})
                '''
        },
        "cProfile": {
            "significado": "Módulo para a medição do desempenho de programas em Python.",
            "uso": "É utilizado para fazer perfis de código e analisar a eficiência do programa.",
            "ejemplo": '''
                import cProfile

                def funcao():
                    for i in range(1000):
                        pass

                cProfile.run('funcao()')
                '''
        },
        "capitalize": {
            "significado": "Método de string que converte a primeira letra em maiúscula e o resto em minúsculas.",
            "uso": "É utilizado para capitalizar a primeira letra de uma string.",
            "ejemplo": '''
                texto = 'ola mundo'
                print(texto.capitalize())  # Saída: 'Ola mundo'
                '''
        },
        "center": {
            "significado": "Método de string que centraliza uma string dentro de um campo de comprimento especificado.",
            "uso": "É utilizado para alinhar texto no centro de uma string com preenchimento.",
            "ejemplo": '''
                texto = 'ola'
                print(texto.center(10, '*'))  # Saída: '**ola****'
                '''
        },
        "ceil": {
            "significado": "Função do módulo `math` que retorna o inteiro mais próximo maior ou igual a um número dado.",
            "uso": "É utilizada para arredondar um número para cima.",
            "ejemplo": '''
                import math

                numero = 3.4
                print(math.ceil(numero))  # Saída: 4
                '''
        },
        "call": {
            "significado": "Método utilizado para invocar um objeto que é callable, como funções ou classes.",
            "uso": "É utilizado para chamar um objeto que pode ser executado.",
            "ejemplo": '''
                def saudacao():
                    return 'Olá'

                print(callable(saudacao))  # Saída: True
                '''
        },
        "clamp": {
            "significado": "Função que restringe um valor dentro de um intervalo especificado.",
            "uso": "É utilizada para garantir que um valor permaneça dentro de um intervalo definido.",
            "ejemplo": '''
                def clamp(valor, minimo, maximo):
                    return max(minimo, min(valor, maximo))

                print(clamp(5, 1, 10))  # Saída: 5
                '''
        },
        "choice": {
            "significado": "Função do módulo `random` que seleciona um elemento aleatório de uma sequência.",
            "uso": "É utilizada para escolher um valor aleatório de uma lista ou sequência.",
            "ejemplo": '''
                import random

                lista = [1, 2, 3, 4, 5]
                print(random.choice(lista))  # Saída: um valor aleatório da lista
                '''
        },
        "collections": {
            "significado": "Módulo que implementa tipos de dados especializados como `Counter`, `deque`, `OrderedDict`, entre outros.",
            "uso": "É utilizado para trabalhar com coleções de dados de forma eficiente.",
            "ejemplo": '''
                from collections import deque

                fila = deque([1, 2, 3])
                fila.append(4)
                print(fila)  # Saída: deque([1, 2, 3, 4])
                '''
        },
        "compress": {
            "significado": "Função no módulo `itertools` que permite comprimir elementos de um iterável.",
            "uso": "É utilizada para filtrar os elementos de um iterável com base em uma condição booleana.",
            "ejemplo": '''
                import itertools

                dados = [1, 2, 3, 4, 5]
                condicoes = [True, False, True, False, True]
                resultado = list(itertools.compress(dados, condicoes))
                print(resultado)  # Saída: [1, 3, 5]
                '''
        },
        "complex_conjugate": {
            "significado": "Método dos números complexos em Python que retorna o conjugado complexo de um número.",
            "uso": "É utilizado para obter o conjugado de um número complexo.",
            "ejemplo": '''
                numero_complexo = 3 + 4j
                print(numero_complexo.conjugate())  # Saída: (3-4j)
                '''
        },
        "ctypes": {
            "significado": "Módulo em Python que permite interagir com bibliotecas de C e realizar chamadas de funções de baixo nível.",
            "uso": "É utilizado para trabalhar com tipos de dados e funções de bibliotecas externas escritas em C.",
            "ejemplo": '''
                import ctypes

                # Criar uma variável de tipo inteiro
                valor = ctypes.c_int(5)
                print(valor.value)  # Saída: 5
                '''
        },
        "clear_screen": {
            "significado": "Função utilizada para limpar a tela do console.",
            "uso": "É utilizada para remover o conteúdo visível do terminal ou console.",
            "ejemplo": '''
                import os

                def clear_screen():
                    os.system('cls' if os.name == 'nt' else 'clear')

                clear_screen()
                '''
        },
        "call_later": {
            "significado": "Método utilizado para agendar a execução de uma função após um certo tempo.",
            "uso": "É utilizado em programação assíncrona para executar tarefas após um atraso.",
            "ejemplo": '''
                import asyncio

                async def tarefa():
                    print('Tarefa executada')

                asyncio.get_event_loop().call_later(2, asyncio.create_task, tarefa())
                '''
        },
        "chunk": {
            "significado": "Técnica que divide um iterável em partes menores ou blocos.",
            "uso": "É utilizada para dividir grandes volumes de dados em partes mais manejáveis.",
            "ejemplo": '''
                def chunk(iteravel, tamanho):
                    for i in range(0, len(iteravel), tamanho):
                        yield iteravel[i:i + tamanho]

                lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                for bloco in chunk(lista, 3):
                    print(bloco)  # Saída: [1, 2, 3], [4, 5, 6], [7, 8, 9]
                '''
        },
        "cycle": {
            "significado": "Função no módulo `itertools` que cria um iterador que repete indefinidamente uma sequência.",
            "uso": "É utilizada para percorrer um iterável em loop infinito.",
            "ejemplo": '''
                import itertools

                ciclo = itertools.cycle([1, 2, 3])
                for i in range(6):
                    print(next(ciclo))  # Saída: 1, 2, 3, 1, 2, 3
                '''
        },
        "coerce": {
            "significado": "Função que tenta converter um valor em um tipo compatível.",
            "uso": "Era utilizada para forçar a conversão de um valor para um tipo de dados específico.",
            "ejemplo": '''
                # A função coerce foi removida em versões modernas do Python.
                '''
        },
        "current_thread": {
            "significado": "Método do módulo `threading` que retorna a thread atual de execução.",
            "uso": "É utilizado para obter a thread de execução onde o código está sendo executado.",
            "ejemplo": '''
                import threading

                def mostrar_thread():
                    print(threading.current_thread())

                mostrar_thread()
                '''
        },
        "configparser": {
            "significado": "Módulo que permite manipular arquivos de configuração, como arquivos INI.",
            "uso": "É utilizado para ler, escrever e modificar arquivos de configuração.",
            "ejemplo": '''
                import configparser

                config = configparser.ConfigParser()
                config.read('config.ini')

                print(config['DEFAULT']['color'])  # Saída: vermelho
                '''
        },
        "compileall": {
            "significado": "Módulo em Python que compila todos os arquivos `.py` em um diretório e seus subdiretórios.",
            "uso": "É utilizado para compilar código Python para bytecode, o que pode melhorar o desempenho da execução.",
            "ejemplo": '''
                import compileall

                compileall.compile_dir('meu_diretorio')
                '''
        },
        "copytree": {
            "significado": "Função no módulo `shutil` que copia um diretório completo, incluindo seu conteúdo, para outro destino.",
            "uso": "É utilizada para copiar um diretório e todo o seu conteúdo para um novo local.",
            "ejemplo": '''
                import shutil

                shutil.copytree('origem', 'destino')
                '''
        },
    },
    "d": {
        "def": {
            "significado": "Palavra-chave em Python usada para definir uma função.",
            "uso": "É utilizada para criar uma nova função com um nome e um bloco de código.",
            "ejemplo": '''
                def saudacao():
                    print('Olá Mundo')

                saudacao()  # Saída: Olá Mundo
                '''
        },
        "delattr": {
            "significado": "Função que remove um atributo de um objeto em Python.",
            "uso": "É utilizada para excluir um atributo específico de um objeto.",
            "ejemplo": '''
                class Pessoa:
                    def __init__(self, nome):
                        self.nome = nome

                p = Pessoa('João')
                delattr(p, 'nome')
                print(hasattr(p, 'nome'))  # Saída: False
                '''
        },
        "dataframe": {
            "significado": "Estrutura de dados bidimensional na biblioteca Pandas, similar a uma tabela, que permite armazenar dados de diferentes tipos.",
            "uso": "É utilizada para manipular grandes volumes de dados tabulares em Python.",
            "ejemplo": '''
                import pandas as pd

                dados = {'Nome': ['João', 'Ana'], 'Idade': [28, 22]}
                df = pd.DataFrame(dados)
                print(df)
                '''
        },
        "decode": {
            "significado": "Método utilizado para decodificar dados binários para um formato de texto, geralmente em uma codificação como UTF-8.",
            "uso": "É utilizado para converter dados binários em cadeias de texto legíveis.",
            "ejemplo": '''
                codificado = b'Olá Mundo'
                decodificado = codificado.decode('utf-8')
                print(decodificado)  # Saída: Olá Mundo
                '''
        },
        "decimal": {
            "significado": "Módulo em Python que fornece suporte para realizar cálculos com decimais de precisão arbitrária.",
            "uso": "É utilizado para realizar operações aritméticas precisas sem os erros de arredondamento típicos dos números de ponto flutuante.",
            "ejemplo": '''
                from decimal import Decimal

                x = Decimal('0.1')
                y = Decimal('0.2')
                print(x + y)  # Saída: 0.3
                '''
        },
        "device": {
            "significado": "Termo geral para se referir a qualquer dispositivo de hardware ou sistema onde um programa é executado.",
            "uso": "É utilizado para se referir a dispositivos como computadores, telefones móveis, etc.",
            "ejemplo": "Não é um termo específico de Python, mas pode ser usado em bibliotecas como TensorFlow para se referir a dispositivos de processamento como CPU ou GPU."
        },
        "dict.get": {
            "significado": "Método dos dicionários em Python que retorna o valor de uma chave especificada ou um valor padrão se a chave não existir.",
            "uso": "É utilizado para obter o valor associado a uma chave sem gerar um erro se a chave não existir.",
            "ejemplo": '''
                d = {'a': 1, 'b': 2}
                print(d.get('a'))  # Saída: 1
                print(d.get('c', 'Não encontrado'))  # Saída: Não encontrado
                '''
        },
        "dropna": {
            "significado": "Método em Pandas utilizado para remover valores ausentes (NaN) em um DataFrame ou Série.",
            "uso": "É utilizado para limpar os dados removendo as linhas ou colunas que contêm valores nulos.",
            "ejemplo": '''
                import pandas as pd

                df = pd.DataFrame({'A': [1, 2, None], 'B': [None, 3, 4]})
                print(df.dropna())
                '''
        },
        "dtype": {
            "significado": "Propriedade dos arrays em Numpy ou das colunas em um DataFrame do Pandas que indica o tipo de dado dos elementos.",
            "uso": "É utilizada para obter ou especificar o tipo de dados de um array ou coluna.",
            "ejemplo": '''
                import numpy as np

                arr = np.array([1, 2, 3])
                print(arr.dtype)  # Saída: int64
                '''
        },
        "deque.appendleft": {
            "significado": "Método do tipo de dado `deque` no módulo `collections` que adiciona um elemento ao início da deque.",
            "uso": "É utilizado para inserir um novo elemento na parte esquerda de uma deque.",
            "ejemplo": '''
                from collections import deque

                d = deque([2, 3, 4])
                d.appendleft(1)
                print(d)  # Saída: deque([1, 2, 3, 4])
                '''
        },
        "dict.update": {
            "significado": "Método dos dicionários em Python que atualiza um dicionário com os elementos de outro dicionário ou iterável.",
            "uso": "É utilizado para adicionar ou modificar elementos em um dicionário usando outro dicionário ou iterável.",
            "ejemplo": '''
                d1 = {'a': 1, 'b': 2}
                d2 = {'b': 3, 'c': 4}
                d1.update(d2)
                print(d1)  # Saída: {'a': 1, 'b': 3, 'c': 4}
                '''
        },
        "del": {
            "significado": "Palavra-chave em Python que remove um atributo ou um elemento de uma coleção.",
            "uso": "É utilizada para remover elementos de uma lista, atributo de um objeto ou uma variável.",
            "ejemplo": '''
                lista = [1, 2, 3]
                del lista[1]
                print(lista)  # Saída: [1, 3]
                '''
        },
        "dict": {
            "significado": "Tipo de dado em Python que representa um dicionário, uma coleção de pares chave-valor.",
            "uso": "É utilizado para armazenar e manipular dados de forma eficiente, associando chaves únicas a valores.",
            "ejemplo": '''
                d = {'a': 1, 'b': 2}
                print(d['a'])  # Saída: 1
                '''
        },
        "dir": {
            "significado": "Função que retorna uma lista dos atributos e métodos de um objeto.",
            "uso": "É utilizada para obter informações sobre os métodos e atributos disponíveis para um objeto ou módulo.",
            "ejemplo": '''
                x = [1, 2, 3]
                print(dir(x))
                '''
        },
        "divmod": {
            "significado": "Função que recebe dois números e retorna uma tupla com o quociente e o resto da sua divisão.",
            "uso": "É utilizada para obter tanto o quociente quanto o resto de uma divisão em uma única operação.",
            "ejemplo": '''
                resultado = divmod(9, 4)
                print(resultado)  # Saída: (2, 1)
                '''
        },
        "deque": {
            "significado": "Tipo de dado no módulo `collections` do Python que representa uma fila duplamente terminada, permitindo adicionar e remover elementos de ambos os extremos de forma eficiente.",
            "uso": "É usado para implementar filas e pilhas de maneira eficiente.",
            "ejemplo": '''
                from collections import deque

                d = deque([1, 2, 3])
                d.append(4)
                print(d)  # Saída: deque([1, 2, 3, 4])
                '''
        },
        "defaultdict": {
            "significado": "Classe no módulo `collections` que estende o dicionário padrão e permite definir um valor padrão para chaves inexistentes.",
            "uso": "É usado para evitar erros ao acessar chaves não existentes, fornecendo um valor padrão.",
            "ejemplo": '''
                from collections import defaultdict

                d = defaultdict(int)
                d['a'] += 1
                print(d)  # Saída: defaultdict(<class 'int'>, {'a': 1})
                '''
        },
        "decode": {
            "significado": "Método usado para converter dados binários em texto em uma codificação específica.",
            "uso": "É usado para decodificar uma sequência de bytes em uma string de texto em uma codificação específica.",
            "ejemplo": '''
                encoded = b'Olá Mundo'
                decoded = encoded.decode('utf-8')
                print(decoded)  # Saída: Olá Mundo
                '''
        },
        "deflate": {
            "significado": "Algoritmo de compressão de dados sem perda, usado para reduzir o tamanho de arquivos.",
            "uso": "É usado para compactar dados em um formato mais eficiente.",
            "ejemplo": '''
                import zlib

                data = b'Olá Mundo'*100
                compressed = zlib.compress(data)
                print(compressed)
                '''
        },
        "deepcopy": {
            "significado": "Função do módulo `copy` que cria uma cópia profunda de um objeto, ou seja, copia todos os elementos do objeto original, incluindo objetos dentro de objetos.",
            "uso": "É usado quando é necessário fazer uma cópia completa e independente de um objeto.",
            "ejemplo": '''
                import copy

                original = {'a': [1, 2, 3]}
                copia = copy.deepcopy(original)
                copia['a'][0] = 100
                print(original)  # Saída: {'a': [1, 2, 3]}
                print(copia)     # Saída: {'a': [100, 2, 3]}
                '''
        },
        "detach": {
            "significado": "Método usado em objetos no Python para desvincular um objeto de seu contexto ou fluxo de dados.",
            "uso": "É usado para liberar recursos ou desvincular um objeto de seu ambiente de execução.",
            "ejemplo": '''
                import torch

                tensor = torch.tensor([1, 2, 3])
                detached_tensor = tensor.detach()
                print(detached_tensor)  # Saída: tensor([1, 2, 3])
                '''
        },
        "dump": {
            "significado": "Método da biblioteca `pickle` que serializa um objeto e o grava em um arquivo.",
            "uso": "É usado para salvar um objeto em um arquivo de forma serializada.",
            "ejemplo": '''
                import pickle

                data = {'a': 1, 'b': 2}
                with open('data.pkl', 'wb') as f:
                    pickle.dump(data, f)
                '''
        },
        "dumps": {
            "significado": "Método da biblioteca `pickle` que serializa um objeto e o retorna como uma string de bytes.",
            "uso": "É usado para converter um objeto em um formato de string para armazenamento ou transmissão.",
            "ejemplo": '''
                import pickle

                data = {'a': 1, 'b': 2}
                serialized = pickle.dumps(data)
                print(serialized)
                '''
        },
        "difference": {
            "significado": "Método de conjuntos no Python que retorna a diferença entre dois ou mais conjuntos.",
            "uso": "É usado para encontrar os elementos que estão em um conjunto, mas não nos outros.",
            "ejemplo": '''
                a = {1, 2, 3}
                b = {2, 3, 4}
                print(a.difference(b))  # Saída: {1}
                '''
        },
        "difference_update": {
            "significado": "Método de conjuntos no Python que remove os elementos de um conjunto que estão presentes em outro conjunto.",
            "uso": "É usado para modificar um conjunto, removendo os elementos que se encontram em outro conjunto.",
            "ejemplo": '''
                a = {1, 2, 3}
                b = {2, 3, 4}
                a.difference_update(b)
                print(a)  # Saída: {1}
                '''
        },
        "decode_header": {
            "significado": "Função do módulo `email.header` que decodifica um cabeçalho de e-mail.",
            "uso": "É usada para decodificar um cabeçalho de e-mail que pode estar em diferentes codificações.",
            "ejemplo": '''
                from email.header import decode_header

                header = '=?utf-8?B?SG9sYSBNdW5kbyA8MTIzNDU+?='
                decoded, encoding = decode_header(header)[0]
                print(decoded.decode(encoding))  # Saída: Olá Mundo <12345>
                '''
        },
        "disk_usage": {
            "significado": "Função do módulo `shutil` que retorna o uso do disco de um caminho ou diretório.",
            "uso": "É usada para obter informações sobre o espaço usado e disponível em um sistema de arquivos.",
            "ejemplo": '''
                import shutil

                usage = shutil.disk_usage('/')
                print(usage)  # Saída: usage(total=500000000, used=200000000, free=300000000)
                '''
        },
        "datetime": {
            "significado": "Módulo do Python que fornece classes para trabalhar com datas e horas.",
            "uso": "É usado para manipular e trabalhar com datas, horas e tempos em geral.",
            "ejemplo": '''
                import datetime

                agora = datetime.datetime.now()
                print(agora)  # Saída: 2024-11-22 12:00:00.123456
                '''
        },
        "disk_cache": {
            "significado": "Armazenamento em cache no disco para melhorar a velocidade de acesso a dados ou resultados computacionais.",
            "uso": "É usado para armazenar temporariamente resultados ou dados no disco para evitar a necessidade de recalcular ou obter novamente os dados.",
            "ejemplo": '''
                import joblib

                result = joblib.Memory('cache_dir').cache(some_function)
                '''
        },
    },
    "e": {
        "enumerate": {
            "significado": "Função incorporada do Python que adiciona um contador a um iterável e o retorna como um objeto iterável de tuplas.",
            "uso": "É usada para obter tanto o índice quanto o valor dos elementos em um iterável.",
            "ejemplo": '''
                lista = ['a', 'b', 'c']
                for indice, valor in enumerate(lista):
                    print(indice, valor)
                # Saída:
                # 0 a
                # 1 b
                # 2 c
                '''
        },
        "eval": {
            "significado": "Função incorporada do Python que avalia uma string de código como uma expressão Python.",
            "uso": "É usada para executar expressões Python contidas em uma string e retornar o resultado.",
            "ejemplo": '''
                x = 2
                resultado = eval('x + 1')
                print(resultado)  # Saída: 3
                '''
        },
        "exec": {
            "significado": "Função incorporada do Python que executa uma string de código como um bloco de código completo.",
            "uso": "É usada para executar código Python dinamicamente.",
            "ejemplo": '''
                codigo = 'for i in range(3): print(i)'
                exec(codigo)
                # Saída:
                # 0
                # 1
                # 2
                '''
        },
        "except": {
            "significado": "Palavra-chave no Python usada para tratar exceções dentro de um bloco try-except.",
            "uso": "É usada para capturar e tratar exceções que ocorrem no bloco try.",
            "ejemplo": '''
                try:
                    x = 1 / 0
                except ZeroDivisionError:
                    print('Erro: Divisão por zero')
                # Saída: Erro: Divisão por zero
                '''
        },
        "else": {
            "significado": "Palavra-chave no Python usada em estruturas de controle condicional (if, try) para executar um bloco de código se a condição não for atendida ou nenhuma exceção ocorrer.",
            "uso": "É usada para executar um bloco de código quando a condição não for atendida ou nenhuma exceção ocorrer.",
            "ejemplo": '''
                if 3 > 1:
                    print('Condição verdadeira')
                else:
                    print('Condição falsa')
                # Saída: Condição verdadeira
                '''
        },
        "elif": {
            "significado": "Palavra-chave no Python usada em estruturas condicionais para verificar uma condição adicional caso as anteriores não sejam atendidas.",
            "uso": "É usada para lidar com múltiplas condições em uma estrutura if-elif-else.",
            "ejemplo": '''
                x = 3
                if x > 5:
                    print('Maior que 5')
                elif x == 3:
                    print('Igual a 3')
                else:
                    print('Menor que 3')
                # Saída: Igual a 3
                '''
        },
        "exit": {
            "significado": "Função incorporada do Python que finaliza a execução do programa.",
            "uso": "É usada para sair de um programa ou fechar um ambiente de execução.",
            "ejemplo": '''
                import sys
                sys.exit('Finalizando o programa')
                # O programa é encerrado com a mensagem 'Finalizando o programa'
                '''
        },
        "end": {
            "significado": "Palavra-chave usada no Python para especificar o fim de um bloco ou a terminação de uma string.",
            "uso": "É usada principalmente nas funções de impressão para controlar o fim da saída.",
            "ejemplo": '''
                print('Olá', end=' ')
                print('Mundo')
                # Saída: Olá Mundo
                '''
        },
        "expandtabs": {
            "significado": "Método de strings no Python que substitui os caracteres de tabulação por espaços.",
            "uso": "É usada para alinhar texto substituindo as tabulações por um número determinado de espaços.",
            "ejemplo": '''
                texto = 'Olá\tMundo'
                print(texto.expandtabs(4))
                # Saída: Olá   Mundo
                '''
        },
        "encode": {
            "significado": "Método de strings no Python que codifica uma string em uma sequência de bytes usando um codificador específico.",
            "uso": "É usada para converter uma string em uma sequência de bytes para ser armazenada ou transmitida em formatos específicos.",
            "ejemplo": '''
                texto = 'Olá Mundo'
                encoded = texto.encode('utf-8')
                print(encoded)
                # Saída: b'Olá Mundo'
                '''
        },
        "element": {
            "significado": "Um item individual dentro de uma coleção ou estrutura de dados.",
            "uso": "É usada para se referir a um objeto dentro de uma lista, conjunto, dicionário, etc.",
            "ejemplo": '''
                lista = [1, 2, 3]
                print(lista[0])  # Saída: 1
                '''
        },
        "error": {
            "significado": "Condição anômala na execução de um programa que interrompe seu fluxo normal.",
            "uso": "É usada para indicar que algo deu errado durante a execução do código.",
            "ejemplo": '''
                try:
                    1 / 0
                except ZeroDivisionError as e:
                    print(f'Erro: {e}')
                # Saída: Erro: division by zero
                '''
        },
        "exception": {
            "significado": "Evento que altera o fluxo normal de execução do programa, geralmente devido a um erro.",
            "uso": "É usada para tratar erros no código e executar ações específicas quando ocorrem.",
            "ejemplo": '''
                try:
                    int('a')
                except ValueError:
                    print('Erro: não é possível converter para inteiro')
                # Saída: Erro: não é possível converter para inteiro
                '''
        },
        "evaluate": {
            "significado": "Executar ou calcular o valor de uma expressão ou função.",
            "uso": "É usada para obter o resultado de uma expressão.",
            "ejemplo": '''
                x = 5
                resultado = eval('x + 2')
                print(resultado)  # Saída: 7
                '''
        },
        "elements": {
            "significado": "Itens ou componentes individuais dentro de um conjunto ou coleção.",
            "uso": "É usada para se referir às partes de uma estrutura de dados.",
            "ejemplo": '''
                conjunto = {1, 2, 3}
                for elemento in conjunto:
                    print(elemento)
                # Saída:
                # 1
                # 2
                # 3
                '''
        },
        "exponential": {
            "significado": "Relacionado com a operação matemática de exponenciação, que calcula o valor de uma base elevada a um expoente.",
            "uso": "É usada para realizar cálculos exponenciais.",
            "ejemplo": '''
                import math
                resultado = math.exp(2)
                print(resultado)  # Saída: 7.3890560989306495
                '''
        },
        "enumerations": {
            "significado": "Uma lista ou conjunto de elementos, muitas vezes com um valor associado ou um identificador.",
            "uso": "É usada para representar um conjunto de valores possíveis de uma variável.",
            "ejemplo": '''
                from enum import Enum

                class Cor(Enum):
                    VERMELHO = 1
                    VERDE = 2
                    AZUL = 3

                print(Cor.VERMELHO)  # Saída: Cor.VERMELHO
                '''
        },
        "encode_utf8": {
            "significado": "Método de codificação que converte uma string de caracteres em uma sequência de bytes usando o formato UTF-8.",
            "uso": "É usada para converter texto em uma representação binária usando UTF-8.",
            "ejemplo": '''
                texto = 'Olá Mundo'
                encoded = texto.encode('utf-8')
                print(encoded)  # Saída: b'Olá Mundo'
                '''
        },
        "execfile": {
            "significado": "Função que executa um arquivo Python como se fosse um script.",
            "uso": "É usada para executar um arquivo Python externo.",
            "ejemplo": '''
                # Este comando está disponível apenas no Python 2
                execfile('script.py')
                '''
        },
        "edit_distance": {
            "significado": "Medida que calcula a diferença entre duas strings com base nas operações necessárias para converter uma na outra.",
            "uso": "É usada para comparar quão semelhantes são duas strings e determinar quantas mudanças são necessárias para torná-las idênticas.",
            "ejemplo": '''
                from nltk.metrics import edit_distance

                distancia = edit_distance('kitten', 'sitting')
                print(distancia)  # Saída: 3
                '''
        },
        "eval_input": {
            "significado": "Função que avalia uma entrada do usuário, normalmente através da função `input()`.",
            "uso": "É usada para obter e avaliar uma entrada fornecida pelo usuário.",
            "ejemplo": '''
                entrada = input('Digite um número: ')
                resultado = eval(entrada)
                print(resultado)
                '''
        },
        "xceed": {
            "significado": "Termo usado para descrever algo que supera ou excede um limite ou expectativa.",
            "uso": "É usada para indicar que algo superou um padrão ou limite.",
            "ejemplo": "A nova atualização excede nossas expectativas em termos de desempenho."
        },
        "expected": {
            "significado": "Algo antecipado ou previsto, com base em expectativas ou previsões.",
            "uso": "É usada para descrever o que se espera que aconteça em uma situação.",
            "ejemplo": "O resultado esperado era um aumento na velocidade de processamento."
        },
        "encode_base64": {
            "significado": "Método de codificação que converte dados binários em uma representação de texto em base 64.",
            "uso": "É usada para codificar dados binários em uma string de texto legível em base 64.",
            "ejemplo": '''
                import base64
                encoded = base64.b64encode(b'olá')
                print(encoded)  # Saída: b'b2xh'
                '''
        },
        "execute": {
            "significado": "Realizar ou executar um conjunto de instruções ou um programa.",
            "uso": "É usada para colocar em prática uma ação ou executar código.",
            "ejemplo": '''
                def funcao():
                    print('Executando...')
                funcao()  # Saída: Executando...
                '''
        },
        "exit_code": {
            "significado": "Valor retornado por um programa ou script ao finalizar, indicando se foi executado corretamente ou se ocorreu um erro.",
            "uso": "É usada para verificar se um programa foi concluído com sucesso ou se ocorreu um erro.",
            "ejemplo": '''
                import sys
                sys.exit(0)  # Saída: 0 indica sucesso, outro número indica erro.
                '''
        },
        "evaluate_expression": {
            "significado": "Avaliar uma expressão para obter seu resultado.",
            "uso": "É usada para calcular ou obter o valor de uma expressão matemática ou lógica.",
            "ejemplo": '''
                resultado = eval('3 + 5')
                print(resultado)  # Saída: 8
                '''
        },
        "environment": {
            "significado": "O contexto ou conjunto de condições em que um programa ou aplicação é executado.",
            "uso": "É usada para se referir ao conjunto de variáveis, configurações e recursos disponíveis para um programa.",
            "ejemplo": '''
                import os
                print(os.environ)  # Saída: Mostra as variáveis de ambiente do sistema.
                '''
        },
        "environment_variable": {
            "significado": "Variável que armazena informações sobre o ambiente do sistema ou aplicação.",
            "uso": "É usada para armazenar configurações específicas que afetam o comportamento dos programas.",
            "ejemplo": '''
                import os
                print(os.getenv('PATH'))  # Saída: Mostra a variável de ambiente PATH.
                '''
        },
        "exp": {
            "significado": "Função matemática que calcula a exponencial de um número, ou seja, e elevado à potência desse número.",
            "uso": "É usada para realizar cálculos exponenciais.",
            "ejemplo": '''
                import math
                resultado = math.exp(1)
                print(resultado)  # Saída: 2.718281828459045
                '''
        },
        "exception_handling": {
            "significado": "Processo de gerenciar e responder a erros ou exceções que ocorrem durante a execução de um programa.",
            "uso": "É usada para capturar e gerenciar erros, garantindo que o programa não pare inesperadamente.",
            "ejemplo": '''
                try:
                    valor = 1 / 0
                except ZeroDivisionError as e:
                    print(f'Erro: {e}')  # Saída: Erro: division by zero
                '''
        },
        "expand": {
            "significado": "Ampliar ou aumentar o tamanho ou o alcance de algo.",
            "uso": "É usada para fazer algo maior ou incluir mais informações.",
            "ejemplo": '''
                texto = "Olá"
                print(texto.expandtabs(4))  # Saída: 'Olá' com tabulações ampliadas
                '''
        },
        "environment_config": {
            "significado": "Configuração relacionada ao ambiente de execução de um programa ou sistema.",
            "uso": "É usada para especificar ou ajustar parâmetros que afetam o funcionamento de um programa ou aplicação.",
            "ejemplo": '''
                config = {
                    'host': 'localhost',
                    'port': 8080
                }
                print(config)  # Saída: {'host': 'localhost', 'port': 8080}
                '''
        },
        "equal": {
            "significado": "Indica que dois elementos são idênticos em valor.",
            "uso": "É usada para comparar dois valores ou expressões para verificar se são iguais.",
            "ejemplo": '''
                a = 5
                b = 5
                print(a == b)  # Saída: True
                '''
        },
        "error_handling": {
            "significado": "Processo de gerenciar erros e exceções que ocorrem durante a execução de um programa.",
            "uso": "É usada para capturar e gerenciar erros de maneira controlada para evitar que o programa termine inesperadamente.",
            "ejemplo": '''
                try:
                    valor = 10 / 0
                except ZeroDivisionError:
                    print('Erro de divisão por zero')  # Saída: Erro de divisão por zero
                '''
        },
        "event": {
            "significado": "Ação ou evento que pode ser detectado e gerenciado em um programa.",
            "uso": "É usada para gerenciar e responder a atividades ou mudanças em um sistema ou programa.",
            "ejemplo": '''
                import tkinter as tk
                def click():
                    print('Botão pressionado')
                root = tk.Tk()
                button = tk.Button(root, text="Clique em mim", command=click)
                button.pack()
                root.mainloop()  # Saída: Mostra um botão que, ao ser pressionado, executa o evento click
                '''
        },
        "event_loop": {
            "significado": "Ciclo contínuo que espera e gerencia eventos ou tarefas assíncronas em um programa.",
            "uso": "É usada para executar tarefas ou responder a eventos em ordem, sem bloquear o fluxo principal de execução.",
            "ejemplo": '''
                import asyncio
                async def hello():
                    print("Olá")
                asyncio.run(hello())  # Saída: Olá
                '''
        },
        "exception_type": {
            "significado": "O tipo específico de uma exceção ou erro que ocorre em um programa.",
            "uso": "É usada para identificar qual tipo de erro ocorreu e tomar ações adequadas.",
            "ejemplo": '''
                try:
                    valor = 10 / 0
                except ZeroDivisionError as e:
                    print(f"Tipo de erro: {type(e)}")  # Saída: Tipo de erro: <class 'ZeroDivisionError'>
                '''
        },
        "error_message": {
            "significado": "Mensagem que descreve o erro ou problema ocorrido durante a execução de um programa.",
            "uso": "É usada para fornecer detalhes sobre o que falhou ou causou uma exceção.",
            "ejemplo": '''
                try:
                    x = int("abc")
                except ValueError as e:
                    print(f"Mensagem de erro: {e}")  # Saída: Mensagem de erro: invalid literal for int() with base 10: 'abc'
                '''
        },
        "extract": {
            "significado": "Obter uma parte específica de um conjunto de dados ou informações.",
            "uso": "É usada para retirar ou extrair um componente específico de um conjunto maior de dados.",
            "ejemplo": '''
                texto = 'Olá Mundo'
                print(texto[0:4])  # Saída: Olá
                '''
        },
        "exit_status": {
            "significado": "Código de saída que indica se um programa ou processo terminou corretamente ou com erro.",
            "uso": "É usada para verificar se um processo ou comando terminou com sucesso ou se ocorreu algum erro.",
            "ejemplo": '''
                import sys
                sys.exit(0)  # Saída: 0 indica sucesso, qualquer outro número indica erro.
                '''
        },
    },
    "f": {
        "filemode": {
            "significado": "Modo de abertura de um arquivo que determina as operações que podem ser realizadas nele.",
            "uso": "É usada para especificar o tipo de acesso desejado para um arquivo (leitura, escrita, etc.).",
            "ejemplo": '''
                arquivo = open('arquivo.txt', 'r')  # 'r' indica modo de leitura somente
                print(arquivo.mode)  # Saída: 'r'
                '''
        },
        "frozen_set": {
            "significado": "Conjunto imutável em Python, similar a um conjunto padrão, mas sem a possibilidade de modificá-lo após sua criação.",
            "uso": "É usada para criar conjuntos que não devem ser modificados após a sua criação.",
            "ejemplo": '''
                conjunto = frozenset([1, 2, 3])
                print(conjunto)  # Saída: frozenset({1, 2, 3})
                '''
        },
        "format_map": {
            "significado": "Método que retorna uma string formatada usando um dicionário ou objeto similar.",
            "uso": "É usada para realizar substituições de valores em uma string usando um mapa (como um dicionário).",
            "ejemplo": '''
                dados = {'nome': 'João', 'idade': 30}
                texto = 'Nome: {nome}, Idade: {idade}'.format_map(dados)
                print(texto)  # Saída: Nome: João, Idade: 30
                '''
        },
        "find": {
            "significado": "Método que busca uma substring dentro de uma string e retorna o índice da primeira ocorrência.",
            "uso": "É usada para encontrar a posição de um texto dentro de outro.",
            "ejemplo": '''
                texto = 'Olá Mundo'
                print(texto.find('Mundo'))  # Saída: 5
                '''
        },
        "float32": {
            "significado": "Tipo de dado no NumPy que representa um número de ponto flutuante de 32 bits.",
            "uso": "É usada para armazenar números com decimais de forma mais eficiente em termos de memória.",
            "ejemplo": '''
                import numpy as np
                numero = np.float32(3.1415)
                print(numero)  # Saída: 3.1415
                '''
        },
        "float64": {
            "significado": "Tipo de dado no NumPy que representa um número de ponto flutuante de 64 bits.",
            "uso": "É usada para armazenar números com decimais com maior precisão do que o tipo float32.",
            "ejemplo": '''
                import numpy as np
                numero = np.float64(3.141592653589793)
                print(numero)  # Saída: 3.141592653589793
                '''
        },
        "formatting": {
            "significado": "O processo de aplicar um formato a dados ou strings, como alinhamento, larguras e tipos de dados.",
            "uso": "É usada para organizar ou mostrar dados de forma mais legível ou específica.",
            "ejemplo": '''
                texto = 'Nome: {0:10}, Idade: {1:5}'.format('João', 30)
                print(texto)  # Saída: Nome: João      , Idade: 30
                '''
        },
        "flush_output": {
            "significado": "Método utilizado para esvaziar o buffer de saída, forçando que os dados sejam escritos imediatamente.",
            "uso": "É usada quando se quer garantir que todos os dados pendentes no buffer de saída sejam escritos no destino.",
            "ejemplo": '''
                import sys
                sys.stdout.write('Olá Mundo')
                sys.stdout.flush()  # Saída: 'Olá Mundo' imediatamente
                '''
        },
        "function_definition": {
            "significado": "O processo de criar uma função em Python usando a palavra-chave 'def'.",
            "uso": "É usada para declarar funções reutilizáveis que executam um bloco de código específico.",
            "ejemplo": '''
                def saudar(nome):
                    return f'Olá {nome}'
                print(saudar('João'))  # Saída: Olá João
                '''
        },
        "filepath": {
            "significado": "Caminho ou endereço de um arquivo no sistema de arquivos.",
            "uso": "É usada para especificar a localização de um arquivo no sistema de arquivos.",
            "ejemplo": '''
                import os
                caminho = os.path.join('pasta', 'arquivo.txt')
                print(caminho)  # Saída: pasta/arquivo.txt
                '''
        },
        "flask": {
            "significado": "Um micro-framework em Python para o desenvolvimento de aplicações web.",
            "uso": "É usada para criar aplicações web de maneira simples e rápida com rotas, formulários e outras funcionalidades.",
            "ejemplo": '''
                from flask import Flask
                app = Flask(__name__)

                @app.route('/')
                def hello():
                    return 'Olá Mundo'

                app.run()  # Saída: 'Olá Mundo' em uma aplicação web
                '''
        },
        "filtering": {
            "significado": "Processo de selecionar elementos de uma coleção que atendem a uma condição específica.",
            "uso": "É usada para extrair elementos de uma lista, conjunto ou qualquer iterável com base em uma condição.",
            "ejemplo": '''
                lista = [1, 2, 3, 4, 5]
                resultado = filter(lambda x: x > 2, lista)
                print(list(resultado))  # Saída: [3, 4, 5]
                '''
        },
        "futures": {
            "significado": "Módulo que fornece uma interface para executar tarefas assíncronas e paralelizadas.",
            "uso": "É usada para executar funções de maneira concorrente usando threads ou processos.",
            "ejemplo": '''
                from concurrent.futures import ThreadPoolExecutor

                def tarefa(x):
                    return x * x

                with ThreadPoolExecutor() as executor:
                    resultados = executor.map(tarefa, [1, 2, 3])
                    print(list(resultados))  # Saída: [1, 4, 9]
                '''
        },
        "fold": {
            "significado": "Função que aplica uma operação acumulativa sobre os elementos de uma sequência.",
            "uso": "É usada para reduzir uma sequência de elementos a um único valor aplicando uma operação binária.",
            "ejemplo": '''
                from functools import reduce
                lista = [1, 2, 3, 4]
                resultado = reduce(lambda x, y: x + y, lista)
                print(resultado)  # Saída: 10
                '''
        },
        "fromkeys": {
            "significado": "Método de dicionário que cria um novo dicionário com chaves especificadas e valores padrão.",
            "uso": "É usada para criar dicionários a partir de uma lista de chaves com um valor padrão.",
            "ejemplo": '''
                dicionario = dict.fromkeys(['a', 'b', 'c'], 0)
                print(dicionario)  # Saída: {'a': 0, 'b': 0, 'c': 0}
                '''
        },
        "flask_restful": {
            "significado": "Extensão para Flask que simplifica a criação de APIs RESTful.",
            "uso": "É usada para desenvolver aplicações web que seguem a arquitetura REST usando recursos.",
            "ejemplo": '''
                from flask import Flask
                from flask_restful import Api, Resource

                app = Flask(__name__)
                api = Api(app)

                class HelloWorld(Resource):
                    def get(self):
                        return {'mensagem': 'Olá Mundo'}

                api.add_resource(HelloWorld, '/')
                app.run()  # Saída: 'Olá Mundo' como resposta da API
                '''
        },
        "fix": {
            "significado": "Termo geral para corrigir ou ajustar algo que não funciona corretamente.",
            "uso": "É usada quando se faz um ajuste ou correção no código ou na configuração de algo.",
            "ejemplo": '''
                # ejemplo no contexto de código: correção de um erro de sintaxe
                def corrigir_erro():
                    print('Esta é a mensagem corrigida')
                corrigir_erro()
                '''
        },
        "float_conversion": {
            "significado": "Processo de converter dados de outros tipos para tipo flutuante.",
            "uso": "É usada para converter valores em números de ponto flutuante (decimais).",
            "ejemplo": '''
                numero = '3.14'
                resultado = float(numero)
                print(resultado)  # Saída: 3.14
                '''
        },
        "full_path": {
            "significado": "Caminho completo para um arquivo ou diretório no sistema de arquivos.",
            "uso": "É usada para especificar a localização exata de um arquivo ou diretório desde a raiz do sistema de arquivos.",
            "ejemplo": '''
                import os
                caminho_completo = os.path.abspath('arquivo.txt')
                print(caminho_completo)  # Saída: /home/usuario/arquivo.txt
                '''
        },
        "filter": {
            "significado": "Função que aplica uma condição a cada elemento de um iterável e retorna os elementos que atendem à condição.",
            "uso": "É usada para selecionar apenas os elementos que atendem a uma condição específica.",
            "ejemplo": '''
                lista = [1, 2, 3, 4, 5]
                resultado = filter(lambda x: x % 2 == 0, lista)
                print(list(resultado))  # Saída: [2, 4]
                '''
        },
        "float": {
            "significado": "Tipo de dado em Python para representar números de ponto flutuante (números com decimais).",
            "uso": "É usada para representar números que exigem decimais.",
            "ejemplo": '''
                numero = 3.14
                print(type(numero))  # Saída: <class 'float'>
                '''
        },
        "for": {
            "significado": "Palavra-chave em Python usada para iterar sobre os elementos de um iterável.",
            "uso": "É usada para executar um bloco de código repetidamente para cada elemento de um iterável.",
            "ejemplo": '''
                for i in range(5):
                    print(i)
                # Saída:
                # 0
                # 1
                # 2
                # 3
                # 4
                '''
        },
        "format": {
            "significado": "Método utilizado para formatar cadeias de texto, inserindo valores dentro delas.",
            "uso": "É usado para criar cadeias de texto mais legíveis e dinâmicas com valores variáveis.",
            "ejemplo": '''
                nome = 'Juan'
                idade = 30
                print('Meu nome é {} e tenho {} anos'.format(nome, idade))
                # Saída: Meu nome é Juan e tenho 30 anos
                '''
        },
        "from": {
            "significado": "Palavra-chave em Python usada para importar módulos ou funções específicas de módulos.",
            "uso": "É usada para trazer funcionalidades específicas de um módulo para o espaço de nomes atual.",
            "ejemplo": '''
                from math import sqrt
                print(sqrt(16))  # Saída: 4.0
                '''
        },
        "function": {
            "significado": "Bloco de código projetado para realizar uma tarefa específica e que pode ser reutilizado.",
            "uso": "É usado para agrupar código relacionado que realiza uma tarefa comum, permitindo reutilização e modularidade.",
            "ejemplo": '''
                def saudacao(nome):
                    return f'Olá, {nome}'
                
                print(saudacao('Juan'))  # Saída: Olá, Juan
                '''
        },
        "fibonacci": {
            "significado": "Sequência matemática onde cada número é a soma dos dois anteriores.",
            "uso": "É usada para gerar a sequência de Fibonacci, frequentemente em exercícios de programação ou algoritmos.",
            "ejemplo": '''
                def fibonacci(n):
                    if n <= 1:
                        return n
                    else:
                        return fibonacci(n-1) + fibonacci(n-2)
                
                print(fibonacci(5))  # Saída: 5
                '''
        },
        "file": {
            "significado": "Objeto em Python que permite interagir com arquivos no sistema de arquivos.",
            "uso": "É usado para abrir, ler, escrever e manipular arquivos.",
            "ejemplo": '''
                with open('arquivo.txt', 'r') as f:
                    conteudo = f.read()
                print(conteudo)
                '''
        },
        "fwrite": {
            "significado": "Função usada para escrever dados em um arquivo.",
            "uso": "É usada para escrever dados binários em um arquivo aberto em modo de escrita.",
            "ejemplo": '''
                with open('arquivo.bin', 'wb') as f:
                    f.write(b'Hello, World!')
                '''
        },
        "fread": {
            "significado": "Função usada para ler dados de um arquivo.",
            "uso": "É usada para ler dados binários de um arquivo aberto em modo de leitura.",
            "ejemplo": '''
                with open('arquivo.bin', 'rb') as f:
                    dados = f.read()
                print(dados)  # Saída: b'Hello, World!'
                '''
        },
        "finally": {
            "significado": "Palavra-chave em Python que define um bloco de código que será executado sempre, independentemente de ocorrer uma exceção ou não.",
            "uso": "É usada em estruturas try-except para garantir que um bloco de código final seja executado, mesmo que ocorra um erro.",
            "ejemplo": '''
                try:
                    x = 1 / 0
                except ZeroDivisionError:
                    print('Divisão por zero')
                finally:
                    print('Este bloco sempre é executado')
                '''
        },
        "freeze": {
            "significado": "Processo de converter um objeto mutável em um objeto imutável.",
            "uso": "É usada para evitar que um objeto seja modificado após ter sido criado.",
            "ejemplo": '''
                # Não há uma função explícita chamada freeze, mas em alguns casos como com `frozenset` pode-se obter o mesmo efeito
                a = frozenset([1, 2, 3])
                print(a)  # Saída: frozenset({1, 2, 3})
                '''
        },
        "flush": {
            "significado": "Método usado para esvaziar os buffers de um arquivo, garantindo que todos os dados sejam escritos no disco.",
            "uso": "É usada quando é necessário garantir que os dados armazenados em um buffer sejam imediatamente escritos no arquivo.",
            "ejemplo": '''
                with open('arquivo.txt', 'w') as f:
                    f.write('Olá')
                    f.flush()  # Garante que os dados sejam escritos no arquivo
                '''
        },
        "fstring": {
            "significado": "Cadeia de texto que permite inserir expressões dentro da cadeia de forma mais legível e eficiente.",
            "uso": "É usada para criar cadeias de texto interpoladas, onde variáveis podem ser inseridas diretamente dentro da cadeia.",
            "ejemplo": '''
                nome = 'Juan'
                idade = 30
                print(f'Meu nome é {nome} e tenho {idade} anos')  # Saída: Meu nome é Juan e tenho 30 anos
                '''
        },
        "factorial": {
            "significado": "Função matemática que calcula o produto de todos os números inteiros positivos até um número dado.",
            "uso": "É usada para calcular o fatorial de um número, frequentemente em algoritmos de combinatória e probabilidade.",
            "ejemplo": '''
                import math
                print(math.factorial(5))  # Saída: 120
                '''
        },
        "frozen": {
            "significado": "Objeto imutável que não pode ser modificado após sua criação.",
            "uso": "É usado para criar objetos que não podem ser alterados, como um `frozenset` em Python.",
            "ejemplo": '''
                a = frozenset([1, 2, 3])
                print(a)  # Saída: frozenset({1, 2, 3})
                '''
        },
        "filterfalse": {
            "significado": "Função que retorna um iterador que filtra os elementos de um iterável, excluindo os que retornam `True` na função fornecida.",
            "uso": "É usada para obter os elementos de um iterável para os quais a função retorna `False`.",
            "ejemplo": '''
                from itertools import filterfalse
                resultado = filterfalse(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])
                print(list(resultado))  # Saída: [1, 3, 5]
                '''
        },
        "fuzzy": {
            "significado": "Relacionado à lógica difusa, que permite lidar com informações imprecisas ou incertas.",
            "uso": "É usado em sistemas que precisam processar dados aproximados ou incertos.",
            "ejemplo": '''
                # ejemplo de uma biblioteca de lógica difusa como `fuzzywuzzy` (para correspondência difusa de texto)
                from fuzzywuzzy import fuzz
                print(fuzz.ratio('hola', 'Hola'))  # Saída: 100
                '''
        },
        "fibonacci_sequence": {
            "significado": "Sequência matemática onde cada número é a soma dos dois anteriores.",
            "uso": "É usada para gerar a sequência de Fibonacci.",
            "ejemplo": '''
                def fibonacci(n):
                    sequencia = [0, 1]
                    while len(sequencia) < n:
                        sequencia.append(sequencia[-1] + sequencia[-2])
                    return sequencia
                
                print(fibonacci(10))  # Saída: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
                '''
        },
        "format_spec": {
            "significado": "Cadeia usada para definir como os valores devem ser apresentados dentro de um formato de cadeia.",
            "uso": "É usada para especificar o formato dos valores dentro de uma cadeia, como precisão decimal, alinhamento, entre outros.",
            "ejemplo": '''
                pi = 3.14159
                print(f'{pi:.2f}')  # Saída: 3.14
                '''
        },
        "fork": {
            "significado": "Processo de criar um novo processo, copiado do processo original.",
            "uso": "É usado na programação de sistemas para criar processos secundários.",
            "ejemplo": '''
                import os
                pid = os.fork()
                if pid > 0:
                    print(f'Processo pai, PID: {pid}')
                else:
                    print(f'Processo filho, PID: {os.getpid()}')
                '''
        },
        "forking": {
            "significado": "Ação de criar um novo processo ou subprocesso a partir de um processo principal.",
            "uso": "É usado em sistemas operacionais para criar processos adicionais que executam tarefas de forma concorrente.",
            "ejemplo": '''
                import os
                pid = os.fork()
                # Semelhante ao ejemplo de 'fork', mas abrangendo o conceito de 'forking'
                '''
        },
        "first": {
            "significado": "Ação de obter o primeiro elemento de uma sequência ou iterável.",
            "uso": "É usado para acessar o primeiro valor de um iterável, como uma lista ou conjunto.",
            "ejemplo": '''
                lista = [1, 2, 3, 4]
                print(lista[0])  # Saída: 1
                '''
        },
        "float_format": {
            "significado": "Formato que define como os números de ponto flutuante devem ser apresentados em uma cadeia.",
            "uso": "É usado para especificar a quantidade de casas decimais a ser exibida em um número de ponto flutuante.",
            "ejemplo": '''
                pi = 3.14159
                print(f'{pi:.2f}')  # Saída: 3.14
                '''
        },
        "filter_none": {
            "significado": "Função que filtra elementos de um iterável, excluindo os valores `None`.",
            "uso": "É usada para excluir valores `None` de uma sequência.",
            "ejemplo": '''
                lista = [1, None, 2, None, 3]
                resultado = filter(None, lista)
                print(list(resultado))  # Saída: [1, 2, 3]
                '''
        },
        "func_code": {
            "significado": "Atributo que contém o bytecode da função em Python.",
            "uso": "É usado para acessar o código da função, geralmente em contextos de depuração ou análise.",
            "ejemplo": '''
                def ejemplo():
                    pass
                
                print(ejemplo.__code__)  # Saída: <code object ejemplo at 0x...>
                '''
        },
        "float_power": {
            "significado": "Função que calcula um número elevado a uma potência flutuante.",
            "uso": "É usada para realizar exponenciação com números flutuantes.",
            "ejemplo": '''
                print(pow(2, 3.5))  # Saída: 11.313708498984761
                '''
        },
        "format_string": {
            "significado": "Cadeia que define a estrutura de um valor que se deseja mostrar, utilizando especificadores de formato.",
            "uso": "É usada para definir como os valores devem ser exibidos em uma cadeia, como o número de casas decimais ou o alinhamento.",
            "ejemplo": '''
                nome = 'Juan'
                idade = 25
                print(f'Nome: {nome}, Idade: {idade}')  # Saída: Nome: Juan, Idade: 25
                '''
        },
        "filename": {
            "significado": "Cadeia que representa o nome de um arquivo no sistema de arquivos.",
            "uso": "É usada para especificar o nome e a localização de um arquivo que se deseja manipular.",
            "ejemplo": '''
                arquivo = 'documento.txt'
                with open(arquivo, 'r') as f:
                    print(f.read())
                '''
        },
        "file_object": {
            "significado": "Objeto que representa um arquivo aberto em Python, por meio do qual é possível ler, escrever ou manipular o arquivo.",
            "uso": "É usado para interagir com arquivos abertos em Python, acessando ou modificando seus conteúdos.",
            "ejemplo": '''
                with open('documento.txt', 'r') as f:
                    conteudo = f.read()
                    print(conteudo)
                '''
        },
        "finally_clause": {
            "significado": "Parte de um bloco de código que sempre é executada após uma instrução `try`, independentemente de uma exceção ser gerada ou não.",
            "uso": "É usada para executar código de limpeza ou finalização, como o fechamento de arquivos ou liberação de recursos.",
            "ejemplo": '''
                try:
                    arquivo = open('documento.txt', 'r')
                    conteudo = arquivo.read()
                finally:
                    arquivo.close()
                    print('Arquivo fechado')
                '''
        },
        "file_read": {
            "significado": "Operação que permite ler o conteúdo de um arquivo em Python.",
            "uso": "É usada para obter os dados armazenados em um arquivo para processamento ou exibição.",
            "ejemplo": '''
                with open('documento.txt', 'r') as arquivo:
                    conteudo = arquivo.read()
                    print(conteudo)
                '''
        },
        "form": {
            "significado": "Estrutura ou modelo utilizado para organizar dados de maneira específica.",
            "uso": "É usado em interfaces de usuário ou aplicações web para capturar e organizar dados do usuário.",
            "ejemplo": '''
                formulario = {'nome': 'Juan', 'idade': 25}
                print(formulario)
                '''
        },
        "function_call": {
            "significado": "Ação de invocar uma função no código, passando os parâmetros necessários para executar sua tarefa.",
            "uso": "É usada para executar uma função e obter seu resultado.",
            "ejemplo": '''
                def soma(a, b):
                    return a + b
                resultado = soma(3, 4)
                print(resultado)  # Saída: 7
                '''
        },
        "force": {
            "significado": "Ação de impor ou forçar a execução de algo, geralmente no contexto de programação ou manipulação de objetos.",
            "uso": "É usada para forçar um comportamento específico em um programa, como evitar erros ou realizar uma ação independentemente das condições.",
            "ejemplo": '''
                # Não existe um 'force' direto em Python, mas é possível usar 'assert' para forçar condições
                assert 1 == 1, 'Condição falsa'
                '''
        },
        "function_pointer": {
            "significado": "Referência a uma função que pode ser passada e executada como um argumento.",
            "uso": "É usada em linguagens como C ou C++ para referenciar funções e passá-las como parâmetros.",
            "ejemplo": '''
                # Em Python não existe um ponteiro de função direto, mas as funções podem ser passadas como objetos
                def saudacao():
                    print('Olá')
                funcao = saudacao
                funcao()  # Saída: Olá
                '''
        },
        "float_precision": {
            "significado": "Número de dígitos usados para representar um número flutuante com precisão.",
            "uso": "É usado para especificar a quantidade de casas decimais a serem consideradas ao realizar operações com números flutuantes.",
            "ejemplo": '''
                numero = 3.14159265359
                print(f'{numero:.2f}')  # Saída: 3.14
                '''
        },
        "format_error": {
            "significado": "Erro que ocorre quando há um problema ao formatar dados, como uma cadeia mal estruturada.",
            "uso": "É usada para tratar erros relacionados à conversão ou formatação incorreta de dados.",
            "ejemplo": '''
                try:
                    int('abc')
                except ValueError as e:
                    print(f'Erro de formato: {e}')
                '''
        },
        "file_write": {
            "significado": "Operação que permite escrever dados em um arquivo em Python.",
            "uso": "É usada para armazenar informações em um arquivo, sobrescrevendo-o ou adicionando novos dados.",
            "ejemplo": '''
                with open('documento.txt', 'w') as arquivo:
                    arquivo.write('Olá, mundo!')
                '''
        },
        "fibonacci_search": {
            "significado": "Método de busca que utiliza os números de Fibonacci para dividir o espaço de busca de forma eficiente.",
            "uso": "É usado como uma alternativa ao algoritmo de busca binária para encontrar um elemento em um array.",
            "ejemplo": '''
                # Implementação de Fibonacci Search não padrão, mas pode ser usado como alternativa à busca binária
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
            "significado": "Função que filtra os elementos de um iterável e, em seguida, aplica uma função de mapeamento aos elementos restantes.",
            "uso": "É usada para realizar transformações e filtragens de forma eficiente em sequências de dados.",
            "ejemplo": '''
                from itertools import filterfalse
                dados = [1, 2, 3, 4, 5]
                resultado = map(lambda x: x * 2, filter(lambda x: x % 2 == 0, dados))
                print(list(resultado))  # Saída: [4, 8]
                '''
        },
    },
    "g": {
        "get": {
            "significado": "Método que obtiene el valor de una clave en un diccionario. Si la clave no existe, devuelve un valor por defecto.",
            "uso": "Se utiliza para obtener el valor asociado a una clave en un diccionario de manera segura.",
            "ejemplo": '''
                diccionario = {'a': 1, 'b': 2}
                print(diccionario.get('a'))  # Saída: 1
                print(diccionario.get('c', 'No encontrado'))  # Saída: No encontrado
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
                print(x)  # Saída: 20
                '''
        },
        "generator": {
            "significado": "Función que devuelve un iterador, permitiendo generar elementos de uno en uno durante la ejecución.",
            "uso": "Se utiliza para crear secuencias de elementos de manera perezosa (lazy evaluation), sin tener que almacenarlos todos en memoria.",
            "ejemplo": '''
                def contar_hasta_tres():
                    yield 1
                    yield 2
                    yield 3
                for num in contar_hasta_tres():
                    print(num)  # Saída: 1, 2, 3
                '''
        },
        "globals": {
            "significado": "Función que devuelve un diccionario de todas las variables globales.",
            "uso": "Se utiliza para acceder y modificar el diccionario de variables globales.",
            "ejemplo": '''
                x = 10
                print(globals())  # Saída: {'x': 10, ...}
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
                print(getattr(p, 'nombre'))  # Saída: Juan
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
                    print(clave, list(grupo))  # Saída: 1 [1], 2 [2, 2], 3 [3, 3, 3]
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
                    print(num)  # Saída: 0, 2, 4, 6, 8
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
                    print(fila)  # Saída: [1, 2, 3], [4, 5, 6], [7, 8, 9]
                '''
        },
        "getopt": {
            "significado": "Módulo que fornece uma forma de analisar argumentos da linha de comando.",
            "uso": "É usado para gerenciar opções e parâmetros passados a um programa pela linha de comando.",
            "ejemplo": '''
                import getopt
                opcoes, argumentos = getopt.getopt(['-f', 'arquivo.txt'], 'f:')
                print(opcoes)  # Saída: [('f', 'arquivo.txt')]
                '''
        },
        "gcd": {
            "significado": "Função que calcula o maior divisor comum (MDC) de dois números.",
            "uso": "É usada para encontrar o maior número que divide dois números sem deixar resto.",
            "ejemplo": '''
                import math
                print(math.gcd(24, 36))  # Saída: 12
                '''
        },
        "getpass": {
            "significado": "Função que lê uma senha de forma oculta (sem exibir caracteres ao digitar).",
            "uso": "É usada para ler senhas ou entradas sensíveis de forma segura no terminal.",
            "ejemplo": '''
                import getpass
                senha = getpass.getpass('Digite sua senha: ')
                print(senha)  # A senha não é exibida enquanto é digitada
                '''
        },
        "gradients": {
            "significado": "Mudança no valor de uma variável em relação a outra, comumente usada em cálculo e aprendizado de máquina.",
            "uso": "É usada para calcular a direção e a taxa de variação de uma função em relação às suas variáveis.",
            "ejemplo": '''
                # ejemplo de gradiente em otimização
                def funcao(x):
                    return x**2
                gradiente = 2 * 3  # Gradiente de x^2 em x = 3
                print(gradiente)  # Saída: 6
                '''
        },
        "graphlib": {
            "significado": "Módulo em Python que fornece estruturas de dados para trabalhar com grafos.",
            "uso": "É usado para representar e manipular grafos de maneira eficiente.",
            "ejemplo": '''
                import graphlib
                grafo = graphlib.TopologicalSorter({'A': ['B'], 'B': ['C'], 'C': []})
                print(list(grafo.static_order()))  # Saída: ['A', 'B', 'C']
                '''
        },
        "get_event_loop": {
            "significado": "Função da biblioteca `asyncio` que obtém o loop de eventos da aplicação.",
            "uso": "É usada para obter o loop de eventos principal em um programa assíncrono.",
            "ejemplo": '''
                import asyncio
                loop = asyncio.get_event_loop()
                print(loop)  # Saída: <_UnixSelectorEventLoop running=True closed=False pid=12345>
                '''
        },
        "get_terminal_size": {
            "significado": "Função que obtém o tamanho do terminal em linhas e colunas.",
            "uso": "É usada para obter a resolução do terminal e ajustar o layout da saída.",
            "ejemplo": '''
                import shutil
                tamanho = shutil.get_terminal_size()
                print(tamanho)  # Saída: os.terminal_size(columns=80, lines=24)
                '''
        },
        "getsizeof": {
            "significado": "Função do módulo `sys` que retorna o tamanho de um objeto em bytes.",
            "uso": "É usada para medir a memória ocupada por um objeto em Python.",
            "ejemplo": '''
                import sys
                objeto = [1, 2, 3]
                print(sys.getsizeof(objeto))  # Saída: 72 (dependendo do sistema)
                '''
        },
        "google": {
            "significado": "Motor de busca da internet, também usado como nome da empresa.",
            "uso": "É usado para buscar informações na web através de um navegador ou API.",
            "ejemplo": '''
                # Pesquisando algo no Google
                # Pode ser feito por meio da interface web em www.google.com
                '''
        },
        "getdefaultencoding": {
            "significado": "Método que retorna o nome da codificação padrão usada pelo sistema.",
            "uso": "É usado para conhecer a codificação padrão de texto em Python.",
            "ejemplo": '''
                import sys
                print(sys.getdefaultencoding())  # Saída: 'utf-8' (dependendo do sistema)
                '''
        },
        "geometry": {
            "significado": "Área da matemática que trata das propriedades e relações de pontos, linhas, superfícies e sólidos.",
            "uso": "É usada em campos como computação gráfica, engenharia e arquitetura para descrever formas e estruturas.",
            "ejemplo": '''
                # ejemplo de geometria em programação
                import math
                area_circulo = math.pi * (5**2)  # Área de um círculo com raio 5
                print(area_circulo)  # Saída: 78.53981633974483
                '''
        },
        "greenlet": {
            "significado": "Módulo que fornece primitivas para controle de fluxo cooperativo de threads (lightweight threads).",
            "uso": "É usado para executar funções de forma concorrente sem a sobrecarga das threads tradicionais.",
            "ejemplo": '''
                from greenlet import greenlet
                def funcao1():
                    print('Na função 1')
                    g2.switch()
                def funcao2():
                    print('Na função 2')
                    g1.switch()
                g1 = greenlet(funcao1)
                g2 = greenlet(funcao2)
                g1.switch()  # Saída: Na função 1, Na função 2
                '''
        },
        "gitignore": {
            "significado": "Arquivo de configuração usado pelo Git para especificar quais arquivos ou diretórios devem ser ignorados no controle de versão.",
            "uso": "É usado para evitar que certos arquivos sejam incluídos no repositório Git, como arquivos temporários ou de configuração local.",
            "ejemplo": '''
                # ejemplo de .gitignore
                *.log
                __pycache__/
                '''
        },
        "grammar": {
            "significado": "Conjunto de regras que descrevem a estrutura de uma linguagem.",
            "uso": "É usada para definir como formar sentenças ou expressões válidas em um idioma ou linguagem.",
            "ejemplo": '''
                # ejemplo de gramática em programação
                def somar(a, b):
                    return a + b
                # A sintaxe é a gramática da função somar
                '''
        },
        "gettext": {
            "significado": "Função que traduz um texto para um idioma específico, geralmente usada em aplicações multilíngues.",
            "uso": "É usada para obter uma string traduzida de acordo com o idioma atual do sistema.",
            "ejemplo": '''
                import gettext
                traducao = gettext.translation('minha_app', localedir='locales', languages=['pt'])
                print(traducao.gettext('Hello'))  # Saída: Olá
                '''
        },
        "generate_tokens": {
            "significado": "Função que gera uma sequência de tokens a partir de um objeto de texto, usada para analisar e processar código fonte.",
            "uso": "É usada na criação de analisadores léxicos para dividir um texto em unidades significativas.",
            "ejemplo": '''
                import token
                import tokenize
                codigo = 'print("Olá Mundo")'
                tokens = tokenize.generate_tokens(iter(codigo).__next__)
                for t in tokens:
                    print(t)
                '''
        },
        "gevent": {
            "significado": "Biblioteca de Python para trabalhar com concorrência baseada em threads leves, usando corrotinas.",
            "uso": "É usada para lidar com tarefas concorrentes de forma eficiente sem a necessidade de múltiplas threads.",
            "ejemplo": '''
                import gevent
                def tarefa():
                    print('Tarefa concluída')
                gevent.spawn(tarefa).join()
                '''
        },
        "gui": {
            "significado": "Interface gráfica do usuário, um sistema de interação visual com programas de computador.",
            "uso": "É usada para criar aplicações com interfaces visuais, facilitando a interação do usuário.",
            "ejemplo": '''
                import tkinter as tk
                janela = tk.Tk()
                janela.title('Minha GUI')
                janela.mainloop()
                '''
        },
        "generator_function": {
            "significado": "Função que usa `yield` para retornar um gerador.",
            "uso": "É usada para criar funções que retornam um gerador e permitem a iteração preguiçosa.",
            "ejemplo": '''
                def contar():
                    yield 1
                    yield 2
                    yield 3
                for numero in contar():
                    print(numero)  # Saída: 1, 2, 3
                '''
        },
        "get_data": {
            "significado": "Método ou função que obtém dados de uma fonte externa ou interna.",
            "uso": "É usado para recuperar dados de bancos de dados, APIs ou outras fontes.",
            "ejemplo": '''
                def obter_dados():
                    return {'nome': 'João', 'idade': 25}
                print(obter_dados())  # Saída: {'nome': 'João', 'idade': 25}
                '''
        },
        "git_branch": {
            "significado": "Comando do Git que permite trabalhar com branches dentro de um repositório.",
            "uso": "É usado para criar, listar e alternar entre diferentes branches de um projeto no Git.",
            "ejemplo": '''
                git branch  # Mostra os branches existentes
                git checkout -b nova_branch  # Cria e muda para o novo branch
                '''
        },
        "governance": {
            "significado": "O processo de tomada de decisões e gestão em uma organização ou sistema.",
            "uso": "É usado para se referir a como um sistema ou entidade é administrado e regulamentado.",
            "ejemplo": '''
                A governança corporativa refere-se às práticas e estruturas organizacionais para a tomada de decisões.
                '''
        },
        "gtts": {
            "significado": "Biblioteca de Python para converter texto em fala usando o serviço Google Text-to-Speech.",
            "uso": "É usada para gerar arquivos de áudio a partir de texto em vários idiomas.",
            "ejemplo": '''
                from gtts import gTTS
                tts = gTTS('Olá, como você está?', lang='pt')
                tts.save('ola.mp3')
                '''
        },
        "get_identity": {
            "significado": "Método ou função que obtém a identidade de um objeto ou usuário.",
            "uso": "É usada para obter informações sobre a identidade de um objeto ou entidade, como um identificador único.",
            "ejemplo": '''
                def get_identity(usuario):
                    return usuario['id']
                usuario = {'id': 123, 'nome': 'João'}
                print(get_identity(usuario))  # Saída: 123
                '''
        },
        "get_status": {
            "significado": "Método ou função que obtém o estado de uma operação, processo ou entidade.",
            "uso": "É usado para verificar ou recuperar o estado atual de um sistema ou processo.",
            "ejemplo": '''
                def get_status(operacao):
                    return operacao['estado']
                operacao = {'estado': 'concluída'}
                print(get_status(operacao))  # Saída: concluída
                '''
        },
        "generator_instance": {
            "significado": "Instância de um gerador, que é um objeto que permite iterar sobre uma sequência de elementos.",
            "uso": "É usada para gerenciar iterações de maneira eficiente usando a palavra-chave `yield`.",
            "ejemplo": '''
                def contador():
                    yield 1
                    yield 2
                    yield 3
                gerador = contador()
                for numero in gerador:
                    print(numero)  # Saída: 1, 2, 3
                '''
        },
        "guess_encoding": {
            "significado": "Método que tenta adivinhar a codificação de um arquivo de texto com base no seu conteúdo.",
            "uso": "É usado para detectar a codificação de arquivos de texto que não têm especificada uma.",
            "ejemplo": '''
                import chardet
                with open('arquivo.txt', 'rb') as f:
                    resultado = chardet.detect(f.read())
                print(resultado['encoding'])  # Saída: utf-8
                '''
        },
        "git_commit": {
            "significado": "Comando do Git usado para registrar mudanças no repositório.",
            "uso": "É usado para salvar um conjunto de alterações feitas nos arquivos de um projeto no repositório.",
            "ejemplo": '''
                git commit -m "Mensagem do commit"
                '''
        },
        "gradient_descent": {
            "significado": "Método de otimização utilizado para minimizar funções iterativamente, ajustando os parâmetros na direção do gradiente negativo.",
            "uso": "É amplamente usado em aprendizado de máquina para encontrar os valores ótimos dos parâmetros de um modelo.",
            "ejemplo": '''
                # ejemplo simplificado de gradiente descendente
                def gradiente_descendente(funcao, derivada, x_inicial, taxa_aprendizado, iteracoes):
                    x = x_inicial
                    for _ in range(iteracoes):
                        x -= taxa_aprendizado * derivada(x)
                    return x
                '''
        },
        "get_referrers": {
            "significado": "Função que obtém uma lista de objetos que fazem referência a um objeto específico.",
            "uso": "É usada para rastrear as referências a um objeto, útil para análise de memória.",
            "ejemplo": '''
                import sys
                referencia = sys.get_referrers(objeto)
                print(referencia)
                '''
        },
        "get_window_extent": {
            "significado": "Método que obtém as dimensões de uma janela gráfica ou área na tela.",
            "uso": "É usado para determinar o tamanho e as coordenadas da janela de uma aplicação ou gráfico.",
            "ejemplo": '''
                import matplotlib.pyplot as plt
                fig, ax = plt.subplots()
                extent = ax.get_window_extent()
                print(extent)
                '''
        },
        "group": {
            "significado": "Método que agrupa elementos em uma coleção ou estrutura com base em algum critério.",
            "uso": "É usado para organizar dados em grupos ou categorias.",
            "ejemplo": '''
                from itertools import groupby
                lista = [1, 1, 2, 2, 3]
                grupo = groupby(lista)
                for chave, valor in grupo:
                    print(chave, list(valor))  # Saída: 1 [1, 1], 2 [2, 2], 3 [3]
                '''
        },
        "get_history": {
            "significado": "Método que obtém o histórico de operações ou ações anteriores.",
            "uso": "É usado para recuperar as ações anteriores realizadas em um sistema ou aplicação.",
            "ejemplo": '''
                # ejemplo de recuperação do histórico em um sistema
                historico = get_history()
                print(historico)
                '''
        },
        "gradient": {
            "significado": "O vetor que indica a direção e a taxa de variação de uma função em um ponto específico.",
            "uso": "É amplamente usado no cálculo diferencial e no treinamento de modelos de aprendizado de máquina.",
            "ejemplo": '''
                # ejemplo de gradiente de uma função
                import numpy as np
                def funcao(x):
                    return x**2
                gradiente = 2 * 3  # Gradiente de x^2 em x = 3
                print(gradiente)  # Saída: 6
                '''
        },
        "getfqdn": {
            "significado": "Função que obtém o nome de domínio completo (FQDN) da máquina local.",
            "uso": "É usada para obter o nome completo de domínio do computador em uma rede.",
            "ejemplo": '''
                import socket
                fqdn = socket.getfqdn()
                print(fqdn)  # Saída: ejemplo.local
                '''
        },
        "get_url": {
            "significado": "Função que obtém uma URL específica, geralmente para acessar um recurso online.",
            "uso": "É usada para recuperar uma URL de uma fonte externa ou gerar uma URL para um recurso.",
            "ejemplo": '''
                import requests
                url = "http://example.com"
                resposta = requests.get(url)
                print(resposta.url)
                '''
        },
        "get_line": {
            "significado": "Método que obtém uma linha específica de um arquivo ou conjunto de dados.",
            "uso": "É usado para acessar uma linha específica dentro de um arquivo ou texto.",
            "ejemplo": '''
                with open('arquivo.txt', 'r') as f:
                    linha = f.readline()
                    print(linha)
                '''
        },
        "get_clock_info": {
            "significado": "Método que obtém informações sobre o relógio do sistema, como a frequência de atualização.",
            "uso": "É usado para obter detalhes sobre o desempenho e as características do relógio do sistema.",
            "ejemplo": '''
                import time
                info = time.get_clock_info('time')
                print(info)
                '''
        },
        "getmtime": {
            "significado": "Função que obtém a data e hora da última modificação de um arquivo.",
            "uso": "É usada para verificar quando foi a última modificação de um arquivo ou diretório.",
            "ejemplo": '''
                import os
                ultima_modificacao = os.path.getmtime('arquivo.txt')
                print(ultima_modificacao)
                '''
        },
        "gettext_install": {
            "significado": "Comando ou função que instala o pacote `gettext` para internacionalização de aplicativos.",
            "uso": "É usado para instalar o pacote necessário para traduzir strings de texto em aplicações Python.",
            "ejemplo": '''
                # ejemplo no terminal
                pip install gettext
                '''
        },
        "geometry_manager": {
            "significado": "Método usado para gerenciar o tamanho e a localização dos widgets em interfaces gráficas.",
            "uso": "É usado em bibliotecas de interfaces gráficas como Tkinter para organizar a disposição dos elementos.",
            "ejemplo": '''
                import tkinter as tk
                root = tk.Tk()
                label = tk.Label(root, text="Olá Mundo")
                label.pack()  # Usa o geometry manager 'pack'
                root.mainloop()
                '''
        },
        "gcd_algorithm": {
            "significado": "Algoritmo para calcular o maior divisor comum (MDC) de dois números.",
            "uso": "É usado para encontrar o maior número que divide exatamente dois números.",
            "ejemplo": '''
                import math
                mdc = math.gcd(24, 36)
                print(mdc)  # Saída: 12
                '''
        },
        "googletrans": {
            "significado": "Biblioteca Python que usa a API do Google Translate para traduzir texto entre diferentes idiomas.",
            "uso": "É usada para traduzir texto automaticamente usando os serviços do Google Translate.",
            "ejemplo": '''
                from googletrans import Translator
                translator = Translator()
                traducao = translator.translate('Olá, como você está?', src='pt', dest='en')
                print(traducao.text)  # Saída: Hello, how are you?
                '''
        },
        "get_dpi": {
            "significado": "Função que obtém a densidade de pixels por polegada (DPI) da tela.",
            "uso": "É usada para obter a resolução da tela em termos de pixels por polegada.",
            "ejemplo": '''
                import tkinter as tk
                root = tk.Tk()
                dpi = root.winfo_fpixels('1i')  # Pixels por polegada
                print(dpi)
                '''
        },
        "geolocation": {
            "significado": "Processo de determinar a localização geográfica de um dispositivo.",
            "uso": "É usado para obter a latitude, longitude e outros detalhes sobre a localização de um dispositivo.",
            "ejemplo": '''
                # ejemplo usando geopy
                from geopy.geocoders import Nominatim
                geolocator = Nominatim(user_agent="minha_app")
                localizacao = geolocator.geocode("1600 Pennsylvania Ave NW, Washington, DC 20500")
                print(localizacao.address)
                '''
        },
        "git_merge": {
            "significado": "Comando do Git que combina mudanças de diferentes branches em um único branch.",
            "uso": "É usado para mesclar branches de um repositório no Git.",
            "ejemplo": '''
                git checkout master
                git merge branch-feature
                '''
        },
        "get_tick_params": {
            "significado": "Função que obtém os parâmetros dos 'ticks' em um gráfico.",
            "uso": "É usada em bibliotecas gráficas como Matplotlib para ajustar os valores dos eixos nos gráficos.",
            "ejemplo": '''
                import matplotlib.pyplot as plt
                fig, ax = plt.subplots()
                ticks = ax.get_xticks()
                print(ticks)
                '''
        },
        "getrandbits": {
            "significado": "Método que retorna um número aleatório com uma quantidade específica de bits.",
            "uso": "É usado para gerar números aleatórios binários com um número determinado de bits.",
            "ejemplo": '''
                import random
                numero = random.getrandbits(8)  # 8 bits
                print(numero)  # Saída: número aleatório de 8 bits
                '''
        },
        "gui_toolkit": {
            "significado": "Conjunto de ferramentas ou bibliotecas utilizadas para desenvolver interfaces gráficas de usuário (GUI).",
            "uso": "É usado para construir aplicações com interfaces visuais interativas.",
            "ejemplo": '''
                # ejemplo com Tkinter
                import tkinter as tk
                root = tk.Tk()
                label = tk.Label(root, text="Olá Mundo")
                label.pack()
                root.mainloop()
                '''
        },
        "getpid": {
            "significado": "Função que obtém o ID do processo atual.",
            "uso": "É usada para obter o identificador único do processo em execução.",
            "ejemplo": '''
                import os
                pid = os.getpid()
                print(pid)  # Saída: ID do processo atual
                '''
        },
        "get_event": {
            "significado": "Método que obtém um evento específico no contexto de um sistema ou aplicação.",
            "uso": "É usado para recuperar um evento de um sistema de gestão de eventos.",
            "ejemplo": '''
                # ejemplo em um sistema de eventos
                evento = get_event("click")
                print(evento)
                '''
        },
        "gmm": {
            "significado": "Modelo de Mistura Gaussiana (GMM), um modelo probabilístico para a distribuição de dados.",
            "uso": "É usado em machine learning para modelar dados como uma mistura de distribuições gaussianas.",
            "ejemplo": '''
                from sklearn.mixture import GaussianMixture
                gmm = GaussianMixture(n_components=2)
                gmm.fit(dados)
                '''
        },
        "gather": {
            "significado": "Função usada para coletar ou agrupar elementos ou resultados em uma estrutura.",
            "uso": "É usada para reunir resultados de operações paralelas ou de múltiplas fontes.",
            "ejemplo": '''
                import asyncio
                async def tarefa():
                    return 1
                async def main():
                    resultados = await asyncio.gather(tarefa(), tarefa())
                    print(resultados)
                asyncio.run(main())
                '''
        },
        "get_statistics": {
            "significado": "Método que obtém as estatísticas de um conjunto de dados.",
            "uso": "É usado para calcular e recuperar métricas estatísticas como média, mediana, desvio padrão, etc.",
            "ejemplo": '''
                import statistics
                dados = [1, 2, 3, 4, 5]
                media = statistics.mean(dados)
                print(media)  # Saída: 3
                '''
        },
        "get_user": {
            "significado": "Método que obtém as informações do usuário atual.",
            "uso": "É usado para recuperar os detalhes do usuário em um sistema.",
            "ejemplo": '''
                import os
                usuario = os.getlogin()
                print(usuario)  # Saída: nome de usuário
                '''
        },
        "get_unique": {
            "significado": "Função que obtém os elementos únicos de um conjunto de dados.",
            "uso": "É usada para recuperar os valores não repetidos de uma lista ou conjunto.",
            "ejemplo": '''
                import numpy as np
                dados = [1, 2, 2, 3, 4, 4]
                unicos = np.unique(dados)
                print(unicos)  # Saída: [1 2 3 4]
                '''
        },
        "git_rebase": {
            "significado": "Comando do Git que permite aplicar mudanças de um branch em outro, reescrevendo o histórico.",
            "uso": "É usado para integrar as mudanças de um branch em outro de maneira mais limpa, reorganizando os commits.",
            "ejemplo": '''
                git checkout feature-branch
                git rebase main
                '''
        },
        "get_score": {
            "significado": "Método para obter uma pontuação ou classificação com base em algum critério ou cálculo.",
            "uso": "É usado em diversas aplicações para obter a pontuação de um sistema, jogo, exame, etc.",
            "ejemplo": '''
                score = game.get_score()
                print(score)  # Saída: pontuação atual
                '''
        },
        "graph_data": {
            "significado": "Processo de representar dados em forma de gráficos.",
            "uso": "É usado para visualizar informações e padrões por meio de gráficos como barras, linhas, etc.",
            "ejemplo": '''
                import matplotlib.pyplot as plt
                dados = [1, 2, 3, 4, 5]
                plt.plot(dados)
                plt.show()
                '''
        },
        "get_installed_distributions": {
            "significado": "Função que obtém as distribuições de pacotes instaladas no ambiente do Python.",
            "uso": "É usada para obter uma lista dos pacotes instalados em um ambiente Python.",
            "ejemplo": '''
                from pkg_resources import get_distribution
                distribs = get_installed_distributions()
                for distrib in distribs:
                    print(distrib)
                '''
        },
        "geocode": {
            "significado": "Processo de converter um endereço em coordenadas geográficas (latitude e longitude).",
            "uso": "É usado para obter a localização geográfica de um endereço textual.",
            "ejemplo": '''
                from geopy.geocoders import Nominatim
                geolocator = Nominatim(user_agent="minha_app")
                local = geolocator.geocode("1600 Pennsylvania Ave NW, Washington, DC 20500")
                print(local.latitude, local.longitude)
                '''
        },
        "get_type_hints": {
            "significado": "Função que obtém as dicas de tipos dos parâmetros e valores de retorno de uma função.",
            "uso": "É usada para obter as anotações de tipo de uma função.",
            "ejemplo": '''
                from typing import get_type_hints
                def ejemplo(x: int, y: str) -> bool:
                    return True
                print(get_type_hints(ejemplo))
                '''
        },
        "genericpath": {
            "significado": "Módulo que fornece funções para trabalhar com caminhos de arquivos e diretórios de forma genérica.",
            "uso": "É usado para manipular caminhos de arquivos e diretórios.",
            "ejemplo": '''
                import genericpath
                arquivo = "/caminho/para/arquivo.txt"
                print(genericpath.exists(arquivo))  # Saída: True ou False
                '''
        },
        "get_resource_path": {
            "significado": "Método que obtém o caminho de um recurso dentro de um pacote ou aplicação.",
            "uso": "É usado para localizar recursos dentro de um ambiente empacotado.",
            "ejemplo": '''
                import pkg_resources
                caminho = pkg_resources.resource_filename('meu_pacote', 'recurso.txt')
                print(caminho)
                '''
        },
        "git_pull": {
            "significado": "Comando do Git que atualiza o repositório local com as mudanças mais recentes do repositório remoto.",
            "uso": "É usado para obter as mudanças mais recentes do repositório remoto e mesclá-las ao branch local.",
            "ejemplo": '''
                git pull origin master
                '''
        },
        "get_cached_properties": {
            "significado": "Método para obter propriedades que foram armazenadas em cache.",
            "uso": "É usado para acessar propriedades previamente calculadas e armazenadas na memória para melhorar a eficiência.",
            "ejemplo": '''
                class MinhaClasse:
                    @property
                    def propriedade(self):
                        if not hasattr(self, '_cached_propriedade'):
                            self._cached_propriedade = 42  # ejemplo de cálculo
                        return self._cached_propriedade
                obj = MinhaClasse()
                print(obj.propriedade)  # Saída: 42
                '''
        },
        "geopandas": {
            "significado": "Biblioteca de Python para a manipulação e análise de dados geoespaciais.",
            "uso": "É usada para trabalhar com dados espaciais, como mapas e coordenadas geográficas.",
            "ejemplo": '''
                import geopandas as gpd
                gdf = gpd.read_file('mapa.shp')
                gdf.plot()
                '''
        },
        "get_open_files": {
            "significado": "Função que obtém uma lista de arquivos abertos em um sistema.",
            "uso": "É usada para monitorar os arquivos abertos em um processo ou sistema.",
            "ejemplo": '''
                import psutil
                processos = psutil.process_iter(['pid', 'name'])
                for processo in processos:
                    arquivos = processo.open_files()
                    for arquivo in arquivos:
                        print(arquivo.path)
                '''
        },
        "get_active_connections": {
            "significado": "Método que obtém as conexões ativas em um sistema ou rede.",
            "uso": "É usado para obter as conexões ativas em uma aplicação ou sistema operacional.",
            "ejemplo": '''
                import psutil
                conexoes = psutil.net_connections()
                for conexao in conexoes:
                    print(conexao)
                '''
        },
        "guess_language": {
            "significado": "Função que adivinha o idioma de um texto dado.",
            "uso": "É usada para determinar o idioma de uma string de texto.",
            "ejemplo": '''
                from langdetect import detect
                idioma = detect("Olá, como você está?")
                print(idioma)  # Saída: pt
                '''
        },
        "get_doc": {
            "significado": "Método que obtém a documentação associada a um objeto ou função.",
            "uso": "É usado para obter a string de documentação (docstring) de um objeto ou função.",
            "ejemplo": '''
                def ejemplo():
                    \"\"\"Esta é a documentação da função\"\"\"
                    pass
                print(ejemplo.__doc__)
                '''
        },
    },
    "h": {
        # Aquí puedes agregar funciones que comiencen con la letra H
        "hash": {
        "significado": "Função que gera um valor de hash para um objeto, útil para armazenamento e comparação eficiente.",
        "uso": "É usada para calcular o hash de um objeto imutável.",
        "ejemplo": '''
            valor = hash("ejemplo")
            print(valor)  # Saída: valor de hash único
            '''
        },
        "help": {
            "significado": "Função que exibe a documentação e ajuda de um objeto ou módulo.",
            "uso": "É usada para obter informações sobre o uso de funções, classes ou módulos.",
            "ejemplo": '''
                help(print)  # Mostra a documentação da função 'print'
                '''
        },
        "hex": {
            "significado": "Função que converte um número inteiro em sua representação hexadecimal.",
            "uso": "É usada para obter a representação hexadecimal de um valor.",
            "ejemplo": '''
                numero = 255
                print(hex(numero))  # Saída: '0xff'
                '''
        },
        "head": {
            "significado": "Comando ou função que retorna as primeiras linhas de um arquivo ou conjunto de dados.",
            "uso": "É usada para visualizar rapidamente os primeiros registros.",
            "ejemplo": '''
                # ejemplo com pandas
                import pandas as pd
                dados = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
                print(dados.head())
                '''
        },
        "heapq": {
            "significado": "Módulo que implementa uma fila de prioridade baseada em heaps.",
            "uso": "É usado para gerenciar coleções de dados em uma ordem específica com eficiência.",
            "ejemplo": '''
                import heapq
                heap = []
                heapq.heappush(heap, 3)
                heapq.heappush(heap, 1)
                heapq.heappush(heap, 2)
                print(heapq.heappop(heap))  # Saída: 1
                '''
        },
        "hstack": {
            "significado": "Função que empilha arrays horizontalmente.",
            "uso": "É usada para combinar arrays ao longo de suas colunas.",
            "ejemplo": '''
                import numpy as np
                a = np.array([1, 2])
                b = np.array([3, 4])
                print(np.hstack((a, b)))  # Saída: [1 2 3 4]
                '''
        },
        "hypot": {
            "significado": "Função que calcula a hipotenusa de um triângulo retângulo.",
            "uso": "É usada para encontrar a distância euclidiana em um espaço bidimensional.",
            "ejemplo": '''
                import math
                print(math.hypot(3, 4))  # Saída: 5.0
                '''
        },
        "hist": {
            "significado": "Função que cria e exibe um histograma de dados.",
            "uso": "É usada para visualizar a distribuição de dados em bins.",
            "ejemplo": '''
                import matplotlib.pyplot as plt
                dados = [1, 1, 2, 2, 2, 3, 3]
                plt.hist(dados, bins=3)
                plt.show()
                '''
        },
        "hostname": {
            "significado": "Nome que identifica um dispositivo dentro de uma rede.",
            "uso": "É usado para distinguir dispositivos em redes locais ou globais.",
            "ejemplo": '''
                import socket
                print(socket.gethostname())  # Saída: Nome do dispositivo
                '''
        },
        "hashlib": {
            "significado": "Módulo que fornece funções de hash criptográficas.",
            "uso": "É usado para gerar hashes seguros como MD5, SHA-1 e SHA-256.",
            "ejemplo": '''
                import hashlib
                texto = "ejemplo"
                hash_sha256 = hashlib.sha256(texto.encode()).hexdigest()
                print(hash_sha256)  # Saída: hash em formato hexadecimal
                '''
        },
        "homedir": {
            "significado": "Diretório principal de um usuário no sistema operacional.",
            "uso": "É usado para acessar ou identificar o diretório inicial do usuário.",
            "ejemplo": '''
                import os
                print(os.path.expanduser('~'))  # Saída: Caminho do diretório inicial
                '''
        },
        "highlight": {
            "significado": "Processo de destacar texto ou código, geralmente para fins de visualização.",
            "uso": "É usado para melhorar a legibilidade do código ou texto em editores e terminais.",
            "ejemplo": '''
                from pygments import highlight
                from pygments.lexers import PythonLexer
                from pygments.formatters import TerminalFormatter
                codigo = "print('Olá Mundo')"
                print(highlight(codigo, PythonLexer(), TerminalFormatter()))
                '''
        },
        "histogram": {
            "significado": "Representação gráfica da distribuição de um conjunto de dados.",
            "uso": "É usada para visualizar frequências de dados em intervalos.",
            "ejemplo": '''
                import numpy as np
                dados = np.array([1, 2, 2, 3, 3, 3])
                hist, bins = np.histogram(dados, bins=3)
                print(hist)  # Saída: Contagem de cada intervalo
                '''
        },
        "hook": {
            "significado": "Função ou método que intercepta ou se conecta a um processo para estender ou modificar seu comportamento.",
            "uso": "É usado para personalizar ou alterar o fluxo de execução de um sistema.",
            "ejemplo": '''
                def meu_hook(evento):
                    print(f"Evento: {evento}")
                sistema.registrar_hook(meu_hook)
                '''
        },
        "http": {
            "significado": "Protocolo usado para transferir informações na web.",
            "uso": "É usado para comunicação entre clientes (navegadores) e servidores.",
            "ejemplo": '''
                import requests
                resposta = requests.get("http://example.com")
                print(resposta.status_code)  # Saída: Código de status HTTP
                '''
        },
        "hist2d": {
            "significado": "Função que cria um gráfico de histograma bidimensional.",
            "uso": "É usada para visualizar a distribuição de dados em dois eixos.",
            "ejemplo": '''
                import numpy as np
                import matplotlib.pyplot as plt
                x = np.random.randn(1000)
                y = np.random.randn(1000)
                plt.hist2d(x, y, bins=30)
                plt.show()
                '''
        },
        "histc": {
            "significado": "Função que calcula o histograma com contagens acumuladas de dados.",
            "uso": "É usada para contar a frequência de valores em intervalos, com contagem acumulada.",
            "ejemplo": '''
                import numpy as np
                dados = np.random.randn(1000)
                hist, bins = np.histogram(dados, bins=10)
                print(hist)
                '''
        },
        "hamming": {
            "significado": "Função que gera uma janela de Hamming, usada em análise de sinais.",
            "uso": "É usada para aplicar uma janela de suavização a um conjunto de dados.",
            "ejemplo": '''
                import numpy as np
                janela = np.hamming(10)
                print(janela)
                '''
        },
        "heapify": {
            "significado": "Função que organiza uma lista em um heap, estrutura de dados de fila de prioridade.",
            "uso": "É usada para transformar uma lista em uma estrutura heap.",
            "ejemplo": '''
                import heapq
                lista = [5, 3, 8, 1]
                heapq.heapify(lista)
                print(lista)  # Saída: [1, 3, 8, 5]
                '''
        },
        "hsv": {
            "significado": "Modelo de cores baseado em matiz (H), saturação (S) e valor (V).",
            "uso": "É usado para representar cores de forma mais intuitiva para certas operações, como em processamento de imagens.",
            "ejemplo": '''
                import matplotlib.pyplot as plt
                h = 0.5  # Matiz
                s = 1    # Saturação
                v = 1    # Valor
                cor = (h, s, v)
                plt.imshow([[cor]])
                plt.show()
                '''
        },
        "headless": {
            "significado": "Modo de operação em que um software ou aplicativo é executado sem interface gráfica.",
            "uso": "É usado para rodar programas em servidores ou ambientes sem display, como em testes automatizados ou servidores web.",
            "ejemplo": '''
                from selenium import webdriver
                options = webdriver.ChromeOptions()
                options.add_argument("--headless")
                driver = webdriver.Chrome(options=options)
                driver.get("http://example.com")
                '''
        },
        "histcounts": {
            "significado": "Função que calcula a contagem de elementos em intervalos definidos, similar a um histograma.",
            "uso": "É usada para contar o número de ocorrências de valores em intervalos específicos.",
            "ejemplo": '''
                import numpy as np
                dados = np.random.randn(1000)
                contagem, bins = np.histogram(dados, bins=20)
                print(contagem)
                '''
        },
        "hexbin": {
            "significado": "Função que cria um gráfico de dispersão hexagonal para visualizar a densidade de pontos.",
            "uso": "É usada para visualizar a densidade de pontos em gráficos de dois eixos.",
            "ejemplo": '''
                import numpy as np
                import matplotlib.pyplot as plt
                x = np.random.randn(1000)
                y = np.random.randn(1000)
                plt.hexbin(x, y, gridsize=30, cmap='Blues')
                plt.colorbar()
                plt.show()
                '''
        },
        "http.client": {
            "significado": "Módulo Python que fornece classes e funções para comunicação HTTP.",
            "uso": "É usado para fazer requisições HTTP a servidores web.",
            "ejemplo": '''
                import http.client
                conn = http.client.HTTPSConnection("www.example.com")
                conn.request("GET", "/")
                resposta = conn.getresponse()
                print(resposta.status, resposta.reason)
                '''
        },
        "hook_fn": {
            "significado": "Função personalizada que é chamada em resposta a um evento ou condição específica.",
            "uso": "É usada para modificar o comportamento de um sistema quando um evento ocorre.",
            "ejemplo": '''
                def hook_fn(evento):
                    print(f"Evento ocorrido: {evento}")
                sistema.registrar_hook(hook_fn)
                '''
        },
        "hue": {
            "significado": "Matiz de uma cor no modelo de cores HSL ou HSV.",
            "uso": "É usado para determinar a cor de um objeto com base em seu matiz.",
            "ejemplo": '''
                import matplotlib.pyplot as plt
                h = 0.5  # Matiz
                s = 1    # Saturação
                v = 1    # Valor
                cor = (h, s, v)
                plt.imshow([[cor]])
                plt.show()
                '''
        },
        "hashset": {
            "significado": "Estrutura de dados que armazena elementos únicos de maneira eficiente, baseada em hash.",
            "uso": "É usada para armazenar itens de forma que duplicatas sejam descartadas automaticamente.",
            "ejemplo": '''
                meu_hashset = set([1, 2, 3, 2, 1])
                print(meu_hashset)  # Saída: {1, 2, 3}
                '''
        },
        "hdf5": {
            "significado": "Formato de arquivo e biblioteca para armazenar dados em grandes volumes, eficiente para arrays multidimensionais.",
            "uso": "É usado para armazenar e acessar dados científicos e de engenharia.",
            "ejemplo": '''
                import h5py
                with h5py.File('meuarquivo.h5', 'w') as f:
                    f.create_dataset("meudados", data=[1, 2, 3, 4, 5])
                '''
        },
        "hanning": {
            "significado": "Função que gera uma janela de Hanning, usada em análise de sinais.",
            "uso": "É usada para suavizar um conjunto de dados e reduzir o efeito de descontinuidade nas bordas.",
            "ejemplo": '''
                import numpy as np
                janela = np.hanning(10)
                print(janela)
                '''
        },
        "help_module": {
            "significado": "Função que exibe a documentação de um módulo ou pacote Python.",
            "uso": "É usada para obter ajuda sobre módulos específicos no Python.",
            "ejemplo": '''
                help(os)  # Mostra a documentação do módulo 'os'
                '''
        },
        "handle": {
            "significado": "Função ou método que lida com eventos ou ações em um sistema.",
            "uso": "É usado para processar ou responder a eventos, como cliques ou solicitações de rede.",
            "ejemplo": '''
                def handle(evento):
                    print(f"Evento {evento} recebido")
                handle('clique')
                '''
        },
        "hotspot": {
            "significado": "Área ou local específico onde ocorre uma atividade intensa ou concentração de dados.",
            "uso": "É usado para descrever regiões em imagens ou mapas onde há maior intensidade ou interesse.",
            "ejemplo": '''
                hotspot = (x, y)  # Coordenadas de um hotspot em uma imagem
                print(hotspot)
                '''
        },
        "hstack_block": {
            "significado": "Função ou operação que empilha blocos ou arrays horizontalmente.",
            "uso": "É usada para combinar várias matrizes ou arrays em uma única estrutura, alinhando-os horizontalmente.",
            "ejemplo": '''
                import numpy as np
                a = np.array([1, 2, 3])
                b = np.array([4, 5, 6])
                resultado = np.hstack((a, b))
                print(resultado)  # Saída: [1 2 3 4 5 6]
                '''
        },
        "http.server": {
            "significado": "Módulo Python para criar um servidor HTTP simples.",
            "uso": "É usado para servir arquivos ou responder a requisições HTTP em um servidor local.",
            "ejemplo": '''
                import http.server
                from socketserver import TCPServer
                handler = http.server.SimpleHTTPRequestHandler
                with TCPServer(('localhost', 8000), handler) as httpd:
                    httpd.serve_forever()
                '''
        },
        "haversine": {
            "significado": "Fórmula para calcular a distância entre dois pontos na superfície da Terra, dado a latitude e longitude.",
            "uso": "É usada para calcular a distância entre dois pontos geográficos, levando em conta a curvatura da Terra.",
            "ejemplo": '''
                from math import radians, sin, cos, sqrt, atan2
                def haversine(lat1, lon1, lat2, lon2):
                    R = 6371.0
                    lat1 = radians(lat1)
                    lon1 = radians(lon1)
                    lat2 = radians(lat2)
                    lon2 = radians(lon2)
                    dlon = lon2 - lon1
                    dlat = lat2 - lat1
                    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
                    c = 2 * atan2(sqrt(a), sqrt(1-a))
                    distancia = R * c
                    return distancia
                print(haversine(52.2296756, 21.0122287, 41.8919300, 12.5113300))  # Saída: distância em km
                '''
        },
        "hspace": {
            "significado": "Espaço horizontal entre elementos em uma interface gráfica ou layout.",
            "uso": "É usado para controlar o espaçamento horizontal em layouts de gráficos ou interfaces.",
            "ejemplo": '''
                import matplotlib.pyplot as plt
                fig, ax = plt.subplots()
                ax.plot([1, 2, 3], [1, 4, 9])
                plt.subplots_adjust(hspace=0.5)
                plt.show()
                '''
        },
        "hex_color": {
            "significado": "Código de cor em formato hexadecimal, representando valores de RGB.",
            "uso": "É usado para definir cores em páginas web ou gráficos com a notação hexadecima.",
            "ejemplo": '''
                cor = "#FF5733"  # Código hexadecimal para uma cor vermelha
                print(cor)
                '''
        },
        "handle_request": {
            "significado": "Função ou método que lida com uma solicitação, geralmente em servidores web.",
            "uso": "É usado para processar ou responder a uma solicitação de rede, como uma requisição HTTP.",
            "ejemplo": '''
                def handle_request(request):
                    print(f"Processando solicitação: {request}")
                handle_request('GET /index.html')
                '''
        },
        "html": {
            "significado": "Linguagem de marcação utilizada para criar páginas web.",
            "uso": "É usada para estruturar conteúdo na web, como texto, imagens e links.",
            "ejemplo": '''
                html = '<html><body><h1>Olá, mundo!</h1></body></html>'
                print(html)
                '''
        },
        "hybrid": {
            "significado": "Algo que combina dois ou mais elementos distintos.",
            "uso": "É usado para descrever sistemas ou métodos que combinam diferentes tecnologias ou abordagens.",
            "ejemplo": '''
                carro_hibrido = 'carro com motor elétrico e a combustão'
                print(carro_hibrido)
                '''
        },
        "hclust": {
            "significado": "Algoritmo de agrupamento hierárquico utilizado para agrupar dados.",
            "uso": "É usado em análise de dados para agrupar elementos com base em sua similaridade.",
            "ejemplo": '''
                from scipy.cluster.hierarchy import linkage, dendrogram
                from scipy.spatial.distance import pdist
                dados = [[1, 2], [2, 3], [3, 4], [5, 6]]
                Z = linkage(dados, method='ward')
                dendrogram(Z)
                '''
        },
        "harden": {
            "significado": "Tornar um sistema ou aplicação mais seguro, aplicando medidas de proteção.",
            "uso": "É usado para melhorar a segurança de sistemas, restringindo acessos ou fortalecendo defesas.",
            "ejemplo": '''
                def harden_system():
                    print("Aplicando medidas de segurança ao sistema.")
                harden_system()
                '''
        },
        "hist_equalize": {
            "significado": "Método de equalização de histograma, usado para melhorar o contraste de uma imagem.",
            "uso": "É usado para ajustar o contraste de imagens, distribuindo de maneira mais uniforme os valores de intensidade.",
            "ejemplo": '''
                import cv2
                import numpy as np
                img = cv2.imread('imagem.jpg', 0)
                img_eq = cv2.equalizeHist(img)
                cv2.imshow('Imagem Equalizada', img_eq)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                '''
        },
        "httpx": {
            "significado": "Biblioteca Python para fazer requisições HTTP, alternativa ao 'requests' com suporte a requisições assíncronas.",
            "uso": "É usada para fazer requisições HTTP de maneira simples e eficiente, com suporte para async.",
            "ejemplo": '''
                import httpx
                async def get_url():
                    async with httpx.AsyncClient() as client:
                        response = await client.get('https://www.example.com')
                        print(response.text)
                import asyncio
                asyncio.run(get_url())
                '''
        },
        "hdf": {
            "significado": "Formato de arquivo para armazenar grandes volumes de dados científicos, como matrizes multidimensionais.",
            "uso": "É usado em ciência de dados e pesquisa para armazenar dados grandes e complexos.",
            "ejemplo": '''
                import h5py
                with h5py.File('meuarquivo.h5', 'w') as f:
                    f.create_dataset('meudados', data=[1, 2, 3, 4, 5])
                '''
        },
        "histmatch": {
            "significado": "Método utilizado para ajustar o igualar o histograma de uma imagem a outro.",
            "uso": "É usado para modificar o contraste de uma imagem, fazendo com que seu histograma se assemelhe ao de outra imagem.",
            "ejemplo": '''
                import skimage.exposure as exposure
                imagem_original = imagem
                imagem_alvo = outra_imagem
                imagem_resultado = exposure.match_histograms(imagem_original, imagem_alvo)
                '''
        },
        "hasattr": {
            "significado": "Função que verifica se um objeto possui um atributo específico.",
            "uso": "É usada para verificar se um objeto tem um determinado atributo, evitando erros.",
            "ejemplo": '''
                class Pessoa:
                    def __init__(self, nome):
                        self.nome = nome

                p = Pessoa("João")
                print(hasattr(p, 'nome'))  # Saída: True
                '''
        },
        "httpx_session": {
            "significado": "Instância do objeto 'Session' da biblioteca httpx, que mantém conexões e gerencia requisições HTTP de forma eficiente.",
            "uso": "É usada para persistir configurações e conexões entre múltiplas requisições HTTP.",
            "ejemplo": '''
                import httpx
                with httpx.Client() as client:
                    resposta = client.get('https://www.ejemplo.com')
                    print(resposta.text)
                '''
        },
        "hash_table": {
            "significado": "Estrutura de dados que armazena pares chave-valor, permitindo buscas rápidas.",
            "uso": "É usada para mapear chaves a valores, oferecendo desempenho rápido para inserções, remoções e buscas.",
            "ejemplo": '''
                hash_table = {}
                hash_table['chave'] = 'valor'
                print(hash_table['chave'])  # Saída: valor
                '''
        },
        "hough_transform": {
            "significado": "Transformação matemática usada para detectar formas geométricas em imagens, como linhas e círculos.",
            "uso": "É utilizada em visão computacional para identificar padrões geométricos em imagens.",
            "ejemplo": '''
                import cv2
                import numpy as np
                img = cv2.imread('imagem.jpg', 0)
                linhas = cv2.HoughLines(img, 1, np.pi / 180, 200)
                '''
        },
        "hsv_to_rgb": {
            "significado": "Função que converte uma cor do espaço de cores HSV para o espaço RGB.",
            "uso": "É usada para converter cores representadas em valores de matiz, saturação e valor (HSV) para vermelho, verde e azul (RGB).",
            "ejemplo": '''
                import colorsys
                h, s, v = 0.5, 0.5, 0.5
                r, g, b = colorsys.hsv_to_rgb(h, s, v)
                print(r, g, b)
                '''
        },
        "http_code": {
            "significado": "Código numérico que representa o status de uma requisição HTTP.",
            "uso": "É utilizado para indicar o resultado de uma requisição HTTP, como sucesso, erro ou redirecionamento.",
            "ejemplo": '''
                codigo_http = 200  # Código de sucesso
                print(f"Código HTTP: {codigo_http}")
                '''
        },
        "http_status": {
            "significado": "Status textual associado a um código HTTP, que descreve o resultado de uma requisição.",
            "uso": "É utilizado para fornecer uma descrição legível do status de uma requisição HTTP.",
            "ejemplo": '''
                status_http = 'OK'  # Status de sucesso para código 200
                print(f"Status HTTP: {status_http}")
                '''
        },
        "hessian": {
            "significado": "Matriz de segundas derivadas de uma função, usada em otimização e em análise de imagens.",
            "uso": "É utilizada para entender a curvatura de uma função ou para detectar características em imagens, como bordas.",
            "ejemplo": '''
                import numpy as np
                hessiana = np.array([[1, 2], [3, 4]])
                print(hessiana)
                '''
        },
        "huber": {
            "significado": "Função de perda usada em regressão robusta, combinando os benefícios de erro quadrático e absoluto.",
            "uso": "É usada para reduzir o impacto de valores extremos em modelos de regressão.",
            "ejemplo": '''
                from sklearn.linear_model import HuberRegressor
                modelo = HuberRegressor()
                modelo.fit(X_train, y_train)
                '''
        },
        "hue_shift": {
            "significado": "Mudança no matiz de uma cor, que altera a percepção da cor sem afetar sua saturação ou brilho.",
            "uso": "É usado para alterar a tonalidade de uma cor em processamento de imagens.",
            "ejemplo": '''
                import colorsys
                h, s, v = 0.5, 1, 1
                h += 0.1  # Deslocar matiz
                r, g, b = colorsys.hsv_to_rgb(h, s, v)
                '''
        },
        "hard_limit": {
            "significado": "Função que limita um valor a um valor máximo ou mínimo específico.",
            "uso": "É usada em redes neurais ou controle de sistemas para limitar valores a um intervalo pré-definido.",
            "ejemplo": '''
                def hard_limit(x, limite=10):
                    return min(max(x, -limite), limite)
                print(hard_limit(15))  # Saída: 10
                '''
        },
        "highlight_text": {
            "significado": "Função que realça um texto, geralmente em uma interface gráfica ou em documentos.",
            "uso": "É usada para destacar uma parte do texto, como palavras-chave ou resultados de busca.",
            "ejemplo": '''
                def highlight_text(texto, palavra):
                    return texto.replace(palavra, f"*{palavra}*")
                print(highlight_text("Este é um ejemplo", "ejemplo"))
                '''
        },
        "hierarchical": {
            "significado": "Relativo a uma hierarquia, uma estrutura organizada por níveis ou camadas.",
            "uso": "É utilizado para descrever sistemas organizados de maneira hierárquica, como árvores ou agrupamentos.",
            "ejemplo": '''
                organizacao = {'CEO': {'CTO': {'Dev1': {}, 'Dev2': {}}}}
                print(organizacao)
                '''
        },
        "hash_code": {
            "significado": "Código gerado a partir de uma função de hash, usado para identificar de forma única objetos ou dados.",
            "uso": "É utilizado para verificar a integridade dos dados ou para comparar objetos rapidamente.",
            "ejemplo": '''
                hash_code = hash('ejemplo')
                print(hash_code)
                '''
        },
        "hermite": {
            "significado": "Interpolação polinomial que aproxima uma função e suas derivadas com polinômios.",
            "uso": "É usada para criar aproximações de funções suaves em cálculos numéricos e gráficos.",
            "ejemplo": '''
                from scipy.interpolate import CubicHermiteSpline
                x = [1, 2, 3]
                y = [2, 3, 5]
                dydx = [1, 0, -1]
                interpolador = CubicHermiteSpline(x, y, dydx)
                '''
        },
        "handle_event": {
            "significado": "Função que lida com eventos, geralmente em interfaces gráficas ou sistemas de resposta a entradas.",
            "uso": "É usada para processar e responder a ações ou eventos como cliques, pressionamento de teclas, etc.",
            "ejemplo": '''
                def handle_event(event):
                    print(f"Evento recebido: {event}")
                handle_event("Clique")
                '''
        },
        "homogeneous": {
            "significado": "Refere-se a algo que é uniforme ou consistente em sua composição.",
            "uso": "É usado para descrever sistemas ou dados que possuem características ou propriedades homogêneas.",
            "ejemplo": '''
                grupo_homogeneo = [1, 2, 3, 4]
                print("Lista homogênea:", grupo_homogeneo)
                '''
        },
        "hash_set": {
            "significado": "Estrutura de dados que armazena elementos únicos sem garantir uma ordem específica.",
            "uso": "É usada para garantir que não existam elementos duplicados em um conjunto.",
            "ejemplo": '''
                hash_set = set([1, 2, 3])
                hash_set.add(4)
                print(hash_set)  # Saída: {1, 2, 3, 4}
                '''
        },
        "hough_line": {
            "significado": "Transformação de Hough para detectar linhas retas em uma imagem.",
            "uso": "É usada em visão computacional para detectar linhas em imagens, mesmo quando as linhas estão parcialmente obstruídas.",
            "ejemplo": '''
                import cv2
                import numpy as np
                img = cv2.imread('imagem.jpg', 0)
                linhas = cv2.HoughLines(img, 1, np.pi / 180, 200)
                '''
        },
        "http_methods": {
            "significado": "Métodos HTTP que determinam a ação a ser realizada em uma requisição, como GET, POST, PUT, DELETE.",
            "uso": "São usados para especificar a ação desejada em uma requisição HTTP para um servidor.",
            "ejemplo": '''
                import requests
                resposta = requests.get('https://www.ejemplo.com')
                print(resposta.status_code)
                '''
        },
        "http_response": {
            "significado": "Objeto ou estrutura que contém os dados retornados de uma requisição HTTP.",
            "uso": "É usado para acessar o corpo, cabeçalhos e status de uma resposta a uma requisição HTTP.",
            "ejemplo": '''
                import requests
                resposta = requests.get('https://www.ejemplo.com')
                print(resposta.text)
                '''
        },
        "hex_to_bin": {
            "significado": "Função que converte um número hexadecimal para sua representação binária.",
            "uso": "É usada para converter números de base hexadecimal para base binária.",
            "ejemplo": '''
                hex_num = "1a"
                bin_num = bin(int(hex_num, 16))
                print(bin_num)  # Saída: 0b11010
                '''
        },
        "hist_interpolate": {
            "significado": "Método para interpolar ou suavizar dados de um histograma.",
            "uso": "É utilizado para ajustar a distribuição de um histograma ou melhorar sua precisão.",
            "ejemplo": '''
                import numpy as np
                import matplotlib.pyplot as plt
                dados = np.random.normal(size=1000)
                plt.hist(dados, bins=30, density=True, histtype='step', linestyle='-', color='blue')
                plt.show()
                '''
        },
        "hyperlink": {
            "significado": "Link clicável que direciona para outro recurso, página ou documento.",
            "uso": "É usado para navegar entre páginas web ou documentos ao clicar em um texto ou imagem.",
            "ejemplo": '''
                <a href="https://www.ejemplo.com">Clique aqui</a>
                '''
        },
        "hypertune": {
            "significado": "Processo de ajuste fino de parâmetros de um modelo ou algoritmo para melhorar seu desempenho.",
            "uso": "É usado para encontrar a configuração ideal para um modelo de aprendizado de máquina ou outro algoritmo.",
            "ejemplo": '''
                from sklearn.model_selection import GridSearchCV
                modelo = GridSearchCV(estimator, parametros)
                modelo.fit(X_train, y_train)
                '''
        },
        "http_parser": {
            "significado": "Componente responsável por analisar e interpretar o conteúdo de uma requisição ou resposta HTTP.",
            "uso": "É usado para decompor o conteúdo de uma requisição ou resposta HTTP e facilitar o processamento.",
            "ejemplo": '''
                import http.client
                conn = http.client.HTTPSConnection("www.ejemplo.com")
                conn.request("GET", "/")
                resposta = conn.getresponse()
                print(resposta.status, resposta.reason)
                '''
        },
        "hover": {
            "significado": "Ação de passar o cursor sobre um elemento sem clicar.",
            "uso": "É usado para exibir informações adicionais ou ativar efeitos interativos quando o cursor está sobre um item.",
            "ejemplo": '''
                <div class="hover-item">Passe o mouse aqui</div>
                <style>
                .hover-item:hover { color: red; }
                </style>
                '''
        },
        "http_auth": {
            "significado": "Métodos de autenticação utilizados para verificar a identidade de um usuário ou sistema em uma requisição HTTP.",
            "uso": "É usado para garantir que apenas usuários autorizados possam acessar certos recursos ou informações.",
            "ejemplo": '''
                import requests
                from requests.auth import HTTPBasicAuth
                resposta = requests.get('https://www.ejemplo.com', auth=HTTPBasicAuth('usuario', 'senha'))
                '''
        },
        "hstack_array": {
            "significado": "Função que empilha arrays horizontalmente, ou seja, os coloca lado a lado.",
            "uso": "É usada para combinar múltiplos arrays ao longo do eixo horizontal.",
            "ejemplo": '''
                import numpy as np
                a = np.array([1, 2, 3])
                b = np.array([4, 5, 6])
                c = np.hstack((a, b))
                print(c)  # Saída: [1 2 3 4 5 6]
                '''
        },
        "heightmap": {
            "significado": "Imagem ou representação de dados em que a intensidade de cada pixel representa a elevação em um ponto específico.",
            "uso": "É usada em gráficos e modelagem para representar a topografia de uma superfície ou terreno.",
            "ejemplo": '''
                import numpy as np
                import matplotlib.pyplot as plt
                dados = np.random.rand(10, 10)
                plt.imshow(dados, cmap='gray')
                plt.show()
                '''
        },
        "high_frequency": {
            "significado": "Frequência elevada, geralmente associada a sinais ou ondas com altas taxas de oscilação.",
            "uso": "É usado para descrever sinais, ondas ou sistemas que operam em altas frequências.",
            "ejemplo": '''
                sinais = ['sinal_1', 'sinal_2']
                print("Frequência alta: ", sinais)
                '''
        },
        "hidden_state": {
            "significado": "Estado interno de um modelo de aprendizado de máquina, especialmente em redes neurais recorrentes.",
            "uso": "É usado para armazenar informações de estados anteriores em modelos que possuem memória, como LSTM e RNN.",
            "ejemplo": '''
                import tensorflow as tf
                modelo = tf.keras.Sequential([tf.keras.layers.LSTM(50)])
                print(modelo.get_weights())
                '''
        },
        "hashmap": {
            "significado": "Estrutura de dados que armazena pares de chave-valor e permite acesso rápido aos valores com base na chave.",
            "uso": "É usada para criar dicionários ou tabelas de busca eficientes, com tempo de acesso constante em média.",
            "ejemplo": '''
                hashmap = {"chave": "valor", "a": 1, "b": 2}
                print(hashmap["a"])  # Saída: 1
                '''
        },
        "hostfile": {
            "significado": "Arquivo que contém informações sobre os hosts em uma rede, incluindo endereços IP e nomes de máquina.",
            "uso": "É utilizado para armazenar configurações e informações de rede, muitas vezes em ambientes distribuídos.",
            "ejemplo": '''
                # ejemplo de conteúdo de hostfile
                # 192.168.1.1  servidor1
                # 192.168.1.2  servidor2
                '''
        },
        "hit_rate": {
            "significado": "Taxa de acertos, geralmente associada ao desempenho de sistemas de cache ou busca.",
            "uso": "É usada para medir a eficiência de um sistema, como a quantidade de vezes que um item foi encontrado em um cache em relação ao número total de tentativas.",
            "ejemplo": '''
                hits = 80
                tentativas = 100
                taxa_de_acerto = hits / tentativas
                print(f"Taxa de acerto: {taxa_de_acerto}")
                '''
        },
        "horizontal_flip": {
            "significado": "Operação que inverte a imagem ou objeto de forma horizontal.",
            "uso": "É usada em processamento de imagem e aprendizado de máquina para aumentar a variedade de dados de treinamento.",
            "ejemplo": '''
                from PIL import Image
                imagem = Image.open('imagem.jpg')
                imagem_flip = imagem.transpose(Image.FLIP_LEFT_RIGHT)
                imagem_flip.show()
                '''
        },
        "http_request": {
            "significado": "Requisição feita a um servidor HTTP, que pode ser de diversos tipos, como GET, POST, PUT, DELETE.",
            "uso": "É usada para enviar dados a um servidor ou recuperar informações de um servidor.",
            "ejemplo": '''
                import requests
                resposta = requests.get('https://www.ejemplo.com')
                print(resposta.text)
                '''
        },
        "hysteresis": {
            "significado": "Fenômeno onde a resposta de um sistema depende não apenas da entrada atual, mas também do histórico recente.",
            "uso": "É usado para descrever sistemas com dependência temporal, como em circuitos eletrônicos e processos de decisão.",
            "ejemplo": '''
                # ejemplo simplificado de histerese
                def histerese(valor, limite_superior, limite_inferior):
                    if valor > limite_superior:
                        return "Ligado"
                    elif valor < limite_inferior:
                        return "Desligado"
                    else:
                        return "Indeterminado"
                '''
        },
        "half_width": {
            "significado": "A metade da largura de um objeto, geralmente usada para cálculos geométricos.",
            "uso": "É usada em cálculos envolvendo simetrias ou para centralizar elementos em gráficos e designs.",
            "ejemplo": '''
                largura = 10
                metade_largura = largura / 2
                print(f"Metade da largura: {metade_largura}")
                '''
        },
        "hatch_fill": {
            "significado": "Preenchimento de uma área com um padrão de linhas ou marcas.",
            "uso": "É usado para criar padrões em gráficos, como barras de histograma ou imagens vetoriais.",
            "ejemplo": '''
                import matplotlib.pyplot as plt
                fig, ax = plt.subplots()
                ax.bar([1, 2, 3], [4, 5, 6], hatch='//')
                plt.show()
                '''
        },
        "http_proxy": {
            "significado": "Servidor intermediário que encaminha requisições HTTP entre o cliente e o servidor.",
            "uso": "É usado para controlar e monitorar o tráfego de rede, permitindo filtros, cache e anonimato.",
            "ejemplo": '''
                import requests
                proxies = {"http": "http://10.10.1.10:3128"}
                resposta = requests.get('https://www.ejemplo.com', proxies=proxies)
                print(resposta.text)
                '''
        },
        "header_bytes": {
            "significado": "Quantidade de dados que representam os cabeçalhos em uma requisição ou resposta HTTP.",
            "uso": "É usada para medir o tamanho dos cabeçalhos de uma requisição, que contêm metadados sobre a comunicação.",
            "ejemplo": '''
                import requests
                resposta = requests.head('https://www.ejemplo.com')
                print(len(resposta.headers))  # Número de bytes dos cabeçalhos
                '''
        },
        "hexa_grid": {
            "significado": "Grade de células hexagonais, geralmente usada em gráficos ou mapas.",
            "uso": "É usada para representar dados espaciais ou criar mapas de calor em ambientes com topografia ou dados irregulares.",
            "ejemplo": '''
                import numpy as np
                import matplotlib.pyplot as plt
                x = np.random.randn(1000)
                y = np.random.randn(1000)
                plt.hexbin(x, y, gridsize=30)
                plt.show()
                '''
        },
        "http_cache": {
            "significado": "Armazenamento temporário de dados de respostas HTTP para melhorar o desempenho.",
            "uso": "É usado para reduzir a carga do servidor e melhorar a velocidade de acesso a dados frequentemente requisitados.",
            "ejemplo": '''
                import requests
                from requests_cache import CachedSession
                session = CachedSession()
                resposta = session.get('https://www.ejemplo.com')
                print(resposta.text)
                '''
        },
        "hierarchy_tree": {
            "significado": "Representação gráfica de uma estrutura hierárquica, com níveis ou camadas organizacionais.",
            "uso": "É usado para exibir relações de parentesco, como árvores genealógicas, estruturas corporativas ou sistemas de arquivos.",
            "ejemplo": '''
                import matplotlib.pyplot as plt
                import networkx as nx
                G = nx.DiGraph()
                G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 5)])
                nx.draw(G, with_labels=True)
                plt.show()
                '''
        },
        "hex_to_rgb": {
            "significado": "Função que converte um valor hexadecimal de cor em valores RGB (vermelho, verde e azul).",
            "uso": "É usada para transformar cores representadas em formato hexadecimal para o formato RGB, utilizado em gráficos e interfaces.",
            "ejemplo": '''
                def hex_to_rgb(hex):
                    hex = hex.lstrip('#')
                    r, g, b = bytes.fromhex(hex)
                    return r, g, b

                print(hex_to_rgb('#ff5733'))  # Saída: (255, 87, 51)
                '''
        },
        "highlight_color": {
            "significado": "Cor utilizada para destacar ou chamar a atenção para um elemento visual.",
            "uso": "É usada para modificar a cor de um item em uma interface ou gráfico, destacando-o para melhorar a legibilidade.",
            "ejemplo": '''
                import matplotlib.pyplot as plt
                dados = [1, 2, 3, 4]
                plt.bar([1, 2, 3, 4], dados, color='yellow')  # Destaque com a cor amarela
                plt.show()
                '''
        },
        "hyperbolic": {
            "significado": "Relativo a uma geometria ou função hiperbólica, que envolve curvas e espaços não euclidianos.",
            "uso": "É usado para descrever fenômenos ou gráficos que seguem uma forma hiperbólica ou comportamentos não lineares.",
            "ejemplo": '''
                import numpy as np
                import matplotlib.pyplot as plt
                x = np.linspace(-2, 2, 100)
                y = np.sinh(x)  # Função hiperbólica
                plt.plot(x, y)
                plt.show()
                '''
        },
        "http_headers": {
            "significado": "Cabeçalhos enviados em uma requisição ou resposta HTTP que contêm metadados sobre a comunicação.",
            "uso": "São usados para transmitir informações sobre o formato, tipo e outras propriedades da comunicação HTTP.",
            "ejemplo": '''
                import requests
                resposta = requests.get('https://www.ejemplo.com')
                print(resposta.headers)  # Exibe os cabeçalhos HTTP
                '''
        },
        "hist_norm": {
            "significado": "Normalização de histograma, processo de ajustar a distribuição de intensidade de uma imagem.",
            "uso": "É usada em processamento de imagem para melhorar o contraste e equalizar os níveis de intensidade.",
            "ejemplo": '''
                import cv2
                import numpy as np
                img = cv2.imread('imagem.jpg', 0)
                img_normalizada = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)
                cv2.imshow('Imagem Normalizada', img_normalizada)
                cv2.waitKey(0)
                '''
        },
        "hover_text": {
            "significado": "Texto que aparece quando o usuário passa o cursor do mouse sobre um elemento.",
            "uso": "É usado para fornecer informações adicionais ou dicas sobre um item quando o cursor passa sobre ele em uma interface de usuário.",
            "ejemplo": '''
                import tkinter as tk
                root = tk.Tk()
                label = tk.Label(root, text="Passe o mouse aqui")
                label.pack()
                label.bind("<Enter>", lambda e: label.config(text="Texto de ajuda"))
                root.mainloop()
                '''
        },
        "http_status_code": {
            "significado": "Código numérico retornado por um servidor HTTP para indicar o resultado de uma requisição.",
            "uso": "É usado para informar o estado da requisição, como sucesso (200), erro (404), ou servidor indisponível (503).",
            "ejemplo": '''
                import requests
                resposta = requests.get('https://www.ejemplo.com')
                print(resposta.status_code)  # Exibe o código de status HTTP, como 200
                '''
        },
        "http_endpoint": {
            "significado": "Ponto final de uma API HTTP, onde o cliente faz requisições para acessar recursos.",
            "uso": "É utilizado para definir a URL e método de acesso a um serviço ou recurso em uma API.",
            "ejemplo": '''
                import requests
                resposta = requests.get('https://www.ejemplo.com/api/recurso')
                print(resposta.json())
                '''
        },
        "holdout": {
            "significado": "Método de validação de modelos de aprendizado de máquina em que uma parte dos dados é mantida de fora do treinamento para testes.",
            "uso": "É usado para avaliar a performance de um modelo usando um conjunto de dados que não foi utilizado para treinamento.",
            "ejemplo": '''
                from sklearn.model_selection import train_test_split
                X_train, X_test = train_test_split(X, test_size=0.2)
                '''
        },
        "hypergraph": {
            "significado": "Estrutura de dados generalizada que conecta vários vértices a um único hiperaresta, ao invés de conexões binárias.",
            "uso": "É usado para representar relacionamentos complexos em grafos e redes, onde um único vínculo pode conectar múltiplos elementos.",
            "ejemplo": '''
                # ejemplo básico de um hypergraph
                hypergraph = {1: [2, 3], 2: [1, 4], 3: [1], 4: [2]}
                print(hypergraph)
                '''
        },
        "hamming_window": {
            "significado": "Função de janela usada em processamento de sinais para suavizar os limites de uma sequência.",
            "uso": "É usada para reduzir o desvio espectral e melhorar a resolução de sinais em transformadas rápidas de Fourier.",
            "ejemplo": '''
                import numpy as np
                import matplotlib.pyplot as plt
                janela = np.hamming(100)
                plt.plot(janela)
                plt.show()
                '''
        },
        "headless_mode": {
            "significado": "Modo de operação onde uma aplicação é executada sem uma interface gráfica de usuário.",
            "uso": "É usado em servidores ou scripts automatizados para executar tarefas de forma eficiente sem a necessidade de uma interface visual.",
            "ejemplo": '''
                from selenium import webdriver
                options = webdriver.ChromeOptions()
                options.add_argument('--headless')
                driver = webdriver.Chrome(options=options)
                driver.get('https://www.ejemplo.com')
                '''
        },
        "http_redirect": {
            "significado": "Redirecionamento HTTP, onde uma requisição é automaticamente enviada para um novo local.",
            "uso": "É usado para encaminhar usuários de uma URL para outra, comumente utilizado em URLs obsoletas ou mudanças de domínio.",
            "ejemplo": '''
                # ejemplo de redirecionamento em resposta HTTP
                resposta = requests.get('https://www.ejemplo.com', allow_redirects=True)
                print(resposta.url)  # Exibe o URL final após o redirecionamento
                '''
        },
        "highlighter": {
            "significado": "Ferramenta usada para destacar ou realçar texto ou elementos em uma interface ou documento.",
            "uso": "É usada para chamar a atenção para informações importantes ou relevantes em documentos e interfaces gráficas.",
            "ejemplo": '''
                import tkinter as tk
                root = tk.Tk()
                label = tk.Label(root, text="Texto destacado", fg="yellow", bg="black")
                label.pack()
                root.mainloop()
                '''
        },
    },
    "i": {
        "if": {
            "significado": "Condição que é avaliada como verdadeira ou falsa.",
            "uso": "Usado para tomar decisões no fluxo de um programa.",
            "ejemplo": "if x > 10: print('Maior que 10')"
        },
        "immutable": {
            "significado": "Propriedade de um objeto ou estrutura de dados que não pode ser modificado após sua criação.",
            "uso": "É usado para garantir que o conteúdo de um objeto não seja alterado depois de definido.",
            "ejemplo": '''
                tupla = (1, 2, 3)
                # tupla[0] = 4  # Isso geraria um erro, pois tuplas são imutáveis.
                '''
        },
        "index": {
            "significado": "Posição de um elemento dentro de uma sequência ou estrutura de dados.",
            "uso": "É utilizado para acessar ou referenciar elementos em listas, tuplas ou outros tipos de dados sequenciais.",
            "ejemplo": '''
                lista = [10, 20, 30]
                print(lista[1])  # Saída: 20
                '''
        },
        "instance": {
            "significado": "Objeto individual de uma classe em programação orientada a objetos.",
            "uso": "É utilizado para criar e manipular um objeto que foi instanciado a partir de uma classe.",
            "ejemplo": '''
                class Carro:
                    def __init__(self, modelo):
                        self.modelo = modelo

                carro1 = Carro("Fusca")  # Instância da classe Carro
                print(carro1.modelo)  # Saída: Fusca
                '''
        },
        "inheritance": {
            "significado": "Mecanismo da programação orientada a objetos onde uma classe herda propriedades e métodos de outra.",
            "uso": "É utilizado para criar uma nova classe com base em uma classe existente, reutilizando seu código.",
            "ejemplo": '''
                class Animal:
                    def falar(self):
                        print("Som do animal")

                class Cachorro(Animal):
                    def falar(self):
                        print("Latido")

                cachorro = Cachorro()
                cachorro.falar()  # Saída: Latido
                '''
        },
        "interface": {
            "significado": "Contrato que define um conjunto de métodos que uma classe deve implementar, sem fornecer a implementação.",
            "uso": "É utilizado para especificar o comportamento esperado de classes que implementam a interface.",
            "ejemplo": '''
                from abc import ABC, abstractmethod

                class Forma(ABC):
                    @abstractmethod
                    def area(self):
                        pass

                class Circulo(Forma):
                    def area(self):
                        return 3.14 * 10 * 10
                '''
        },
        "instance_method": {
            "significado": "Método que é definido dentro de uma classe e opera sobre instâncias dessa classe.",
            "uso": "É utilizado para realizar operações ou manipular dados associados a uma instância específica de uma classe.",
            "ejemplo": '''
                class Pessoa:
                    def saudacao(self):
                        print("Olá, sou uma pessoa.")

                p = Pessoa()
                p.saudacao()  # Saída: Olá, sou uma pessoa.
                '''
        },
        "immutable_set": {
            "significado": "Estrutura de dados do tipo conjunto (set) que não pode ser modificada após sua criação.",
            "uso": "É usado quando se deseja garantir que os elementos de um conjunto não sejam alterados após a criação.",
            "ejemplo": '''
                conjunto_imutavel = frozenset([1, 2, 3])
                # conjunto_imutavel.add(4)  # Isso geraria um erro, pois o conjunto é imutável
                '''
        },
        "increment": {
            "significado": "Ação de aumentar o valor de uma variável ou contador.",
            "uso": "É utilizado para adicionar um valor a uma variável, frequentemente usado em contagens ou iterações.",
            "ejemplo": '''
                contador = 0
                contador += 1  # Incrementa o valor de contador
                print(contador)  # Saída: 1
                '''
        },
        "input_validation": {
            "significado": "Processo de verificar se os dados inseridos são válidos de acordo com critérios específicos.",
            "uso": "É utilizado para garantir que os dados fornecidos pelo usuário ou sistema estejam no formato correto antes de serem processados.",
            "ejemplo": '''
                idade = int(input("Qual a sua idade? "))
                if idade < 0:
                    print("Idade inválida.")
                else:
                    print("Idade válida.")
                '''
        },
        "indexing": {
            "significado": "Ação de acessar um elemento em uma estrutura de dados sequencial usando seu índice.",
            "uso": "É utilizado para buscar elementos em listas, tuplas, ou strings usando a posição de cada item.",
            "ejemplo": '''
                lista = ['a', 'b', 'c']
                print(lista[0])  # Saída: 'a'
                '''
        },
        "insertion_sort": {
            "significado": "Algoritmo de ordenação que constrói a sequência ordenada um item de cada vez, inserindo o item na posição correta.",
            "uso": "É utilizado para ordenar listas ou arrays de forma eficiente para pequenos conjuntos de dados.",
            "ejemplo": '''
                def insertion_sort(arr):
                    for i in range(1, len(arr)):
                        chave = arr[i]
                        j = i - 1
                        while j >= 0 and chave < arr[j]:
                            arr[j + 1] = arr[j]
                            j -= 1
                        arr[j + 1] = chave
                    return arr

                lista = [12, 11, 13, 5, 6]
                print(insertion_sort(lista))  # Saída: [5, 6, 11, 12, 13]
                '''
        },
        "integer": {
            "significado": "Tipo de dado que representa números inteiros, sem parte decimal.",
            "uso": "É utilizado para armazenar valores numéricos inteiros.",
            "ejemplo": '''
                numero = 42
                print(type(numero))  # Saída: <class 'int'>
                '''
        },
        "iterable": {
            "significado": "Objeto que pode ser iterado (percorrido) em um loop, como listas, tuplas e strings.",
            "uso": "É utilizado para referir-se a qualquer objeto que tenha suporte a iteração, permitindo o acesso aos seus elementos um a um.",
            "ejemplo": '''
                lista = [1, 2, 3]
                for item in lista:
                    print(item)
                '''
        },
        "identifier": {
            "significado": "Nome que identifica uma variável, função, classe ou outro elemento no código.",
            "uso": "É utilizado para dar nome a componentes de um programa, como variáveis e funções, para que possam ser referenciados no código.",
            "ejemplo": '''
                nome = "João"
                idade = 30
                print(nome, idade)  # Saída: João 30
                '''
        },
        "iteration": {
                "significado": "Processo de percorrer uma sequência ou estrutura de dados, como uma lista ou tupla, para acessar seus elementos um a um.",
                "uso": "É utilizado para realizar operações em cada elemento de uma sequência, geralmente com o uso de um laço de repetição.",
                "ejemplo": '''
                    lista = [1, 2, 3]
                    for item in lista:
                        print(item)
                    '''
            },
            "IP_address": {
                "significado": "Endereço único atribuído a dispositivos conectados a uma rede, usado para identificá-los e permitir a comunicação.",
                "uso": "É utilizado para identificar de forma única dispositivos em redes locais ou na internet.",
                "ejemplo": '''
                    ip = "192.168.1.1"
                    print("IP do dispositivo:", ip)
                    '''
            },
            "if_statement": {
                "significado": "Estrutura condicional utilizada para executar um bloco de código se uma condição for verdadeira.",
                "uso": "É utilizado para controlar o fluxo de execução de um programa, realizando diferentes ações dependendo das condições.",
                "ejemplo": '''
                    idade = 18
                    if idade >= 18:
                        print("Maior de idade")
                    else:
                        print("Menor de idade")
                    '''
            },
            "interface_class": {
                "significado": "Classe que define um conjunto de métodos que outras classes devem implementar, sem fornecer uma implementação concreta.",
                "uso": "É utilizado para criar contratos de comportamento que as classes que a implementarem devem seguir.",
                "ejemplo": '''
                    from abc import ABC, abstractmethod

                    class Veiculo(ABC):
                        @abstractmethod
                        def mover(self):
                            pass

                    class Carro(Veiculo):
                        def mover(self):
                            print("Carro em movimento")
                    '''
            },
            "input_device": {
                "significado": "Dispositivo utilizado para inserir dados em um computador ou sistema, como teclado, mouse, ou scanner.",
                "uso": "É utilizado para permitir que o usuário ou outro sistema forneça dados para o computador.",
                "ejemplo": '''
                    teclado = "Teclado USB"
                    print("Dispositivo de entrada:", teclado)
                    '''
            },
            "introspection": {
                "significado": "Processo de inspeção de objetos em tempo de execução para obter informações sobre suas propriedades e comportamentos.",
                "uso": "É utilizado para examinar e manipular a estrutura interna de um objeto ou classe em um programa.",
                "ejemplo": '''
                    x = 42
                    print(type(x))  # Saída: <class 'int'>
                    print(dir(x))  # Saída: lista de atributos e métodos do objeto
                    '''
            },
            "instance_variable": {
                "significado": "Variável que pertence a uma instância específica de uma classe, armazenando dados relacionados àquela instância.",
                "uso": "É utilizado para armazenar dados que são específicos a cada objeto instanciado de uma classe.",
                "ejemplo": '''
                    class Carro:
                        def __init__(self, modelo):
                            self.modelo = modelo

                    carro1 = Carro("Fusca")
                    print(carro1.modelo)  # Saída: Fusca
                    '''
            },
            "index_out_of_bounds": {
                "significado": "Erro que ocorre quando se tenta acessar um índice fora do intervalo válido de uma sequência ou lista.",
                "uso": "É utilizado para descrever um erro comum quando se trabalha com índices em sequências de dados.",
                "ejemplo": '''
                    lista = [1, 2, 3]
                    # print(lista[5])  # Isso causaria um erro de índice fora dos limites
                    '''
            },
            "input_output": {
                "significado": "Operações que envolvem a recepção (entrada) e o envio (saída) de dados entre o programa e o ambiente externo.",
                "uso": "É utilizado para descrever a interação de um programa com o usuário ou outros sistemas, por meio de entrada e saída de dados.",
                "ejemplo": '''
                    nome = input("Qual seu nome? ")
                    print("Olá, " + nome)
                    '''
            },
            "inplace": {
                "significado": "Operação realizada diretamente sobre os dados originais, sem criar uma cópia.",
                "uso": "É utilizado para modificar os dados diretamente na memória sem a necessidade de alocar novo espaço para os dados.",
                "ejemplo": '''
                    lista = [1, 2, 3]
                    lista.append(4)  # Modifica a lista original inplace
                    print(lista)  # Saída: [1, 2, 3, 4]
                    '''
            },
            "inherit": {
                "significado": "Ação de uma classe herdar propriedades e métodos de outra classe, permitindo reutilização de código.",
                "uso": "É utilizado para criar classes derivadas, que herdam funcionalidades de classes base.",
                "ejemplo": '''
                    class Animal:
                        def falar(self):
                            print("Som do animal")

                    class Cachorro(Animal):
                        def falar(self):
                            print("Latido")

                    cachorro = Cachorro()
                    cachorro.falar()  # Saída: Latido
                    '''
            },
            "index_of": {
                "significado": "Método utilizado para encontrar a posição (índice) de um elemento dentro de uma sequência, como uma lista ou string.",
                "uso": "É utilizado para localizar a posição de um item em uma lista ou sequência.",
                "ejemplo": '''
                    lista = [10, 20, 30, 40]
                    print(lista.index(30))  # Saída: 2
                    '''
            },
            "instruction_set": {
                "significado": "Conjunto de instruções que um processador é capaz de executar, formando a base para a execução de programas.",
                "uso": "É utilizado para descrever as operações que um processador pode realizar para executar um programa.",
                "ejemplo": '''
                    A arquitetura de um processador define seu conjunto de instruções.
                    '''
            },
            "iterable_object": {
                "significado": "Objeto que pode ser percorrido em um laço de repetição, como listas, tuplas e strings.",
                "uso": "É utilizado para se referir a objetos que implementam o protocolo de iteração, permitindo o acesso a seus elementos sequencialmente.",
                "ejemplo": '''
                    lista = [1, 2, 3]
                    for item in lista:
                        print(item)
                    '''
            },
            "image_processing": {
                "significado": "Técnicas e algoritmos usados para manipular e analisar imagens digitais.",
                "uso": "É utilizado para modificar, melhorar ou extrair informações de imagens por meio de processos computacionais.",
                "ejemplo": '''
                    import cv2
                    imagem = cv2.imread("imagem.jpg")
                    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
                    cv2.imshow("Imagem em cinza", imagem_cinza)
                    cv2.waitKey(0)
                    '''
            },
            "indirect_addressing": {
                "significado": "Método de acesso a dados em que o endereço de memória é armazenado em um local, e o valor real é obtido a partir desse endereço.",
                "uso": "É utilizado para referenciar dados de forma indireta, permitindo maior flexibilidade e dinamismo na manipulação de memória.",
                "ejemplo": '''
                    # Isso envolve manipulação avançada de ponteiros e endereços em linguagens como C.
                    '''
            },
            "i/o_buffer": {
                "significado": "Área de almacenamiento temporal utilizada para transferir datos entre dispositivos de entrada y salida.",
                "uso": "É utilizado para suavizar a comunicação entre sistemas que operam com diferentes velocidades, armazenando dados temporariamente.",
                "ejemplo": '''
                    with open('arquivo.txt', 'r') as file:
                        buffer = file.read()
                        print(buffer)
                    '''
            },
            "instance_variable": {
                "significado": "Variável que pertence a uma instância específica de uma classe, armazenando dados relacionados àquela instância.",
                "uso": "É utilizado para armazenar dados que são específicos a cada objeto instanciado de uma classe.",
                "ejemplo": '''
                    class Carro:
                        def __init__(self, modelo):
                            self.modelo = modelo

                    carro1 = Carro("Fusca")
                    print(carro1.modelo)  # Saída: Fusca
                    '''
            },


    },
    "j": {
            
        "join": {
            "significado": "Método ou função que combina elementos de uma lista ou sequência em uma única string, separada por um delimitador.",
            "uso": "É utilizado para unir elementos de uma lista em uma string, com um separador especificado.",
            "ejemplo": '''
                lista = ["Olá", "mundo"]
                resultado = " ".join(lista)
                print(resultado)  # Saída: "Olá mundo"
            '''
        },
        "json": {
            "significado": "Formato de dados leve usado para armazenar e transportar dados em formato de texto.",
            "uso": "É utilizado para trocar informações entre sistemas, especialmente em APIs.",
            "ejemplo": '''
                import json
                dados = {"nome": "João", "idade": 30}
                json_str = json.dumps(dados)
                print(json_str)  # Saída: {"nome": "João", "idade": 30}
            '''
        },
        "jupyter_notebook": {
            "significado": "Ferramenta interativa que permite criar e compartilhar documentos contendo código, texto, gráficos e outros elementos.",
            "uso": "É utilizado principalmente para análise de dados, aprendizado de máquina e visualização de resultados.",
            "ejemplo": '''
                # Para iniciar o Jupyter Notebook:
                jupyter notebook
                # Ele abrirá no navegador e permitirá criar novos notebooks.
            '''
        },
        "jump_table": {
            "significado": "Estrutura de dados que armazena endereços de instruções, usada para transferir controle rapidamente em programas.",
            "uso": "É utilizada para implementar switch cases ou tabelas de despachadores em linguagens de programação.",
            "ejemplo": '''
                jump_table = {
                    "op1": funcao1,
                    "op2": funcao2
                }
                opcao = "op1"
                jump_table[opcao]()  # Executa funcao1
            '''
        },
        "jvm": {
            "significado": "Java Virtual Machine, componente que executa bytecode Java em qualquer sistema operacional.",
            "uso": "É utilizado para executar programas Java, garantindo portabilidade entre diferentes sistemas.",
            "ejemplo": '''
                # Código Java compilado em bytecode
                javac MeuPrograma.java
                # Executado pela JVM
                java MeuPrograma
            '''
        },
        "jshell": {
            "significado": "Ferramenta interativa de linha de comando para executar código Java em tempo real.",
            "uso": "É utilizada para prototipar, testar e aprender Java de maneira interativa.",
            "ejemplo": '''
                # Iniciar o JShell:
                jshell
                # Dentro do JShell:
                System.out.println("Olá Mundo");
            '''
        },
        "jupyter": {
            "significado": "Plataforma que suporta notebooks interativos para diferentes linguagens de programação.",
            "uso": "É utilizada para executar código, visualizar resultados e documentar análises.",
            "ejemplo": '''
                # Para iniciar o Jupyter:
                jupyter notebook
                '''
        },
        "jupyter_lab": {
            "significado": "Interface avançada para o Jupyter, oferecendo mais funcionalidades que o Jupyter Notebook.",
            "uso": "É utilizado para organizar notebooks, arquivos de dados e visualizações de maneira integrada.",
            "ejemplo": '''
                # Para iniciar o Jupyter Lab:
                jupyter lab
            '''
        },
        "jupyter_widgets": {
            "significado": "Componentes interativos usados em notebooks Jupyter para criar controles de interface de usuário.",
            "uso": "É utilizado para adicionar sliders, botões e gráficos interativos em notebooks.",
            "ejemplo": '''
                from ipywidgets import IntSlider
                slider = IntSlider(value=5, min=0, max=10)
                slider
            '''
        },
        "jsonschema": {
            "significado": "Biblioteca usada para validar documentos JSON contra um esquema definido.",
            "uso": "É utilizada para garantir que dados JSON atendam a uma estrutura predefinida.",
            "ejemplo": '''
                from jsonschema import validate
                schema = {"type": "object", "properties": {"idade": {"type": "integer"}}}
                dados = {"idade": 25}
                validate(instance=dados, schema=schema)
            '''
        },
        "jwt": {
            "significado": "JSON Web Token, formato usado para transmitir informações de maneira segura entre partes.",
            "uso": "É utilizado para autenticação e troca segura de informações em APIs.",
            "ejemplo": '''
                import jwt
                token = jwt.encode({"usuario": "admin"}, "segredo", algorithm="HS256")
                print(token)
            '''
        },
        "jupyterhub": {
            "significado": "Versão multiusuário do Jupyter, projetada para organizações e equipes.",
            "uso": "É utilizada para fornecer notebooks Jupyter a vários usuários em um ambiente compartilhado.",
            "ejemplo": '''
                # Para iniciar o JupyterHub:
                jupyterhub
            '''
        },
        "jython": {
            "significado": "Implementação da linguagem Python que roda em cima da JVM.",
            "uso": "É utilizado para integrar código Python em projetos Java.",
            "ejemplo": '''
                # Executar código Python com Jython:
                jython MeuScript.py
            '''
        },
        "jalview": {
            "significado": "Software de visualização para múltiplos alinhamentos de sequência biológica.",
            "uso": "É utilizado em bioinformática para analisar e editar alinhamentos de sequências.",
            "ejemplo": '''
                # Importar um arquivo de alinhamento no Jalview para análise
            '''
        },
        "jupyter_console": {
            "significado": "Interface de linha de comando interativa para o kernel do Jupyter.",
            "uso": "É utilizada para executar comandos em um ambiente de terminal, sem interface gráfica.",
            "ejemplo": '''
                # Para iniciar:
                jupyter console
            '''
        },
        "jsonpickle": {
            "significado": "Biblioteca para serializar objetos Python em formato JSON e restaurá-los.",
            "uso": "É utilizada para salvar e carregar objetos complexos como JSON.",
            "ejemplo": '''
                import jsonpickle
                obj = {"nome": "Maria"}
                json_str = jsonpickle.encode(obj)
                print(json_str)
            '''
        },
        "jose": {
            "significado": "Biblioteca para trabalhar com JSON Object Signing and Encryption (JOSE).",
            "uso": "É utilizada para assinar, criptografar e autenticar dados JSON.",
            "ejemplo": '''
                from jose import jwt
                token = jwt.encode({"dados": "seguro"}, "segredo", algorithm="HS256")
                print(token)
            '''
        },
        "jupyter_client": {
            "significado": "Biblioteca para comunicação entre clientes e kernels Jupyter.",
            "uso": "É utilizada para executar e controlar kernels de notebooks remotamente.",
            "ejemplo": '''
                from jupyter_client import KernelManager
                km = KernelManager()
                km.start_kernel()
            '''
        },
        "joblib": {
            "significado": "Biblioteca Python para salvar e carregar objetos, além de realizar paralelismo leve.",
            "uso": "É utilizada para serializar objetos e distribuir tarefas computacionais de forma eficiente.",
            "ejemplo": '''
                from joblib import dump, load
                modelo = {"peso": [0.1, 0.5, 0.3]}
                dump(modelo, 'modelo.joblib')
                carregado = load('modelo.joblib')
                print(carregado)
            '''
        },
        "jupyter_notebook_extension": {
            "significado": "Extensão para notebooks Jupyter que adiciona funcionalidades extras.",
            "uso": "É utilizada para expandir as capacidades dos notebooks Jupyter, como melhorias de interface e ferramentas adicionais.",
            "ejemplo": '''
                # Instalar extensões:
                pip install jupyter_contrib_nbextensions
                # Ativar extensões:
                jupyter nbextension enable <nome_da_extensão>
            '''
        },
        "json_response": {
            "significado": "Resposta de uma API em formato JSON.",
            "uso": "É utilizada para transmitir dados estruturados de um servidor para um cliente.",
            "ejemplo": '''
                from flask import Flask, jsonify
                app = Flask(__name__)
                @app.route('/dados')
                def dados():
                    return jsonify({"status": "sucesso", "mensagem": "Olá"})
            '''
        },
        "jupyter_contrib_nbextensions": {
            "significado": "Conjunto de extensões comunitárias para Jupyter Notebook.",
            "uso": "É utilizado para adicionar funcionalidades personalizadas aos notebooks.",
            "ejemplo": '''
                # Instalar extensões comunitárias:
                pip install jupyter_contrib_nbextensions
            '''
        },
        "jupyter_novice": {
            "significado": "Termo usado para indicar usuários iniciantes no ecossistema Jupyter.",
            "uso": "Refere-se a tutoriais ou materiais voltados para pessoas que estão começando com o Jupyter.",
            "ejemplo": '''
                # Exemplos de tutoriais para iniciantes podem ser encontrados no site oficial:
                https://jupyter.org
            '''
        },
        "jenkins": {
            "significado": "Ferramenta de integração contínua para automação de tarefas em desenvolvimento de software.",
            "uso": "É utilizada para construir, testar e implantar software de forma automatizada.",
            "ejemplo": '''
                # Para instalar Jenkins:
                sudo apt install jenkins
                # Acesse o painel:
                http://localhost:8080
            '''
        },
        "jupyter_terminal": {
            "significado": "Terminal integrado ao Jupyter que permite execução de comandos do sistema operacional.",
            "uso": "É utilizado para executar comandos diretamente em um ambiente Jupyter.",
            "ejemplo": '''
                # No Jupyter, abra o terminal clicando em "New > Terminal"
            '''
        },
        "jupyter_lab_extension": {
            "significado": "Extensões para JupyterLab que adicionam funcionalidades ou melhoram a experiência do usuário.",
            "uso": "É utilizada para personalizar o JupyterLab com ferramentas adicionais.",
            "ejemplo": '''
                # Instalar uma extensão:
                jupyter labextension install <nome_da_extensão>
            '''
        },
        "jupyter_kernel": {
            "significado": "Processo que executa o código em notebooks Jupyter.",
            "uso": "É utilizado para processar comandos enviados pelos notebooks.",
            "ejemplo": '''
                # Listar kernels disponíveis:
                jupyter kernelspec list
            '''
        },
        "jump_start": {
            "significado": "Início rápido ou guia introdutório para uma ferramenta ou tecnologia.",
            "uso": "É utilizado para começar rapidamente com uma nova tecnologia.",
            "ejemplo": '''
                # Um guia de jump start para Jupyter pode ser encontrado em:
                https://jupyter.org/install
            '''
        },
        "jupyter_tutorial": {
            "significado": "Material educativo que ensina a usar Jupyter Notebook ou JupyterLab.",
            "uso": "É utilizado para aprender as funcionalidades e aplicações do Jupyter.",
            "ejemplo": '''
                # Um exemplo de tutorial:
                https://realpython.com/jupyter-notebook-introduction/
            '''
        },
        "jupyter_quickstart": {
            "significado": "Guia rápido para configurar e começar a usar o Jupyter.",
            "uso": "É utilizado para facilitar a instalação e os primeiros passos com o Jupyter.",
            "ejemplo": '''
                # Guia oficial:
                https://jupyter.org/install
            '''
        },
        "jupyter_magic": {
            "significado": "Comandos especiais que estendem as funcionalidades dos notebooks Jupyter.",
            "uso": "É utilizado para realizar tarefas específicas, como carregar extensões ou controlar execução de código.",
            "ejemplo": '''
                # Comando mágico para verificar o tempo de execução:
                %timeit x = 2 + 2
            '''
        },
        "jinja2": {
            "significado": "Biblioteca de templates usada para criar HTML dinâmico com Python.",
            "uso": "É utilizada para renderizar páginas web com dados dinâmicos.",
            "ejemplo": '''
                from jinja2 import Template
                template = Template("Olá, {{ nome }}!")
                renderizado = template.render(nome="João")
                print(renderizado)  # Saída: Olá, João!
            '''
        },
        "jax": {
            "significado": "Biblioteca para computação numérica que combina autograd e paralelismo.",
            "uso": "É utilizada para acelerar cálculos científicos e aprendizado de máquina.",
            "ejemplo": '''
                import jax.numpy as jnp
                x = jnp.array([1.0, 2.0, 3.0])
                y = jnp.sin(x)
                print(y)
            '''
        },
        "jupyter_config": {
            "significado": "Arquivo ou ferramenta de configuração para o ambiente Jupyter.",
            "uso": "É utilizado para personalizar o comportamento de notebooks ou servidores Jupyter.",
            "ejemplo": '''
                # Para editar o arquivo de configuração do Jupyter:
                jupyter notebook --generate-config
                # Editar o arquivo em ~/.jupyter/jupyter_notebook_config.py
            '''
        },
        "job_queue": {
            "significado": "Estrutura que gerencia e organiza tarefas em fila para execução.",
            "uso": "É utilizada em sistemas de processamento paralelo ou distribuído para gerenciar tarefas pendentes.",
            "ejemplo": '''
                from queue import Queue
                fila = Queue()
                fila.put('Tarefa 1')
                fila.put('Tarefa 2')
                print(fila.get())  # Saída: Tarefa 1
            '''
        },
        "jinja2_templates": {
            "significado": "Modelos de template utilizados com o motor de templates Jinja2 para criar HTML dinâmico.",
            "uso": "É utilizado para renderizar páginas HTML com dados dinâmicos em aplicações web.",
            "ejemplo": '''
                from flask import Flask, render_template
                app = Flask(__name__)
                @app.route('/')
                def home():
                    return render_template('index.html', nome='João')
            '''
        },
        "jupyter_dashboard": {
            "significado": "Ferramenta para criar dashboards interativos no Jupyter Notebook.",
            "uso": "É utilizada para apresentar visualizações e dados de maneira interativa e organizada.",
            "ejemplo": '''
                # Instalar o pacote:
                pip install jupyter_dashboards
                # Configurar e exibir um dashboard no notebook.
            '''
        },
        "jq": {
            "significado": "Ferramenta de linha de comando para processar e manipular dados em formato JSON.",
            "uso": "É utilizada para filtrar, transformar e analisar dados JSON diretamente no terminal.",
            "ejemplo": '''
                # Exemplo de uso:
                echo '{ "nome": "João", "idade": 30 }' | jq '.nome'
                # Saída: "João"
            '''
        },

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
        "kde": {
            "significado": "Estimativa de Densidade Kernel (Kernel Density Estimation), um método para estimar a densidade de probabilidade de uma variável.",
            "uso": "É utilizado em estatística e machine learning para modelar a distribuição de dados de maneira não-paramétrica.",
            "ejemplo": '''
                import seaborn as sns
                import numpy as np
                dados = np.random.randn(100)
                sns.kdeplot(dados)
            '''
        },
        "kmeans": {
            "significado": "Algoritmo de agrupamento baseado na minimização da soma das distâncias ao centróide mais próximo.",
            "uso": "É utilizado em machine learning para dividir dados em grupos ou clusters.",
            "ejemplo": '''
                from sklearn.cluster import KMeans
                import numpy as np
                dados = np.array([[1, 2], [1, 4], [1, 0], [10, 2], [10, 4], [10, 0]])
                kmeans = KMeans(n_clusters=2, random_state=0).fit(dados)
                print(kmeans.labels_)
            '''
        },
        "knn": {
            "significado": "K-Nearest Neighbors, um algoritmo de classificação baseado na proximidade dos dados no espaço.",
            "uso": "É utilizado em machine learning para classificação ou regressão com base nos vizinhos mais próximos.",
            "ejemplo": '''
                from sklearn.neighbors import KNeighborsClassifier
                X = [[0], [1], [2], [3]]
                y = [0, 0, 1, 1]
                knn = KNeighborsClassifier(n_neighbors=2)
                knn.fit(X, y)
                print(knn.predict([[1.5]]))  # Saída: [0]
            '''
        },
        "key": {
            "significado": "Um identificador ou índice utilizado em coleções como dicionários para acessar valores.",
            "uso": "É utilizado para armazenar e acessar pares de chave-valor em estruturas de dados como dicionários.",
            "ejemplo": '''
                dicionario = {'nome': 'João', 'idade': 30}
                print(dicionario['nome'])  # Saída: João
            '''
        },
        "kivy": {
            "significado": "Biblioteca de Python para desenvolvimento de aplicações com interfaces gráficas multi-touch.",
            "uso": "É utilizada para criar aplicativos multiplataforma com interface gráfica.",
            "ejemplo": '''
                from kivy.app import App
                from kivy.uix.label import Label
                class MeuApp(App):
                    def build(self):
                        return Label(text='Olá, Mundo!')
                MeuApp().run()
            '''
        },
        "kiwisolver": {
            "significado": "Biblioteca de resolução de restrições para layout de interfaces.",
            "uso": "É utilizada em frameworks como Kivy para resolver equações de layout.",
            "ejemplo": '''
                from kiwisolver import Variable, Solver
                x = Variable('x')
                solver = Solver()
                solver.add_constraint(x >= 10)
                solver.update_variables()
                print(x.value())  # Saída: 10
            '''
        },
        "keras": {
            "significado": "Biblioteca de alto nível para construir e treinar redes neurais.",
            "uso": "É utilizada para implementar modelos de deep learning de forma simples e eficiente.",
            "ejemplo": '''
                from keras.models import Sequential
                from keras.layers import Dense
                modelo = Sequential([Dense(10, activation='relu', input_shape=(8,))])
                modelo.compile(optimizer='adam', loss='mse')
            '''
        },
        "kdb": {
            "significado": "Banco de dados em memória, frequentemente utilizado em aplicações financeiras para análise de grandes volumes de dados.",
            "uso": "É utilizado para armazenar e consultar dados rapidamente.",
            "ejemplo": '''
                # Consultas são feitas com q, a linguagem do KDB:
                q) tabela: ([] col1: 1 2 3; col2: `a`b`c)
                q) select from tabela where col1 > 1
            '''
        },
        "kivy_garden": {
            "significado": "Conjunto de pacotes comunitários para Kivy.",
            "uso": "É utilizado para expandir a funcionalidade do Kivy com widgets e componentes adicionais.",
            "ejemplo": '''
                # Instalar um pacote:
                garden install graph
                # Usar o pacote no aplicativo Kivy
            '''
        },
        "knapsack": {
            "significado": "Problema da mochila, um problema de otimização combinatória.",
            "uso": "É utilizado para encontrar a melhor combinação de itens que maximizam um valor dentro de uma capacidade limitada.",
            "ejemplo": '''
                def mochila(capacidade, valores, pesos):
                    n = len(valores)
                    tabela = [[0] * (capacidade + 1) for _ in range(n + 1)]
                    for i in range(1, n + 1):
                        for w in range(1, capacidade + 1):
                            if pesos[i - 1] <= w:
                                tabela[i][w] = max(tabela[i - 1][w], tabela[i - 1][w - pesos[i - 1]] + valores[i - 1])
                            else:
                                tabela[i][w] = tabela[i - 1][w]
                    return tabela[n][capacidade]
                print(mochila(50, [60, 100, 120], [10, 20, 30]))  # Saída: 220
            '''
        },
        "kalman_filter": {
            "significado": "Algoritmo que utiliza uma série de medições ao longo do tempo para estimar valores desconhecidos.",
            "uso": "É utilizado em aplicações de rastreamento e previsão, como em navegação e controle.",
            "ejemplo": '''
                from pykalman import KalmanFilter
                filtro = KalmanFilter(initial_state_mean=0, n_dim_obs=1)
                medidas = [1, 2, 3]
                estimativas = filtro.em(measures).smooth(measures)
                print(estimativas)
            '''
        },
        "kruskal": {
            "significado": "Algoritmo para encontrar a árvore geradora mínima de um grafo.",
            "uso": "É utilizado em grafos ponderados para encontrar o conjunto de arestas que conecta todos os vértices com o menor custo total.",
            "ejemplo": '''
                class Grafo:
                    def __init__(self, vertices):
                        self.V = vertices
                        self.grafo = []
                    def adicionar_aresta(self, u, v, w):
                        self.grafo.append([u, v, w])
                    def kruskal(self):
                        self.grafo = sorted(self.grafo, key=lambda item: item[2])
                        # Implementação do algoritmo continua...
                '''
        },
        "kmer": {
            "significado": "Subsequências de comprimento k em uma sequência biológica.",
            "uso": "É utilizado em bioinformática para análise de sequências de DNA e RNA.",
            "ejemplo": '''
                def gerar_kmers(sequencia, k):
                    return [sequencia[i:i+k] for i in range(len(sequencia) - k + 1)]
                print(gerar_kmers('ATCG', 2))  # Saída: ['AT', 'TC', 'CG']
            '''
        },
        "kivy_uix": {
            "significado": "Módulo de widgets de interface de usuário no Kivy.",
            "uso": "É utilizado para criar elementos de interface como botões, caixas de texto, etc.",
            "ejemplo": '''
                from kivy.uix.button import Button
                btn = Button(text='Clique Aqui')
            '''
        },
        "kalman_smooth": {
            "significado": "Processo de suavizar uma série temporal usando o filtro de Kalman.",
            "uso": "É utilizado para melhorar estimativas em sistemas dinâmicos.",
            "ejemplo": '''
                from pykalman import KalmanFilter
                filtro = KalmanFilter(initial_state_mean=0, n_dim_obs=1)
                medidas = [1, 2, 3]
                estimativas = filtro.smooth(medidas)[0]
                print(estimativas)
            '''
        },
        "kurtosis": {
            "significado": "Métrica estatística que descreve a forma da cauda de uma distribuição.",
            "uso": "É utilizado para entender a forma de uma distribuição em relação a sua cauda e centralidade.",
            "ejemplo": '''
                from scipy.stats import kurtosis
                dados = [1, 2, 3, 4, 5]
                print(kurtosis(dados))  # Saída: valor de curtose
            '''
        },
        "knn_classifier": {
            "significado": "Uma implementação do algoritmo K-Nearest Neighbors para classificação.",
            "uso": "Utilizado para prever a classe de uma amostra com base nas classes dos vizinhos mais próximos.",
            "ejemplo": '''
                from sklearn.neighbors import KNeighborsClassifier
                X = [[0], [1], [2], [3]]
                y = [0, 0, 1, 1]
                knn = KNeighborsClassifier(n_neighbors=3)
                knn.fit(X, y)
                print(knn.predict([[1.5]]))  # Saída: [0]
            '''
        },
        "keylogger": {
            "significado": "Software ou script que registra todas as teclas pressionadas em um teclado.",
            "uso": "Frequentemente usado para segurança ou monitoramento (com consentimento) e, em casos maliciosos, para espionagem.",
            "ejemplo": '''
                # Código de exemplo não fornecido por questões éticas.
            '''
        },
        "kron": {
            "significado": "Operação de produto de Kronecker entre dois arrays ou matrizes.",
            "uso": "Utilizado em álgebra linear para operações matriciais específicas.",
            "ejemplo": '''
                import numpy as np
                A = np.array([[1, 2], [3, 4]])
                B = np.array([[0, 5], [6, 7]])
                resultado = np.kron(A, B)
                print(resultado)
            '''
        },
        "k-means++": {
            "significado": "Uma variante do algoritmo K-Means que melhora a inicialização dos centróides.",
            "uso": "Utilizado para melhorar a eficiência e precisão do algoritmo K-Means.",
            "ejemplo": '''
                from sklearn.cluster import KMeans
                X = [[1, 2], [1, 4], [1, 0], [10, 2], [10, 4], [10, 0]]
                kmeans = KMeans(n_clusters=2, init='k-means++', random_state=0).fit(X)
                print(kmeans.cluster_centers_)
            '''
        },
        "kingfisher": {
            "significado": "Um nome usado em tecnologia para ferramentas, bibliotecas ou projetos específicos.",
            "uso": "Variante contextual; pode se referir a um banco de dados ou ferramenta de análise.",
            "ejemplo": "Depende do contexto do projeto 'Kingfisher' em uso."
        },
        "ksplit": {
            "significado": "Operação de divisão de dados ou strings em partes específicas.",
            "uso": "Utilizado em particionamento de conjuntos de dados ou manipulação de strings.",
            "ejemplo": '''
                string = "a,b,c,d"
                partes = string.split(',')
                print(partes)  # Saída: ['a', 'b', 'c', 'd']
            '''
        },
        "key_value_pair": {
            "significado": "Estrutura de dados composta por uma chave e um valor associado.",
            "uso": "Utilizada em dicionários ou mapas para armazenar informações organizadas.",
            "ejemplo": '''
                dicionario = {"nome": "Alice", "idade": 25}
                print(dicionario["nome"])  # Saída: Alice
            '''
        },
        "knn_regressor": {
            "significado": "Uma implementação do algoritmo K-Nearest Neighbors para regressão.",
            "uso": "Utilizado para prever valores numéricos com base nos vizinhos mais próximos.",
            "ejemplo": '''
                from sklearn.neighbors import KNeighborsRegressor
                X = [[0], [1], [2], [3]]
                y = [0, 0.5, 2.5, 3]
                knn = KNeighborsRegressor(n_neighbors=2)
                knn.fit(X, y)
                print(knn.predict([[1.5]]))  # Saída: [1.5]
            '''
        },
        "kerberos": {
            "significado": "Protocolo de autenticação para redes de computadores.",
            "uso": "Utilizado para garantir comunicações seguras em redes não confiáveis.",
            "ejemplo": '''
                # Configuração de exemplo feita no ambiente do servidor, geralmente com comandos CLI.
            '''
        },
        "keras_tuner": {
            "significado": "Biblioteca para ajuste de hiperparâmetros em modelos Keras.",
            "uso": "Utilizado para encontrar automaticamente os melhores hiperparâmetros para um modelo de aprendizado profundo.",
            "ejemplo": '''
                from keras_tuner import RandomSearch
                def modelo_builder(hp):
                    modelo = Sequential()
                    hp_units = hp.Int('units', min_value=32, max_value=512, step=32)
                    modelo.add(Dense(units=hp_units, activation='relu'))
                    return modelo
            '''
        },
        "keystone": {
            "significado": "Módulo de autenticação e gerenciamento de identidade na nuvem OpenStack.",
            "uso": "Utilizado para fornecer autenticação centralizada em ambientes OpenStack.",
            "ejemplo": '''
                # Exemplos dependem da CLI ou API Keystone para integração.
            '''
        },
        "kotlin": {
            "significado": "Linguagem de programação moderna e tipada, usada para desenvolvimento Android e multiplataforma.",
            "uso": "Utilizada para construir aplicativos móveis, web e backend.",
            "ejemplo": '''
                fun main() {
                    println("Olá, Mundo!")
                }
            '''
        },
        "kivymd": {
            "significado": "Biblioteca que adiciona componentes Material Design ao Kivy.",
            "uso": "Utilizada para criar interfaces baseadas no Material Design em aplicativos Kivy.",
            "ejemplo": '''
                from kivymd.app import MDApp
                from kivymd.uix.button import MDRaisedButton
                class MeuApp(MDApp):
                    def build(self):
                        return MDRaisedButton(text="Clique Aqui")
                MeuApp().run()
            '''
        },
        "kmerscan": {
            "significado": "Ferramenta de bioinformática para análise de k-mers em sequências genéticas.",
            "uso": "Utilizado para detectar padrões em sequências de DNA ou RNA.",
            "ejemplo": '''
                # Ferramenta geralmente executada via terminal para analisar dados biológicos.
            '''
        },
        "knockoff": {
            "significado": "Método estatístico para seleção de variáveis usando falsificações controladas.",
            "uso": "Utilizado em análises estatísticas para reduzir falsos positivos em seleções de variáveis.",
            "ejemplo": '''
                # Requer bibliotecas específicas como knockoff.py, usadas para experimentos estatísticos.
            '''
        },
        "keycloak": {
            "significado": "Uma ferramenta de gerenciamento de identidade e acesso (IAM) de código aberto.",
            "uso": "Utilizada para autenticação, autorização e gerenciamento de usuários em aplicativos e serviços.",
            "ejemplo": '''
                # Exemplo de uso: configurar um cliente OAuth2 para um aplicativo web
                # Configurações realizadas via interface Keycloak ou API REST.
            '''
        },
        "kudl": {
            "significado": "Ferramenta para manipulação de dados ou estruturas específicas.",
            "uso": "Depende do contexto; pode ser uma biblioteca ou ferramenta personalizada em um projeto.",
            "ejemplo": "Descrição detalhada necessária para um exemplo aplicável."
        },
        "katib": {
            "significado": "Plataforma de ajuste de hiperparâmetros em aprendizado de máquina, parte do Kubeflow.",
            "uso": "Utilizada para realizar buscas automatizadas por hiperparâmetros ideais em modelos de aprendizado.",
            "ejemplo": '''
                # Configuração YAML para um experimento Katib:
                apiVersion: kubeflow.org/v1
                kind: Experiment
                metadata:
                name: exemplo-katib
                '''
        },
        "kwarg": {
            "significado": "Argumento de palavra-chave (keyword argument) em funções Python.",
            "uso": "Utilizado para passar argumentos nomeados em uma função, com flexibilidade para aceitar parâmetros adicionais.",
            "ejemplo": '''
                def funcao_exemplo(**kwargs):
                    for chave, valor in kwargs.items():
                        print(f"{chave}: {valor}")
                funcao_exemplo(nome="Alice", idade=25)
            '''
        },
        "kwlist": {
            "significado": "Lista de palavras reservadas em Python.",
            "uso": "Utilizada para verificar palavras reservadas que não podem ser usadas como identificadores em Python.",
            "ejemplo": '''
                import keyword
                print(keyword.kwlist)  # Saída: lista de palavras reservadas em Python
            '''
        },
        "kdb+": {
            "significado": "Banco de dados em memória e mecanismo de processamento orientado a colunas.",
            "uso": "Utilizado principalmente em análises financeiras e científicas para lidar com grandes volumes de dados em alta velocidade.",
            "ejemplo": '''
                // Exemplo em q, a linguagem de consulta do kdb+:
                t:([] time:09:00+til 5; price:100+til 5)
                select from t where price>102
            '''
        },
        "kexi": {
            "significado": "Ferramenta de gerenciamento de banco de dados gráfico, parte da suíte Calligra.",
            "uso": "Utilizada para criar e gerenciar bancos de dados sem a necessidade de escrever código SQL.",
            "ejemplo": '''
                # Exemplos de uso geralmente são interativos na interface do Kexi.
            '''
        },
        "kaffeine": {
            "significado": "Um reprodutor multimídia leve para o ambiente KDE.",
            "uso": "Utilizado para reproduzir vídeos, arquivos de áudio e streaming online.",
            "ejemplo": '''
                # Instalação no Linux:
                sudo apt install kaffeine
            '''
        },
        "kerosene": {
            "significado": "Uma biblioteca para aprendizado de máquina em PyTorch que facilita o treinamento de modelos.",
            "uso": "Utilizada para abstrair e simplificar tarefas comuns, como treinamento, validação e registro de métricas.",
            "ejemplo": '''
                from kerosene.trainers import Trainer
                trainer = Trainer(model, optimizer, loss_function)
                trainer.train(data_loader)
            '''
        },
        "kotlinx": {
            "significado": "Conjunto de bibliotecas complementares ao Kotlin, como kotlinx.coroutines ou kotlinx.serialization.",
            "uso": "Facilita tarefas como concorrência, serialização e manipulação de dados em Kotlin.",
            "ejemplo": '''
                import kotlinx.coroutines.*
                fun main() = runBlocking {
                    launch { println("Tarefa concorrente!") }
                }
            '''
        },
        "k3s": {
            "significado": "Versão leve e simplificada do Kubernetes para ambientes com recursos limitados.",
            "uso": "Utilizada para implantar e gerenciar clusters Kubernetes de maneira eficiente.",
            "ejemplo": '''
                # Instalação de k3s:
                curl -sfL https://get.k3s.io | sh -
            '''
        },
        "kerb": {
            "significado": "Abreviação de Kerberos, um protocolo de autenticação segura.",
            "uso": "Utilizado para autenticar usuários e serviços em redes seguras.",
            "ejemplo": '''
                # Configuração de autenticação Kerberos:
                kinit username@DOMAIN.COM
            '''
        },
        "k3d": {
            "significado": "Ferramenta para executar clusters k3s em contêineres Docker.",
            "uso": "Facilita a configuração e o gerenciamento de clusters Kubernetes leves em ambientes locais.",
            "ejemplo": '''
                # Criação de um cluster com k3d:
                k3d cluster create meu-cluster
            '''
        },
        "kali": {
            "significado": "Distribuição Linux projetada para testes de segurança e análise forense.",
            "uso": "Utilizada por profissionais de segurança para testes de penetração e auditorias de segurança.",
            "ejemplo": '''
                # Executar um escaneamento com Nmap no Kali Linux:
                nmap -sV 192.168.0.1
            '''
        },
        "kd-tree": {
            "significado": "Estrutura de dados para particionar espaço multidimensional em árvores binárias.",
            "uso": "Utilizada em busca de vizinhos próximos (k-NN) e outras operações espaciais.",
            "ejemplo": '''
                from scipy.spatial import KDTree
                points = [(1, 2), (3, 4), (5, 6)]
                tree = KDTree(points)
                print(tree.query((2, 3)))
            '''
        },
        "kmeans_clustering": {
            "significado": "Algoritmo de agrupamento que divide dados em k grupos baseados em seus atributos.",
            "uso": "Utilizado em aprendizado não supervisionado para identificar padrões em dados.",
            "ejemplo": '''
                from sklearn.cluster import KMeans
                kmeans = KMeans(n_clusters=3)
                kmeans.fit(dados)
                print(kmeans.labels_)
            '''
        },
        "kmeans_init": {
            "significado": "Método de inicialização de centroides no algoritmo k-means.",
            "uso": "Determina a posição inicial dos centroides para melhorar a eficiência do algoritmo.",
            "ejemplo": '''
                kmeans = KMeans(n_clusters=3, init='k-means++')
                kmeans.fit(dados)
            '''
        },
        "kafka": {
            "significado": "Plataforma de streaming de eventos distribuída de código aberto.",
            "uso": "Utilizada para construir pipelines de dados em tempo real e sistemas de mensageria.",
            "ejemplo": '''
                # Produzir uma mensagem Kafka usando a biblioteca confluent-kafka:
                from confluent_kafka import Producer
                p = Producer({'bootstrap.servers': 'localhost:9092'})
                p.produce('meu-topico', key='chave', value='mensagem')
            '''
        },
        "kubectl": {
            "significado": "Ferramenta de linha de comando para gerenciar clusters Kubernetes.",
            "uso": "Utilizada para executar comandos e interagir com recursos no Kubernetes.",
            "ejemplo": '''
                # Listar todos os pods no Kubernetes:
                kubectl get pods
            '''
        },
        "k8s": {
            "significado": "Abreviação de Kubernetes, um sistema para automação de implantação, escala e gerenciamento de contêineres.",
            "uso": "Utilizado para orquestrar aplicações baseadas em contêineres.",
            "ejemplo": '''
                # Criar um deployment no Kubernetes:
                kubectl create deployment nginx --image=nginx
            '''
        },
        "k-nearest_neighbors": {
            "significado": "Algoritmo k-vizinhos mais próximos, utilizado para classificação ou regressão.",
            "uso": "Baseia-se na proximidade dos dados em um espaço dimensional.",
            "ejemplo": '''
                from sklearn.neighbors import KNeighborsClassifier
                modelo = KNeighborsClassifier(n_neighbors=3)
                modelo.fit(X_train, y_train)
            '''
        },
        "k-nn_regressor": {
            "significado": "Versão do algoritmo k-NN utilizada para regressão em vez de classificação.",
            "uso": "Prevê valores baseando-se na média dos k vizinhos mais próximos.",
            "ejemplo": '''
                from sklearn.neighbors import KNeighborsRegressor
                regressor = KNeighborsRegressor(n_neighbors=3)
                regressor.fit(X_train, y_train)
            '''
        },
        "keras_layers": {
            "significado": "Camadas disponíveis na biblioteca Keras para construir redes neurais.",
            "uso": "Utilizadas para definir a arquitetura de uma rede neural em aprendizado profundo.",
            "ejemplo": '''
                from keras.models import Sequential
                from keras.layers import Dense
                modelo = Sequential()
                modelo.add(Dense(32, activation='relu', input_dim=100))
            '''
        },
        "kivy_app": {
            "significado": "Aplicação desenvolvida usando o framework Kivy para interfaces gráficas em Python.",
            "uso": "Utilizada para criar aplicativos com suporte a touch em várias plataformas.",
            "ejemplo": '''
                from kivy.app import App
                from kivy.uix.label import Label
                class MeuApp(App):
                    def build(self):
                        return Label(text='Olá Mundo!')
                MeuApp().run()
            '''
        },
        "key_error": {
            "significado": "Erro em Python que ocorre ao acessar uma chave inexistente em um dicionário.",
            "uso": "Indica que a chave solicitada não está presente no dicionário.",
            "ejemplo": '''
                dicionario = {'a': 1}
                print(dicionario['b'])  # Gera um KeyError
            '''
        },
        "kde_plot": {
            "significado": "Gráfico de estimativa de densidade kernel, utilizado para visualizar distribuições de dados.",
            "uso": "Comumente usado em análise de dados para representar distribuições contínuas de forma suave.",
            "ejemplo": '''
                import seaborn as sns
                import matplotlib.pyplot as plt
                dados = [1, 2, 2, 3, 3, 3, 4, 5]
                sns.kdeplot(dados)
                plt.show()
            '''
        },
        "kerberos_authentication": {
            "significado": "Processo de autenticação segura usando o protocolo Kerberos.",
            "uso": "Utilizado em redes seguras para autenticar usuários e serviços de forma confiável.",
            "ejemplo": '''
                # Inicializar uma sessão Kerberos:
                kinit username@DOMAIN.COM
            '''
        },
        "kivy_garden_widgets": {
            "significado": "Conjunto de widgets adicionais desenvolvidos pela comunidade Kivy.",
            "uso": "Facilita a criação de interfaces gráficas avançadas em aplicativos Kivy.",
            "ejemplo": '''
                # Instalar um widget do Kivy Garden:
                garden install graph
            '''
        },
        "kafka_consumer": {
            "significado": "Componente do Apache Kafka utilizado para consumir mensagens de um tópico.",
            "uso": "Processa dados transmitidos em tempo real no sistema Kafka.",
            "ejemplo": '''
                from kafka import KafkaConsumer
                consumer = KafkaConsumer('meu-topico', bootstrap_servers='localhost:9092')
                for mensagem in consumer:
                    print(mensagem.value)
            '''
        },
        "kafka_producer": {
            "significado": "Componente do Apache Kafka usado para enviar mensagens para um tópico.",
            "uso": "Utilizado para transmitir dados para sistemas baseados em Kafka.",
            "ejemplo": '''
                from kafka import KafkaProducer
                producer = KafkaProducer(bootstrap_servers='localhost:9092')
                producer.send('meu-topico', b'Mensagem Kafka')
            '''
        },
        "keras_optimizer": {
            "significado": "Otimizador usado em modelos Keras para ajustar pesos durante o treinamento.",
            "uso": "Determina como os pesos do modelo são ajustados com base na função de perda.",
            "ejemplo": '''
                from keras.optimizers import Adam
                otimizador = Adam(learning_rate=0.001)
            '''
        },
        "kubernetes_deployment": {
            "significado": "Objeto no Kubernetes usado para gerenciar a implantação de aplicativos.",
            "uso": "Facilita o gerenciamento de pods e a implantação de aplicativos escaláveis.",
            "ejemplo": '''
                # Arquivo YAML para um deployment:
                apiVersion: apps/v1
                kind: Deployment
                metadata:
                name: nginx-deployment
                spec:
                replicas: 2
                template:
                    spec:
                    containers:
                    - name: nginx
                        image: nginx:1.17.10
                '''
        },
        "kubernetes_cluster": {
            "significado": "Conjunto de máquinas (nós) que executam contêineres gerenciados pelo Kubernetes.",
            "uso": "Permite o gerenciamento de aplicações em contêiner em um ambiente distribuído.",
            "ejemplo": '''
                # Configurar um cluster com Minikube:
                minikube start
            '''
        },
        "k8s_pod": {
            "significado": "Menor unidade executável em Kubernetes que contém um ou mais contêineres.",
            "uso": "Executa aplicativos em contêiner em um cluster Kubernetes.",
            "ejemplo": '''
                # Criar um pod simples:
                apiVersion: v1
                kind: Pod
                metadata:
                name: meu-pod
                spec:
                containers:
                - name: meu-container
                    image: nginx
                '''
        },
        "kalman_filtering": {
            "significado": "Método estatístico para estimar o estado de um sistema dinâmico em tempo real.",
            "uso": "Amplamente utilizado em controle e rastreamento, como navegação e visão computacional.",
            "ejemplo": '''
                import pykalman
                filtro = pykalman.KalmanFilter(initial_state_mean=0, n_dim_obs=1)
                estimativas = filtro.em(dados).smooth(dados)[0]
            '''
        },
        "kafka_streams": {
            "significado": "Biblioteca do Kafka para processar dados em tempo real diretamente de tópicos Kafka.",
            "uso": "Permite criar aplicativos de processamento de dados baseados em fluxo.",
            "ejemplo": '''
                # Exemplo básico com Kafka Streams (Java):
                StreamsBuilder builder = new StreamsBuilder();
                KStream<String, String> stream = builder.stream("meu-topico");
                stream.to("topico-destino");
                '''
        },
        "kotlin_coroutines": {
            "significado": "Conceito de concorrência leve em Kotlin para código assíncrono e não bloqueante.",
            "uso": "Facilita a escrita de programas concorrentes com alta performance.",
            "ejemplo": '''
                import kotlinx.coroutines.*
                fun main() = runBlocking {
                    launch { println("Executando em paralelo!") }
                }
            '''
        },
        "kivy_screen_manager": {
            "significado": "Componente do Kivy para gerenciar e alternar entre várias telas em um aplicativo.",
            "uso": "Utilizado para criar aplicativos com múltiplas interfaces gráficas.",
            "ejemplo": '''
                from kivy.uix.screenmanager import ScreenManager, Screen
                class Tela1(Screen): pass
                class Tela2(Screen): pass
                gerenciador = ScreenManager()
                gerenciador.add_widget(Tela1(name='tela1'))
                gerenciador.add_widget(Tela2(name='tela2'))
            '''
        },
        "kafka_connect": {
            "significado": "Componente do Kafka para integrar diferentes sistemas com Kafka usando conectores.",
            "uso": "Facilita a movimentação de dados entre Kafka e sistemas externos.",
            "ejemplo": '''
                # Configurar um conector de origem no Kafka Connect:
                {
                "name": "meu-conector",
                "config": {
                    "connector.class": "FileStreamSource",
                    "tasks.max": "1",
                    "file": "/caminho/para/o/arquivo.txt",
                    "topic": "meu-topico"
                }
                }
            '''
        },
        "kerberos_ticket": {
            "significado": "Credencial gerada pelo Kerberos para autenticação segura de usuários ou serviços.",
            "uso": "Permite acesso seguro a recursos protegidos em redes baseadas em Kerberos.",
            "ejemplo": '''
                # Verificar tickets Kerberos:
                klist
            '''
        },
        "knapsack_problem": {
            "significado": "Problema de otimização combinatória que busca maximizar o valor em uma mochila limitada pelo seu peso.",
            "uso": "É utilizado em problemas de programação dinâmica para alocação de recursos.",
            "ejemplo": '''
                def knapsack(values, weights, capacity):
                    n = len(values)
                    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
                    for i in range(1, n + 1):
                        for w in range(capacity + 1):
                            if weights[i-1] <= w:
                                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
                            else:
                                dp[i][w] = dp[i-1][w]
                    return dp[n][capacity]
                '''
        },
        "kivy_listview": {
            "significado": "Componente da biblioteca Kivy para mostrar listas em aplicações.",
            "uso": "É utilizado para criar interfaces gráficas com listas de elementos interativos.",
            "ejemplo": '''
                from kivy.app import App
                from kivy.uix.listview import ListView, ListItemButton

                class MyApp(App):
                    def build(self):
                        return ListView()
                
                MyApp().run()
                '''
        },
        "kubernetes_service": {
            "significado": "Recurso do Kubernetes que define uma forma lógica de acessar um grupo de pods.",
            "uso": "É utilizado para balanceamento de carga e comunicação entre pods em um cluster.",
            "ejemplo": '''
                apiVersion: v1
                kind: Service
                metadata:
                name: my-service
                spec:
                selector:
                    app: MyApp
                ports:
                    - protocol: TCP
                    port: 80
                    targetPort: 8080
                '''
        },
        "kfold": {
            "significado": "Método de validação cruzada que divide os dados em k subconjuntos.",
            "uso": "É utilizado para avaliar modelos de machine learning com diferentes partições de dados.",
            "ejemplo": '''
                from sklearn.model_selection import KFold
                import numpy as np

                X = np.array([1, 2, 3, 4, 5])
                kf = KFold(n_splits=2)
                for train, test in kf.split(X):
                    print('train:', train, 'test:', test)
                '''
        },
        "kernel": {
            "significado": "Função que mede a similaridade em machine learning ou o núcleo de um sistema operacional.",
            "uso": "Em machine learning, é utilizado em algoritmos como SVM. Em sistemas, é o componente que interage com o hardware.",
            "ejemplo": '''
                # Kernel em SVM
                from sklearn.svm import SVC
                model = SVC(kernel='linear')
                '''
        },
        "knapsack_algorithm": {
            "significado": "Algoritmo que resolve o problema da mochila, otimizando a seleção de elementos.",
            "uso": "É utilizado para otimização em programação dinâmica e problemas combinatórios.",
            "ejemplo": '''
                # Exemplo em programação dinâmica
                def knapsack(values, weights, capacity):
                    n = len(values)
                    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
                    for i in range(1, n + 1):
                        for w in range(capacity + 1):
                            if weights[i-1] <= w:
                                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
                            else:
                                dp[i][w] = dp[i-1][w]
                    return dp[n][capacity]
                '''
        },
        "k8s_namespace": {
            "significado": "Recurso lógico no Kubernetes para isolar recursos dentro de um cluster.",
            "uso": "É utilizado para organizar e separar ambientes como desenvolvimento, teste e produção.",
            "ejemplo": '''
                apiVersion: v1
                kind: Namespace
                metadata:
                name: dev-environment
                '''
        },
        "keras_model": {
            "significado": "Modelo criado com a biblioteca Keras para deep learning.",
            "uso": "É utilizado para construir e treinar redes neuronais.",
            "ejemplo": '''
                from keras.models import Sequential
                from keras.layers import Dense

                model = Sequential([
                    Dense(10, activation='relu', input_shape=(20,)),
                    Dense(1, activation='sigmoid')
                ])
                '''
        },
        "knn_search": {
            "significado": "Busca dos vizinhos mais próximos em um espaço multidimensional.",
            "uso": "É utilizado em machine learning para classificar dados com base na proximidade.",
            "ejemplo": '''
                from sklearn.neighbors import NearestNeighbors
                import numpy as np

                data = np.array([[1, 2], [3, 4], [5, 6]])
                neigh = NearestNeighbors(n_neighbors=2)
                neigh.fit(data)
                print(neigh.kneighbors([[2, 3]]))
                '''
        },
        "kaggle_kernel": {
            "significado": "Ambiente de execução fornecido pelo Kaggle para experimentos de machine learning.",
            "uso": "É utilizado para executar scripts de análise e modelos diretamente na plataforma Kaggle.",
            "ejemplo": '''
                # Subir dados para um kernel no Kaggle e executá-los
                import pandas as pd
                df = pd.read_csv('/kaggle/input/data.csv')
                print(df.head())
                '''
        },
        "keylogger": {
            "significado": "Programa ou dispositivo que registra pressionamentos de teclas.",
            "uso": "É utilizado para fins de auditoria ou monitoramento do sistema (embora possa ser malicioso).",
            "ejemplo": '''
                # Exemplo básico (educativo, use eticamente)
                from pynput import keyboard

                def on_press(key):
                    print(f"Tecla pressionada: {key}")

                with keyboard.Listener(on_press=on_press) as listener:
                    listener.join()
                '''
        },
        "kotlin_script": {
            "significado": "Script escrito na linguagem de programação Kotlin.",
            "uso": "É utilizado para tarefas automatizadas, desenvolvimento de aplicações e scripting.",
            "ejemplo": '''
                println("Olá de um script de Kotlin")
                '''
        },
        "keyboard_interrupt": {
            "significado": "Exceção que ocorre ao interromper a execução de um programa, geralmente com Ctrl+C.",
            "uso": "É utilizado para interromper um programa em execução de forma controlada.",
            "ejemplo": '''
                try:
                    while True:
                        pass
                except KeyboardInterrupt:
                    print("Programa interrompido")
                '''
        },
        "kriging_interpolation": {
            "significado": "Método de interpolação utilizado em geostatística baseado em um modelo estatístico.",
            "uso": "É utilizado para prever valores em locais não amostrados a partir de dados geográficos.",
            "ejemplo": '''
                from pykrige.ok import OrdinaryKriging

                data = [[1, 1, 10], [2, 2, 20], [3, 3, 30]]
                ok = OrdinaryKriging(
                    [x[0] for x in data],
                    [x[1] for x in data],
                    [x[2] for x in data]
                )
                z, ss = ok.execute("grid", [1, 2, 3], [1, 2, 3])
                '''
        },
        "keypair": {
            "significado": "Par de chaves públicas e privadas utilizado em criptografia.",
            "uso": "É utilizado para criptografar e autenticar dados em sistemas seguros.",
            "ejemplo": '''
                from cryptography.hazmat.primitives.asymmetric import rsa

                key = rsa.generate_private_key(
                    public_exponent=65537,
                    key_size=2048
                )
                private_key = key.private_bytes()
                public_key = key.public_key().public_bytes()
                print(private_key, public_key)
                '''
        },
        "kinesis": {
            "significado": "Serviço da Amazon Web Services (AWS) para processar e analisar dados em tempo real.",
            "uso": "É utilizado para capturar, processar e analisar fluxos de dados como logs, eventos de IoT, entre outros.",
            "ejemplo": '''
                import boto3

                kinesis = boto3.client('kinesis')
                response = kinesis.put_record(
                    StreamName='meu-stream',
                    Data=b'Dados de teste',
                    PartitionKey='chave-de-particao'
                )
                print(response)
                '''
        },
        "kdb_query": {
            "significado": "Consulta executada em bancos de dados Kdb+, projetados para análise de séries temporais.",
            "uso": "É utilizado para análises rápidas em dados de alta frequência.",
            "ejemplo": '''
                // Exemplo em Q (linguagem de consulta do Kdb+)
                trades: ([] time: .z.p + til 10; price: 100 + til 10)
                select from trades where price > 105
                '''
        },
        "kivy_gridlayout": {
            "significado": "Widget da biblioteca Kivy que organiza widgets secundários em uma grade.",
            "uso": "É utilizado para projetar interfaces gráficas organizadas em linhas e colunas.",
            "ejemplo": '''
                from kivy.app import App
                from kivy.uix.gridlayout import GridLayout
                from kivy.uix.button import Button

                class MyApp(App):
                    def build(self):
                        layout = GridLayout(cols=2)
                        layout.add_widget(Button(text='Button 1'))
                        layout.add_widget(Button(text='Button 2'))
                        return layout
                    
                MyApp().run()
                '''
        },
        "kmeans_classifier": {
            "significado": "Algoritmo de machine learning baseado em agrupamento para classificação não supervisionada.",
            "uso": "É utilizado para agrupar dados em categorias com base na semelhança.",
            "ejemplo": '''
                from sklearn.cluster import KMeans

                X = [[1, 2], [3, 4], [1, 0], [10, 20]]
                kmeans = KMeans(n_clusters=2, random_state=0)
                kmeans.fit(X)
                print(kmeans.labels_)
                '''
        },
        "key_error_exception": {
            "significado": "Exceção lançada quando se tenta acessar uma chave inexistente em um dicionário.",
            "uso": "É utilizado para lidar com erros relacionados a chaves não encontradas.",
            "ejemplo": '''
                try:
                    my_dict = {'a': 1, 'b': 2}
                    print(my_dict['c'])
                except KeyError as e:
                    print(f"Chave não encontrada: {e}")
                '''
        },
        "kafka_message": {
            "significado": "Mensagem que é produzida ou consumida usando o Apache Kafka.",
            "uso": "É utilizado para trocar dados entre produtores e consumidores em um sistema distribuído.",
            "ejemplo": '''
                from kafka import KafkaProducer

                producer = KafkaProducer(bootstrap_servers='localhost:9092')
                producer.send('meu-topic', b'Mensagem de teste')
                producer.close()
                '''
        },
        "kde_estimation": {
            "significado": "Método de estimativa de densidade baseado em kernels.",
            "uso": "É utilizado para estimar distribuições de probabilidade a partir de dados observados.",
            "ejemplo": '''
                import numpy as np
                from sklearn.neighbors import KernelDensity

                data = np.array([[1.0], [2.0], [3.0]])
                kde = KernelDensity(kernel='gaussian', bandwidth=1.0).fit(data)
                log_density = kde.score_samples(data)
                print(np.exp(log_density))
                '''
        },
        "kotlin_function": {
            "significado": "Bloco de código reutilizável em Kotlin que realiza uma tarefa específica.",
            "uso": "É utilizado para modularizar código e evitar redundâncias.",
            "ejemplo": '''
                fun saudar(nome: String): String {
                    return "Olá, $nome"
                }

                println(saudar("Mundo"))
                '''
        },
        "k-means++": {
            "significado": "Método de inicialização para o algoritmo K-Means que melhora a seleção inicial de centróides.",
            "uso": "É utilizado para evitar problemas de convergência no K-Means.",
            "ejemplo": '''
                from sklearn.cluster import KMeans

                data = [[1, 2], [3, 4], [1, 0], [10, 20]]
                kmeans = KMeans(n_clusters=2, init='k-means++', random_state=0)
                kmeans.fit(data)
                print(kmeans.cluster_centers_)
                '''
        },
        "kubeflow": {
            "significado": "Plataforma de código aberto para desenvolver, implantar e gerenciar fluxos de trabalho de machine learning no Kubernetes.",
            "uso": "É utilizado para automatizar e escalar processos de machine learning.",
            "ejemplo": '''
                # Arquivo de configuração para implantar um pipeline no Kubeflow
                apiVersion: argoproj.io/v1alpha1
                kind: Workflow
                metadata:
                generateName: meu-pipeline-
                spec:
                entrypoint: minha-tarefa
                templates:
                - name: minha-tarefa
                    container:
                    image: tensorflow/tensorflow:latest
                    command: ["python", "meu_modelo.py"]
                '''
        },
        "keras_layer_dense": {
            "significado": "Camada totalmente conectada de uma rede neural no Keras.",
            "uso": "É utilizada para processar dados em redes neuronais.",
            "ejemplo": '''
                from keras.models import Sequential
                from keras.layers import Dense

                model = Sequential([
                    Dense(64, activation='relu', input_dim=20),
                    Dense(1, activation='sigmoid')
                ])
                '''
        },
        "knn_classifier": {
            "significado": "Classificador baseado nos k vizinhos mais próximos.",
            "uso": "É utilizado para classificar instâncias com base na proximidade a pontos conhecidos.",
            "ejemplo": '''
                from sklearn.neighbors import KNeighborsClassifier

                X = [[0], [1], [2], [3]]
                y = [0, 0, 1, 1]
                knn = KNeighborsClassifier(n_neighbors=2)
                knn.fit(X, y)
                print(knn.predict([[1.5]]))  # Saída: [0]
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
        "lambda_expression": {
            "significado": "Expressão anônima em Python que define uma função sem a necessidade de usar a palavra-chave 'def'.",
            "uso": "É utilizada para definir funções pequenas e simples de forma concisa.",
            "ejemplo": '''
                # Exemplo de uso de expressão lambda
                quadrado = lambda x: x ** 2
                print(quadrado(5))  # Saída: 25
                '''
        },
        "load_balancer": {
            "significado": "Sistema que distribui o tráfego de rede entre vários servidores para otimizar a carga e garantir a disponibilidade.",
            "uso": "É utilizado para gerenciar e balancear a carga entre servidores e melhorar a capacidade de resposta e a disponibilidade de aplicações.",
            "ejemplo": '''
                # Exemplo conceitual de um balanceador de carga
                # Em um ambiente de servidor web, o balanceador de carga pode distribuir solicitações entre vários servidores.
                '''
        },
        "linked_list": {
            "significado": "Estrutura de dados linear na qual os elementos (nós) estão conectados entre si por meio de ponteiros.",
            "uso": "É utilizada para armazenar e gerenciar coleções de dados de maneira flexível.",
            "ejemplo": '''
                class Node:
                    def __init__(self, value):
                        self.value = value
                        self.next = None

                # Criar uma lista encadeada simples
                head = Node(1)
                second = Node(2)
                third = Node(3)

                head.next = second
                second.next = third
                '''
        },
        "learning_rate": {
            "significado": "Parâmetro em algoritmos de otimização que determina o tamanho dos passos para atualizar os parâmetros do modelo.",
            "uso": "É utilizado para controlar a velocidade de aprendizado em modelos de machine learning e deep learning.",
            "ejemplo": '''
                from keras.optimizers import Adam

                optimizer = Adam(learning_rate=0.001)
                '''
        },
        "logger": {
            "significado": "Ferramenta ou módulo em programação que permite registrar eventos e mensagens de um programa.",
            "uso": "É utilizado para capturar e armazenar registros de eventos, erros ou informações em aplicações.",
            "ejemplo": '''
                import logging

                logging.basicConfig(level=logging.INFO)
                logging.info('Esta é uma mensagem de registro')
                '''
        },
        "load_data": {
            "significado": "Processo de carregamento de dados de uma fonte externa, como um arquivo ou banco de dados, para um programa ou sistema.",
            "uso": "É utilizado para importar dados e prepará-los para análise ou processamento em um programa.",
            "ejemplo": '''
                import pandas as pd

                df = pd.read_csv('dados.csv')
                print(df.head())
                '''
        },
        "line_chart": {
            "significado": "Gráfico usado para representar dados em duas dimensões, onde uma linha conecta pontos de dados em um eixo x e y.",
            "uso": "É utilizado para visualizar tendências ao longo do tempo ou mostrar a relação entre variáveis.",
            "ejemplo": '''
                import matplotlib.pyplot as plt

                x = [1, 2, 3, 4, 5]
                y = [2, 3, 5, 7, 11]

                plt.plot(x, y)
                plt.xlabel('X')
                plt.ylabel('Y')
                plt.title('Gráfico de Linha')
                plt.show()
                '''
        },
        "list_comprehension": {
            "significado": "Sintaxe em Python para criar listas de maneira compacta e legível usando uma única linha de código.",
            "uso": "É utilizada para gerar listas baseadas em loops de maneira mais eficiente e concisa.",
            "ejemplo": '''
                # Exemplo de list comprehension
                quadrados = [x ** 2 for x in range(10)]
                print(quadrados)  # Saída: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
                '''
        },
        "local_variable": {
            "significado": "Variável declarada dentro de uma função ou bloco de código e acessível apenas nesse contexto.",
            "uso": "É utilizada para armazenar dados temporários e específicos de uma função ou bloco de código.",
            "ejemplo": '''
                def minha_funcao():
                    variavel_local = 10  # Esta é uma variável local
                    print(variavel_local)

                minha_funcao()
                # print(variavel_local)  # Isso causaria um erro, pois variavel_local não está disponível fora da função
                '''
        },
        "long_integer": {
            "significado": "Tipo de dado em algumas linguagens de programação para representar números inteiros de grande tamanho.",
            "uso": "É utilizado para trabalhar com números que excedem o tamanho padrão dos inteiros.",
            "ejemplo": '''
                # Exemplo em Python 3, onde os inteiros são de tamanho arbitrário
                num = 123456789123456789123456789
                print(num)
                '''
        },
        "library": {
            "significado": "Coleção de funções e módulos pré-escritos que podem ser utilizados em um programa para facilitar tarefas específicas.",
            "uso": "É utilizada para estender as funcionalidades de uma linguagem de programação.",
            "ejemplo": '''
                # Exemplo de uso de uma biblioteca em Python
                import math

                print(math.sqrt(16))  # Saída: 4.0
                '''
        },
        "loop": {
            "significado": "Estrutura de controle que permite executar um bloco de código repetidamente até que uma condição seja atendida.",
            "uso": "É utilizada para repetir tarefas ou iterar sobre elementos de uma coleção.",
            "ejemplo": '''
                for i in range(5):
                    print(i)  # Imprime os números de 0 a 4
                '''
        },
        "load_file": {
            "significado": "Processo de leitura de dados de um arquivo e carregamento na memória de um programa.",
            "uso": "É utilizado para processar ou analisar dados armazenados em arquivos.",
            "ejemplo": '''
                with open('arquivo.txt', 'r') as file:
                    conteudo = file.read()
                    print(conteudo)
                '''
        },
        "list": {
            "significado": "Tipo de dado em Python que representa uma coleção ordenada de elementos que podem ser de diferentes tipos.",
            "uso": "É utilizada para armazenar e manipular sequências de dados.",
            "ejemplo": '''
                minha_lista = [1, 2, 3, 4, 5]
                print(minha_lista[1])  # Saída: 2
                '''
        },
        "lambda_function": {
            "significado": "Função anônima em Python definida com a palavra-chave 'lambda'.",
            "uso": "É utilizada para criar funções pequenas e de uma única linha.",
            "ejemplo": '''
                soma = lambda a, b: a + b
                print(soma(3, 4))  # Saída: 7
                '''
        },
        "lock": {
            "significado": "Mecanismo de sincronização usado para evitar o acesso concorrente a recursos compartilhados em programação concorrente.",
            "uso": "É utilizado para evitar condições de corrida e garantir a integridade dos dados.",
            "ejemplo": '''
                from threading import Lock

                lock = Lock()

                def funcao_segura_para_threads():
                    with lock:
                        print('Acesso controlado')
                '''
        },
        "loss_function": {
            "significado": "Função usada para medir a diferença entre a previsão do modelo e o valor real em machine learning.",
            "uso": "É utilizada para otimizar e ajustar o desempenho do modelo.",
            "ejemplo": '''
                from keras.losses import MeanSquaredError

                funcao_perda = MeanSquaredError()
                y_true = [1, 2, 3]
                y_pred = [1.1, 1.9, 3.2]
                perda = funcao_perda(y_true, y_pred)
                print(perda.numpy())
                '''
        },
        "linear_regression": {
            "significado": "Modelo estatístico que busca a relação entre uma variável dependente e uma ou mais variáveis independentes usando uma linha reta.",
            "uso": "É utilizado para fazer previsões e entender a relação entre variáveis.",
            "ejemplo": '''
                from sklearn.linear_model import LinearRegression

                X = [[1], [2], [3], [4]]
                y = [2, 3, 4, 5]

                modelo = LinearRegression()
                modelo.fit(X, y)
                print(modelo.predict([[5]]))  # Previsão para o valor 5
                '''
        },

    },
    "m": {
        # Aquí puedes agregar funciones que comiencen con la letra M
        "map": {
            "significado": "Função ou método que aplica uma função a cada elemento de um iterável e retorna um iterador dos resultados.",
            "uso": "É utilizado para transformar uma coleção aplicando uma função a cada um de seus elementos.",
            "ejemplo": '''
                # Exemplo de uso de map
                numeros = [1, 2, 3, 4]
                numeros_quadrados = map(lambda x: x ** 2, numeros)
                print(list(numeros_quadrados))  # Saída: [1, 4, 9, 16]
                '''
        },
        "merge": {
            "significado": "Operação de combinar dois ou mais elementos, listas ou conjuntos em um único, mantendo ou criando uma sequência ordenada.",
            "uso": "É utilizado para combinar dados de diferentes fontes ou para ordenar e combinar listas de maneira eficiente.",
            "ejemplo": '''
                # Exemplo de uso de merge em listas
                lista1 = [1, 3, 5]
                lista2 = [2, 4, 6]
                lista_combinada = sorted(lista1 + lista2)
                print(lista_combinada)  # Saída: [1, 2, 3, 4, 5, 6]
                '''
        },
        "memory_leak": {
            "significado": "Problema em programação onde um programa consome mais memória do que o necessário e não a libera, o que pode levar a falhas ou lentidão.",
            "uso": "É utilizado para descrever e diagnosticar problemas relacionados ao uso ineficiente da memória.",
            "ejemplo": '''
                # Exemplo de possível memory leak em Python
                class ExemploMemoryLeak:
                    def __init__(self):
                        self.data = []
                    def add_data(self, new_data):
                        self.data.append(new_data)

                obj = ExemploMemoryLeak()
                obj.add_data('some data')
                # Se obj continuar crescendo sem liberar memória, ocorre um memory leak
                '''
        },
        "mean": {
            "significado": "Valor médio de um conjunto de números, calculado somando todos os valores e dividindo pelo número de elementos.",
            "uso": "É utilizado em estatística e análise de dados para representar o centro de um conjunto de dados.",
            "ejemplo": '''
                # Exemplo de cálculo da média
                import numpy as np

                dados = [1, 2, 3, 4, 5]
                media = np.mean(dados)
                print(media)  # Saída: 3.0
                '''
        },
        "machine_learning": {
            "significado": "Campo da inteligência artificial que permite que os computadores aprendam com os dados e melhorem seu desempenho sem programação explícita.",
            "uso": "É utilizado para criar modelos preditivos e sistemas que podem se adaptar e aprender com a experiência.",
            "ejemplo": '''
                # Exemplo de uso de machine learning com scikit-learn
                from sklearn.linear_model import LinearRegression

                X = [[1], [2], [3]]
                y = [2, 3, 4]

                modelo = LinearRegression()
                modelo.fit(X, y)
                print(modelo.predict([[4]]))  # Previsão para um novo valor
                '''
        },
        "model": {
            "significado": "Representação matemática ou computacional de um sistema ou processo, utilizada para fazer previsões ou análises.",
            "uso": "É utilizado em machine learning e estatística para realizar inferências ou previsões baseadas em dados.",
            "ejemplo": '''
                # Exemplo de um modelo simples em scikit-learn
                from sklearn.model_selection import train_test_split
                from sklearn.linear_model import LinearRegression

                X, y = [[1], [2], [3]], [2, 3, 4]
                X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.2)

                modelo = LinearRegression()
                modelo.fit(X_treino, y_treino)
                print(modelo.score(X_teste, y_teste))
                '''
        },
        "momentum": {
            "significado": "Técnica em otimização de algoritmos que ajuda a acelerar o aprendizado e a evitar mínimos locais mantendo uma 'inércia' na mudança de parâmetros.",
            "uso": "É utilizado em redes neurais e algoritmos de otimização para melhorar a velocidade de convergência e evitar oscilações.",
            "ejemplo": '''
                # Exemplo de uso de momentum na otimização
                from keras.optimizers import SGD

                otimizador = SGD(learning_rate=0.01, momentum=0.9)
                '''
        },
        "matrix": {
            "significado": "Estrutura bidimensional de números organizada em linhas e colunas, utilizada em matemática e programação.",
            "uso": "É utilizado em álgebra linear, gráficos por computador e processamento de dados.",
            "ejemplo": '''
                import numpy as np

                matriz = np.array([[1, 2], [3, 4]])
                print(matriz)
                '''
        },
        "merge_sort": {
            "significado": "Algoritmo de ordenação que divide uma lista em sublistas, ordena-as recursivamente e depois as combina em ordem.",
            "uso": "É utilizado para ordenar listas de maneira eficiente com um tempo de complexidade O(n log n).",
            "ejemplo": '''
                def merge_sort(arr):
                    if len(arr) > 1:
                        meio = len(arr) // 2
                        esquerda = arr[:meio]
                        direita = arr[meio:]

                        merge_sort(esquerda)
                        merge_sort(direita)

                        i = j = k = 0
                        while i < len(esquerda) and j < len(direita):
                            if esquerda[i] < direita[j]:
                                arr[k] = esquerda[i]
                                i += 1
                            else:
                                arr[k] = direita[j]
                                j += 1
                            k += 1

                        while i < len(esquerda):
                            arr[k] = esquerda[i]
                            i += 1
                            k += 1

                        while j < len(direita):
                            arr[k] = direita[j]
                            j += 1
                            k += 1
                '''
        },
        "modularization": {
            "significado": "Processo de dividir um programa em módulos independentes para melhorar a organização e manutenção do código.",
            "uso": "É utilizado para estruturar o código em componentes reutilizáveis e facilitar sua compreensão.",
            "ejemplo": '''
                # Exemplo de modularização em Python
                # Arquivo: modulo.py
                def saudacao():
                    return 'Olá'

                # Arquivo principal
                from modulo import saudacao
                print(saudacao())  # Saída: 'Olá'
                '''
        },
        "multithreading": {
            "significado": "Técnica de programação que permite executar múltiplas threads de um processo simultaneamente para melhorar a eficiência e desempenho.",
            "uso": "É utilizado para realizar tarefas concorrentes e aproveitar melhor os recursos do processador.",
            "ejemplo": '''
                import threading

                def imprimir_numeros():
                    for i in range(5):
                        print(i)

                thread = threading.Thread(target=imprimir_numeros)
                thread.start()
                thread.join()
                '''
        },
        "mse": {
            "significado": "Erro quadrático médio, métrica utilizada para medir a diferença média entre os valores reais e os previstos em modelos de regressão.",
            "uso": "É utilizado para avaliar a precisão de um modelo de regressão.",
            "ejemplo": '''
                from sklearn.metrics import mean_squared_error

                y_real = [1, 2, 3]
                y_predito = [1.1, 2.0, 3.2]
                mse = mean_squared_error(y_real, y_predito)
                print(mse)
                '''
        },
        "minimax": {
            "significado": "Algoritmo utilizado em jogos de dois jogadores para encontrar a estratégia ótima minimizando a perda máxima possível.",
            "uso": "É utilizado em jogos e teoria dos jogos para avaliar os movimentos possíveis de ambos os jogadores e selecionar o melhor.",
            "ejemplo": '''
                # Exemplo conceitual de uso de minimax
                # Em um jogo de xadrez, minimax pode ser usado para escolher o movimento que minimiza a perda máxima.
                '''
        },
        "morphism": {
            "significado": "Função entre duas estruturas matemáticas que preserva a relação entre seus elementos.",
            "uso": "É utilizado em teoria das categorias e matemática para mapear estruturas de maneira coerente.",
            "ejemplo": '''
                # Exemplo de morfismo em álgebra de conjuntos
                def f(x):
                    return x + 1
                # f é um morfismo se preserva a estrutura da operação de adição.
                '''
        },
        "middleware": {
            "significado": "Software que atua como intermediário entre sistemas operacionais ou bancos de dados e as aplicações que são executadas sobre eles.",
            "uso": "É utilizado para facilitar a comunicação e a gestão de dados entre aplicações distribuídas.",
            "ejemplo": '''
                # Exemplo de middleware em uma aplicação web
                # Um middleware em uma aplicação web pode interceptar solicitações e responder antes de que cheguem à lógica de negócios.
                '''
        },
        "mean_absolute_error": {
            "significado": "Métrica utilizada para medir a diferença média absoluta entre os valores reais e os previstos.",
            "uso": "É utilizado para avaliar a precisão de modelos de regressão e é menos sensível a erros grandes em comparação com o MSE.",
            "ejemplo": '''
                from sklearn.metrics import mean_absolute_error

                y_real = [1, 2, 3]
                y_predito = [1.1, 2.0, 3.2]
                mae = mean_absolute_error(y_real, y_predito)
                print(mae)
                '''
        },
        "metric": {
            "significado": "Função utilizada para avaliar e quantificar o desempenho ou qualidade de um modelo ou sistema.",
            "uso": "É utilizado em diversos campos, como machine learning e análise de dados, para medir a efetividade e precisão dos modelos.",
            "ejemplo": '''
                # Exemplo de métrica em machine learning
                from sklearn.metrics import accuracy_score

                y_real = [0, 1, 1, 0]
                y_predito = [0, 1, 1, 1]
                acuracia = accuracy_score(y_real, y_predito)
                print(acuracia)  # Saída: 0.75
                '''
        },
        "monte_carlo_simulation": {
            "significado": "Método de simulação estocástica que utiliza a geração de números aleatórios para obter resultados aproximados de um problema matemático ou estatístico.",
            "uso": "É utilizado para resolver problemas complexos de cálculo, como estimar áreas, integrais ou probabilidades em sistemas com incerteza.",
            "ejemplo": '''
                # Exemplo de uma simulação de Monte Carlo para estimar π
                import numpy as np

                def estimar_pi(num_amostras):
                    dentro_do_circulo = 0
                    for _ in range(num_amostras):
                        x, y = np.random.rand(2)
                        if x**2 + y**2 <= 1:
                            dentro_do_circulo += 1
                    return (dentro_do_circulo / num_amostras) * 4

                print(estimando_pi(1000000))  # Saída aproximada: 3.14159
                '''
        },
        "minimum_spanning_tree": {
            "significado": "Árvore que conecta todos os nós de um grafo com o menor peso possível e sem ciclos.",
            "uso": "É utilizado em redes de computadores, design de circuitos e outras áreas para conectar pontos de maneira eficiente.",
            "ejemplo": '''
                # Exemplo de uso do algoritmo de Kruskal para encontrar uma árvore de expansão mínima
                from scipy.spatial import distance_matrix
                import numpy as np

                pontos = np.array([[0, 0], [1, 0], [0, 1], [1, 1]])
                matriz_de_distancias = distance_matrix(pontos, pontos)
                print("Matriz de distâncias:\n", matriz_de_distancias)
                '''
        },
        "maximum_likelihood": {
            "significado": "Método de estimação de parâmetros de um modelo estatístico que busca maximizar a função de verossimilhança.",
            "uso": "É utilizado para encontrar os valores dos parâmetros de um modelo que melhor explicam os dados observados.",
            "ejemplo": '''
                # Exemplo de estimativa de máxima verossimilhança para uma distribuição normal
                import numpy as np
                from scipy.stats import norm

                dados = np.array([1.2, 2.3, 2.8, 3.1, 4.0])
                media, desvio_padrao = norm.fit(dados)
                print(f"Média estimada: {media}, Desvio padrão estimado: {desvio_padrao}")
                '''
        },
        "model_accuracy": {
            "significado": "Medida de quão bem um modelo de aprendizado de máquina se ajusta aos dados e faz previsões corretas.",
            "uso": "É utilizado para avaliar o desempenho de um modelo em termos de precisão na classificação ou regressão.",
            "ejemplo": '''
                # Exemplo de cálculo de precisão de um modelo de classificação
                from sklearn.metrics import accuracy_score

                y_real = [0, 1, 1, 1]
                y_predito = [0, 1, 0, 1]
                acuracia = accuracy_score(y_real, y_predito)
                print(f"Precisão do modelo: {acuracia}")  # Saída: 0.75
                '''
        },
        "min": {
            "significado": "Função que retorna o valor mínimo de um conjunto de dados.",
            "uso": "É utilizada para encontrar o menor elemento em uma lista ou conjunto de dados.",
            "ejemplo": '''
                # Exemplo de uso da função min
                numeros = [3, 1, 4, 1, 5, 9, 2]
                print(min(numeros))  # Saída: 1
                '''
        },
        "multiprocessing": {
            "significado": "Técnica de programação que permite executar múltiplos processos simultaneamente para aproveitar melhor os recursos do sistema.",
            "uso": "É utilizada na programação concorrente para executar tarefas de forma paralela e melhorar o desempenho de programas intensivos em processamento.",
            "ejemplo": '''
                import multiprocessing

                def funcao_trabalhador(num):
                    print(f"Processo {num} em execução")

                if __name__ == "__main__":
                    processos = []
                    for i in range(5):
                        p = multiprocessing.Process(target=funcao_trabalhador, args=(i,))
                        processos.append(p)
                        p.start()

                    for p in processos:
                        p.join()
                '''
        },
        "modulus": {
            "significado": "Operação matemática que retorna o resto da divisão de dois números.",
            "uso": "É utilizada para encontrar o resto de uma divisão e em algoritmos de programação para avaliar condições de divisibilidade.",
            "ejemplo": '''
                # Exemplo de uso da operação de módulo
                print(10 % 3)  # Saída: 1
                '''
        },
        "machine_vision": {
            "significado": "Campo da inteligência artificial que permite às máquinas interpretar e compreender imagens e vídeos.",
            "uso": "É utilizado em reconhecimento de imagens, diagnóstico médico, controle de qualidade em manufatura, etc.",
            "ejemplo": '''
                # Exemplo de uso do OpenCV para detectar bordas em uma imagem
                import cv2

                imagem = cv2.imread('imagem.jpg', 0)  # Carregar imagem em escala de cinza
                bordas = cv2.Canny(imagem, 100, 200)
                cv2.imshow('Bordas', bordas)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                '''
        },
        "monoid": {
            "significado": "Estrutura algébrica que consiste em um conjunto e uma operação binária que é associativa e tem um elemento neutro.",
            "uso": "É utilizado em teoria da computação e álgebra abstrata para modelar operações combinadas.",
            "ejemplo": '''
                # Exemplo conceitual de um monóide em programação
                # O conjunto de números inteiros com a operação de soma é um monóide
                '''
        },
        "markov_chain": {
            "significado": "Modelo matemático que descreve um sistema que transita de um estado para outro de acordo com probabilidades de transição que dependem apenas do estado atual.",
            "uso": "É utilizado na simulação de processos estocásticos, previsão de sequências e modelagem de processos de decisão.",
            "ejemplo": '''
                # Exemplo de uso de uma cadeia de Markov para modelar uma sequência de estados
                import numpy as np

                estados = ["Ensolarado", "Chuvoso"]
                matriz_de_transicao = [[0.8, 0.2], [0.4, 0.6]]
                estado_atual = 0  # Índice de 'Ensolarado'
                proximo_estado = np.random.choice([0, 1], p=matriz_de_transicao[estado_atual])
                print(f"Próximo estado: {estados[proximo_estado]}")
                '''
        },
        "mean_squared_error": {
            "significado": "Métrica utilizada para medir a diferença média ao quadrado entre os valores reais e os valores previstos por um modelo.",
            "uso": "É utilizada para avaliar a precisão de um modelo de regressão, penalizando mais os erros grandes.",
            "ejemplo": '''
                from sklearn.metrics import mean_squared_error

                y_real = [1, 2, 3]
                y_predito = [1.1, 2.0, 3.2]
                mse = mean_squared_error(y_real, y_predito)
                print(f"Erro quadrático médio: {mse}")
                '''
        },
        "memory_management": {
            "significado": "Processo de gestão e administração da memória em um sistema operacional para otimizar seu uso e desempenho.",
            "uso": "É utilizado para garantir que os programas utilizem de forma eficiente a memória disponível.",
            "ejemplo": '''
                # Exemplo de técnicas de gestão de memória em Python
                import gc
                gc.collect()  # Coleta objetos não utilizados para liberar memória
                '''
        },
        "matrix_multiplication": {
            "significado": "Operação matemática que toma duas matrizes e produz uma nova matriz multiplicando seus elementos de acordo com uma regra de multiplicação de matrizes.",
            "uso": "É utilizado em álgebra linear, gráficos por computador e no treinamento de modelos de machine learning.",
            "ejemplo": '''
                import numpy as np

                A = np.array([[1, 2], [3, 4]])
                B = np.array([[5, 6], [7, 8]])
                resultado = np.matmul(A, B)
                print(resultado)
                '''
        },
        "minimization": {
            "significado": "Processo de encontrar o valor mínimo de uma função objetivo sob certas condições.",
            "uso": "É utilizado em otimização matemática e algoritmos de machine learning para encontrar a melhor solução ou parâmetro.",
            "ejemplo": '''
                from scipy.optimize import minimize

                def funcao_objetivo(x):
                    return x**2 + 5*x + 6

                resultado = minimize(funcao_objetivo, 0)
                print(resultado.x)  # Mostra o mínimo encontrado
                '''
        },
        "module": {
            "significado": "Unidade de código independente em uma linguagem de programação que agrupa funções, variáveis e classes.",
            "uso": "É utilizado para organizar e reutilizar o código de forma estruturada.",
            "ejemplo": '''
                # Exemplo de uso de um módulo em Python
                # Arquivo: my_module.py
                def cumprimentar():
                    return "Hello, world!"

                # Arquivo principal
                from my_module import cumprimentar
                print(cumprimentar())  # Saída: Hello, world!
                '''
        },
        "mapping": {
            "significado": "Processo de associar elementos de um conjunto com elementos de outro conjunto por meio de uma função ou relação.",
            "uso": "É utilizado em programação para transformar dados ou estruturar informações de forma mais eficiente.",
            "ejemplo": '''
                # Exemplo de uso de mapping em Python
                numeros = [1, 2, 3, 4]
                numeros_ao_quadrado = list(map(lambda x: x**2, numeros))
                print(numeros_ao_quadrado)  # Saída: [1, 4, 9, 16]
                '''
        },
        "monadic": {
            "significado": "Relativo a um monádico, que é uma estrutura usada em programação funcional para lidar com efeitos e encadear operações de forma sequencial.",
            "uso": "É utilizado para estruturar e sequenciar operações em linguagens de programação funcional como Haskell.",
            "ejemplo": '''
                # Exemplo de uso de monada em Haskell para operações com Maybe
                safeDivide :: Float -> Float -> Maybe Float
                safeDivide _ 0 = Nothing
                safeDivide x y = Just (x / y)
                '''
        },
        "mutability": {
            "significado": "Propriedade de um objeto ou variável que permite modificar seu estado ou conteúdo após sua criação.",
            "uso": "É utilizado para descrever o comportamento das estruturas de dados em programação e a gestão de estados.",
            "ejemplo": '''
                # Exemplo de mutabilidade em Python
                lst = [1, 2, 3]
                lst[0] = 10  # Modifica o primeiro elemento da lista
                print(lst)  # Saída: [10, 2, 3]
                '''
        },
        "manipulation": {
            "significado": "Processo de modificar ou controlar elementos de um conjunto de dados ou uma estrutura de forma específica.",
            "uso": "É utilizado na programação para transformar e gerenciar dados de forma eficiente.",
            "ejemplo": '''
                # Exemplo de manipulação de uma string em Python
                texto = "Hello, world!"
                texto_modificado = texto.replace("world", "Python")
                print(texto_modificado)  # Saída: Hello, Python!
                '''
        },
        "masking": {
            "significado": "Processo de ocultar ou restringir dados para proteger informações sensíveis ou para modificar a visibilidade de elementos.",
            "uso": "É utilizado em programação e processamento de imagens para filtrar ou modificar a aparência dos dados.",
            "ejemplo": '''
                # Exemplo de uso de masking em processamento de imagens com OpenCV
                import cv2
                import numpy as np

                imagem = cv2.imread('imagem.jpg')
                mascara = np.zeros(imagem.shape[:2], dtype=np.uint8)
                cv2.circle(mascara, (100, 100), 50, 255, -1)
                imagem_mascarada = cv2.bitwise_and(imagem, imagem, mask=mascara)
                cv2.imshow('Imagem Mascarada', imagem_mascarada)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                '''
        },
        "multidimensional_array": {
            "significado": "Estrutura de dados que permite armazenar elementos em mais de uma dimensão, como matrizes ou tensores.",
            "uso": "É utilizado em álgebra linear, ciência de dados e processamento de imagens para representar e manipular dados complexos.",
            "ejemplo": '''
                # Exemplo de uso de arrays multidimensionais com NumPy
                import numpy as np

                array_2d = np.array([[1, 2, 3], [4, 5, 6]])
                print(array_2d.shape)  # Saída: (2, 3)
                '''
        },
        "merge_sort": {
            "significado": "Algoritmo de ordenação eficiente baseado na técnica de dividir e conquistar que divide a lista em sublistas, as ordena e as combina.",
            "uso": "É utilizado para ordenar grandes volumes de dados de forma eficiente e estável.",
            "ejemplo": '''
                # Exemplo de implementação de Merge Sort em Python
                def merge_sort(arr):
                    if len(arr) > 1:
                        mid = len(arr) // 2
                        left_half = arr[:mid]
                        right_half = arr[mid:]

                        merge_sort(left_half)
                        merge_sort(right_half)

                        i = j = k = 0
                        while i < len(left_half) and j < len(right_half):
                            if left_half[i] < right_half[j]:
                                arr[k] = left_half[i]
                                i += 1
                            else:
                                arr[k] = right_half[j]
                                j += 1
                            k += 1

                        while i < len(left_half):
                            arr[k] = left_half[i]
                            i += 1
                            k += 1

                        while j < len(right_half):
                            arr[k] = right_half[j]
                            j += 1
                            k += 1

                arr = [5, 2, 4, 1, 3]
                merge_sort(arr)
                print(arr)  # Saída: [1, 2, 3, 4, 5]
                '''
        },
        "mapreduce": {
            "significado": "Modelo de programação para o processamento e geração de grandes conjuntos de dados que são divididos em tarefas menores e processados em paralelo.",
            "uso": "É utilizado em sistemas distribuídos para processar e analisar grandes volumes de dados de forma eficiente.",
            "ejemplo": '''
                # Exemplo de MapReduce com Python
                from functools import reduce

                data = [1, 2, 3, 4, 5]
                mapped_data = list(map(lambda x: x * 2, data))
                reduced_data = reduce(lambda x, y: x + y, mapped_data)
                print(reduced_data)  # Saída: 30
                '''
        },
        "monad": {
            "significado": "Abstração em programação funcional que permite encadear operações e lidar com efeitos colaterais de forma modular.",
            "uso": "É utilizado para estruturar código e controlar efeitos colaterais em linguagens funcionais como Haskell.",
            "ejemplo": '''
                # Exemplo conceitual de uso de monada em Haskell
                import Control.Monad

                main = do
                    putStrLn "Introduza um número:"
                    num <- readLn
                    putStrLn $ "O dobro é: " ++ show (num * 2)
                '''
        },
        "method_overloading": {
            "significado": "Capacidade de uma classe para definir múltiplos métodos com o mesmo nome, mas com parâmetros diferentes.",
            "uso": "É utilizado para criar métodos que realizam a mesma operação de forma generalizada com diferentes tipos de argumentos.",
            "ejemplo": '''
                # Exemplo de sobrecarga de métodos em Python (com a ajuda de @overload)
                from typing import overload

                class Printer:
                    @overload
                    def print_message(self, message: str) -> None:
                        pass

                    @overload
                    def print_message(self, message: int) -> None:
                        pass

                    def print_message(self, message):
                        print(message)

                p = Printer()
                p.print_message("Olá, mundo!")
                p.print_message(123)
                '''
        },
        "mutable": {
            "significado": "Propriedade de um objeto que permite que seu conteúdo ou estado seja modificado após sua criação.",
            "uso": "É utilizado para descrever o comportamento de estruturas de dados que podem mudar, como listas e dicionários em Python.",
            "ejemplo": '''
                # Exemplo de mutabilidade em Python
                data = [1, 2, 3]
                data.append(4)  # Modifica o conteúdo da lista
                print(data)  # Saída: [1, 2, 3, 4]
                '''
        },
        "multithreaded": {
            "significado": "Descrever um programa ou sistema que pode executar múltiplas threads ou processos de forma concorrente.",
            "uso": "É utilizado para executar tarefas simultaneamente e melhorar o desempenho de programas que requerem processamento paralelo.",
            "ejemplo": '''
                # Exemplo de programação multithreaded em Python com threading
                import threading

                def print_hello():
                    for _ in range(5):
                        print("Hello from thread")

                thread = threading.Thread(target=print_hello)
                thread.start()
                thread.join()
                '''
        },
        "max_heap": {
            "significado": "Estrutura de dados do tipo heap onde o elemento máximo está na raiz e cada nó é maior ou igual aos seus nós filhos.",
            "uso": "É utilizado para implementar filas de prioridade e algoritmos de seleção de elementos máximos.",
            "ejemplo": '''
                # Exemplo de uso de um max-heap em Python com heapq (requer inversão de valores)
                import heapq

                max_heap = []
                heapq.heappush(max_heap, -10)  # Inverter valor para usar min-heap como max-heap
                heapq.heappush(max_heap, -20)
                heapq.heappush(max_heap, -5)

                print(-heapq.heappop(max_heap))  # Saída: 20
                '''
        },
        "min_heap": {
            "significado": "Estrutura de dados do tipo heap onde o elemento mínimo está na raiz e cada nó é menor ou igual aos seus nós filhos.",
            "uso": "É utilizado para manter um conjunto de elementos onde o mínimo pode ser extraído rapidamente.",
            "ejemplo": '''
                # Exemplo de uso de um min-heap em Python com heapq
                import heapq

                min_heap = [5, 3, 7, 1, 9]
                heapq.heapify(min_heap)
                heapq.heappush(min_heap, 2)
                print(heapq.heappop(min_heap))  # Saída: 1
                '''
        },
        "method": {
            "significado": "Função ou procedimento definido em uma classe que realiza uma operação específica.",
            "uso": "É utilizado para definir comportamentos de objetos na programação orientada a objetos.",
            "ejemplo": '''
                class Calculator:
                    def add(self, a, b):
                        return a + b

                calc = Calculator()
                print(calc.add(5, 3))  # Saída: 8
                '''
        },
        "monoid": {
            "significado": "Estrutura algébrica que possui uma operação binária associativa e um elemento neutro que não afeta o resultado da operação.",
            "uso": "É utilizado em programação funcional para modelar operações e estruturas como concatenação de cadeias de caracteres e soma de números.",
            "ejemplo": '''
                # Exemplo de monoid em Python com concatenação de strings
                from functools import reduce

                strings = ["Hello", " ", "World"]
                result = reduce(lambda x, y: x + y, strings)
                print(result)  # Saída: Hello World
                '''
        },
        "memory_management_unit": {
            "significado": "Componente de hardware que gerencia a memória de um sistema, coordenando a transferência de dados entre a memória principal e outros dispositivos.",
            "uso": "É utilizado para garantir o acesso eficiente e seguro à memória em sistemas computacionais.",
            "ejemplo": '''
                # Exemplo conceitual da função de uma MMU em sistemas operacionais
                # A MMU mapeia endereços de memória virtual para endereços físicos na RAM.
                '''
        },
        "mvp": {
            "significado": "Modelo de design de software que separa a lógica de apresentação, a lógica de negócios e a entrada do usuário para promover a prova e a manutenção de aplicações.",
            "uso": "É utilizado no desenvolvimento de aplicações para melhorar a separação de responsabilidades e facilitar a prova e a escalabilidade.",
            "ejemplo": '''
                # Exemplo de estrutura MVP em uma aplicação de Python
                class Model:
                    def get_data(self):
                        return "Data from Model"

                class View:
                    def display(self, data):
                        print(f"Displaying: {data}")

                class Presenter:
                    def __init__(self, model, view):
                        self.model = model
                        self.view = view

                    def update_view(self):
                        data = self.model.get_data()
                        self.view.display(data)

                model = Model()
                view = View()
                presenter = Presenter(model, view)
                presenter.update_view()  # Saída: Displaying: Data from Model
                '''
        },
        "markup_language": {
            "significado": "Linguagem de programação usada para definir a estrutura e apresentação de texto na web, geralmente por meio de tags.",
            "uso": "É utilizado para construir e apresentar documentos com formatação na web.",
            "ejemplo": '''
                # Exemplo de uso de uma linguagem de marcação (HTML)
                <!DOCTYPE html>
                <html>
                <head>
                    <title>My Page</title>
                </head>
                <body>
                    <h1>Hello, World!</h1>
                    <p>This is a paragraph.</p>
                </body>
                </html>
                '''
        },
        "monolithic": {
            "significado": "Arquitetura de software na qual todos os componentes do aplicativo estão integrados em um único bloco ou programa.",
            "uso": "É utilizado para descrever aplicativos que não têm separação de serviços e podem ser difíceis de escalar ou manter.",
            "ejemplo": '''
                # Exemplo conceitual de um aplicativo monolítico em Python
                # Um aplicativo de software onde a lógica de apresentação, negócios e acesso a dados estão em um único arquivo.
                '''
        },
        "memory_block": {
            "significado": "Unidade de armazenamento em memória que é alocada para armazenar dados ou programas.",
            "uso": "É utilizado em programação para gerenciar e manipular segmentos de memória no sistema.",
            "ejemplo": '''
                # Exemplo de uso de blocos de memória em programação C
                # Alocação de um bloco de memória de 100 bytes
                char *block = (char *)malloc(100 * sizeof(char));
                free(block);
                '''
        },
        "multimodal": {
            "significado": "Em tecnologia, refere-se a sistemas ou aplicações que usam múltiplas formas de interação ou entrada/saída de dados.",
            "uso": "É utilizado em interfaces de usuário avançadas e sistemas de inteligência artificial para permitir múltiplas formas de interação.",
            "ejemplo": '''
                # Exemplo conceitual de um sistema multimodal
                # Um assistente virtual que pode responder a comandos de voz e texto
                '''
        },
        "message_queue": {
            "significado": "Estrutura de dados ou sistema que permite a comunicação entre diferentes partes de um sistema por meio do envio e recebimento de mensagens.",
            "uso": "É utilizado em sistemas distribuídos para desacoplar processos e facilitar a comunicação assíncrona.",
            "ejemplo": '''
                # Exemplo de uso de uma fila de mensagens em Python com a biblioteca `queue`
                import queue

                message_queue = queue.Queue()
                message_queue.put("Mensagem 1")
                message_queue.put("Mensagem 2")
                print(message_queue.get())  # Saída: Mensagem 1
                '''
        },
        "mse": {
            "significado": "Erro quadrático médio, uma medida de precisão que calcula a média dos erros ao quadrado entre os valores previstos e os reais.",
            "uso": "É utilizado em estatística e aprendizado de máquina para avaliar a precisão de modelos de previsão.",
            "ejemplo": '''
                # Exemplo de cálculo de MSE em Python
                from sklearn.metrics import mean_squared_error

                y_true = [1, 2, 3, 4, 5]
                y_pred = [1.1, 2.1, 3.1, 4.1, 5.1]
                mse = mean_squared_error(y_true, y_pred)
                print(mse)  # Saída: 0.01
                '''
        },
        "mean_absolute_error": {
            "significado": "Erro absoluto médio, uma medida de precisão que calcula a média dos erros absolutos entre os valores previstos e os reais.",
            "uso": "É utilizado para avaliar a precisão de um modelo de previsão e entender a magnitude média dos erros.",
            "ejemplo": '''
                # Exemplo de cálculo de MAE em Python
                from sklearn.metrics import mean_absolute_error

                y_true = [1, 2, 3, 4, 5]
                y_pred = [1.1, 2.1, 3.1, 4.1, 5.1]
                mae = mean_absolute_error(y_true, y_pred)
                print(mae)  # Saída: 0.1
                '''
        },
        "matrix_factorization": {
            "significado": "Técnica matemática usada para decompor uma matriz em produtos de matrizes menores, geralmente em contextos de análise de dados e sistemas de recomendação.",
            "uso": "É utilizado para reduzir a dimensionalidade de dados, descobrir padrões latentes e fazer recomendações personalizadas.",
            "ejemplo": '''
                # Exemplo de uso de matrix factorization com a biblioteca `scikit-learn` em Python
                from sklearn.decomposition import NMF
                import numpy as np

                data = np.array([[3, 4, 3], [2, 3, 4], [4, 5, 3]])
                model = NMF(n_components=2, init='random', random_state=0)
                W = model.fit_transform(data)
                H = model.components_
                print(W)
                print(H)
                '''
        },
        "multiprocessing": {
            "significado": "Técnica de programação que permite a execução simultânea de processos para aproveitar múltiplos núcleos da CPU e melhorar a eficiência dos programas.",
            "uso": "É utilizado para paralelizar tarefas e melhorar o desempenho de aplicações em Python e outras linguagens.",
            "ejemplo": '''
                # Exemplo de uso de multiprocessing em Python
                from multiprocessing import Process

                def print_hello():
                    print("Hello from process!")

                if __name__ == '__main__':
                    p = Process(target=print_hello)
                    p.start()
                    p.join()
                '''
        },
        "maximum_likelihood_estimation": {
            "significado": "Método estatístico para estimar os parâmetros de um modelo que maximiza a probabilidade dos dados observados.",
            "uso": "É utilizado em modelos de inferência estatística para encontrar os melhores parâmetros que explicam os dados.",
            "ejemplo": '''
                # Exemplo conceitual de MLE em Python para uma distribuição normal
                import numpy as np
                from scipy.stats import norm

                data = np.array([1.5, 2.3, 2.8, 3.1, 3.7])
                mean, var = norm.fit(data)
                print(f"Média: {mean}, Variância: {var}")
                '''
        },
        "minimum_spanning_tree": {
            "significado": "Árvore de um grafo que conecta todos os nós com a mínima soma de pesos de suas arestas e sem ciclos.",
            "uso": "É utilizado em algoritmos de redes e otimização para encontrar a forma mais eficiente de conectar um conjunto de pontos.",
            "ejemplo": '''
                # Exemplo de uso de um algoritmo de árvore de expansão mínima (Prim) em Python
                import networkx as nx

                G = nx.Graph()
                G.add_weighted_edges_from([(1, 2, 1), (1, 3, 3), (2, 3, 2), (3, 4, 4), (2, 4, 5)])
                mst = nx.minimum_spanning_tree(G)
                print(mst.edges(data=True))
                '''
        },
        "markup": {
            "significado": "Linguagem de programação que utiliza tags para definir a estrutura e apresentação de conteúdo, como HTML ou XML.",
            "uso": "É utilizado no desenvolvimento de conteúdo web e na organização de dados estruturados.",
            "ejemplo": '''
                # Exemplo de uso de HTML como linguagem de marcação
                <div>
                    <h1>Welcome to My Page</h1>
                    <p>This is a paragraph in a markup language.</p>
                </div>
                '''
        },
        "median": {
            "significado": "Valor central em um conjunto de dados ordenados, que divide o conjunto em duas metades iguais.",
            "uso": "É utilizado como uma medida de tendência central para representar o valor médio de um conjunto de dados, especialmente quando há valores atípicos.",
            "ejemplo": '''
                # Exemplo de cálculo da mediana em Python
                import numpy as np

                data = [1, 3, 2, 5, 4]
                median = np.median(data)
                print(median)  # Saída: 3
                '''
        },
        "modular_programming": {
            "significado": "Abordagem de desenvolvimento de software na qual o código é dividido em módulos independentes e reutilizáveis.",
            "uso": "É utilizado para organizar o código em partes mais gerenciáveis e facilitar sua manutenção e escalabilidade.",
            "ejemplo": '''
                # Exemplo de programação modular em Python
                # Arquivo modulo.py
                def greet(name):
                    return f"Hello, {name}!"

                # Arquivo main.py
                from modulo import greet
                print(greet("World"))  # Saída: Hello, World!
                '''
        },
        "model_training": {
            "significado": "Processo de ensinar um modelo de machine learning a reconhecer padrões a partir de um conjunto de dados de treinamento.",
            "uso": "É utilizado no desenvolvimento de modelos de aprendizado de máquina para fazer previsões ou classificações com base em dados.",
            "ejemplo": '''
                # Exemplo de treinamento de um modelo de regressão linear em Python
                from sklearn.model_selection import train_test_split
                from sklearn.linear_model import LinearRegression
                import numpy as np

                X = np.array([[1], [2], [3], [4], [5]])
                y = np.array([2, 4, 6, 8, 10])
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

                model = LinearRegression()
                model.fit(X_train, y_train)
                print(model.predict([[6]]))  # Saída: [12.]
                '''
        },
        "monitor": {
            "significado": "Dispositivo ou componente de software que supervisiona e exibe o estado de um sistema ou processo.",
            "uso": "É utilizado para rastrear o desempenho e a atividade de sistemas ou aplicações.",
            "ejemplo": '''
                # Exemplo de uso de um monitor de CPU em Python com psutil
                import psutil

                cpu_usage = psutil.cpu_percent(interval=1)
                print(f"Uso da CPU: {cpu_usage}%")
                '''
        },
        "memory_leak": {
            "significado": "Problema de programação onde uma aplicação não libera a memória que já não precisa, o que pode levar a uma falta de recursos e um desempenho lento.",
            "uso": "É utilizado para descrever um erro de programação que deve ser resolvido para manter a eficiência de uma aplicação.",
            "ejemplo": '''
                # Exemplo conceitual de um vazamento de memória em Python
                # Manter uma referência a objetos que já não são necessários pode causar vazamentos de memória.
                memory_leak_list = []
                while True:
                    memory_leak_list.append([1] * 10**6)  # Simula um vazamento de memória
                '''
        },
        "markov_chain": {
            "significado": "Modelo matemático que descreve um processo estocástico em que o próximo estado depende apenas do estado atual.",
            "uso": "É utilizado em modelos preditivos, como a previsão de sequências de texto, processos de decisão e sistemas de recomendação.",
            "ejemplo": '''
                # Exemplo de uma cadeia de Markov simples em Python
                import random

                states = ['Rain', 'Sunny']
                transitions = {
                    'Rain': {'Rain': 0.7, 'Sunny': 0.3},
                    'Sunny': {'Rain': 0.4, 'Sunny': 0.6}
                }

                current_state = 'Rain'
                next_state = 'Sunny' if random.random() < transitions[current_state]['Sunny'] else 'Rain'
                print(f"Próximo estado: {next_state}")
                '''
        },
    },
    "n": {
        # Aquí puedes agregar funciones que comiencen con la letra N
        "Neural_network": {
            "significado": "Modelo de computação inspirado na estrutura e função do cérebro humano, composto por nós interconectados (neurônios) que podem aprender padrões complexos.",
            "uso": "É utilizado em aprendizado de máquina e inteligência artificial para resolver problemas de classificação, reconhecimento de padrões, previsão e mais.",
            "ejemplo": '''
                # Exemplo de uma rede neural simples com `TensorFlow` em Python
                import tensorflow as tf
                from tensorflow.keras import layers

                model = tf.keras.Sequential([
                    layers.Dense(10, activation='relu', input_shape=(8,)),
                    layers.Dense(1, activation='sigmoid')
                ])
                model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
                '''
        },
        "Naive_bayes": {
            "significado": "Classificador probabilístico baseado no teorema de Bayes com a suposição de independência entre as características.",
            "uso": "É usado para problemas de classificação, como a classificação de e-mails como spam ou não spam.",
            "ejemplo": '''
                # Exemplo de uso de um classificador Naive Bayes com `scikit-learn` em Python
                from sklearn.naive_bayes import GaussianNB
                from sklearn.model_selection import train_test_split
                from sklearn.metrics import accuracy_score

                X = [[1, 2], [1, 3], [2, 3], [3, 4]]
                y = [0, 0, 1, 1]
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

                model = GaussianNB()
                model.fit(X_train, y_train)
                predictions = model.predict(X_test)
                print(accuracy_score(y_test, predictions))
                '''
        },
        "Numpy": {
            "significado": "Biblioteca Python que oferece suporte para matrizes multidimensionais e funções matemáticas de alto nível.",
            "uso": "É utilizado para realizar cálculos numéricos e operações em grandes conjuntos de dados de forma eficiente.",
            "ejemplo": '''
                # Exemplo de uso do NumPy para operações com matrizes
                import numpy as np

                a = np.array([1, 2, 3])
                b = np.array([4, 5, 6])
                sum_ab = a + b
                print(sum_ab)  # Saída: [5 7 9]
                '''
        },
        "Node": {
            "significado": "Elemento fundamental de estruturas de dados como listas encadeadas e árvores, que pode conter dados e referências a outros nós.",
            "uso": "É usado na implementação de estruturas de dados e algoritmos como grafos, listas encadeadas e árvores.",
            "ejemplo": '''
                # Exemplo de implementação de um nó em uma lista encadeada em Python
                class Node:
                    def __init__(self, value):
                        self.value = value
                        self.next = None

                node1 = Node(10)
                node2 = Node(20)
                node1.next = node2
                print(node1.next.value)  # Saída: 20
                '''
        },
        "Nms": {
            "significado": "Siglas de 'Non-Maximum Suppression', um algoritmo usado em visão computacional para filtrar detecções de objetos que se sobrepõem demais.",
            "uso": "É usado na detecção de objetos para eliminar as detecções redundantes e conservar apenas a melhor.",
            "ejemplo": '''
                # Exemplo conceitual de Non-Maximum Suppression em Python
                import numpy as np

                boxes = np.array([[10, 20, 50, 60], [12, 22, 48, 58], [30, 40, 70, 80]])
                scores = np.array([0.9, 0.85, 0.6])

                def non_max_suppression(boxes, scores, threshold=0.5):
                    # Implementação simplificada de NMS (conceitual)
                    indices = np.argsort(scores)[::-1]
                    selected = []
                    while indices.size > 0:
                        idx = indices[0]
                        selected.append(idx)
                        ious = [iou(boxes[idx], boxes[i]) for i in indices[1:]]
                        indices = indices[1:][np.array(ious) < threshold]
                    return selected

                def iou(box1, box2):
                    # Cálculo de Intersection over Union (IoU)
                    x1, y1, x2, y2 = box1
                    x3, y3, x4, y4 = box2
                    inter_area = max(0, min(x2, x4) - max(x1, x3)) * max(0, min(y2, y4) - max(y1, y3))
                    box1_area = (x2 - x1) * (y2 - y1)
                    box2_area = (x4 - x3) * (y4 - y3)
                    union_area = box1_area + box2_area - inter_area
                    return inter_area / union_area

                selected_indices = non_max_suppression(boxes, scores)
                print(selected_indices)
                '''
        },
        "Nearest_neighbor": {
            "significado": "Algoritmo de busca que encontra o ponto de dados mais próximo em um conjunto de dados com base em uma métrica de distância.",
            "uso": "É utilizado em classificação, regressão e problemas de recomendação.",
            "ejemplo": '''
                # Exemplo de uso de um classificador de vizinho mais próximo com `scikit-learn` em Python
                from sklearn.neighbors import KNeighborsClassifier
                from sklearn.model_selection import train_test_split

                X = [[1, 2], [2, 3], [3, 4], [4, 5]]
                y = [0, 1, 1, 0]
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

                model = KNeighborsClassifier(n_neighbors=3)
                model.fit(X_train, y_train)
                prediction = model.predict([[2, 3]])
                print(prediction)  # Saída: [1]
                '''
        },
        "Network_topology": {
            "significado": "Estrutura de interconexão de elementos em uma rede, como nós e links, que define como os dados são transmitidos.",
            "uso": "É utilizado para projetar e analisar redes de computadores e outros sistemas de comunicação.",
            "ejemplo": '''
                # Exemplo de representação de uma topologia de rede em Python
                import networkx as nx

                G = nx.Graph()
                G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1), (2, 4)])
                nx.draw(G, with_labels=True)
                '''
        },
        "Normalization": {
            "significado": "Processo de escalonar os valores de um conjunto de dados para que estejam dentro de um intervalo específico, como [0, 1] ou [-1, 1].",
            "uso": "É utilizado para melhorar a convergência de algoritmos de aprendizado de máquina e tornar comparáveis características de diferentes escalas.",
            "ejemplo": '''
                # Exemplo de normalização de dados em Python usando `scikit-learn`
                from sklearn.preprocessing import MinMaxScaler
                import numpy as np

                data = np.array([[1, 2], [3, 4], [5, 6]])
                scaler = MinMaxScaler()
                normalized_data = scaler.fit_transform(data)
                print(normalized_data)
                '''
        },
        "Naive_bayes_classifier": {
            "significado": "Classificador baseado no teorema de Bayes com a suposição de independência entre as características, otimizado para a classificação de dados.",
            "uso": "É utilizado na classificação de texto, detecção de spam e análise de sentimentos.",
            "ejemplo": '''
                # Exemplo de uso de um classificador Naive Bayes para texto em Python
                from sklearn.feature_extraction.text import CountVectorizer
                from sklearn.naive_bayes import MultinomialNB

                documents = ["spam message", "normal message", "another spam"]
                labels = [1, 0, 1]

                vectorizer = CountVectorizer()
                X = vectorizer.fit_transform(documents)
                model = MultinomialNB()
                model.fit(X, labels)
                new_doc = vectorizer.transform(["new message"])
                print(model.predict(new_doc))
                '''
        },
        "Newton_raphson_method": {
            "significado": "Método iterativo de solução numérica para encontrar raízes de uma função.",
            "uso": "É utilizado na resolução de equações não lineares e problemas de otimização.",
            "ejemplo": '''
                # Exemplo de método de Newton-Raphson em Python
                def newton_raphson(f, df, x0, tol=1e-5, max_iter=100):
                    x = x0
                    for i in range(max_iter):
                        x_new = x - f(x) / df(x)
                        if abs(x_new - x) < tol:
                            return x_new
                        x = x_new
                    raise ValueError("Não converge")

                f = lambda x: x**2 - 2  # Exemplo de função f(x) = x^2 - 2
                df = lambda x: 2*x  # Derivada f'(x) = 2x

                root = newton_raphson(f, df, x0=1)
                print(root)  # Saída: Raiz da função
                '''
        },
        "Named_entity_recognition": {
            "significado": "Tarefa de processamento de linguagem natural que identifica e classifica entidades mencionadas em um texto, como nomes de pessoas, organizações e localizações.",
            "uso": "É utilizado em sistemas de análise de texto, chatbots e mineração de dados.",
            "ejemplo": '''
                # Exemplo de uso de NER com `spaCy` em Python
                import spacy

                nlp = spacy.load('en_core_web_sm')
                text = "O presidente dos Estados Unidos, Joe Biden, visitou Nova York."
                doc = nlp(text)
                for ent in doc.ents:
                    print(ent.text, ent.label_)
                '''
        },
        "Neuron": {
            "significado": "Célula do sistema nervoso que transmite informações na forma de impulsos elétricos e químicos.",
            "uso": "É utilizado no contexto de redes neurais artificiais e na biologia para entender como os sinais são transmitidos no cérebro.",
            "ejemplo": '''
                # Exemplo de representação de um neurônio em uma rede neural simples
                import numpy as np

                class Neuron:
                    def __init__(self, input_size):
                        self.weights = np.random.randn(input_size)
                        self.bias = np.random.randn()

                    def activate(self, inputs):
                        return np.dot(inputs, self.weights) + self.bias

                neuron = Neuron(input_size=3)
                print(neuron.activate([1, 2, 3]))
                '''
        },
        "Node_classification": {
            "significado": "Tarefa de aprendizado de máquina na qual se atribui uma etiqueta a cada nó de um grafo com base nas características dos nós e sua conectividade.",
            "uso": "É utilizado em redes sociais, análise de grafos e recomendações de produtos.",
            "ejemplo": '''
                # Exemplo de classificação de nós em um grafo com `networkx` em Python
                import networkx as nx
                import numpy as np
                from sklearn.preprocessing import LabelEncoder

                G = nx.karate_club_graph()  # Grafo de exemplo da rede de karate
                labels = [1 if node < 10 else 0 for node in G.nodes()]
                label_encoder = LabelEncoder()
                encoded_labels = label_encoder.fit_transform(labels)

                # Exemplo de como treinar um modelo de classificação de nós
                from sklearn.model_selection import train_test_split
                X = np.array([list(G.neighbors(node)) for node in G.nodes()])
                y = encoded_labels
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
                '''
        },
        "Natural_language_processing": {
            "significado": "Campo da inteligência artificial que foca na interação entre computadores e a linguagem humana.",
            "uso": "É utilizado em tradução automática, análise de sentimentos, chatbots e assistentes virtuais.",
            "ejemplo": '''
                # Exemplo de processamento de linguagem natural com `spaCy` em Python
                import spacy

                nlp = spacy.load('en_core_web_sm')
                text = "O processamento de linguagem natural é um campo empolgante."
                doc = nlp(text)

                for token in doc:
                    print(token.text, token.pos_, token.dep_)
                '''
        },
        "Nearest_neighbors_algorithm": {
            "significado": "Algoritmo de busca que encontra os pontos de dados mais próximos em um conjunto de dados utilizando uma métrica de distância, como a distância euclidiana.",
            "uso": "É utilizado em classificação, regressão e sistemas de recomendação.",
            "ejemplo": '''
                # Exemplo de uso do algoritmo de vizinhos mais próximos com `scikit-learn` em Python
                from sklearn.neighbors import NearestNeighbors
                import numpy as np

                data = np.array([[1, 2], [3, 4], [5, 6]])
                model = NearestNeighbors(n_neighbors=2)
                model.fit(data)
                distances, indices = model.kneighbors([[3, 3]])
                print("Distâncias:", distances)
                print("Índices:", indices)
                '''
        },
        "Null_hypothesis": {
            "significado": "Hipótese estatística que sugere que não há efeito ou relação em um experimento e é usada como ponto de partida para testes estatísticos.",
            "uso": "É usada em testes de hipóteses para determinar se há evidências suficientes para rejeitar uma afirmação de ausência de efeito.",
            "ejemplo": '''
                # Exemplo de teste de hipótese com `scipy` em Python
                from scipy import stats

                data1 = [23, 21, 22, 24, 25]
                data2 = [30, 31, 29, 30, 32]

                t_stat, p_value = stats.ttest_ind(data1, data2)
                if p_value < 0.05:
                    print("Rejeitamos a hipótese nula")
                else:
                    print("Não há evidências suficientes para rejeitar a hipótese nula")
                '''
        },
        "Neural_network_training": {
            "significado": "Processo de otimização dos pesos e vieses de uma rede neural para minimizar a função de perda em um conjunto de dados.",
            "uso": "É usado na criação de modelos de aprendizado profundo para resolver tarefas como classificação, regressão e reconhecimento de padrões.",
            "ejemplo": '''
                # Exemplo de treinamento de uma rede neural com `TensorFlow` em Python
                import tensorflow as tf
                from tensorflow.keras import layers

                model = tf.keras.Sequential([
                    layers.Dense(10, activation='relu', input_shape=(8,)),
                    layers.Dense(1, activation='sigmoid')
                ])
                model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

                # Simulação de dados de treinamento
                X_train = np.random.rand(100, 8)
                y_train = np.random.randint(0, 2, 100)

                model.fit(X_train, y_train, epochs=10, batch_size=32)
                '''
        },
        "Norm": {
            "significado": "Valor que indica a magnitude de um vetor em um espaço vetorial, usado na normalização e análise de dados.",
            "uso": "É usado em álgebra linear e estatísticas para medir o comprimento de um vetor e em algoritmos de aprendizado de máquina para normalizar dados.",
            "ejemplo": '''
                # Exemplo de cálculo da norma de um vetor com `numpy` em Python
                import numpy as np

                vector = np.array([3, 4])
                norm = np.linalg.norm(vector)
                print(norm)  # Saída: 5.0 (norma euclidiana)
                '''
        },
        "Natural_gradient": {
            "significado": "Técnica de otimização que utiliza a matriz de Fisher para ajustar os parâmetros de um modelo de forma mais eficiente em comparação com o gradiente padrão.",
            "uso": "É usado em modelos de aprendizado profundo e redes neurais para melhorar a convergência e a estabilidade no treinamento.",
            "ejemplo": '''
                # Exemplo de cálculo do gradiente natural (conceitual)
                import numpy as np

                def natural_gradient(X, y, theta):
                    # Cálculo do gradiente natural, pode incluir operações específicas
                    pass
                '''
        },
        "Negative_log_likelihood": {
            "significado": "Função de perda comumente usada em modelos de classificação e regressão para estimar a probabilidade de observações dadas um conjunto de parâmetros.",
            "uso": "É usada na otimização de modelos estatísticos e de aprendizado de máquina, especialmente em modelos de classificação como redes neurais.",
            "ejemplo": '''
                # Exemplo de implementação da função de perda de log-verossimilhança negativa em Python
                import numpy as np

                def negative_log_likelihood(y_true, y_pred):
                    return -np.sum(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))

                y_true = np.array([1, 0, 1])
                y_pred = np.array([0.8, 0.2, 0.9])
                loss = negative_log_likelihood(y_true, y_pred)
                print(loss)
                '''
        },
        "Nearest_neighbor_search": {
            "significado": "Método de busca que encontra o ponto mais próximo a um ponto de consulta em um conjunto de dados, geralmente usado na busca de padrões e em sistemas de recomendação.",
            "uso": "É usado na busca de imagens semelhantes, recomendações de produtos e motores de busca.",
            "ejemplo": '''
                # Exemplo de busca de vizinho mais próximo com `scikit-learn` em Python
                from sklearn.neighbors import NearestNeighbors
                import numpy as np

                data = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
                model = NearestNeighbors(n_neighbors=2)
                model.fit(data)
                query_point = np.array([[4, 5]])
                distances, indices = model.kneighbors(query_point)
                print("Distâncias:", distances)
                print("Índices:", indices)
                '''
        },
        "Neural_network_model": {
            "significado": "Modelo de inteligência artificial composto por camadas de neurônios interconectados usados para realizar tarefas de aprendizado profundo.",
            "uso": "É usado para resolver problemas complexos como classificação de imagens, reconhecimento de voz e processamento de linguagem natural.",
            "ejemplo": '''
                # Exemplo de criação de um modelo de rede neural com `TensorFlow` em Python
                import tensorflow as tf
                from tensorflow.keras import Sequential
                from tensorflow.keras.layers import Dense

                model = Sequential([
                    Dense(64, activation='relu', input_shape=(10,)),
                    Dense(10, activation='softmax')
                ])
                model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
                '''
        },
        "Natural_language_understanding": {
            "significado": "Subcampo do processamento de linguagem natural (NLP) que se concentra na compreensão e interpretação do significado dos textos.",
            "uso": "É usado em chatbots, assistentes virtuais, análise de sentimentos e sistemas de tradução automática.",
            "ejemplo": '''
                # Exemplo de uso de processamento de linguagem natural com `spaCy` em Python
                import spacy

                nlp = spacy.load('en_core_web_sm')
                text = "Natural language understanding is a complex field of study."
                doc = nlp(text)

                for ent in doc.ents:
                    print(ent.text, ent.label_)
                '''
        },
        "Naive_bayes_theorem": {
            "significado": "Teorema de probabilidade que descreve a probabilidade de um evento dado um conjunto de características, sob a suposição de independência condicional.",
            "uso": "É usado na classificação de textos, como na detecção de spam em e-mails ou classificação de opiniões.",
            "ejemplo": '''
                # Exemplo de classificação com o teorema de Bayes usando `scikit-learn` em Python
                from sklearn.naive_bayes import GaussianNB
                import numpy as np

                X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
                y = np.array([0, 1, 0, 1])
                model = GaussianNB()
                model.fit(X, y)
                predictions = model.predict([[3, 4]])
                print(predictions)
                '''
        },
        "Non_linear_regression": {
            "significado": "Tipo de análise de regressão usada para modelar a relação entre variáveis por meio de funções não lineares.",
            "uso": "É usado em problemas onde a relação entre a variável independente e a dependente não segue uma linha reta, como em modelos de crescimento populacional.",
            "ejemplo": '''
                # Exemplo de regressão não linear usando `scipy` em Python
                from scipy.optimize import curve_fit
                import numpy as np

                def func(x, a, b, c):
                    return a * np.exp(b * x) + c

                x = np.array([1, 2, 3, 4, 5])
                y = np.array([2.7, 7.4, 15.8, 29.4, 52.2])

                popt, pcov = curve_fit(func, x, y)
                print("Parâmetros ótimos:", popt)
                '''
        },
        "Neural_network_layer": {
            "significado": "Componente de uma rede neural que contém um conjunto de nós (ou neurônios) e realiza transformações matemáticas nas entradas.",
            "uso": "É usado para criar redes neuronais profundas e definir a arquitetura de um modelo de aprendizado profundo.",
            "ejemplo": '''
                # Exemplo de uma camada de rede neural em `Keras`
                from tensorflow.keras import layers

                layer = layers.Dense(64, activation='relu', input_shape=(10,))
                print(layer)
                '''
        },
        "Numeric_integration": {
            "significado": "Método numérico usado para calcular a integral de uma função em um intervalo dado, especialmente quando não é possível integrar analiticamente.",
            "uso": "É usado em simulações científicas, processamento de sinais e análise de dados.",
            "ejemplo": '''
                # Exemplo de integração numérica com `scipy` em Python
                from scipy.integrate import quad
                import numpy as np

                def f(x):
                    return x**2

                result, error = quad(f, 0, 1)
                print("Resultado da integral:", result)
                '''
        },
        "Network_security": {
            "significado": "Práticas e tecnologias implementadas para proteger redes de computadores contra acessos não autorizados, ataques e danos.",
            "uso": "É usado para proteger a confidencialidade, integridade e disponibilidade de dados e recursos em redes de computadores.",
            "ejemplo": '''
                # Exemplo conceitual de implementação de um firewall em Python
                import socket

                def simple_firewall(ip):
                    blocked_ips = ['192.168.1.1', '10.0.0.1']
                    if ip in blocked_ips:
                        return False  # Bloqueado
                    return True  # Permitido

                print(simple_firewall('192.168.1.1'))  # Saída: False
                '''
        },
        "Neural_network_weights": {
            "significado": "Parâmetros ajustáveis de uma rede neural que determinam a força da conexão entre neurônios.",
            "uso": "São usados no processo de treinamento da rede para otimizar o desempenho em uma tarefa específica.",
            "ejemplo": '''
                # Exemplo de acesso e ajuste de pesos em uma rede neural com `TensorFlow` em Python
                import tensorflow as tf

                model = tf.keras.Sequential([
                    tf.keras.layers.Dense(10, activation='relu', input_shape=(5,))
                ])
                model.compile(optimizer='adam', loss='mean_squared_error')

                # Ver pesos iniciais
                weights = model.get_weights()
                print("Pesos iniciais:", weights)

                # Ajustar pesos manualmente (exemplo conceitual)
                new_weights = [w * 0.5 for w in weights]
                model.set_weights(new_weights)
                '''
        },
        "Normal_distribution": {
            "significado": "Distribuição de probabilidade contínua que é simétrica em relação à sua média e segue uma curva em forma de sino.",
            "uso": "É usada em estatística para modelar dados que tendem a se concentrar em torno de um valor médio.",
            "ejemplo": '''
                # Exemplo de geração de dados com distribuição normal em Python
                import numpy as np
                import matplotlib.pyplot as plt

                data = np.random.normal(0, 1, 1000)
                plt.hist(data, bins=30, density=True)
                plt.title("Distribuição Normal")
                plt.show()
                '''
        },
        "Nested_loops": {
            "significado": "Estrutura de controle de fluxo que inclui um loop dentro de outro, permitindo realizar operações mais complexas com múltiplas iterações.",
            "uso": "É usado em programação para percorrer matrizes, realizar cálculos complexos e trabalhar com estruturas de dados multidimensionais.",
            "ejemplo": '''
                # Exemplo de loops aninhados em Python
                for i in range(3):
                    for j in range(3):
                        print(f'Linha {i}, Coluna {j}')
                '''
        },
        "Null_pointer": {
            "significado": "Referência em um programa que não aponta para nenhum objeto válido ou endereço de memória, e é usada para indicar a ausência de um valor.",
            "uso": "É usado em programação para lidar com erros e evitar acessos a objetos não inicializados.",
            "ejemplo": '''
                # Exemplo de manejo de ponteiros nulos em Python (simulação)
                pointer = None
                if pointer is None:
                    print("O ponteiro é nulo")
                else:
                    print("O ponteiro aponta para um objeto")
                '''
        },
        "Nested_function": {
            "significado": "Função que está definida dentro de outra função e pode acessar as variáveis da função externa.",
            "uso": "É usada em programação para criar funções auxiliares e facilitar a modularidade e a reutilização do código.",
            "ejemplo": '''
                # Exemplo de função aninhada em Python
                def outer_function():
                    def inner_function():
                        print("Esta é uma função aninhada")
                    inner_function()
                outer_function()
                '''
        },
        "Null_termination": {
            "significado": "Prática de adicionar um caractere nulo (\\0) no final de uma string para indicar o fim da string.",
            "uso": "É usada em linguagens de programação como C e C++ para gerenciar strings de forma segura e evitar a leitura de dados além do final da string.",
            "ejemplo": '''
                # Exemplo de string terminada com nulo em C
                char str[] = "Hello";
                printf("%s", str);  // A string é impressa até o caractere nulo
                '''
        },
        "Network_latency": {
            "significado": "Tempo de atraso que ocorre na transmissão de dados de um ponto a outro em uma rede.",
            "uso": "É usada para avaliar a qualidade de conexões de rede e otimizar a comunicação em sistemas distribuídos.",
            "ejemplo": '''
                # Exemplo de medição de latência de rede com `ping` em Python
                import os

                response = os.system("ping -c 4 google.com")
                if response == 0:
                    print("Conexão com a rede está OK")
                else:
                    print("Erro na conexão com a rede")
                '''
        },
        "Newton_method": {
            "significado": "Método iterativo para encontrar raízes de uma função, usando aproximações sucessivas e a derivada da função.",
            "uso": "É usado em cálculos numéricos para encontrar soluções de equações não lineares de forma eficiente.",
            "ejemplo": '''
                # Exemplo de método de Newton em Python
                def f(x):
                    return x**2 - 2

                def df(x):
                    return 2*x

                x0 = 1.0
                tol = 1e-5
                while abs(f(x0)) > tol:
                    x0 -= f(x0) / df(x0)
                print("Raiz encontrada:", x0)
                '''
        },
        "Nondeterministic_algorithm": {
            "significado": "Algoritmo que, em sua execução, pode produzir resultados diferentes em execuções repetidas com as mesmas entradas.",
            "uso": "É usado em problemas que envolvem incertezas, como algoritmos de otimização e simulações estocásticas.",
            "ejemplo": '''
                # Exemplo de um algoritmo não determinístico (com comportamento aleatório)
                import random

                def random_choice():
                    return random.choice([1, 2, 3, 4, 5])

                print(random_choice())
                '''
        },
        "Negative_feedback": {
            "significado": "Mecanismo de controle onde a saída de um sistema é realimentada de forma a reduzir a diferença entre a saída e a entrada desejada.",
            "uso": "É usado em sistemas de controle para estabilizar e manter o comportamento de um sistema próximo a um valor de referência.",
            "ejemplo": '''
                # Exemplo conceitual de feedback negativo em sistemas de controle
                def system_output(input_signal):
                    output_signal = input_signal * 0.9  # Simulando um feedback negativo
                    return output_signal

                input_signal = 10
                print("Saída do sistema:", system_output(input_signal))
                '''
        },
        "Non_parametric_statistic": {
            "significado": "Estatística que não assume uma forma específica para a distribuição dos dados e é usada quando não se conhece ou não se deseja fazer suposições sobre os parâmetros da população.",
            "uso": "É usada para análises em que os dados não seguem distribuições paramétricas, como no teste de Mann-Whitney e no teste de Kruskal-Wallis.",
            "ejemplo": '''
                # Exemplo de teste não paramétrico com `scipy` em Python
                from scipy import stats

                data1 = [1, 2, 3, 4, 5]
                data2 = [6, 7, 8, 9, 10]
                stat, p_value = stats.mannwhitneyu(data1, data2)
                print("Estatística do teste:", stat)
                print("Valor p:", p_value)
                '''
        },
        "Non_stationary_signal": {
            "significado": "Sinal cuja estatística muda ao longo do tempo, ou seja, suas propriedades como média e variância não são constantes.",
            "uso": "É usado em processamento de sinais para analisar fenômenos que variam ao longo do tempo, como a fala e certos tipos de ruído.",
            "ejemplo": '''
                # Exemplo conceitual de sinal não estacionário
                import numpy as np
                import matplotlib.pyplot as plt

                t = np.linspace(0, 1, 1000)
                signal = np.sin(2 * np.pi * 5 * t) + 0.5 * np.sin(2 * np.pi * 10 * t)
                plt.plot(t, signal)
                plt.title("Sinal Não Estacionário")
                plt.show()
                '''
        },
        "Numba": {
            "significado": "Biblioteca de Python que permite la compilação Just-In-Time (JIT) para acelerar a execução de código numérico.",
            "uso": "É usada para otimizar funções em Python, especialmente aquelas que realizam operações matemáticas intensivas.",
            "ejemplo": '''
                # Exemplo de uso de Numba em Python
                from numba import jit
                import numpy as np

                @jit(nopython=True)
                def soma_matriz(matriz):
                    return np.sum(matriz)

                matriz = np.array([[1, 2], [3, 4]])
                print("Soma da matriz:", soma_matriz(matriz))
                '''
        },
        "Naive_bayes_model": {
            "significado": "Modelo estatístico baseado no teorema de Bayes e na suposição de independência condicional entre as características.",
            "uso": "É usado em classificação de dados, como na análise de sentimentos e detecção de spam.",
            "ejemplo": '''
                # Exemplo de uso de modelo de Naive Bayes com `scikit-learn` em Python
                from sklearn.naive_bayes import GaussianNB
                import numpy as np

                X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
                y = np.array([0, 1, 0, 1])
                modelo = GaussianNB()
                modelo.fit(X, y)
                previsao = modelo.predict([[2, 3]])
                print("Previsão:", previsao)
                '''
        },
        "Neuron_network_weights": {
            "significado": "Parâmetros ajustáveis de uma rede neural que controlam a força das conexões entre os neurônios.",
            "uso": "São usados durante o treinamento da rede para ajustar a aprendizagem e otimizar o desempenho em tarefas específicas.",
            "ejemplo": '''
                # Exemplo de acesso e ajuste de pesos em uma rede neural com `TensorFlow` em Python
                import tensorflow as tf

                modelo = tf.keras.Sequential([
                    tf.keras.layers.Dense(10, activation='relu', input_shape=(5,))
                ])
                modelo.compile(optimizer='adam', loss='mean_squared_error')

                # Obter pesos iniciais
                pesos = modelo.get_weights()
                print("Pesos iniciais:", pesos)

                # Ajustar pesos manualmente (exemplo conceitual)
                novos_pesos = [w * 0.5 for w in pesos]
                modelo.set_weights(novos_pesos)
                '''
        },
        "Nested_list": {
            "significado": "Lista que contém outras listas como elementos, permitindo a criação de estruturas de dados multidimensionais.",
            "uso": "É usada para representar dados em forma de tabelas, matrizes e outras formas complexas de dados.",
            "ejemplo": '''
                # Exemplo de lista aninhada em Python
                matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
                for i in range(len(matriz)):
                    for j in range(len(matriz[i])):
                        print(f'Elemento na posição [{i}][{j}]:', matriz[i][j])
                '''
        },
        "Notebook": {
            "significado": "Ferramenta interativa usada para escrever e executar código, geralmente com suporte para visualização de dados e anotações.",
            "uso": "É usada para documentação e execução de código em Python e outras linguagens, muito comum em ambientes de ciência de dados como Jupyter.",
            "ejemplo": '''
                # Exemplo de uso do Jupyter Notebook (conceitual)
                # Inicie o Jupyter Notebook em um terminal com o comando:
                # jupyter notebook
                '''
        },
        "Name_scope": {
            "significado": "Função usada em bibliotecas de aprendizado de máquina, como TensorFlow, para agrupar operações e variáveis sob um nome específico.",
            "uso": "É usada para organizar o código e facilitar a visualização e depuração de modelos de aprendizado de máquina.",
            "ejemplo": '''
                # Exemplo de uso de name_scope em TensorFlow
                import tensorflow as tf

                with tf.name_scope('camada_densa'):
                    camada = tf.keras.layers.Dense(10)
                    print("Camada criada dentro do name_scope")
                '''
        },
        "Named_tuple": {
            "significado": "Tipo de dado em Python que cria tuplas com campos nomeados, facilitando o acesso aos elementos por nome em vez de índice.",
            "uso": "É usado para criar estruturas de dados imutáveis, acessíveis de forma mais legível e organizada.",
            "ejemplo": '''
                # Exemplo de uso de namedtuple em Python
                from collections import namedtuple

                Pessoa = namedtuple('Pessoa', ['nome', 'idade'])
                pessoa1 = Pessoa(nome='João', idade=30)
                print(f'Nome: {pessoa1.nome}, Idade: {pessoa1.idade}')
                '''
        },
        "Netstat": {
            "significado": "Ferramenta de linha de comando usada para exibir informações sobre conexões de rede e estatísticas de rede em um sistema.",
            "uso": "É usada para monitorar e diagnosticar problemas de rede e verificar as portas de rede abertas em um computador.",
            "ejemplo": '''
                # Exemplo de uso do comando netstat em um terminal
                # Para listar todas as conexões de rede ativas
                netstat -an
                '''
        },
        "Null": {
            "significado": "Valor que representa a ausência de um valor ou objeto em uma variável ou estrutura de dados.",
            "uso": "É usado para indicar que uma variável ou referência não possui um valor válido.",
            "ejemplo": '''
                # Exemplo de uso de null (None) em Python
                variavel = None
                if variavel is None:
                    print("A variável está nula")
                '''
        },
        "Normalize": {
            "significado": "Processo de ajustar ou transformar dados para uma escala ou formato padrão.",
            "uso": "É usado em processamento de dados para garantir que as variáveis tenham uma distribuição semelhante ou sejam comparáveis.",
            "ejemplo": '''
                # Exemplo de normalização de dados com `sklearn` em Python
                from sklearn.preprocessing import MinMaxScaler
                import numpy as np

                dados = np.array([[1, 2], [3, 4], [5, 6]])
                scaler = MinMaxScaler()
                dados_normalizados = scaler.fit_transform(dados)
                print("Dados normalizados:", dados_normalizados)
                '''
        },
        "Next": {
            "significado": "Palavra-chave usada em linguagens de programação para indicar a próxima iteração de um loop.",
            "uso": "É usada para pular a execução do restante de uma iteração e passar para a próxima.",
            "ejemplo": '''
                # Exemplo de uso de `next` em Python
                for i in range(5):
                    if i == 3:
                        continue  # Pula a iteração atual e vai para a próxima
                    print(i)
                '''
        },
        "New": {
            "significado": "Palavra usada para criar uma nova instância de um objeto ou variável em linguagens de programação.",
            "uso": "É usada para alocar espaço de memória para um novo objeto ou variável.",
            "ejemplo": '''
                # Exemplo de criação de uma nova lista em Python
                lista = [1, 2, 3]
                nova_lista = list(lista)
                print("Nova lista:", nova_lista)
                '''
        },
        "Negation": {
            "significado": "Operação lógica que inverte o valor de verdade de uma expressão ou proposição.",
            "uso": "É usada em programação para criar expressões lógicas negativas, como em condições de controle de fluxo.",
            "ejemplo": '''
                # Exemplo de negação em Python
                x = True
                if not x:
                    print("x é falso")
                else:
                    print("x é verdadeiro")
                '''
        },
        "Numpy_array": {
            "significado": "Estrutura de dados bidimensional de alto desempenho usada para armazenar e manipular dados numéricos em Python.",
            "uso": "É usada para cálculos matemáticos e operações de álgebra linear, estatísticas, entre outros.",
            "ejemplo": '''
                # Exemplo de criação de um array Numpy em Python
                import numpy as np

                array = np.array([[1, 2, 3], [4, 5, 6]])
                print("Array Numpy:", array)
                '''
        },
        "Not": {
            "significado": "Operador lógico usado para inverter o valor de uma expressão booleana.",
            "uso": "É usado em expressões condicionais para verificar a negação de uma condição.",
            "ejemplo": '''
                # Exemplo de uso do operador `not` em Python
                a = False
                if not a:
                    print("A variável a é falsa")
                '''
        },
        "None": {
            "significado": "Objeto especial em Python que representa a ausência de valor ou um valor nulo.",
            "uso": "É usado para inicializar variáveis que ainda não possuem um valor definido ou para representar uma ausência de valor.",
            "ejemplo": '''
                # Exemplo de uso de `None` em Python
                variavel = None
                if variavel is None:
                    print("A variável é nula")
                '''
        },
        "Numpy_dot": {
            "significado": "Função da biblioteca Numpy que calcula o produto interno de dois arrays.",
            "uso": "É usada para multiplicar matrizes ou vetores, sendo fundamental em operações de álgebra linear.",
            "ejemplo": '''
                # Exemplo de uso de `numpy.dot` em Python
                import numpy as np

                vetor1 = np.array([1, 2, 3])
                vetor2 = np.array([4, 5, 6])
                produto_interno = np.dot(vetor1, vetor2)
                print("Produto interno:", produto_interno)
                '''
        },
        "Nmap": {
            "significado": "Ferramenta de código aberto usada para escanear redes e detectar dispositivos e serviços em uma rede.",
            "uso": "É usada em auditorias de segurança de redes para identificar portas abertas, serviços em execução e potenciais vulnerabilidades.",
            "ejemplo": '''
                # Exemplo de uso do comando nmap em um terminal
                # Para escanear uma rede específica
                nmap 192.168.1.0/24
                '''
        },
        "Namedtuple": {
            "significado": "Tipo de tupla en Python que permite definir campos con nombres para acceder a sus valores de manera más legible.",
            "uso": "Se utiliza para crear estructuras de datos inmutables y nombradas, facilitando el acceso a los elementos de una tupla.",
            "ejemplo": '''
                # Exemplo de uso de namedtuple em Python
                from collections import namedtuple

                Pessoa = namedtuple('Pessoa', ['nome', 'idade'])
                pessoa1 = Pessoa(nome='João', idade=30)
                print("Nome:", pessoa1.nome, ", Idade:", pessoa1.idade)
                '''
        },
        "Numpy_random": {
            "significado": "Submódulo da biblioteca Numpy que fornece funções para gerar números aleatórios e amostras de distribuições estatísticas.",
            "uso": "É usado para criar dados aleatórios para simulações, amostras estatísticas e testes.",
            "ejemplo": '''
                # Exemplo de uso de `numpy.random` em Python
                import numpy as np

                aleatorio = np.random.rand(3, 3)
                print("Matriz aleatória:", aleatorio)
                '''
        },
        "Networkx": {
            "significado": "Biblioteca de Python para a criação, manipulação e estudo de estruturas de grafos e redes complexas.",
            "uso": "É usada para modelar e analisar redes sociais, estruturas de transporte e outras aplicações baseadas em grafos.",
            "ejemplo": '''
                # Exemplo de criação de um grafo em `networkx`
                import networkx as nx
                import matplotlib.pyplot as plt

                G = nx.Graph()
                G.add_edges_from([(1, 2), (2, 3), (3, 4)])
                nx.draw(G, with_labels=True)
                plt.show()
                '''
        },
        "Numexpr": {
            "significado": "Biblioteca de Python usada para avaliar expressões matemáticas de forma rápida e eficiente, utilizando processamento paralelo.",
            "uso": "É usada para acelerar cálculos numéricos em grandes conjuntos de dados e operações complexas.",
            "ejemplo": '''
                # Exemplo de uso de `numexpr` em Python
                import numexpr as ne
                import numpy as np

                a = np.array([1, 2, 3])
                b = np.array([4, 5, 6])
                resultado = ne.evaluate('a * b + 2')
                print("Resultado:", resultado)
                '''
        },
        "Nonlocal": {
            "significado": "Palavra-chave em Python usada para declarar variáveis que existem em um escopo de nível superior ao do bloco de código atual, mas não no escopo global.",
            "uso": "É usada em funções aninhadas para modificar variáveis de um escopo externo que não é o global.",
            "ejemplo": '''
                # Exemplo de uso de `nonlocal` em Python
                def contador():
                    x = 0
                    def incremento():
                        nonlocal x
                        x += 1
                        return x
                    return incremento

                conta = contador()
                print(conta())  # Saída: 1
                print(conta())  # Saída: 2
                '''
        },
        "Numpy_shape": {
            "significado": "Atributo de um array Numpy que retorna as dimensões do array, indicando o número de elementos em cada eixo.",
            "uso": "É usado para verificar a estrutura de um array e realizar operações de redimensionamento e manipulação.",
            "ejemplo": '''
                # Exemplo de uso do atributo `shape` em um array Numpy
                import numpy as np

                array = np.array([[1, 2, 3], [4, 5, 6]])
                print("Forma do array:", array.shape)
                '''
        },
        "Numpy_sort": {
            "significado": "Função da biblioteca Numpy usada para ordenar os elementos de um array.",
            "uso": "É usada para organizar os elementos de um array em ordem crescente ou decrescente, facilitando a análise de dados.",
            "ejemplo": '''
                # Exemplo de uso de `numpy.sort` em Python
                import numpy as np

                array = np.array([3, 1, 2])
                array_ordenado = np.sort(array)
                print("Array ordenado:", array_ordenado)
                '''
        },
        "Numpy_std": {
            "significado": "Função da biblioteca Numpy que calcula o desvio padrão dos elementos de um array, medindo a dispersão dos dados em relação à média.",
            "uso": "É usada para avaliar a variabilidade ou dispersão de um conjunto de dados.",
            "ejemplo": '''
                # Exemplo de uso de `numpy.std` em Python
                import numpy as np

                array = np.array([1, 2, 3, 4, 5])
                desvio_padrao = np.std(array)
                print("Desvio padrão:", desvio_padrao)
                '''
        },
        "Numpy_sum": {
            "significado": "Função da biblioteca Numpy que retorna a soma dos elementos ao longo de um eixo especificado ou de todo o array.",
            "uso": "É usada para calcular a soma de elementos em arrays multidimensionais e realizar operações de agregação de dados.",
            "ejemplo": '''
                # Exemplo de uso de `numpy.sum` em Python
                import numpy as np

                array = np.array([[1, 2, 3], [4, 5, 6]])
                soma = np.sum(array)
                print("Soma de todos os elementos:", soma)
                '''
        },
        "Numpy_t": {
            "significado": "Atributo de um array Numpy que retorna a transposta do array, trocando suas linhas e colunas.",
            "uso": "É usado para inverter a orientação dos dados em um array, facilitando operações matemáticas e álgebra linear.",
            "ejemplo": '''
                # Exemplo de uso de `.T` para transpor um array Numpy
                import numpy as np

                array = np.array([[1, 2, 3], [4, 5, 6]])
                transposta = array.T
                print("Array transposto:\n", transposta)
                '''
        },
        "Nltk": {
            "significado": "Biblioteca de Python para processamento de linguagem natural, que fornece ferramentas para trabalhar com texto, análise de linguagem e linguística computacional.",
            "uso": "É usada para analisar texto, realizar tokenização, análise de sentimentos, e criar aplicações de processamento de linguagem natural.",
            "ejemplo": '''
                # Exemplo de uso de `nltk` em Python
                import nltk
                from nltk.tokenize import word_tokenize

                nltk.download('punkt')
                texto = "Olá, como você está?"
                palavras = word_tokenize(texto)
                print("Palavras tokenizadas:", palavras)
                '''
        },
        "Numpy_inner": {
            "significado": "Função da biblioteca Numpy que calcula o produto interno de dois arrays, também conhecido como produto escalar.",
            "uso": "É usado para realizar operações de multiplicação de vetores e é fundamental em álgebra linear e análise de dados.",
            "ejemplo": '''
                # Exemplo de uso de `numpy.inner` em Python
                import numpy as np

                a = np.array([1, 2, 3])
                b = np.array([4, 5, 6])
                produto_interno = np.inner(a, b)
                print("Produto interno:", produto_interno)
                '''
        },
        "Network_configuration": {
            "significado": "Processo de definição e ajuste dos parâmetros e componentes de uma rede de computadores para garantir seu funcionamento adequado.",
            "uso": "É utilizado para configurar dispositivos de rede, como roteadores e switches, e para gerenciar endereçamento IP, sub-redes e políticas de segurança.",
            "ejemplo": '''
                # Exemplo conceitual de configuração de rede em Python usando `socket`
                import socket

                def configuracao_rede():
                    host = socket.gethostbyname('example.com')
                    print("Endereço IP:", host)
                
                configuracao_rede()
                '''
        },
        "Namespace": {
            "significado": "Conceito de programação que se refere a um espaço de nomes onde variáveis, funções e objetos são armazenados e identificados de forma única.",
            "uso": "É usado para organizar e evitar conflitos de nomes em projetos de software, especialmente em programação orientada a objetos e linguagens como Python.",
            "ejemplo": '''
                # Exemplo de uso de `namespace` em Python com classes
                class MeuNamespace:
                    variavel = 'Olá'

                print(MeuNamespace.variavel)
                '''
        },
        "Neg_log_likelihood": {
            "significado": "Função de perda usada em estatísticas e aprendizado de máquina para medir a discrepância entre a distribuição de probabilidade estimada e os dados observados.",
            "uso": "É usada para treinar modelos de aprendizado de máquina, como modelos de regressão e classificadores probabilísticos, para otimizar suas previsões.",
            "ejemplo": '''
                # Exemplo conceitual de cálculo de log-verossimilhança negativa em Python
                import numpy as np

                def neg_log_likelihood(y_true, y_pred):
                    return -np.sum(y_true * np.log(y_pred))

                y_true = np.array([1, 0, 1])
                y_pred = np.array([0.9, 0.1, 0.8])
                resultado = neg_log_likelihood(y_true, y_pred)
                print("Log-verossimilhança negativa:", resultado)
                '''
        },
        "Numpy_mean": {
            "significado": "Função da biblioteca Numpy que calcula a média dos elementos de um array ao longo de um eixo especificado.",
            "uso": "É usada para calcular a média de um conjunto de dados, ajudando a entender a tendência central de um array.",
            "ejemplo": '''
                # Exemplo de uso de `numpy.mean` em Python
                import numpy as np

                array = np.array([1, 2, 3, 4, 5])
                media = np.mean(array)
                print("Média dos elementos:", media)
                '''
        },
    },
    "o": {
        # Aquí puedes agregar funciones que comiencen con la letra O
        "Open": {
            "significado": "Função ou comando usado para abrir arquivos, portas de rede ou outros recursos em um sistema de computador.",
            "uso": "É utilizado em programação para acessar arquivos e permitir operações como leitura e escrita.",
            "ejemplo": '''
                # Exemplo de uso de `open` em Python para ler um arquivo
                with open('exemplo.txt', 'r') as arquivo:
                    conteudo = arquivo.read()
                    print(conteudo)
                '''
        },
        "Ord": {
            "significado": "Função em Python que retorna o código numérico de um caractere.",
            "uso": "É usada para obter o valor inteiro correspondente a um caractere, útil em operações de manipulação de strings e codificação.",
            "ejemplo": '''
                # Exemplo de uso de `ord` em Python
                caractere = 'A'
                codigo = ord(caractere)
                print("Código numérico do caractere:", codigo)
                '''
        },
        "Oct": {
            "significado": "Função que converte um número inteiro em sua representação octal (base 8).",
            "uso": "É usada para representar números em diferentes bases, como na programação de sistemas e cálculos de baixo nível.",
            "ejemplo": '''
                # Exemplo de uso de `oct` em Python
                numero = 10
                representacao_octal = oct(numero)
                print("Representação octal:", representacao_octal)
                '''
        },
        "Os": {
            "significado": "Módulo em Python que fornece uma interface para interagir com o sistema operacional.",
            "uso": "É utilizado para acessar funcionalidades do sistema, como manipulação de arquivos, diretórios e variáveis de ambiente.",
            "ejemplo": '''
                # Exemplo de uso do módulo `os` em Python
                import os

                caminho = os.getcwd()
                print("Caminho do diretório atual:", caminho)
                '''
        },
        "Object": {
            "significado": "Instância de uma classe em programação orientada a objetos, que contém atributos e métodos.",
            "uso": "É usado para representar dados e comportamentos em linguagens de programação orientadas a objetos, como Python, Java e C++.",
            "ejemplo": '''
                # Exemplo de criação de um objeto em Python
                class Carro:
                    def __init__(self, modelo, ano):
                        self.modelo = modelo
                        self.ano = ano

                meu_carro = Carro('Fusca', 1974)
                print("Modelo do carro:", meu_carro.modelo)
                '''
        },
        "Output": {
            "significado": "Resultado ou saída gerada por um programa ou função após a execução.",
            "uso": "É utilizado para exibir resultados na tela, salvar em arquivos ou transmitir dados para outros sistemas.",
            "ejemplo": '''
                # Exemplo de saída em Python
                print("Este é um exemplo de saída de um programa")
                '''
        },
        "Operator": {
            "significado": "Símbolo ou palavra-chave que representa uma operação em um programa, como adição, subtração, etc.",
            "uso": "É utilizado para realizar operações aritméticas, lógicas e de comparação entre variáveis.",
            "ejemplo": '''
                # Exemplo de uso de operadores em Python
                a = 5
                b = 3
                soma = a + b
                print("Resultado da soma:", soma)
                '''
        },
        "Options": {
            "significado": "Parâmetros configuráveis que determinam o comportamento de uma função ou programa.",
            "uso": "É utilizado para customizar funções, scripts ou programas de acordo com as preferências do usuário.",
            "ejemplo": '''
                # Exemplo de uso de opções em uma função em Python
                def saudacao(nome, saudacao="Olá"):
                    print(f"{saudacao}, {nome}!")

                saudacao("Maria", saudacao="Bom dia")
                '''
        },
        "Optimize": {
            "significado": "Melhorar o desempenho de um programa ou sistema para torná-lo mais eficiente.",
            "uso": "É utilizado para reduzir o tempo de execução, uso de memória e outros recursos em algoritmos e programas.",
            "ejemplo": '''
                # Exemplo de otimização de um loop em Python
                import time

                # Código não otimizado
                start = time.time()
                for i in range(1000000):
                    pass
                print("Tempo de execução:", time.time() - start)

                # Código otimizado
                start = time.time()
                range(1000000)  # Usar a função `range` diretamente
                print("Tempo de execução otimizado:", time.time() - start)
                '''
        },
        "Overflow": {
            "significado": "Ocorrência quando um valor excede o limite máximo representável em uma variável ou tipo de dado.",
            "uso": "É utilizado para descrever problemas em cálculos que resultam em números maiores que a capacidade de armazenamento de um tipo de dado.",
            "ejemplo": '''
                # Exemplo de overflow em Python
                import numpy as np

                max_int = np.iinfo(np.int32).max
                print("Máximo valor inteiro:", max_int)
                overflow = max_int + 1
                print("Overflow:", overflow)
                '''
        },
        "Offset": {
            "significado": "Deslocamento ou diferença entre a posição de um elemento em uma estrutura de dados e a posição base.",
            "uso": "É usado para referenciar uma posição específica em um array, lista ou memória.",
            "ejemplo": '''
                # Exemplo de uso de offset em Python
                lista = [10, 20, 30, 40, 50]
                offset = 2  # Deslocamento de 2 posições
                print("Elemento com offset:", lista[offset])
                '''
        },
        "Outer": {
            "significado": "Relativo à parte externa de um objeto ou à operação que envolve elementos de diferentes conjuntos, como em álgebra linear e operações de produtos.",
            "uso": "É usado para descrever operações que combinam elementos de diferentes conjuntos, como a multiplicação de matrizes externas.",
            "ejemplo": '''
                # Exemplo de produto externo de vetores em Python com `numpy`
                import numpy as np

                a = np.array([1, 2])
                b = np.array([3, 4])
                resultado = np.outer(a, b)
                print("Produto externo:", resultado)
                '''
        },
        "Or": {
            "significado": "Operador lógico usado para combinar expressões e retornar `True` se pelo menos uma das expressões for verdadeira.",
            "uso": "É utilizado em programação para criar condições compostas em instruções `if`, loops e outros blocos de controle de fluxo.",
            "ejemplo": '''
                # Exemplo de uso do operador `or` em Python
                a = True
                b = False
                resultado = a or b
                print("Resultado do operador `or`:", resultado)
                '''
        },
        "Openpyxl": {
            "significado": "Biblioteca Python usada para ler, escrever e manipular arquivos do Excel (.xlsx).",
            "uso": "É utilizada para criar e modificar planilhas do Excel em programas Python, facilitando a automação de tarefas de processamento de dados.",
            "ejemplo": '''
                # Exemplo de uso do `openpyxl` para criar uma planilha em Python
                from openpyxl import Workbook

                wb = Workbook()
                ws = wb.active
                ws['A1'] = "Olá, mundo!"
                wb.save("exemplo.xlsx")
                '''
        },
        "Overload": {
            "significado": "Conceito de programação onde uma função ou método pode ter diferentes definições ou implementações dependendo do número e tipo de argumentos.",
            "uso": "É utilizado para criar funções que podem realizar tarefas diferentes com base nos argumentos recebidos, facilitando a leitura do código e a reutilização de funções.",
            "ejemplo": '''
                # Exemplo de sobrecarga de função (em Python, a sobrecarga é simulada com funções diferentes)
                def saudacao(nome):
                    print(f"Olá, {nome}!")

                def saudacao(nome, saudacao_especial):
                    print(f"{saudacao_especial}, {nome}!")

                saudacao("Maria")
                saudacao("João", "Bom dia")
                '''
        },
        "Object_id": {
            "significado": "Identificador único associado a um objeto em um sistema de banco de dados ou estrutura de dados.",
            "uso": "É usado para identificar de forma única registros ou instâncias de objetos, como em bancos de dados NoSQL ou em programação orientada a objetos.",
            "ejemplo": '''
                # Exemplo de uso de `ObjectId` em Python com `pymongo` para MongoDB
                from bson import ObjectId

                id_objeto = ObjectId()
                print("ID do objeto:", id_objeto)
                '''
        },
        "On_click": {
            "significado": "Ação ou evento que ocorre quando um elemento é clicado em uma interface de usuário.",
            "uso": "É usado em desenvolvimento web e de aplicativos para definir o comportamento de elementos interativos, como botões e links.",
            "ejemplo": '''
                # Exemplo de uso de `on_click` em Python com `tkinter` para interfaces gráficas
                import tkinter as tk

                def acao():
                    print("Botão clicado!")

                root = tk.Tk()
                botao = tk.Button(root, text="Clique aqui", command=acao)
                botao.pack()
                root.mainloop()
                '''
        },
        "Openai": {
            "significado": "Organização de pesquisa em inteligência artificial (IA) que desenvolve tecnologias para promover e desenvolver IA amigável.",
            "uso": "É usada para implementar soluções de IA como modelos de linguagem e algoritmos avançados em diversas aplicações.",
            "ejemplo": '''
                # Exemplo de uso da biblioteca `openai` em Python para acessar a API da OpenAI
                import openai

                openai.api_key = "sua_chave_api"
                resposta = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt="Olá, como você está?",
                    max_tokens=5
                )
                print("Resposta da OpenAI:", resposta.choices[0].text.strip())
                '''
        },
        "Os_path": {
            "significado": "Submódulo do módulo `os` em Python usado para manipular caminhos de arquivos e diretórios de forma independente do sistema operacional.",
            "uso": "É utilizado para criar, manipular e navegar por caminhos de arquivos e diretórios de maneira portável entre diferentes sistemas operacionais.",
            "ejemplo": '''
                # Exemplo de uso de `os.path` em Python
                import os

                caminho_completo = os.path.join('pasta', 'subpasta', 'arquivo.txt')
                print("Caminho completo:", caminho_completo)
                '''
        },
        "Overflow_error": {
            "significado": "Erro que ocorre quando um valor excede o limite máximo representável por um tipo de dado.",
            "uso": "É usado para indicar que uma operação causou um valor que ultrapassou a capacidade do tipo de dado, podendo causar falhas em cálculos e programas.",
            "ejemplo": '''
                # Exemplo de erro de overflow em Python com tipo `int`
                import numpy as np

                max_int = np.iinfo(np.int32).max
                try:
                    resultado = max_int + 1
                except OverflowError as e:
                    print("Erro de overflow:", e)
                '''
        },
        "Ordered_dict": {
            "significado": "Tipo de estrutura de dados em Python que mantém a ordem de inserção dos elementos em um dicionário.",
            "uso": "É utilizado para manter a ordem dos itens em um dicionário, útil em aplicações que requerem consistência na ordem de elementos.",
            "ejemplo": '''
                # Exemplo de uso de `OrderedDict` em Python
                from collections import OrderedDict

                d = OrderedDict()
                d['a'] = 1
                d['b'] = 2
                d['c'] = 3
                print("Dicionário ordenado:", d)
                '''
        },
        "Override": {
            "significado": "Prática de substituir um método de uma classe pai em uma classe filha, fornecendo uma nova implementação.",
            "uso": "É utilizado em programação orientada a objetos para modificar o comportamento de um método herdado.",
            "ejemplo": '''
                # Exemplo de sobrescrita de método em Python
                class Animal:
                    def falar(self):
                        print("Som de animal")

                class Cachorro(Animal):
                    def falar(self):
                        print("Latido")

                cachorro = Cachorro()
                cachorro.falar()  # Saída: Latido
                '''
        },
        "Output_stream": {
            "significado": "Fluxo de saída utilizado para enviar dados de um programa para um destino, como a tela, arquivos ou outros dispositivos.",
            "uso": "É utilizado para exibir informações na tela ou gravar dados em arquivos em programação.",
            "ejemplo": '''
                # Exemplo de uso de fluxo de saída em Python
                import sys

                sys.stdout.write("Mensagem para saída padrão\n")
                '''
        },
        "Os_walk": {
            "significado": "Função do módulo `os` em Python que permite percorrer diretórios e subdiretórios de forma recursiva.",
            "uso": "É utilizado para iterar sobre a estrutura de diretórios e listar arquivos e subpastas.",
            "ejemplo": '''
                # Exemplo de uso de `os.walk` para percorrer um diretório
                import os

                for pasta, subpastas, arquivos in os.walk('/caminho/do/diretorio'):
                    print('Pasta:', pasta)
                    for arquivo in arquivos:
                        print('Arquivo:', arquivo)
                '''
        },
        "Os_remove": {
            "significado": "Função do módulo `os` em Python que remove (deleta) um arquivo especificado.",
            "uso": "É utilizado para deletar arquivos de um sistema de arquivos em programação.",
            "ejemplo": '''
                # Exemplo de uso de `os.remove` para remover um arquivo
                import os

                os.remove('arquivo.txt')
                print('Arquivo removido')
                '''
        },
        "Option_parser": {
            "significado": "Módulo em Python para analisar e manipular argumentos de linha de comando passados para um script.",
            "uso": "É utilizado para criar scripts que aceitam parâmetros de entrada de forma estruturada.",
            "ejemplo": '''
                # Exemplo de uso de `optparse` em Python
                from optparse import OptionParser

                parser = OptionParser()
                parser.add_option("-f", "--file", dest="filename", help="nome do arquivo")
                (options, args) = parser.parse_args()

                if options.filename:
                    print("Arquivo especificado:", options.filename)
                '''
        },
        "Os_error": {
            "significado": "Erro gerado em Python quando uma operação do sistema operacional falha, como a tentativa de abrir um arquivo inexistente.",
            "uso": "É utilizado para capturar e lidar com erros relacionados a operações de arquivos e manipulação de sistemas em Python.",
            "ejemplo": '''
                # Exemplo de tratamento de erro de sistema com `os.error`
                import os

                try:
                    os.remove('arquivo_inexistente.txt')
                except OSError as e:
                    print("Erro do sistema:", e)
                '''
        },
        "One_hot_encoding": {
            "significado": "Método de codificação de variáveis categóricas em vetores binários, onde cada classe é representada por uma coluna.",
            "uso": "É utilizado em aprendizado de máquina para converter variáveis categóricas em uma forma que pode ser usada por algoritmos de aprendizado.",
            "ejemplo": '''
                # Exemplo de codificação one-hot em Python com `pandas`
                import pandas as pd

                data = pd.DataFrame({'categoria': ['A', 'B', 'C', 'A']})
                encoded_data = pd.get_dummies(data, columns=['categoria'])
                print("Dados codificados:", encoded_data)
                '''
        },
        "Ordered_set": {
            "significado": "Estrutura de dados que mantém a ordem de inserção dos elementos em um conjunto, sem permitir duplicatas.",
            "uso": "É utilizado para armazenar elementos únicos em uma ordem específica, útil quando a ordem é relevante.",
            "ejemplo": '''
                # Exemplo de uso de `OrderedSet` com a biblioteca `ordered-set` em Python
                from ordered_set import OrderedSet

                conjunto = OrderedSet(['a', 'b', 'c', 'a'])
                print("Conjunto ordenado:", conjunto)
                '''
        },
        "On_error": {
            "significado": "Expressão usada para definir o comportamento de um programa em caso de erro ou exceção.",
            "uso": "É utilizado em programação para capturar e tratar exceções, garantindo que o programa continue executando de forma controlada.",
            "ejemplo": '''
                # Exemplo de uso de `try-except` para tratamento de erros em Python
                try:
                    resultado = 10 / 0
                except ZeroDivisionError:
                    print("Erro: divisão por zero")
                '''
        },
        "Os_stat": {
            "significado": "Função do módulo `os` em Python que retorna informações sobre um arquivo ou diretório, como tamanho, permissões e data de modificação.",
            "uso": "É utilizado para obter metadados sobre arquivos e diretórios em Python.",
            "ejemplo": '''
                # Exemplo de uso de `os.stat` para obter informações de um arquivo
                import os

                info = os.stat('arquivo.txt')
                print("Tamanho do arquivo:", info.st_size, "bytes")
                '''
        },
        "Os_mkdir": {
            "significado": "Função do módulo `os` em Python que cria um novo diretório no sistema de arquivos.",
            "uso": "É utilizado para criar pastas programaticamente em um diretório especificado.",
            "ejemplo": '''
                # Exemplo de criação de diretório com `os.mkdir`
                import os

                os.mkdir('novo_diretorio')
                print('Diretório criado')
                '''
        },
        "Operator_overloading": {
            "significado": "Habilidade de redefinir o comportamento de operadores padrão (como +, -, *, etc.) em classes definidas pelo usuário.",
            "uso": "É utilizado em programação orientada a objetos para personalizar o comportamento de operadores para objetos de uma classe.",
            "ejemplo": '''
                # Exemplo de sobrecarga de operador em Python
                class Ponto:
                    def __init__(self, x, y):
                        self.x = x
                        self.y = y

                    def __add__(self, outro):
                        return Ponto(self.x + outro.x, self.y + outro.y)

                p1 = Ponto(1, 2)
                p2 = Ponto(3, 4)
                resultado = p1 + p2
                print(f"Resultado: ({resultado.x}, {resultado.y})")
                '''
        },
        "Offset_mapping": {
            "significado": "Relação entre os índices de uma estrutura de dados e suas posições reais ou virtuais.",
            "uso": "É utilizado em processamento de dados e linguagens para alinhar dados ou converter índices.",
            "ejemplo": '''
                # Exemplo de mapeamento de offset
                dados = ['a', 'b', 'c', 'd']
                offset = 2
                mapeados = [(i + offset, valor) for i, valor in enumerate(dados)]
                print('Mapeamento de offset:', mapeados)
                '''
        },
        "Os_path_exists": {
            "significado": "Função do módulo `os.path` em Python que verifica se um caminho de arquivo ou diretório existe.",
            "uso": "É utilizado para evitar erros ao acessar arquivos ou diretórios inexistentes.",
            "ejemplo": '''
                # Exemplo de uso de `os.path.exists`
                import os

                if os.path.exists('arquivo.txt'):
                    print('O arquivo existe')
                else:
                    print('O arquivo não existe')
                '''
        },
        "Output_file": {
            "significado": "Arquivo usado para armazenar os dados gerados ou processados por um programa.",
            "uso": "É utilizado para salvar resultados de programas em arquivos para uso posterior.",
            "ejemplo": '''
                # Exemplo de criação e escrita em um arquivo de saída
                with open('saida.txt', 'w') as arquivo:
                    arquivo.write('Este é o conteúdo do arquivo de saída.')
                print('Arquivo de saída criado')
                '''
        },
        "Optimization": {
            "significado": "Processo de melhorar o desempenho ou a eficiência de um algoritmo, sistema ou aplicação.",
            "uso": "É utilizado em ciência da computação, aprendizado de máquina e engenharia para resolver problemas de forma mais eficiente.",
            "ejemplo": '''
                # Exemplo de otimização de função com `scipy`
                from scipy.optimize import minimize

                def funcao(x):
                    return x**2 + 3*x + 2

                resultado = minimize(funcao, x0=0)
                print("Valor otimizado:", resultado.x)
                '''
        },
        "Os_getcwd": {
            "significado": "Função do módulo `os` em Python que retorna o diretório de trabalho atual.",
            "uso": "É utilizado para determinar o diretório onde o script está sendo executado.",
            "ejemplo": '''
                # Exemplo de uso de `os.getcwd`
                import os

                diretorio_atual = os.getcwd()
                print('Diretório atual:', diretorio_atual)
                '''
        },
        "Os_rename": {
            "significado": "Função do módulo `os` em Python que renomeia ou move um arquivo ou diretório.",
            "uso": "É utilizado para modificar nomes de arquivos ou diretórios ou movê-los para novos locais.",
            "ejemplo": '''
                # Exemplo de renomeação de arquivo com `os.rename`
                import os

                os.rename('arquivo_antigo.txt', 'arquivo_novo.txt')
                print('Arquivo renomeado')
                '''
        },
        "Os_chmod": {
            "significado": "Função do módulo `os` em Python que altera as permissões de um arquivo ou diretório.",
            "uso": "É utilizado para modificar permissões de leitura, escrita ou execução em arquivos e diretórios.",
            "ejemplo": '''
                # Exemplo de uso de `os.chmod` para alterar permissões
                import os
                import stat

                os.chmod('arquivo.txt', stat.S_IRUSR | stat.S_IWUSR)  # Permissão de leitura e escrita para o dono
                print('Permissões alteradas')
                '''
        },
        "Open_file_mode": {
            "significado": "Parâmetro da função `open` em Python que especifica o modo de abertura do arquivo (leitura, escrita, etc.).",
            "uso": "É utilizado para definir como o arquivo será manipulado (por exemplo, apenas leitura ou leitura e escrita).",
            "ejemplo": '''
                # Exemplo de abertura de arquivo no modo 'r+' (leitura e escrita)
                with open('arquivo.txt', 'r+') as arquivo:
                    conteudo = arquivo.read()
                    print('Conteúdo:', conteudo)
                    arquivo.write('Adicionando mais conteúdo.')
                '''
        },
        "Open_source": {
            "significado": "Termo que se refere a software cujo código-fonte está disponível publicamente para uso, modificação e distribuição.",
            "uso": "É utilizado para promover a colaboração e a transparência no desenvolvimento de software.",
            "ejemplo": '''
                # Exemplo de projeto open source: Python
                print('O Python é uma linguagem de programação open source.')
                '''
        },
        "Output_format": {
            "significado": "Especificação de como os dados ou resultados de um programa devem ser apresentados ou armazenados.",
            "uso": "É utilizado para ajustar o formato de saída em relatórios, gráficos ou arquivos de dados.",
            "ejemplo": '''
                # Exemplo de formatar saída com string formatada
                valor = 123.456
                print(f"Valor formatado: {valor:.2f}")  # Saída: Valor formatado: 123.46
                '''
        },
        "One_time_pad": {
            "significado": "Método de criptografia que utiliza uma chave aleatória única para criptografar e descriptografar mensagens.",
            "uso": "É utilizado em comunicações altamente seguras devido à sua invulnerabilidade matemática, se aplicado corretamente.",
            "ejemplo": '''
                # Exemplo conceitual de um One-Time Pad em Python
                mensagem = "HELLO"
                chave = "XMCKL"  # Chave aleatória
                criptografada = ''.join(chr((ord(m) ^ ord(k))) for m, k in zip(mensagem, chave))
                print("Mensagem criptografada:", criptografada)
                '''
        },
        "Override_property": {
            "significado": "Prática em programação orientada a objetos de redefinir o comportamento de uma propriedade herdada em uma classe derivada.",
            "uso": "É utilizado para modificar ou estender o comportamento padrão de classes base.",
            "ejemplo": '''
                # Exemplo de sobrescrita de propriedade em Python
                class Base:
                    @property
                    def valor(self):
                        return "Valor da classe base"

                class Derivada(Base):
                    @property
                    def valor(self):
                        return "Valor sobrescrito na classe derivada"

                obj = Derivada()
                print(obj.valor)  # Saída: Valor sobrescrito na classe derivada
                '''
        },
    },
    "p": { 
        # Aquí puedes agregar funciones que comiencen con la letra P
        "Print": {
            "significado": "Função embutida em Python usada para exibir mensagens ou valores no console.",
            "uso": "É utilizada para debugar código ou mostrar informações ao usuário.",
            "ejemplo": '''
                # Exemplo de uso da função print
                nome = "Python"
                print(f"Bem-vindo ao {nome}!")  # Saída: Bem-vindo ao Python!
                '''
        },
        "Pop": {
            "significado": "Método de listas ou dicionários em Python que remove e retorna um elemento.",
            "uso": "É utilizado para manipular estruturas de dados, especialmente ao trabalhar com pilhas ou remoções específicas.",
            "ejemplo": '''
                # Exemplo de pop em uma lista
                lista = [1, 2, 3, 4]
                elemento = lista.pop()  # Remove o último elemento
                print(elemento)  # Saída: 4
                '''
        },
        "Property": {
            "significado": "Decorador em Python que define métodos como atributos, permitindo acesso controlado a variáveis de instância.",
            "uso": "É utilizado para encapsular a lógica de acesso e evitar mudanças diretas nos atributos.",
            "ejemplo": '''
                # Exemplo de uso de @property
                class Pessoa:
                    def __init__(self, nome):
                        self._nome = nome

                    @property
                    def nome(self):
                        return self._nome.upper()

                pessoa = Pessoa("João")
                print(pessoa.nome)  # Saída: JOÃO
                '''
        },
        "Pow": {
            "significado": "Função embutida que calcula a potência de um número, incluindo suporte para módulo.",
            "uso": "É utilizada para operações matemáticas que envolvem exponenciação.",
            "ejemplo": '''
                # Exemplo de uso da função pow
                resultado = pow(2, 3)  # 2 elevado à 3
                print(resultado)  # Saída: 8
                '''
        },
        "Pprint": {
            "significado": "Módulo ou função em Python para imprimir dados estruturados de forma mais legível.",
            "uso": "É utilizado para depuração ou visualização de estruturas de dados complexas.",
            "ejemplo": '''
                # Exemplo de uso do pprint
                import pprint
                dados = {'nome': 'Ana', 'idade': 25, 'habilidades': ['Python', 'Data Science']}
                pprint.pprint(dados)
                '''
        },
        "Pass": {
            "significado": "Declaração em Python que não executa nenhuma ação, usada como um marcador ou preenchimento.",
            "uso": "É utilizada para criar blocos de código que ainda não foram implementados.",
            "ejemplo": '''
                # Exemplo de uso de pass
                def funcao():
                    pass  # Placeholder para lógica futura
                '''
        },
        "Pip": {
            "significado": "Ferramenta de gerenciamento de pacotes para instalar e gerenciar bibliotecas em Python.",
            "uso": "É utilizada para adicionar dependências ao projeto de forma prática.",
            "ejemplo": '''
                # Instalar um pacote usando pip
                # Comando no terminal:
                pip install numpy
                '''
        },
        "Pickle": {
            "significado": "Módulo em Python para serializar e desserializar objetos Python.",
            "uso": "É utilizado para armazenar objetos complexos em arquivos ou transferi-los entre programas.",
            "ejemplo": '''
                # Exemplo de serialização com pickle
                import pickle
                dados = {"nome": "Maria", "idade": 30}

                with open("dados.pkl", "wb") as arquivo:
                    pickle.dump(dados, arquivo)

                # Desserializar
                with open("dados.pkl", "rb") as arquivo:
                    carregado = pickle.load(arquivo)
                    print(carregado)  # Saída: {'nome': 'Maria', 'idade': 30}
                '''
        },
        "Partition": {
            "significado": "Método de strings em Python que divide a string em três partes com base no delimitador especificado.",
            "uso": "É utilizado para separar partes de uma string para processamento adicional.",
            "ejemplo": '''
                # Exemplo de uso de partition
                texto = "Python é incrível"
                partes = texto.partition("é")
                print(partes)  # Saída: ('Python ', 'é', ' incrível')
                '''
        },
        "Pathlib": {
            "significado": "Módulo em Python que fornece uma interface orientada a objetos para manipulação de caminhos de arquivos e diretórios.",
            "uso": "É utilizado para trabalhar com arquivos e diretórios de forma mais intuitiva e cross-platform.",
            "ejemplo": '''
                from pathlib import Path

                caminho = Path("meu_arquivo.txt")
                if not caminho.exists():
                    caminho.touch()  # Cria o arquivo
                print(f"Arquivo criado: {caminho.resolve()}")
                '''
        },
        "Partial": {
            "significado": "Função do módulo `functools` que permite fixar alguns argumentos de uma função, criando uma nova função com menos argumentos necessários.",
            "uso": "É utilizada para simplificar chamadas de funções com argumentos frequentemente reutilizados.",
            "ejemplo": '''
                from functools import partial

                def potencia(base, expoente):
                    return base ** expoente

                quadrado = partial(potencia, expoente=2)
                print(quadrado(4))  # Saída: 16
                '''
        },
        "Popitem": {
            "significado": "Método de dicionários em Python que remove e retorna o último par chave-valor inserido.",
            "uso": "É utilizado para manipular dicionários que seguem a ordem de inserção de itens (Python 3.7+).",
            "ejemplo": '''
                dicionario = {'a': 1, 'b': 2, 'c': 3}
                ultimo_item = dicionario.popitem()
                print(ultimo_item)  # Saída: ('c', 3)
                '''
        },
        "Permutations": {
            "significado": "Função do módulo `itertools` que gera todas as permutações possíveis de um iterável.",
            "uso": "É utilizada em problemas de combinação e probabilidade.",
            "ejemplo": '''
                from itertools import permutations

                itens = ['a', 'b', 'c']
                todas_permutacoes = list(permutations(itens))
                print(todas_permutacoes)  # Saída: [('a', 'b', 'c'), ('a', 'c', 'b'), ...]
                '''
        },
        "Plt_plot": {
            "significado": "Função do módulo `matplotlib.pyplot` usada para criar gráficos de linhas.",
            "uso": "É utilizada para visualização de dados em gráficos simples.",
            "ejemplo": '''
                import matplotlib.pyplot as plt

                x = [1, 2, 3, 4]
                y = [10, 20, 30, 40]
                plt.plot(x, y)
                plt.title("Gráfico de Linha")
                plt.show()
                '''
        },
        "Paramiko": {
            "significado": "Módulo Python para implementação de SSH2, permitindo comunicação segura com servidores remotos.",
            "uso": "É utilizado para executar comandos remotos, transferir arquivos ou gerenciar servidores.",
            "ejemplo": '''
                import paramiko

                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect('servidor.com', username='usuario', password='senha')
                stdin, stdout, stderr = ssh.exec_command('ls')
                print(stdout.read().decode())
                ssh.close()
                '''
        },
        "Path": {
            "significado": "Classe principal do módulo `pathlib` para representar e manipular caminhos de arquivos ou diretórios.",
            "uso": "É utilizada para criar, verificar ou alterar arquivos e diretórios.",
            "ejemplo": '''
                from pathlib import Path

                pasta = Path("nova_pasta")
                if not pasta.exists():
                    pasta.mkdir()
                    print("Pasta criada!")
                '''
        },
        "Pdf_merger": {
            "significado": "Classe do módulo `PyPDF2` usada para combinar vários arquivos PDF em um único documento.",
            "uso": "É utilizada em aplicações que exigem manipulação de arquivos PDF.",
            "ejemplo": '''
                from PyPDF2 import PdfMerger

                merger = PdfMerger()
                merger.append("arquivo1.pdf")
                merger.append("arquivo2.pdf")
                merger.write("combinado.pdf")
                merger.close()
                '''
        },
        "Pandas": {
            "significado": "Biblioteca de Python para manipulação e análise de dados, especialmente com estruturas como DataFrames.",
            "uso": "É utilizada para lidar com grandes conjuntos de dados, realizar cálculos e transformar dados.",
            "ejemplo": '''
                import pandas as pd

                dados = {'Nome': ['Ana', 'João'], 'Idade': [25, 30]}
                df = pd.DataFrame(dados)
                print(df)
                '''
        },
        "Parse": {
            "significado": "Processo de analisar e interpretar uma string ou dados de entrada de acordo com uma estrutura ou formato específico.",
            "uso": "É utilizado em linguagens de programação, processamento de arquivos e análise de dados.",
            "ejemplo": '''
                from xml.etree import ElementTree as ET

                xml_data = '<data><item>123</item></data>'
                root = ET.fromstring(xml_data)
                print(root.find('item').text)  # Saída: 123
                '''
        },
        "Pipe": {
            "significado": "Método ou conceito usado para encadear comandos ou processos, frequentemente em sistemas baseados em Unix.",
            "uso": "É utilizado para transmitir saída de um programa como entrada de outro.",
            "ejemplo": '''
                # Em Python, o subprocess pode ser usado para simular pipes
                import subprocess

                proc1 = subprocess.Popen(['echo', 'Hello, World!'], stdout=subprocess.PIPE)
                proc2 = subprocess.Popen(['grep', 'World'], stdin=proc1.stdout, stdout=subprocess.PIPE)
                output = proc2.communicate()[0]
                print(output.decode())  # Saída: Hello, World!
                '''
        },
        "Print_function": {
            "significado": "Função embutida em Python usada para imprimir texto ou dados no console.",
            "uso": "É utilizada para depuração, mensagens ou exibição de resultados.",
            "ejemplo": '''
                print("Olá, Mundo!")
                print("O resultado é:", 42)
                '''
        },
        "Proxy": {
            "significado": "Intermediário que atua entre um cliente e um servidor, geralmente para controlar, filtrar ou otimizar as comunicações.",
            "uso": "É utilizado para anonimato, balanceamento de carga ou segurança em redes.",
            "ejemplo": '''
                # Exemplo simples com um servidor proxy em Python
                import requests

                proxies = {
                    "http": "http://proxy.example.com:8080",
                    "https": "http://proxy.example.com:8080"
                }
                response = requests.get("http://example.com", proxies=proxies)
                print(response.status_code)
                '''
        },
        "Profile": {
            "significado": "Ferramenta ou módulo usado para medir o desempenho de um código, incluindo o tempo de execução de funções.",
            "uso": "É utilizado para otimizar o código identificando gargalos de desempenho.",
            "ejemplo": '''
                import cProfile

                def calcular():
                    resultado = sum(range(1_000_000))
                    print(resultado)

                cProfile.run('calcular()')
                '''
        },
        "Pool": {
            "significado": "Classe do módulo `multiprocessing` que gerencia um grupo de processos para execução paralela de tarefas.",
            "uso": "É utilizada para distribuir trabalho entre vários processos em sistemas multi-core.",
            "ejemplo": '''
                from multiprocessing import Pool

                def quadrado(x):
                    return x * x

                with Pool(4) as p:
                    resultados = p.map(quadrado, [1, 2, 3, 4])
                print(resultados)  # Saída: [1, 4, 9, 16]
                '''
        },
        "Pow_function": {
            "significado": "Função embutida em Python que calcula a potência de um número.",
            "uso": "É utilizada para cálculos matemáticos.",
            "ejemplo": '''
                resultado = pow(2, 3)  # 2 elevado a 3
                print(resultado)  # Saída: 8
                '''
        },
        "Proxy_server": {
            "significado": "Servidor que atua como intermediário para solicitações entre clientes e servidores, oferecendo controle e segurança.",
            "uso": "É utilizado em redes corporativas e pessoais para melhorar a segurança ou gerenciar o acesso à internet.",
            "ejemplo": '''
                # Configuração de um proxy em Python com `http.server`
                from http.server import SimpleHTTPRequestHandler
                from socketserver import TCPServer

                class ProxyHandler(SimpleHTTPRequestHandler):
                    def do_GET(self):
                        print(f"Requisição para: {self.path}")
                        super().do_GET()

                with TCPServer(("localhost", 8080), ProxyHandler) as httpd:
                    print("Proxy rodando na porta 8080")
                    httpd.serve_forever()
                '''
        },
        "Plotly": {
            "significado": "Biblioteca Python para criar visualizações interativas como gráficos de linhas, barras e mapas.",
            "uso": "É utilizada para análise e apresentação de dados.",
            "ejemplo": '''
                import plotly.express as px

                df = px.data.iris()
                fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
                fig.show()
                '''
        },
        "Pipeline": {
            "significado": "Estrutura que permite encadear etapas de processamento de dados ou aprendizado de máquina de forma sequencial.",
            "uso": "É utilizada em projetos de machine learning para organizar fluxos de trabalho.",
            "ejemplo": '''
                from sklearn.pipeline import Pipeline
                from sklearn.preprocessing import StandardScaler
                from sklearn.linear_model import LogisticRegression

                pipeline = Pipeline([
                    ('scaler', StandardScaler()),
                    ('classifier', LogisticRegression())
                ])
                print(pipeline)
                '''
        },
        "Partial_fit": {
            "significado": "Método utilizado em modelos de aprendizado de máquina para treinar incrementadamente, permitindo lidar com grandes volumes de dados.",
            "uso": "É utilizado em situações onde o conjunto de dados completo não pode ser carregado na memória de uma só vez.",
            "ejemplo": '''
                from sklearn.linear_model import SGDClassifier
                import numpy as np

                X = np.random.rand(100, 10)
                y = np.random.randint(0, 2, 100)

                modelo = SGDClassifier()
                modelo.partial_fit(X[:50], y[:50], classes=[0, 1])
                modelo.partial_fit(X[50:], y[50:])
                print("Modelo treinado incrementadamente.")
                '''
        },
        "Parquet": {
            "significado": "Formato de armazenamento eficiente e orientado a colunas usado para análise de dados de alto desempenho.",
            "uso": "É utilizado em ferramentas como Apache Spark e pandas para armazenar grandes volumes de dados.",
            "exemplo": """
                import pandas as pd

                df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
                df.to_parquet('arquivo.parquet')
                df_carregado = pd.read_parquet('arquivo.parquet')
                print(df_carregado)
                """
        },
        "Pkg_resources": {
            "significado": "Módulo da biblioteca `setuptools` que lida com pacotes e dependências em Python.",
            "uso": "É utilizado para consultar e gerenciar recursos de pacotes Python instalados.",
            "exemplo": """
                import pkg_resources

                distribs = pkg_resources.working_set
                for dist in distribs:
                    print(dist.project_name, dist.version)
                """
        },
        "Plot": {
            "significado": "Função básica de visualização de gráficos em bibliotecas como Matplotlib.",
            "uso": "É utilizada para criar gráficos de linhas, dispersão ou visualizações simples.",
            "exemplo": """
                import matplotlib.pyplot as plt

                x = [1, 2, 3, 4]
                y = [10, 20, 25, 30]
                plt.plot(x, y)
                plt.title("Gráfico Simples")
                plt.show()
                """
        },
        "Path_exists": {
            "significado": "Função para verificar se um arquivo ou diretório existe em um caminho especificado.",
            "uso": "É utilizada para validação de caminhos antes de realizar operações de leitura ou escrita.",
            "exemplo": """
                import os

                if os.path.exists('arquivo.txt'):
                    print('O arquivo existe.')
                else:
                    print('O arquivo não foi encontrado.')
                """
        },
        "Preprocess": {
            "significado": "Etapa de preparação de dados antes de serem usados em análises ou modelos de aprendizado de máquina.",
            "uso": "É utilizada para normalizar, limpar ou transformar dados brutos.",
            "exemplo": """
                from sklearn.preprocessing import StandardScaler
                import numpy as np

                dados = np.array([[1, 2], [3, 4], [5, 6]])
                scaler = StandardScaler()
                dados_normalizados = scaler.fit_transform(dados)
                print(dados_normalizados)
                """
        },
        "Push": {
            "significado": "Operação que adiciona um elemento ao topo de uma pilha (stack).",
            "uso": "É utilizada em estruturas de dados baseadas em LIFO (último a entrar, primeiro a sair).",
            "exemplo": """
                stack = []

                # Adicionando elementos à pilha
                stack.append(10)
                stack.append(20)
                print(stack)  # Saída: [10, 20]
                """
        },
        "Pop_stack": {
            "significado": "Operação que remove e retorna o elemento do topo de uma pilha.",
            "uso": "É utilizada para recuperar elementos em estruturas LIFO.",
            "exemplo": """
                stack = [10, 20, 30]

                topo = stack.pop()
                print(topo)  # Saída: 30
                print(stack)  # Saída: [10, 20]
                """
        },
        "Polynomial_features": {
            "significado": "Transformação usada para criar combinações de recursos em termos polinomiais para aprendizado de máquina.",
            "uso": "É utilizada para aumentar a capacidade de modelos simples, como a regressão linear.",
            "exemplo": """
                from sklearn.preprocessing import PolynomialFeatures
                import numpy as np

                X = np.array([[1, 2], [3, 4]])
                poly = PolynomialFeatures(degree=2)
                X_poly = poly.fit_transform(X)
                print(X_poly)
                """
        },
        "Plt_legend": {
            "significado": "Função em Matplotlib para adicionar legendas a gráficos.",
            "uso": "É utilizada para identificar diferentes séries de dados em gráficos.",
            "exemplo": """
                import matplotlib.pyplot as plt

                plt.plot([1, 2, 3], label='Linha 1')
                plt.plot([3, 2, 1], label='Linha 2')
                plt.legend()
                plt.show()
                """
        },
        "Precision_score": {
            "significado": "Métrica de avaliação usada para medir a precisão de um modelo, calculada como a proporção de predições positivas corretas.",
            "uso": "É utilizada em problemas de classificação para avaliar o desempenho do modelo.",
            "exemplo": """
                from sklearn.metrics import precision_score

                y_true = [0, 1, 1, 1]
                y_pred = [0, 1, 0, 1]
                precision = precision_score(y_true, y_pred)
                print('Precisão:', precision)  # Saída: 1.0
                """
        },
        "Pipe_operation": {
            "significado": "Método para conectar a saída de um comando ou processo diretamente à entrada de outro, geralmente em sistemas baseados em Unix.",
            "uso": "Utilizado para criar fluxos de dados eficientes entre comandos ou funções.",
            "exemplo": """
                # Exemplo em Bash (uso de pipe)
                ls -l | grep '.py'
                """
        },
        "Plt_bar": {
            "significado": "Função em Matplotlib para criar gráficos de barras.",
            "uso": "Utilizada para representar dados categóricos visualmente.",
            "exemplo": """
                import matplotlib.pyplot as plt

                categorias = ['A', 'B', 'C']
                valores = [10, 20, 15]
                plt.bar(categorias, valores)
                plt.title('Gráfico de Barras')
                plt.show()
                """
        },
        "Proxy_handler": {
            "significado": "Componente ou função que gerencia solicitações enviadas por meio de um proxy em redes ou em aplicativos.",
            "uso": "Utilizado para configurar proxies em conexões HTTP ou HTTPS.",
            "exemplo": """
                from urllib.request import ProxyHandler, build_opener

                proxy = ProxyHandler({'http': 'http://proxy.com:8080'})
                opener = build_opener(proxy)
                response = opener.open('http://example.com')
                print(response.read())
                """
        },
        "Print_exception": {
            "significado": "Método para exibir informações detalhadas sobre uma exceção durante a execução de um programa.",
            "uso": "Utilizado em depuração e análise de erros.",
            "exemplo": """
                try:
                    x = 1 / 0
                except Exception as e:
                    print('Erro:', e)
                """
        },
        "Post_request": {
            "significado": "Solicitação HTTP usada para enviar dados ao servidor, geralmente para criar ou atualizar recursos.",
            "uso": "Utilizada em APIs e formulários web para enviar informações.",
            "exemplo": """
                import requests

                dados = {'nome': 'João', 'idade': 30}
                response = requests.post('http://api.exemplo.com/dados', json=dados)
                print(response.status_code)
                """
        },
        "Plt_pie": {
            "significado": "Função em Matplotlib para criar gráficos de pizza.",
            "uso": "Utilizada para representar proporções entre categorias.",
            "exemplo": """
                import matplotlib.pyplot as plt

                labels = ['A', 'B', 'C']
                valores = [30, 50, 20]
                plt.pie(valores, labels=labels, autopct='%1.1f%%')
                plt.title('Gráfico de Pizza')
                plt.show()
                """
        },
        "Proxy_object": {
            "significado": "Objeto que atua como intermediário para controlar o acesso a outro objeto ou recurso.",
            "uso": "Utilizado para implementar padrões de design como Proxy, Cache e Lazy Initialization.",
            "exemplo": """
                class Proxy:
                    def __init__(self, obj):
                        self._obj = obj
                    
                    def __getattr__(self, name):
                        print(f'Acessando {name}')
                        return getattr(self._obj, name)

                obj = Proxy([1, 2, 3])
                obj.append(4)
                print(obj)
                """
        },
        "Pandas_series": {
            "significado": "Estrutura unidimensional em pandas para armazenar e manipular dados.",
            "uso": "Utilizada para representar dados de uma coluna em um DataFrame ou listas indexadas.",
            "exemplo": """
                import pandas as pd

                serie = pd.Series([10, 20, 30], index=['A', 'B', 'C'])
                print(serie)
                """
        },
        "Plt_scatter": {
            "significado": "Função em Matplotlib para criar gráficos de dispersão.",
            "uso": "Utilizada para visualizar a relação entre duas variáveis.",
            "exemplo": """
                import matplotlib.pyplot as plt

                x = [1, 2, 3, 4]
                y = [10, 20, 25, 30]
                plt.scatter(x, y)
                plt.title('Gráfico de Dispersão')
                plt.show()
                """
        },
        "Plt_grid": {
            "significado": "Função em Matplotlib para adicionar grades aos gráficos.",
            "uso": "Utilizada para melhorar a legibilidade dos gráficos.",
            "exemplo": """
                import matplotlib.pyplot as plt

                x = [1, 2, 3, 4]
                y = [10, 20, 25, 30]
                plt.plot(x, y)
                plt.grid(True)
                plt.title('Gráfico com Grade')
                plt.show()
                """
        },
        "Plt_hist": {
            "significado": "Função em Matplotlib para criar histogramas.",
            "uso": "Utilizada para visualizar a distribuição de uma variável.",
            "exemplo": """
                import matplotlib.pyplot as plt
                import numpy as np

                dados = np.random.randn(1000)
                plt.hist(dados, bins=30, alpha=0.7)
                plt.title('Histograma')
                plt.show()
                """
        },
        "Plt_savefig": {
            "significado": "Função em Matplotlib usada para salvar o gráfico gerado em um arquivo.",
            "uso": "Utilizada para exportar gráficos em formatos como PNG, PDF ou SVG.",
            "exemplo": """
                import matplotlib.pyplot as plt

                x = [1, 2, 3, 4]
                y = [10, 20, 25, 30]
                plt.plot(x, y)
                plt.title('Gráfico Exemplo')
                plt.savefig('grafico.png')
                """
        },
        "Plt_title": {
            "significado": "Função em Matplotlib para adicionar um título ao gráfico.",
            "uso": "Utilizada para descrever brevemente o conteúdo ou objetivo do gráfico.",
            "exemplo": """
                import matplotlib.pyplot as plt

                plt.plot([1, 2, 3], [4, 5, 6])
                plt.title('Meu Gráfico')
                plt.show()
                """
        },
        "Plt_xlabel": {
            "significado": "Função em Matplotlib para definir o rótulo do eixo X no gráfico.",
            "uso": "Utilizada para identificar o significado dos dados no eixo X.",
            "exemplo": """
                import matplotlib.pyplot as plt

                plt.plot([1, 2, 3], [4, 5, 6])
                plt.xlabel('Eixo X')
                plt.show()
                """
        },
        "Plt_ylabel": {
            "significado": "Função em Matplotlib para definir o rótulo do eixo Y no gráfico.",
            "uso": "Utilizada para identificar o significado dos dados no eixo Y.",
            "exemplo": """
                import matplotlib.pyplot as plt

                plt.plot([1, 2, 3], [4, 5, 6])
                plt.ylabel('Eixo Y')
                plt.show()
                """
        },
        "Plt_show": {
            "significado": "Função em Matplotlib usada para exibir o gráfico gerado em uma janela ou interface interativa.",
            "uso": "Utilizada para mostrar os gráficos após serem configurados.",
            "exemplo": """
                import matplotlib.pyplot as plt

                plt.plot([1, 2, 3], [4, 5, 6])
                plt.show()
                """
        },
        "Plt_colorbar": {
            "significado": "Função em Matplotlib para adicionar uma barra de cores a um gráfico, representando a escala de valores.",
            "uso": "Utilizada em gráficos como mapas de calor ou contornos para indicar o significado das cores.",
            "exemplo": """
                import matplotlib.pyplot as plt
                import numpy as np

                data = np.random.rand(10, 10)
                plt.imshow(data, cmap='viridis')
                plt.colorbar()
                plt.show()
                """
        },
        "Plt_contour": {
            "significado": "Função em Matplotlib para criar gráficos de contorno baseados em dados tridimensionais ou bidimensionais.",
            "uso": "Utilizada para representar linhas de igual valor em mapas ou superfícies.",
            "exemplo": """
                import matplotlib.pyplot as plt
                import numpy as np

                x = np.linspace(-5, 5, 100)
                y = np.linspace(-5, 5, 100)
                X, Y = np.meshgrid(x, y)
                Z = np.sin(np.sqrt(X**2 + Y**2))

                plt.contour(X, Y, Z, levels=10, cmap='coolwarm')
                plt.colorbar()
                plt.title('Gráfico de Contornos')
                plt.show()
                """
        },
        "Plt_fill_between": {
            "significado": "Função em Matplotlib para preencher a área entre duas curvas ou uma curva e um eixo.",
            "uso": "Utilizada para destacar regiões em gráficos, como intervalos de confiança ou áreas específicas.",
            "exemplo": """
                import matplotlib.pyplot as plt
                import numpy as np

                x = np.linspace(0, 10, 100)
                y1 = np.sin(x)
                y2 = np.cos(x)

                plt.fill_between(x, y1, y2, color='lightblue', alpha=0.5)
                plt.plot(x, y1, label='Seno')
                plt.plot(x, y2, label='Cosseno')
                plt.legend()
                plt.show()
                """
        },
        "Plt_annotate": {
            "significado": "Função em Matplotlib para adicionar anotações a um gráfico, como textos ou setas apontando para pontos específicos.",
            "uso": "Utilizada para destacar ou explicar pontos de interesse no gráfico.",
            "exemplo": """
                import matplotlib.pyplot as plt

                x = [1, 2, 3, 4]
                y = [10, 20, 15, 25]
                plt.plot(x, y)

                plt.annotate('Ponto Máximo', xy=(4, 25), xytext=(3, 22),
                            arrowprops=dict(facecolor='black', arrowstyle='->'))
                plt.show()
                """
        },
        "Plt_boxplot": {
            "significado": "Função em Matplotlib para criar gráficos de caixa (boxplots) que representam a distribuição de um conjunto de dados.",
            "uso": "Utilizada para visualizar a mediana, quartis e valores atípicos em dados.",
            "exemplo": """
                import matplotlib.pyplot as plt

                data = [7, 8, 5, 6, 9, 4, 7, 8, 5, 6]
                plt.boxplot(data)
                plt.title('Boxplot dos Dados')
                plt.show()
                """
        },
        "Plt_stackplot": {
            "significado": "Função em Matplotlib para criar gráficos de área empilhados, representando várias séries de dados como áreas preenchidas.",
            "uso": "Utilizada para visualizar a composição de dados ao longo de um eixo.",
            "exemplo": """
                import matplotlib.pyplot as plt

                x = [1, 2, 3, 4, 5]
                y1 = [1, 2, 3, 4, 5]
                y2 = [2, 3, 4, 5, 6]
                y3 = [3, 4, 5, 6, 7]

                plt.stackplot(x, y1, y2, y3, labels=['A', 'B', 'C'], alpha=0.5)
                plt.legend(loc='upper left')
                plt.title('Gráfico de Áreas Empilhadas')
                plt.show()
                """
        },
        "Plt_quiver": {
            "significado": "Função em Matplotlib para criar gráficos de vetores, representando magnitude e direção em coordenadas bidimensionais.",
            "uso": "Utilizada para visualização de campos vetoriais, como fluxos de vento ou gradientes.",
            "exemplo": """
                import matplotlib.pyplot as plt
                import numpy as np

                x, y = np.meshgrid(np.arange(-2, 2, 0.5), np.arange(-2, 2, 0.5))
                u = -y
                v = x

                plt.quiver(x, y, u, v)
                plt.title('Gráfico de Vetores (Quiver)')
                plt.show()
                """
        },
        "Plt_arrow": {
            "significado": "Função em Matplotlib para desenhar uma única seta em um gráfico.",
            "uso": "Utilizada para destacar direções ou movimentos em um gráfico.",
            "exemplo": """
                import matplotlib.pyplot as plt

                plt.plot([0, 10], [0, 10])
                plt.arrow(2, 2, 5, 5, head_width=0.5, head_length=0.7, fc='red', ec='red')
                plt.title('Gráfico com Seta')
                plt.show()
                """
        },
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
