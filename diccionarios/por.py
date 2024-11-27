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
        "input": {
            "significado": "Lê dados inseridos pelo usuário no console",
            "uso": "Serve para interagir com o usuário e obter informações.",
            "ejemplo": "input('insira um número')"
        },
        "immutable": {
            "significado": "Propriedade de um objeto ou estrutura de dados que não pode ser modificado após sua criação.",
            "uso": "É usado para garantir que o conteúdo de um objeto não seja alterado depois de definido.",
            "exemplo": """
                tupla = (1, 2, 3)
                # tupla[0] = 4  # Isso geraria um erro, pois tuplas são imutáveis.
                """
        },
        "index": {
            "significado": "Posição de um elemento dentro de uma sequência ou estrutura de dados.",
            "uso": "É utilizado para acessar ou referenciar elementos em listas, tuplas ou outros tipos de dados sequenciais.",
            "exemplo": """
                lista = [10, 20, 30]
                print(lista[1])  # Saída: 20
                """
        },
        "instance": {
            "significado": "Objeto individual de uma classe em programação orientada a objetos.",
            "uso": "É utilizado para criar e manipular um objeto que foi instanciado a partir de uma classe.",
            "exemplo": """
                class Carro:
                    def __init__(self, modelo):
                        self.modelo = modelo

                carro1 = Carro("Fusca")  # Instância da classe Carro
                print(carro1.modelo)  # Saída: Fusca
                """
        },
        "inheritance": {
            "significado": "Mecanismo da programação orientada a objetos onde uma classe herda propriedades e métodos de outra.",
            "uso": "É utilizado para criar uma nova classe com base em uma classe existente, reutilizando seu código.",
            "exemplo": """
                class Animal:
                    def falar(self):
                        print("Som do animal")

                class Cachorro(Animal):
                    def falar(self):
                        print("Latido")

                cachorro = Cachorro()
                cachorro.falar()  # Saída: Latido
                """
        },
        "interface": {
            "significado": "Contrato que define um conjunto de métodos que uma classe deve implementar, sem fornecer a implementação.",
            "uso": "É utilizado para especificar o comportamento esperado de classes que implementam a interface.",
            "exemplo": """
                from abc import ABC, abstractmethod

                class Forma(ABC):
                    @abstractmethod
                    def area(self):
                        pass

                class Circulo(Forma):
                    def area(self):
                        return 3.14 * 10 * 10
                """
        },
        "instance_method": {
            "significado": "Método que é definido dentro de uma classe e opera sobre instâncias dessa classe.",
            "uso": "É utilizado para realizar operações ou manipular dados associados a uma instância específica de uma classe.",
            "exemplo": """
                class Pessoa:
                    def saudacao(self):
                        print("Olá, sou uma pessoa.")

                p = Pessoa()
                p.saudacao()  # Saída: Olá, sou uma pessoa.
                """
        },
        "immutable_set": {
            "significado": "Estrutura de dados do tipo conjunto (set) que não pode ser modificada após sua criação.",
            "uso": "É usado quando se deseja garantir que os elementos de um conjunto não sejam alterados após a criação.",
            "exemplo": """
                conjunto_imutavel = frozenset([1, 2, 3])
                # conjunto_imutavel.add(4)  # Isso geraria um erro, pois o conjunto é imutável
                """
        },
        "increment": {
            "significado": "Ação de aumentar o valor de uma variável ou contador.",
            "uso": "É utilizado para adicionar um valor a uma variável, frequentemente usado em contagens ou iterações.",
            "exemplo": """
                contador = 0
                contador += 1  # Incrementa o valor de contador
                print(contador)  # Saída: 1
                """
        },
        "input_validation": {
            "significado": "Processo de verificar se os dados inseridos são válidos de acordo com critérios específicos.",
            "uso": "É utilizado para garantir que os dados fornecidos pelo usuário ou sistema estejam no formato correto antes de serem processados.",
            "exemplo": """
                idade = int(input("Qual a sua idade? "))
                if idade < 0:
                    print("Idade inválida.")
                else:
                    print("Idade válida.")
                """
        },
        "indexing": {
            "significado": "Ação de acessar um elemento em uma estrutura de dados sequencial usando seu índice.",
            "uso": "É utilizado para buscar elementos em listas, tuplas, ou strings usando a posição de cada item.",
            "exemplo": """
                lista = ['a', 'b', 'c']
                print(lista[0])  # Saída: 'a'
                """
        },
        "insertion_sort": {
            "significado": "Algoritmo de ordenação que constrói a sequência ordenada um item de cada vez, inserindo o item na posição correta.",
            "uso": "É utilizado para ordenar listas ou arrays de forma eficiente para pequenos conjuntos de dados.",
            "exemplo": """
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
                """
        },
        "integer": {
            "significado": "Tipo de dado que representa números inteiros, sem parte decimal.",
            "uso": "É utilizado para armazenar valores numéricos inteiros.",
            "exemplo": """
                numero = 42
                print(type(numero))  # Saída: <class 'int'>
                """
        },
        "iterable": {
            "significado": "Objeto que pode ser iterado (percorrido) em um loop, como listas, tuplas e strings.",
            "uso": "É utilizado para referir-se a qualquer objeto que tenha suporte a iteração, permitindo o acesso aos seus elementos um a um.",
            "exemplo": """
                lista = [1, 2, 3]
                for item in lista:
                    print(item)
                """
        },
        "identifier": {
            "significado": "Nome que identifica uma variável, função, classe ou outro elemento no código.",
            "uso": "É utilizado para dar nome a componentes de um programa, como variáveis e funções, para que possam ser referenciados no código.",
            "exemplo": """
                nome = "João"
                idade = 30
                print(nome, idade)  # Saída: João 30
                """
        },
        "iteration": {
                "significado": "Processo de percorrer uma sequência ou estrutura de dados, como uma lista ou tupla, para acessar seus elementos um a um.",
                "uso": "É utilizado para realizar operações em cada elemento de uma sequência, geralmente com o uso de um laço de repetição.",
                "exemplo": """
                    lista = [1, 2, 3]
                    for item in lista:
                        print(item)
                    """
            },
            "IP_address": {
                "significado": "Endereço único atribuído a dispositivos conectados a uma rede, usado para identificá-los e permitir a comunicação.",
                "uso": "É utilizado para identificar de forma única dispositivos em redes locais ou na internet.",
                "exemplo": """
                    ip = "192.168.1.1"
                    print("IP do dispositivo:", ip)
                    """
            },
            "if_statement": {
                "significado": "Estrutura condicional utilizada para executar um bloco de código se uma condição for verdadeira.",
                "uso": "É utilizado para controlar o fluxo de execução de um programa, realizando diferentes ações dependendo das condições.",
                "exemplo": """
                    idade = 18
                    if idade >= 18:
                        print("Maior de idade")
                    else:
                        print("Menor de idade")
                    """
            },
            "interface_class": {
                "significado": "Classe que define um conjunto de métodos que outras classes devem implementar, sem fornecer uma implementação concreta.",
                "uso": "É utilizado para criar contratos de comportamento que as classes que a implementarem devem seguir.",
                "exemplo": """
                    from abc import ABC, abstractmethod

                    class Veiculo(ABC):
                        @abstractmethod
                        def mover(self):
                            pass

                    class Carro(Veiculo):
                        def mover(self):
                            print("Carro em movimento")
                    """
            },
            "input_device": {
                "significado": "Dispositivo utilizado para inserir dados em um computador ou sistema, como teclado, mouse, ou scanner.",
                "uso": "É utilizado para permitir que o usuário ou outro sistema forneça dados para o computador.",
                "exemplo": """
                    teclado = "Teclado USB"
                    print("Dispositivo de entrada:", teclado)
                    """
            },
            "introspection": {
                "significado": "Processo de inspeção de objetos em tempo de execução para obter informações sobre suas propriedades e comportamentos.",
                "uso": "É utilizado para examinar e manipular a estrutura interna de um objeto ou classe em um programa.",
                "exemplo": """
                    x = 42
                    print(type(x))  # Saída: <class 'int'>
                    print(dir(x))  # Saída: lista de atributos e métodos do objeto
                    """
            },
            "instance_variable": {
                "significado": "Variável que pertence a uma instância específica de uma classe, armazenando dados relacionados àquela instância.",
                "uso": "É utilizado para armazenar dados que são específicos a cada objeto instanciado de uma classe.",
                "exemplo": """
                    class Carro:
                        def __init__(self, modelo):
                            self.modelo = modelo

                    carro1 = Carro("Fusca")
                    print(carro1.modelo)  # Saída: Fusca
                    """
            },
            "index_out_of_bounds": {
                "significado": "Erro que ocorre quando se tenta acessar um índice fora do intervalo válido de uma sequência ou lista.",
                "uso": "É utilizado para descrever um erro comum quando se trabalha com índices em sequências de dados.",
                "exemplo": """
                    lista = [1, 2, 3]
                    # print(lista[5])  # Isso causaria um erro de índice fora dos limites
                    """
            },
            "input_output": {
                "significado": "Operações que envolvem a recepção (entrada) e o envio (saída) de dados entre o programa e o ambiente externo.",
                "uso": "É utilizado para descrever a interação de um programa com o usuário ou outros sistemas, por meio de entrada e saída de dados.",
                "exemplo": """
                    nome = input("Qual seu nome? ")
                    print("Olá, " + nome)
                    """
            },
            "inplace": {
                "significado": "Operação realizada diretamente sobre os dados originais, sem criar uma cópia.",
                "uso": "É utilizado para modificar os dados diretamente na memória sem a necessidade de alocar novo espaço para os dados.",
                "exemplo": """
                    lista = [1, 2, 3]
                    lista.append(4)  # Modifica a lista original inplace
                    print(lista)  # Saída: [1, 2, 3, 4]
                    """
            },
            "inherit": {
                "significado": "Ação de uma classe herdar propriedades e métodos de outra classe, permitindo reutilização de código.",
                "uso": "É utilizado para criar classes derivadas, que herdam funcionalidades de classes base.",
                "exemplo": """
                    class Animal:
                        def falar(self):
                            print("Som do animal")

                    class Cachorro(Animal):
                        def falar(self):
                            print("Latido")

                    cachorro = Cachorro()
                    cachorro.falar()  # Saída: Latido
                    """
            },
            "index_of": {
                "significado": "Método utilizado para encontrar a posição (índice) de um elemento dentro de uma sequência, como uma lista ou string.",
                "uso": "É utilizado para localizar a posição de um item em uma lista ou sequência.",
                "exemplo": """
                    lista = [10, 20, 30, 40]
                    print(lista.index(30))  # Saída: 2
                    """
            },
            "instruction_set": {
                "significado": "Conjunto de instruções que um processador é capaz de executar, formando a base para a execução de programas.",
                "uso": "É utilizado para descrever as operações que um processador pode realizar para executar um programa.",
                "exemplo": """
                    A arquitetura de um processador define seu conjunto de instruções.
                    """
            },
            "iterable_object": {
                "significado": "Objeto que pode ser percorrido em um laço de repetição, como listas, tuplas e strings.",
                "uso": "É utilizado para se referir a objetos que implementam o protocolo de iteração, permitindo o acesso a seus elementos sequencialmente.",
                "exemplo": """
                    lista = [1, 2, 3]
                    for item in lista:
                        print(item)
                    """
            },
            "image_processing": {
                "significado": "Técnicas e algoritmos usados para manipular e analisar imagens digitais.",
                "uso": "É utilizado para modificar, melhorar ou extrair informações de imagens por meio de processos computacionais.",
                "exemplo": """
                    import cv2
                    imagem = cv2.imread("imagem.jpg")
                    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
                    cv2.imshow("Imagem em cinza", imagem_cinza)
                    cv2.waitKey(0)
                    """
            },
            "indirect_addressing": {
                "significado": "Método de acesso a dados em que o endereço de memória é armazenado em um local, e o valor real é obtido a partir desse endereço.",
                "uso": "É utilizado para referenciar dados de forma indireta, permitindo maior flexibilidade e dinamismo na manipulação de memória.",
                "exemplo": """
                    # Isso envolve manipulação avançada de ponteiros e endereços em linguagens como C.
                    """
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
