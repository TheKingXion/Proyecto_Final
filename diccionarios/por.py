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
            "exemplo": '''
                def funcao():
                    return "Olá"

                print(callable(funcao))  # Saída: True
                print(callable(42))  # Saída: False
                '''
        },
        "chr": {
            "significado": "Retorna o caractere Unicode correspondente a um número inteiro.",
            "uso": "É utilizado para converter um código Unicode em sua representação de caractere.",
            "exemplo": '''
                print(chr(65))  # Saída: 'A'
                print(chr(8364))  # Saída: '€'
                '''
        },
        "class": {
            "significado": "Palavra-chave para definir uma classe em Python.",
            "uso": "É utilizada para criar objetos personalizados com atributos e métodos.",
            "exemplo": '''
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
            "exemplo": '''
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
            "exemplo": '''
                codigo = "print('Olá Mundo')"
                compilado = compile(codigo, '<string>', 'exec')
                exec(compilado)  # Saída: Olá Mundo
                '''
        },
        "complex": {
            "significado": "Cria um número complexo em Python.",
            "uso": "É utilizado para representar números complexos com parte real e imaginária.",
            "exemplo": '''
                c = complex(2, 3)
                print(c)  # Saída: (2+3j)
                print(c.real, c.imag)  # Saída: 2.0 3.0
                '''
        },
        "continue": {
            "significado": "Palavra-chave que salta para a próxima iteração de um loop.",
            "uso": "É utilizada para ignorar o restante do código na iteração atual.",
            "exemplo": '''
                for i in range(5):
                    if i == 2:
                        continue
                    print(i)  # Saída: 0 1 3 4
                '''
        },
        "copy": {
            "significado": "Cria uma cópia superficial de um objeto.",
            "uso": "É utilizada para duplicar estruturas de dados sem duplicar objetos aninhados.",
            "exemplo": '''
                import copy

                lista = [1, 2, [3, 4]]
                copia = copy.copy(lista)
                print(copia)  # Saída: [1, 2, [3, 4]]
                '''
        },
        "coroutine": {
            "significado": "Objeto que representa uma função assíncrona suspensa.",
            "uso": "É utilizada para lidar com tarefas assíncronas usando `async` e `await`.",
            "exemplo": '''
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
            "exemplo": '''
                lista = [1, 2, 2, 3]
                print(lista.count(2))  # Saída: 2
                '''
        },
        "clear": {
            "significado": "Remove todos os elementos de uma lista ou dicionário.",
            "uso": "É utilizada para esvaziar o conteúdo de uma lista ou dicionário.",
            "exemplo": '''
                lista = [1, 2, 3]
                lista.clear()
                print(lista)  # Saída: []
                '''
        },
        "cmath": {
            "significado": "Módulo que fornece funções matemáticas para trabalhar com números complexos.",
            "uso": "É utilizado para realizar operações matemáticas em números complexos.",
            "exemplo": '''
                import cmath

                numero = cmath.sqrt(-1)
                print(numero)  # Saída: 1j
                '''
        },
        "chain": {
            "significado": "Função que combina vários iteradores em um só.",
            "uso": "É utilizada para concatenar múltiplos iteradores.",
            "exemplo": '''
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
            "exemplo": '''
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
            "exemplo": '''
                import copyreg

                def criar_pessoa(nome, idade):
                    return {'nome': nome, 'idade': idade}

                copyreg.pickle(dict, criar_pessoa)
                '''
        },
        "counter": {
            "significado": "Classe no módulo `collections` que conta elementos hasháveis em uma sequência.",
            "uso": "É utilizada para contar a frequência de elementos em um iterável.",
            "exemplo": '''
                from collections import Counter

                contador = Counter([1, 2, 2, 3, 3, 3])
                print(contador)  # Saída: Counter({3: 3, 2: 2, 1: 1})
                '''
        },
        "cProfile": {
            "significado": "Módulo para a medição do desempenho de programas em Python.",
            "uso": "É utilizado para fazer perfis de código e analisar a eficiência do programa.",
            "exemplo": '''
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
            "exemplo": '''
                texto = 'ola mundo'
                print(texto.capitalize())  # Saída: 'Ola mundo'
                '''
        },
        "center": {
            "significado": "Método de string que centraliza uma string dentro de um campo de comprimento especificado.",
            "uso": "É utilizado para alinhar texto no centro de uma string com preenchimento.",
            "exemplo": '''
                texto = 'ola'
                print(texto.center(10, '*'))  # Saída: '**ola****'
                '''
        },
        "ceil": {
            "significado": "Função do módulo `math` que retorna o inteiro mais próximo maior ou igual a um número dado.",
            "uso": "É utilizada para arredondar um número para cima.",
            "exemplo": '''
                import math

                numero = 3.4
                print(math.ceil(numero))  # Saída: 4
                '''
        },
        "call": {
            "significado": "Método utilizado para invocar um objeto que é callable, como funções ou classes.",
            "uso": "É utilizado para chamar um objeto que pode ser executado.",
            "exemplo": '''
                def saudacao():
                    return 'Olá'

                print(callable(saudacao))  # Saída: True
                '''
        },
        "clamp": {
            "significado": "Função que restringe um valor dentro de um intervalo especificado.",
            "uso": "É utilizada para garantir que um valor permaneça dentro de um intervalo definido.",
            "exemplo": '''
                def clamp(valor, minimo, maximo):
                    return max(minimo, min(valor, maximo))

                print(clamp(5, 1, 10))  # Saída: 5
                '''
        },
        "choice": {
            "significado": "Função do módulo `random` que seleciona um elemento aleatório de uma sequência.",
            "uso": "É utilizada para escolher um valor aleatório de uma lista ou sequência.",
            "exemplo": '''
                import random

                lista = [1, 2, 3, 4, 5]
                print(random.choice(lista))  # Saída: um valor aleatório da lista
                '''
        },
        "collections": {
            "significado": "Módulo que implementa tipos de dados especializados como `Counter`, `deque`, `OrderedDict`, entre outros.",
            "uso": "É utilizado para trabalhar com coleções de dados de forma eficiente.",
            "exemplo": '''
                from collections import deque

                fila = deque([1, 2, 3])
                fila.append(4)
                print(fila)  # Saída: deque([1, 2, 3, 4])
                '''
        },
        "compress": {
            "significado": "Função no módulo `itertools` que permite comprimir elementos de um iterável.",
            "uso": "É utilizada para filtrar os elementos de um iterável com base em uma condição booleana.",
            "exemplo": '''
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
            "exemplo": '''
                numero_complexo = 3 + 4j
                print(numero_complexo.conjugate())  # Saída: (3-4j)
                '''
        },
        "ctypes": {
            "significado": "Módulo em Python que permite interagir com bibliotecas de C e realizar chamadas de funções de baixo nível.",
            "uso": "É utilizado para trabalhar com tipos de dados e funções de bibliotecas externas escritas em C.",
            "exemplo": '''
                import ctypes

                # Criar uma variável de tipo inteiro
                valor = ctypes.c_int(5)
                print(valor.value)  # Saída: 5
                '''
        },
        "clear_screen": {
            "significado": "Função utilizada para limpar a tela do console.",
            "uso": "É utilizada para remover o conteúdo visível do terminal ou console.",
            "exemplo": '''
                import os

                def clear_screen():
                    os.system('cls' if os.name == 'nt' else 'clear')

                clear_screen()
                '''
        },
        "call_later": {
            "significado": "Método utilizado para agendar a execução de uma função após um certo tempo.",
            "uso": "É utilizado em programação assíncrona para executar tarefas após um atraso.",
            "exemplo": '''
                import asyncio

                async def tarefa():
                    print('Tarefa executada')

                asyncio.get_event_loop().call_later(2, asyncio.create_task, tarefa())
                '''
        },
        "chunk": {
            "significado": "Técnica que divide um iterável em partes menores ou blocos.",
            "uso": "É utilizada para dividir grandes volumes de dados em partes mais manejáveis.",
            "exemplo": '''
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
            "exemplo": '''
                import itertools

                ciclo = itertools.cycle([1, 2, 3])
                for i in range(6):
                    print(next(ciclo))  # Saída: 1, 2, 3, 1, 2, 3
                '''
        },
        "coerce": {
            "significado": "Função que tenta converter um valor em um tipo compatível.",
            "uso": "Era utilizada para forçar a conversão de um valor para um tipo de dados específico.",
            "exemplo": '''
                # A função coerce foi removida em versões modernas do Python.
                '''
        },
        "current_thread": {
            "significado": "Método do módulo `threading` que retorna a thread atual de execução.",
            "uso": "É utilizado para obter a thread de execução onde o código está sendo executado.",
            "exemplo": '''
                import threading

                def mostrar_thread():
                    print(threading.current_thread())

                mostrar_thread()
                '''
        },
        "configparser": {
            "significado": "Módulo que permite manipular arquivos de configuração, como arquivos INI.",
            "uso": "É utilizado para ler, escrever e modificar arquivos de configuração.",
            "exemplo": '''
                import configparser

                config = configparser.ConfigParser()
                config.read('config.ini')

                print(config['DEFAULT']['color'])  # Saída: vermelho
                '''
        },
        "compileall": {
            "significado": "Módulo em Python que compila todos os arquivos `.py` em um diretório e seus subdiretórios.",
            "uso": "É utilizado para compilar código Python para bytecode, o que pode melhorar o desempenho da execução.",
            "exemplo": '''
                import compileall

                compileall.compile_dir('meu_diretorio')
                '''
        },
        "copytree": {
            "significado": "Função no módulo `shutil` que copia um diretório completo, incluindo seu conteúdo, para outro destino.",
            "uso": "É utilizada para copiar um diretório e todo o seu conteúdo para um novo local.",
            "exemplo": '''
                import shutil

                shutil.copytree('origem', 'destino')
                '''
        },
    },
    "d": {
        "def": {
            "significado": "Palavra-chave em Python usada para definir uma função.",
            "uso": "É utilizada para criar uma nova função com um nome e um bloco de código.",
            "exemplo": '''
                def saudacao():
                    print('Olá Mundo')

                saudacao()  # Saída: Olá Mundo
                '''
        },
        "delattr": {
            "significado": "Função que remove um atributo de um objeto em Python.",
            "uso": "É utilizada para excluir um atributo específico de um objeto.",
            "exemplo": '''
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
            "exemplo": '''
                import pandas as pd

                dados = {'Nome': ['João', 'Ana'], 'Idade': [28, 22]}
                df = pd.DataFrame(dados)
                print(df)
                '''
        },
        "decode": {
            "significado": "Método utilizado para decodificar dados binários para um formato de texto, geralmente em uma codificação como UTF-8.",
            "uso": "É utilizado para converter dados binários em cadeias de texto legíveis.",
            "exemplo": '''
                codificado = b'Olá Mundo'
                decodificado = codificado.decode('utf-8')
                print(decodificado)  # Saída: Olá Mundo
                '''
        },
        "decimal": {
            "significado": "Módulo em Python que fornece suporte para realizar cálculos com decimais de precisão arbitrária.",
            "uso": "É utilizado para realizar operações aritméticas precisas sem os erros de arredondamento típicos dos números de ponto flutuante.",
            "exemplo": '''
                from decimal import Decimal

                x = Decimal('0.1')
                y = Decimal('0.2')
                print(x + y)  # Saída: 0.3
                '''
        },
        "device": {
            "significado": "Termo geral para se referir a qualquer dispositivo de hardware ou sistema onde um programa é executado.",
            "uso": "É utilizado para se referir a dispositivos como computadores, telefones móveis, etc.",
            "exemplo": "Não é um termo específico de Python, mas pode ser usado em bibliotecas como TensorFlow para se referir a dispositivos de processamento como CPU ou GPU."
        },
        "dict.get": {
            "significado": "Método dos dicionários em Python que retorna o valor de uma chave especificada ou um valor padrão se a chave não existir.",
            "uso": "É utilizado para obter o valor associado a uma chave sem gerar um erro se a chave não existir.",
            "exemplo": '''
                d = {'a': 1, 'b': 2}
                print(d.get('a'))  # Saída: 1
                print(d.get('c', 'Não encontrado'))  # Saída: Não encontrado
                '''
        },
        "dropna": {
            "significado": "Método em Pandas utilizado para remover valores ausentes (NaN) em um DataFrame ou Série.",
            "uso": "É utilizado para limpar os dados removendo as linhas ou colunas que contêm valores nulos.",
            "exemplo": '''
                import pandas as pd

                df = pd.DataFrame({'A': [1, 2, None], 'B': [None, 3, 4]})
                print(df.dropna())
                '''
        },
        "dtype": {
            "significado": "Propriedade dos arrays em Numpy ou das colunas em um DataFrame do Pandas que indica o tipo de dado dos elementos.",
            "uso": "É utilizada para obter ou especificar o tipo de dados de um array ou coluna.",
            "exemplo": '''
                import numpy as np

                arr = np.array([1, 2, 3])
                print(arr.dtype)  # Saída: int64
                '''
        },
        "deque.appendleft": {
            "significado": "Método do tipo de dado `deque` no módulo `collections` que adiciona um elemento ao início da deque.",
            "uso": "É utilizado para inserir um novo elemento na parte esquerda de uma deque.",
            "exemplo": '''
                from collections import deque

                d = deque([2, 3, 4])
                d.appendleft(1)
                print(d)  # Saída: deque([1, 2, 3, 4])
                '''
        },
        "dict.update": {
            "significado": "Método dos dicionários em Python que atualiza um dicionário com os elementos de outro dicionário ou iterável.",
            "uso": "É utilizado para adicionar ou modificar elementos em um dicionário usando outro dicionário ou iterável.",
            "exemplo": '''
                d1 = {'a': 1, 'b': 2}
                d2 = {'b': 3, 'c': 4}
                d1.update(d2)
                print(d1)  # Saída: {'a': 1, 'b': 3, 'c': 4}
                '''
        },
        "del": {
            "significado": "Palavra-chave em Python que remove um atributo ou um elemento de uma coleção.",
            "uso": "É utilizada para remover elementos de uma lista, atributo de um objeto ou uma variável.",
            "exemplo": '''
                lista = [1, 2, 3]
                del lista[1]
                print(lista)  # Saída: [1, 3]
                '''
        },
        "dict": {
            "significado": "Tipo de dado em Python que representa um dicionário, uma coleção de pares chave-valor.",
            "uso": "É utilizado para armazenar e manipular dados de forma eficiente, associando chaves únicas a valores.",
            "exemplo": '''
                d = {'a': 1, 'b': 2}
                print(d['a'])  # Saída: 1
                '''
        },
        "dir": {
            "significado": "Função que retorna uma lista dos atributos e métodos de um objeto.",
            "uso": "É utilizada para obter informações sobre os métodos e atributos disponíveis para um objeto ou módulo.",
            "exemplo": '''
                x = [1, 2, 3]
                print(dir(x))
                '''
        },
        "divmod": {
            "significado": "Função que recebe dois números e retorna uma tupla com o quociente e o resto da sua divisão.",
            "uso": "É utilizada para obter tanto o quociente quanto o resto de uma divisão em uma única operação.",
            "exemplo": '''
                resultado = divmod(9, 4)
                print(resultado)  # Saída: (2, 1)
                '''
        },
        "deque": {
            "significado": "Tipo de dado no módulo `collections` do Python que representa uma fila duplamente terminada, permitindo adicionar e remover elementos de ambos os extremos de forma eficiente.",
            "uso": "É usado para implementar filas e pilhas de maneira eficiente.",
            "exemplo": '''
                from collections import deque

                d = deque([1, 2, 3])
                d.append(4)
                print(d)  # Saída: deque([1, 2, 3, 4])
                '''
        },
        "defaultdict": {
            "significado": "Classe no módulo `collections` que estende o dicionário padrão e permite definir um valor padrão para chaves inexistentes.",
            "uso": "É usado para evitar erros ao acessar chaves não existentes, fornecendo um valor padrão.",
            "exemplo": '''
                from collections import defaultdict

                d = defaultdict(int)
                d['a'] += 1
                print(d)  # Saída: defaultdict(<class 'int'>, {'a': 1})
                '''
        },
        "decode": {
            "significado": "Método usado para converter dados binários em texto em uma codificação específica.",
            "uso": "É usado para decodificar uma sequência de bytes em uma string de texto em uma codificação específica.",
            "exemplo": '''
                encoded = b'Olá Mundo'
                decoded = encoded.decode('utf-8')
                print(decoded)  # Saída: Olá Mundo
                '''
        },
        "deflate": {
            "significado": "Algoritmo de compressão de dados sem perda, usado para reduzir o tamanho de arquivos.",
            "uso": "É usado para compactar dados em um formato mais eficiente.",
            "exemplo": '''
                import zlib

                data = b'Olá Mundo'*100
                compressed = zlib.compress(data)
                print(compressed)
                '''
        },
        "deepcopy": {
            "significado": "Função do módulo `copy` que cria uma cópia profunda de um objeto, ou seja, copia todos os elementos do objeto original, incluindo objetos dentro de objetos.",
            "uso": "É usado quando é necessário fazer uma cópia completa e independente de um objeto.",
            "exemplo": '''
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
            "exemplo": '''
                import torch

                tensor = torch.tensor([1, 2, 3])
                detached_tensor = tensor.detach()
                print(detached_tensor)  # Saída: tensor([1, 2, 3])
                '''
        },
        "dump": {
            "significado": "Método da biblioteca `pickle` que serializa um objeto e o grava em um arquivo.",
            "uso": "É usado para salvar um objeto em um arquivo de forma serializada.",
            "exemplo": '''
                import pickle

                data = {'a': 1, 'b': 2}
                with open('data.pkl', 'wb') as f:
                    pickle.dump(data, f)
                '''
        },
        "dumps": {
            "significado": "Método da biblioteca `pickle` que serializa um objeto e o retorna como uma string de bytes.",
            "uso": "É usado para converter um objeto em um formato de string para armazenamento ou transmissão.",
            "exemplo": '''
                import pickle

                data = {'a': 1, 'b': 2}
                serialized = pickle.dumps(data)
                print(serialized)
                '''
        },
        "difference": {
            "significado": "Método de conjuntos no Python que retorna a diferença entre dois ou mais conjuntos.",
            "uso": "É usado para encontrar os elementos que estão em um conjunto, mas não nos outros.",
            "exemplo": '''
                a = {1, 2, 3}
                b = {2, 3, 4}
                print(a.difference(b))  # Saída: {1}
                '''
        },
        "difference_update": {
            "significado": "Método de conjuntos no Python que remove os elementos de um conjunto que estão presentes em outro conjunto.",
            "uso": "É usado para modificar um conjunto, removendo os elementos que se encontram em outro conjunto.",
            "exemplo": '''
                a = {1, 2, 3}
                b = {2, 3, 4}
                a.difference_update(b)
                print(a)  # Saída: {1}
                '''
        },
        "decode_header": {
            "significado": "Função do módulo `email.header` que decodifica um cabeçalho de e-mail.",
            "uso": "É usada para decodificar um cabeçalho de e-mail que pode estar em diferentes codificações.",
            "exemplo": '''
                from email.header import decode_header

                header = '=?utf-8?B?SG9sYSBNdW5kbyA8MTIzNDU+?='
                decoded, encoding = decode_header(header)[0]
                print(decoded.decode(encoding))  # Saída: Olá Mundo <12345>
                '''
        },
        "disk_usage": {
            "significado": "Função do módulo `shutil` que retorna o uso do disco de um caminho ou diretório.",
            "uso": "É usada para obter informações sobre o espaço usado e disponível em um sistema de arquivos.",
            "exemplo": '''
                import shutil

                usage = shutil.disk_usage('/')
                print(usage)  # Saída: usage(total=500000000, used=200000000, free=300000000)
                '''
        },
        "datetime": {
            "significado": "Módulo do Python que fornece classes para trabalhar com datas e horas.",
            "uso": "É usado para manipular e trabalhar com datas, horas e tempos em geral.",
            "exemplo": '''
                import datetime

                agora = datetime.datetime.now()
                print(agora)  # Saída: 2024-11-22 12:00:00.123456
                '''
        },
        "disk_cache": {
            "significado": "Armazenamento em cache no disco para melhorar a velocidade de acesso a dados ou resultados computacionais.",
            "uso": "É usado para armazenar temporariamente resultados ou dados no disco para evitar a necessidade de recalcular ou obter novamente os dados.",
            "exemplo": '''
                import joblib

                result = joblib.Memory('cache_dir').cache(some_function)
                '''
        },
    },
    "e": {
        "enumerate": {
            "significado": "Função incorporada do Python que adiciona um contador a um iterável e o retorna como um objeto iterável de tuplas.",
            "uso": "É usada para obter tanto o índice quanto o valor dos elementos em um iterável.",
            "exemplo": '''
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
            "exemplo": '''
                x = 2
                resultado = eval('x + 1')
                print(resultado)  # Saída: 3
                '''
        },
        "exec": {
            "significado": "Função incorporada do Python que executa uma string de código como um bloco de código completo.",
            "uso": "É usada para executar código Python dinamicamente.",
            "exemplo": '''
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
            "exemplo": '''
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
            "exemplo": '''
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
            "exemplo": '''
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
            "exemplo": '''
                import sys
                sys.exit('Finalizando o programa')
                # O programa é encerrado com a mensagem 'Finalizando o programa'
                '''
        },
        "end": {
            "significado": "Palavra-chave usada no Python para especificar o fim de um bloco ou a terminação de uma string.",
            "uso": "É usada principalmente nas funções de impressão para controlar o fim da saída.",
            "exemplo": '''
                print('Olá', end=' ')
                print('Mundo')
                # Saída: Olá Mundo
                '''
        },
        "expandtabs": {
            "significado": "Método de strings no Python que substitui os caracteres de tabulação por espaços.",
            "uso": "É usada para alinhar texto substituindo as tabulações por um número determinado de espaços.",
            "exemplo": '''
                texto = 'Olá\tMundo'
                print(texto.expandtabs(4))
                # Saída: Olá   Mundo
                '''
        },
        "encode": {
            "significado": "Método de strings no Python que codifica uma string em uma sequência de bytes usando um codificador específico.",
            "uso": "É usada para converter uma string em uma sequência de bytes para ser armazenada ou transmitida em formatos específicos.",
            "exemplo": '''
                texto = 'Olá Mundo'
                encoded = texto.encode('utf-8')
                print(encoded)
                # Saída: b'Olá Mundo'
                '''
        },
        "element": {
            "significado": "Um item individual dentro de uma coleção ou estrutura de dados.",
            "uso": "É usada para se referir a um objeto dentro de uma lista, conjunto, dicionário, etc.",
            "exemplo": '''
                lista = [1, 2, 3]
                print(lista[0])  # Saída: 1
                '''
        },
        "error": {
            "significado": "Condição anômala na execução de um programa que interrompe seu fluxo normal.",
            "uso": "É usada para indicar que algo deu errado durante a execução do código.",
            "exemplo": '''
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
            "exemplo": '''
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
            "exemplo": '''
                x = 5
                resultado = eval('x + 2')
                print(resultado)  # Saída: 7
                '''
        },
        "elements": {
            "significado": "Itens ou componentes individuais dentro de um conjunto ou coleção.",
            "uso": "É usada para se referir às partes de uma estrutura de dados.",
            "exemplo": '''
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
            "exemplo": '''
                import math
                resultado = math.exp(2)
                print(resultado)  # Saída: 7.3890560989306495
                '''
        },
        "enumerations": {
            "significado": "Uma lista ou conjunto de elementos, muitas vezes com um valor associado ou um identificador.",
            "uso": "É usada para representar um conjunto de valores possíveis de uma variável.",
            "exemplo": '''
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
            "exemplo": '''
                texto = 'Olá Mundo'
                encoded = texto.encode('utf-8')
                print(encoded)  # Saída: b'Olá Mundo'
                '''
        },
        "execfile": {
            "significado": "Função que executa um arquivo Python como se fosse um script.",
            "uso": "É usada para executar um arquivo Python externo.",
            "exemplo": '''
                # Este comando está disponível apenas no Python 2
                execfile('script.py')
                '''
        },
        "edit_distance": {
            "significado": "Medida que calcula a diferença entre duas strings com base nas operações necessárias para converter uma na outra.",
            "uso": "É usada para comparar quão semelhantes são duas strings e determinar quantas mudanças são necessárias para torná-las idênticas.",
            "exemplo": '''
                from nltk.metrics import edit_distance

                distancia = edit_distance('kitten', 'sitting')
                print(distancia)  # Saída: 3
                '''
        },
        "eval_input": {
            "significado": "Função que avalia uma entrada do usuário, normalmente através da função `input()`.",
            "uso": "É usada para obter e avaliar uma entrada fornecida pelo usuário.",
            "exemplo": '''
                entrada = input('Digite um número: ')
                resultado = eval(entrada)
                print(resultado)
                '''
        },
        "xceed": {
            "significado": "Termo usado para descrever algo que supera ou excede um limite ou expectativa.",
            "uso": "É usada para indicar que algo superou um padrão ou limite.",
            "exemplo": "A nova atualização excede nossas expectativas em termos de desempenho."
        },
        "expected": {
            "significado": "Algo antecipado ou previsto, com base em expectativas ou previsões.",
            "uso": "É usada para descrever o que se espera que aconteça em uma situação.",
            "exemplo": "O resultado esperado era um aumento na velocidade de processamento."
        },
        "encode_base64": {
            "significado": "Método de codificação que converte dados binários em uma representação de texto em base 64.",
            "uso": "É usada para codificar dados binários em uma string de texto legível em base 64.",
            "exemplo": '''
                import base64
                encoded = base64.b64encode(b'olá')
                print(encoded)  # Saída: b'b2xh'
                '''
        },
        "execute": {
            "significado": "Realizar ou executar um conjunto de instruções ou um programa.",
            "uso": "É usada para colocar em prática uma ação ou executar código.",
            "exemplo": '''
                def funcao():
                    print('Executando...')
                funcao()  # Saída: Executando...
                '''
        },
        "exit_code": {
            "significado": "Valor retornado por um programa ou script ao finalizar, indicando se foi executado corretamente ou se ocorreu um erro.",
            "uso": "É usada para verificar se um programa foi concluído com sucesso ou se ocorreu um erro.",
            "exemplo": '''
                import sys
                sys.exit(0)  # Saída: 0 indica sucesso, outro número indica erro.
                '''
        },
        "evaluate_expression": {
            "significado": "Avaliar uma expressão para obter seu resultado.",
            "uso": "É usada para calcular ou obter o valor de uma expressão matemática ou lógica.",
            "exemplo": '''
                resultado = eval('3 + 5')
                print(resultado)  # Saída: 8
                '''
        },
        "environment": {
            "significado": "O contexto ou conjunto de condições em que um programa ou aplicação é executado.",
            "uso": "É usada para se referir ao conjunto de variáveis, configurações e recursos disponíveis para um programa.",
            "exemplo": '''
                import os
                print(os.environ)  # Saída: Mostra as variáveis de ambiente do sistema.
                '''
        },
        "environment_variable": {
            "significado": "Variável que armazena informações sobre o ambiente do sistema ou aplicação.",
            "uso": "É usada para armazenar configurações específicas que afetam o comportamento dos programas.",
            "exemplo": '''
                import os
                print(os.getenv('PATH'))  # Saída: Mostra a variável de ambiente PATH.
                '''
        },
        "exp": {
            "significado": "Função matemática que calcula a exponencial de um número, ou seja, e elevado à potência desse número.",
            "uso": "É usada para realizar cálculos exponenciais.",
            "exemplo": '''
                import math
                resultado = math.exp(1)
                print(resultado)  # Saída: 2.718281828459045
                '''
        },
        "exception_handling": {
            "significado": "Processo de gerenciar e responder a erros ou exceções que ocorrem durante a execução de um programa.",
            "uso": "É usada para capturar e gerenciar erros, garantindo que o programa não pare inesperadamente.",
            "exemplo": '''
                try:
                    valor = 1 / 0
                except ZeroDivisionError as e:
                    print(f'Erro: {e}')  # Saída: Erro: division by zero
                '''
        },
        "expand": {
            "significado": "Ampliar ou aumentar o tamanho ou o alcance de algo.",
            "uso": "É usada para fazer algo maior ou incluir mais informações.",
            "exemplo": '''
                texto = "Olá"
                print(texto.expandtabs(4))  # Saída: 'Olá' com tabulações ampliadas
                '''
        },
        "environment_config": {
            "significado": "Configuração relacionada ao ambiente de execução de um programa ou sistema.",
            "uso": "É usada para especificar ou ajustar parâmetros que afetam o funcionamento de um programa ou aplicação.",
            "exemplo": '''
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
            "exemplo": '''
                a = 5
                b = 5
                print(a == b)  # Saída: True
                '''
        },
        "error_handling": {
            "significado": "Processo de gerenciar erros e exceções que ocorrem durante a execução de um programa.",
            "uso": "É usada para capturar e gerenciar erros de maneira controlada para evitar que o programa termine inesperadamente.",
            "exemplo": '''
                try:
                    valor = 10 / 0
                except ZeroDivisionError:
                    print('Erro de divisão por zero')  # Saída: Erro de divisão por zero
                '''
        },
        "event": {
            "significado": "Ação ou evento que pode ser detectado e gerenciado em um programa.",
            "uso": "É usada para gerenciar e responder a atividades ou mudanças em um sistema ou programa.",
            "exemplo": '''
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
            "exemplo": '''
                import asyncio
                async def hello():
                    print("Olá")
                asyncio.run(hello())  # Saída: Olá
                '''
        },
        "exception_type": {
            "significado": "O tipo específico de uma exceção ou erro que ocorre em um programa.",
            "uso": "É usada para identificar qual tipo de erro ocorreu e tomar ações adequadas.",
            "exemplo": '''
                try:
                    valor = 10 / 0
                except ZeroDivisionError as e:
                    print(f"Tipo de erro: {type(e)}")  # Saída: Tipo de erro: <class 'ZeroDivisionError'>
                '''
        },
        "error_message": {
            "significado": "Mensagem que descreve o erro ou problema ocorrido durante a execução de um programa.",
            "uso": "É usada para fornecer detalhes sobre o que falhou ou causou uma exceção.",
            "exemplo": '''
                try:
                    x = int("abc")
                except ValueError as e:
                    print(f"Mensagem de erro: {e}")  # Saída: Mensagem de erro: invalid literal for int() with base 10: 'abc'
                '''
        },
        "extract": {
            "significado": "Obter uma parte específica de um conjunto de dados ou informações.",
            "uso": "É usada para retirar ou extrair um componente específico de um conjunto maior de dados.",
            "exemplo": '''
                texto = 'Olá Mundo'
                print(texto[0:4])  # Saída: Olá
                '''
        },
        "exit_status": {
            "significado": "Código de saída que indica se um programa ou processo terminou corretamente ou com erro.",
            "uso": "É usada para verificar se um processo ou comando terminou com sucesso ou se ocorreu algum erro.",
            "exemplo": '''
                import sys
                sys.exit(0)  # Saída: 0 indica sucesso, qualquer outro número indica erro.
                '''
        },
    },
    "f": {
        "filemode": {
            "significado": "Modo de abertura de um arquivo que determina as operações que podem ser realizadas nele.",
            "uso": "É usada para especificar o tipo de acesso desejado para um arquivo (leitura, escrita, etc.).",
            "exemplo": '''
                arquivo = open('arquivo.txt', 'r')  # 'r' indica modo de leitura somente
                print(arquivo.mode)  # Saída: 'r'
                '''
        },
        "frozen_set": {
            "significado": "Conjunto imutável em Python, similar a um conjunto padrão, mas sem a possibilidade de modificá-lo após sua criação.",
            "uso": "É usada para criar conjuntos que não devem ser modificados após a sua criação.",
            "exemplo": '''
                conjunto = frozenset([1, 2, 3])
                print(conjunto)  # Saída: frozenset({1, 2, 3})
                '''
        },
        "format_map": {
            "significado": "Método que retorna uma string formatada usando um dicionário ou objeto similar.",
            "uso": "É usada para realizar substituições de valores em uma string usando um mapa (como um dicionário).",
            "exemplo": '''
                dados = {'nome': 'João', 'idade': 30}
                texto = 'Nome: {nome}, Idade: {idade}'.format_map(dados)
                print(texto)  # Saída: Nome: João, Idade: 30
                '''
        },
        "find": {
            "significado": "Método que busca uma substring dentro de uma string e retorna o índice da primeira ocorrência.",
            "uso": "É usada para encontrar a posição de um texto dentro de outro.",
            "exemplo": '''
                texto = 'Olá Mundo'
                print(texto.find('Mundo'))  # Saída: 5
                '''
        },
        "float32": {
            "significado": "Tipo de dado no NumPy que representa um número de ponto flutuante de 32 bits.",
            "uso": "É usada para armazenar números com decimais de forma mais eficiente em termos de memória.",
            "exemplo": '''
                import numpy as np
                numero = np.float32(3.1415)
                print(numero)  # Saída: 3.1415
                '''
        },
        "float64": {
            "significado": "Tipo de dado no NumPy que representa um número de ponto flutuante de 64 bits.",
            "uso": "É usada para armazenar números com decimais com maior precisão do que o tipo float32.",
            "exemplo": '''
                import numpy as np
                numero = np.float64(3.141592653589793)
                print(numero)  # Saída: 3.141592653589793
                '''
        },
        "formatting": {
            "significado": "O processo de aplicar um formato a dados ou strings, como alinhamento, larguras e tipos de dados.",
            "uso": "É usada para organizar ou mostrar dados de forma mais legível ou específica.",
            "exemplo": '''
                texto = 'Nome: {0:10}, Idade: {1:5}'.format('João', 30)
                print(texto)  # Saída: Nome: João      , Idade: 30
                '''
        },
        "flush_output": {
            "significado": "Método utilizado para esvaziar o buffer de saída, forçando que os dados sejam escritos imediatamente.",
            "uso": "É usada quando se quer garantir que todos os dados pendentes no buffer de saída sejam escritos no destino.",
            "exemplo": '''
                import sys
                sys.stdout.write('Olá Mundo')
                sys.stdout.flush()  # Saída: 'Olá Mundo' imediatamente
                '''
        },
        "function_definition": {
            "significado": "O processo de criar uma função em Python usando a palavra-chave 'def'.",
            "uso": "É usada para declarar funções reutilizáveis que executam um bloco de código específico.",
            "exemplo": '''
                def saudar(nome):
                    return f'Olá {nome}'
                print(saudar('João'))  # Saída: Olá João
                '''
        },
        "filepath": {
            "significado": "Caminho ou endereço de um arquivo no sistema de arquivos.",
            "uso": "É usada para especificar a localização de um arquivo no sistema de arquivos.",
            "exemplo": '''
                import os
                caminho = os.path.join('pasta', 'arquivo.txt')
                print(caminho)  # Saída: pasta/arquivo.txt
                '''
        },
        "flask": {
            "significado": "Um micro-framework em Python para o desenvolvimento de aplicações web.",
            "uso": "É usada para criar aplicações web de maneira simples e rápida com rotas, formulários e outras funcionalidades.",
            "exemplo": '''
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
            "exemplo": '''
                lista = [1, 2, 3, 4, 5]
                resultado = filter(lambda x: x > 2, lista)
                print(list(resultado))  # Saída: [3, 4, 5]
                '''
        },
        "futures": {
            "significado": "Módulo que fornece uma interface para executar tarefas assíncronas e paralelizadas.",
            "uso": "É usada para executar funções de maneira concorrente usando threads ou processos.",
            "exemplo": '''
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
            "exemplo": '''
                from functools import reduce
                lista = [1, 2, 3, 4]
                resultado = reduce(lambda x, y: x + y, lista)
                print(resultado)  # Saída: 10
                '''
        },
        "fromkeys": {
            "significado": "Método de dicionário que cria um novo dicionário com chaves especificadas e valores padrão.",
            "uso": "É usada para criar dicionários a partir de uma lista de chaves com um valor padrão.",
            "exemplo": '''
                dicionario = dict.fromkeys(['a', 'b', 'c'], 0)
                print(dicionario)  # Saída: {'a': 0, 'b': 0, 'c': 0}
                '''
        },
        "flask_restful": {
            "significado": "Extensão para Flask que simplifica a criação de APIs RESTful.",
            "uso": "É usada para desenvolver aplicações web que seguem a arquitetura REST usando recursos.",
            "exemplo": '''
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
            "exemplo": '''
                # Exemplo no contexto de código: correção de um erro de sintaxe
                def corrigir_erro():
                    print('Esta é a mensagem corrigida')
                corrigir_erro()
                '''
        },
        "float_conversion": {
            "significado": "Processo de converter dados de outros tipos para tipo flutuante.",
            "uso": "É usada para converter valores em números de ponto flutuante (decimais).",
            "exemplo": '''
                numero = '3.14'
                resultado = float(numero)
                print(resultado)  # Saída: 3.14
                '''
        },
        "full_path": {
            "significado": "Caminho completo para um arquivo ou diretório no sistema de arquivos.",
            "uso": "É usada para especificar a localização exata de um arquivo ou diretório desde a raiz do sistema de arquivos.",
            "exemplo": '''
                import os
                caminho_completo = os.path.abspath('arquivo.txt')
                print(caminho_completo)  # Saída: /home/usuario/arquivo.txt
                '''
        },
        "filter": {
            "significado": "Função que aplica uma condição a cada elemento de um iterável e retorna os elementos que atendem à condição.",
            "uso": "É usada para selecionar apenas os elementos que atendem a uma condição específica.",
            "exemplo": '''
                lista = [1, 2, 3, 4, 5]
                resultado = filter(lambda x: x % 2 == 0, lista)
                print(list(resultado))  # Saída: [2, 4]
                '''
        },
        "float": {
            "significado": "Tipo de dado em Python para representar números de ponto flutuante (números com decimais).",
            "uso": "É usada para representar números que exigem decimais.",
            "exemplo": '''
                numero = 3.14
                print(type(numero))  # Saída: <class 'float'>
                '''
        },
        "for": {
            "significado": "Palavra-chave em Python usada para iterar sobre os elementos de um iterável.",
            "uso": "É usada para executar um bloco de código repetidamente para cada elemento de um iterável.",
            "exemplo": '''
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
            "exemplo": '''
                nome = 'Juan'
                idade = 30
                print('Meu nome é {} e tenho {} anos'.format(nome, idade))
                # Saída: Meu nome é Juan e tenho 30 anos
                '''
        },
        "from": {
            "significado": "Palavra-chave em Python usada para importar módulos ou funções específicas de módulos.",
            "uso": "É usada para trazer funcionalidades específicas de um módulo para o espaço de nomes atual.",
            "exemplo": '''
                from math import sqrt
                print(sqrt(16))  # Saída: 4.0
                '''
        },
        "function": {
            "significado": "Bloco de código projetado para realizar uma tarefa específica e que pode ser reutilizado.",
            "uso": "É usado para agrupar código relacionado que realiza uma tarefa comum, permitindo reutilização e modularidade.",
            "exemplo": '''
                def saudacao(nome):
                    return f'Olá, {nome}'
                
                print(saudacao('Juan'))  # Saída: Olá, Juan
                '''
        },
        "fibonacci": {
            "significado": "Sequência matemática onde cada número é a soma dos dois anteriores.",
            "uso": "É usada para gerar a sequência de Fibonacci, frequentemente em exercícios de programação ou algoritmos.",
            "exemplo": '''
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
            "exemplo": '''
                with open('arquivo.txt', 'r') as f:
                    conteudo = f.read()
                print(conteudo)
                '''
        },
        "fwrite": {
            "significado": "Função usada para escrever dados em um arquivo.",
            "uso": "É usada para escrever dados binários em um arquivo aberto em modo de escrita.",
            "exemplo": '''
                with open('arquivo.bin', 'wb') as f:
                    f.write(b'Hello, World!')
                '''
        },
        "fread": {
            "significado": "Função usada para ler dados de um arquivo.",
            "uso": "É usada para ler dados binários de um arquivo aberto em modo de leitura.",
            "exemplo": '''
                with open('arquivo.bin', 'rb') as f:
                    dados = f.read()
                print(dados)  # Saída: b'Hello, World!'
                '''
        },
        "finally": {
            "significado": "Palavra-chave em Python que define um bloco de código que será executado sempre, independentemente de ocorrer uma exceção ou não.",
            "uso": "É usada em estruturas try-except para garantir que um bloco de código final seja executado, mesmo que ocorra um erro.",
            "exemplo": '''
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
            "exemplo": '''
                # Não há uma função explícita chamada freeze, mas em alguns casos como com `frozenset` pode-se obter o mesmo efeito
                a = frozenset([1, 2, 3])
                print(a)  # Saída: frozenset({1, 2, 3})
                '''
        },
        "flush": {
            "significado": "Método usado para esvaziar os buffers de um arquivo, garantindo que todos os dados sejam escritos no disco.",
            "uso": "É usada quando é necessário garantir que os dados armazenados em um buffer sejam imediatamente escritos no arquivo.",
            "exemplo": '''
                with open('arquivo.txt', 'w') as f:
                    f.write('Olá')
                    f.flush()  # Garante que os dados sejam escritos no arquivo
                '''
        },
        "fstring": {
            "significado": "Cadeia de texto que permite inserir expressões dentro da cadeia de forma mais legível e eficiente.",
            "uso": "É usada para criar cadeias de texto interpoladas, onde variáveis podem ser inseridas diretamente dentro da cadeia.",
            "exemplo": '''
                nome = 'Juan'
                idade = 30
                print(f'Meu nome é {nome} e tenho {idade} anos')  # Saída: Meu nome é Juan e tenho 30 anos
                '''
        },
        "factorial": {
            "significado": "Função matemática que calcula o produto de todos os números inteiros positivos até um número dado.",
            "uso": "É usada para calcular o fatorial de um número, frequentemente em algoritmos de combinatória e probabilidade.",
            "exemplo": '''
                import math
                print(math.factorial(5))  # Saída: 120
                '''
        },
        "frozen": {
            "significado": "Objeto imutável que não pode ser modificado após sua criação.",
            "uso": "É usado para criar objetos que não podem ser alterados, como um `frozenset` em Python.",
            "exemplo": '''
                a = frozenset([1, 2, 3])
                print(a)  # Saída: frozenset({1, 2, 3})
                '''
        },
        "filterfalse": {
            "significado": "Função que retorna um iterador que filtra os elementos de um iterável, excluindo os que retornam `True` na função fornecida.",
            "uso": "É usada para obter os elementos de um iterável para os quais a função retorna `False`.",
            "exemplo": '''
                from itertools import filterfalse
                resultado = filterfalse(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])
                print(list(resultado))  # Saída: [1, 3, 5]
                '''
        },
        "fuzzy": {
            "significado": "Relacionado à lógica difusa, que permite lidar com informações imprecisas ou incertas.",
            "uso": "É usado em sistemas que precisam processar dados aproximados ou incertos.",
            "exemplo": '''
                # Exemplo de uma biblioteca de lógica difusa como `fuzzywuzzy` (para correspondência difusa de texto)
                from fuzzywuzzy import fuzz
                print(fuzz.ratio('hola', 'Hola'))  # Saída: 100
                '''
        },
        "fibonacci_sequence": {
            "significado": "Sequência matemática onde cada número é a soma dos dois anteriores.",
            "uso": "É usada para gerar a sequência de Fibonacci.",
            "exemplo": '''
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
            "exemplo": '''
                pi = 3.14159
                print(f'{pi:.2f}')  # Saída: 3.14
                '''
        },
        "fork": {
            "significado": "Processo de criar um novo processo, copiado do processo original.",
            "uso": "É usado na programação de sistemas para criar processos secundários.",
            "exemplo": '''
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
            "exemplo": '''
                import os
                pid = os.fork()
                # Semelhante ao exemplo de 'fork', mas abrangendo o conceito de 'forking'
                '''
        },
        "first": {
            "significado": "Ação de obter o primeiro elemento de uma sequência ou iterável.",
            "uso": "É usado para acessar o primeiro valor de um iterável, como uma lista ou conjunto.",
            "exemplo": '''
                lista = [1, 2, 3, 4]
                print(lista[0])  # Saída: 1
                '''
        },
        "float_format": {
            "significado": "Formato que define como os números de ponto flutuante devem ser apresentados em uma cadeia.",
            "uso": "É usado para especificar a quantidade de casas decimais a ser exibida em um número de ponto flutuante.",
            "exemplo": '''
                pi = 3.14159
                print(f'{pi:.2f}')  # Saída: 3.14
                '''
        },
        "filter_none": {
            "significado": "Função que filtra elementos de um iterável, excluindo os valores `None`.",
            "uso": "É usada para excluir valores `None` de uma sequência.",
            "exemplo": '''
                lista = [1, None, 2, None, 3]
                resultado = filter(None, lista)
                print(list(resultado))  # Saída: [1, 2, 3]
                '''
        },
        "func_code": {
            "significado": "Atributo que contém o bytecode da função em Python.",
            "uso": "É usado para acessar o código da função, geralmente em contextos de depuração ou análise.",
            "exemplo": '''
                def exemplo():
                    pass
                
                print(exemplo.__code__)  # Saída: <code object exemplo at 0x...>
                '''
        },

        "float_power": {
            "significado": "Función que calcula un número elevado a una potencia flotante.",
            "uso": "Se utiliza para realizar exponentiación con números flotantes.",
            "ejemplo": '''
                print(pow(2, 3.5))  # Saída: 11.313708498984761
                '''
        },
        "format_string": {
            "significado": "Cadena que define la estructura de un valor que se desea mostrar, utilizando especificadores de formato.",
            "uso": "Se utiliza para definir cómo deben mostrarse los valores en una cadena, como el número de decimales o la alineación.",
            "ejemplo": '''
                nombre = 'Juan'
                edad = 25
                print(f'Nombre: {nombre}, Edad: {edad}')  # Saída: Nombre: Juan, Edad: 25
                '''
        },
        "filename": {
            "significado": "Cadena que representa el nombre de un archivo en el sistema de archivos.",
            "uso": "Se utiliza para especificar el nombre y la ubicación de un archivo que se desea manipular.",
            "ejemplo": '''
                archivo = 'documento.txt'
                with open(archivo, 'r') as f:
                    print(f.read())
                '''
        },
        "file_object": {
            "significado": "Objeto que representa un archivo abierto en Python, a través del cual se puede leer, escribir o manipular el archivo.",
            "uso": "Se utiliza para interactuar con archivos abiertos en Python, accediendo a sus contenidos o modificándolos.",
            "ejemplo": '''
                with open('documento.txt', 'r') as f:
                    contenido = f.read()
                    print(contenido)
                '''
        },
        "finally_clause": {
            "significado": "Parte de un bloque de código que siempre se ejecuta después de una instrucción `try`, independientemente de si se generó una excepción.",
            "uso": "Se utiliza para ejecutar código de limpieza o finalización, como el cierre de archivos o liberación de recursos.",
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
            "significado": "Operación que permite leer los contenidos de un archivo en Python.",
            "uso": "Se utiliza para obtener los datos almacenados en un archivo para su procesamiento o visualización.",
            "ejemplo": '''
                with open('documento.txt', 'r') as archivo:
                    contenido = archivo.read()
                    print(contenido)
                '''
        },
        "form": {
            "significado": "Estructura o plantilla utilizada para organizar datos de manera específica.",
            "uso": "Se utiliza en interfaces de usuario o aplicaciones web para capturar y organizar datos del usuario.",
            "ejemplo": '''
                formulario = {'nombre': 'Juan', 'edad': 25}
                print(formulario)
                '''
        },
        "function_call": {
            "significado": "Acción de invocar una función en el código, pasándole los parámetros necesarios para ejecutar su tarea.",
            "uso": "Se utiliza para ejecutar una función y obtener su resultado.",
            "ejemplo": '''
                def suma(a, b):
                    return a + b
                resultado = suma(3, 4)
                print(resultado)  # Saída: 7
                '''
        },
        "force": {
            "significado": "Acción de imponer o forzar la ejecución de algo, generalmente en el contexto de programación o manipulación de objetos.",
            "uso": "Se utiliza para forzar un comportamiento específico en un programa, como evitar errores o realizar una acción sin importar las condiciones.",
            "ejemplo": '''
                # No existe un 'force' directo en Python, pero se puede usar 'assert' para forzar condiciones
                assert 1 == 1, 'Condición falsa'
                '''
        },
        "function_pointer": {
            "significado": "Referencia a una función que puede ser pasada y ejecutada como un argumento.",
            "uso": "Se utiliza en lenguajes como C o C++ para referenciar funciones y pasarlas como parámetros.",
            "ejemplo": '''
                # En Python no existe un puntero de función directo, pero las funciones se pueden pasar como objetos
                def saludar():
                    print('Hola')
                funcion = saludar
                funcion()  # Saída: Hola
                '''
        },
        "float_precision": {
            "significado": "Número de dígitos que se usan para representar un número flotante con precisión.",
            "uso": "Se utiliza para especificar la cantidad de decimales que deben considerarse al realizar operaciones con números flotantes.",
            "ejemplo": '''
                numero = 3.14159265359
                print(f'{numero:.2f}')  # Saída: 3.14
                '''
        },
        "format_error": {
            "significado": "Error que ocurre cuando hay un problema al formatear datos, como una cadena mal estructurada.",
            "uso": "Se utiliza para manejar errores relacionados con la conversión o formateo incorrecto de datos.",
            "ejemplo": '''
                try:
                    int('abc')
                except ValueError as e:
                    print(f'Error de formato: {e}')
                '''
        },
        "file_write": {
            "significado": "Operación que permite escribir datos en un archivo en Python.",
            "uso": "Se utiliza para almacenar información en un archivo, sobrescribiéndolo o agregando nuevos datos.",
            "ejemplo": '''
                with open('documento.txt', 'w') as archivo:
                    archivo.write('Hola, mundo!')
                '''
        },
        "fibonacci_search": {
            "significado": "Método de búsqueda que utiliza los números de Fibonacci para dividir el espacio de búsqueda de manera eficiente.",
            "uso": "Se utiliza como una alternativa al algoritmo de búsqueda binaria para encontrar un elemento en un array.",
            "ejemplo": '''
                # Implementación de Fibonacci Search no estándar, pero puede utilizarse como alternativa a la búsqueda binaria
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
            "uso": "Se utiliza para realizar transformaciones y filtrados de manera eficiente en secuencias de datos.",
            "ejemplo": '''
                from itertools import filterfalse
                data = [1, 2, 3, 4, 5]
                result = map(lambda x: x * 2, filter(lambda x: x % 2 == 0, data))
                print(list(result))  # Saída: [4, 8]
                '''
        },

    },
    "g": {
        "get": {
            "significado": "Método que obtiene el valor de una clave en un diccionario. Si la clave no existe, devuelve un valor por defecto.",
            "uso": "Se utiliza para obtener el valor asociado a una clave en un diccionario de manera segura.",
            "exemplo": """
                diccionario = {'a': 1, 'b': 2}
                print(diccionario.get('a'))  # Saída: 1
                print(diccionario.get('c', 'No encontrado'))  # Saída: No encontrado
                """
        },
        "global": {
            "significado": "Palabra clave que se utiliza para declarar que una variable es global, es decir, que pertenece al ámbito global.",
            "uso": "Se utiliza para modificar variables globales dentro de una función.",
            "exemplo": """
                x = 10
                def cambiar_global():
                    global x
                    x = 20
                cambiar_global()
                print(x)  # Saída: 20
                """
        },
        "generator": {
            "significado": "Función que devuelve un iterador, permitiendo generar elementos de uno en uno durante la ejecución.",
            "uso": "Se utiliza para crear secuencias de elementos de manera perezosa (lazy evaluation), sin tener que almacenarlos todos en memoria.",
            "exemplo": """
                def contar_hasta_tres():
                    yield 1
                    yield 2
                    yield 3
                for num in contar_hasta_tres():
                    print(num)  # Saída: 1, 2, 3
                """
        },
        "globals": {
            "significado": "Función que devuelve un diccionario de todas las variables globales.",
            "uso": "Se utiliza para acceder y modificar el diccionario de variables globales.",
            "exemplo": """
                x = 10
                print(globals())  # Saída: {'x': 10, ...}
                """
        },
        "getattr": {
            "significado": "Función que obtiene el valor de un atributo de un objeto.",
            "uso": "Se utiliza para acceder a un atributo de un objeto, incluso si no se conoce su nombre de antemano.",
            "exemplo": """
                class Persona:
                    def __init__(self, nombre):
                        self.nombre = nombre
                p = Persona('Juan')
                print(getattr(p, 'nombre'))  # Saída: Juan
                """
        },
        "groupby": {
            "significado": "Función de `itertools` que agrupa los elementos de un iterable según una clave.",
            "uso": "Se utiliza para agrupar datos en función de un criterio, como en el caso de una lista de elementos.",
            "exemplo": """
                from itertools import groupby
                datos = [1, 2, 2, 3, 3, 3]
                grupos = groupby(datos, key=lambda x: x)
                for clave, grupo in grupos:
                    print(clave, list(grupo))  # Saída: 1 [1], 2 [2, 2], 3 [3, 3, 3]
                """
        },
        "gc": {
            "significado": "Módulo de recolección de basura que permite interactuar con el recolector de basura de Python.",
            "uso": "Se utiliza para gestionar la memoria y liberar objetos no referenciados.",
            "exemplo": """
                import gc
                gc.collect()  # Forzar la recolección de basura
                """
        },
        "git": {
            "significado": "Sistema de control de versiones distribuido para gestionar el código fuente.",
            "uso": "Se utiliza para manejar versiones de código, facilitando el trabajo en equipo y el control de cambios.",
            "exemplo": """
                # Usando Git en la terminal
                git clone https://github.com/usuario/repositorio.git
                """
        },
        "generator_expression": {
            "significado": "Expresión que permite generar un generador de manera compacta, similar a una lista por comprensión.",
            "uso": "Se utiliza para crear generadores de manera eficiente y sin necesidad de almacenar todos los elementos.",
            "exemplo": """
                numeros = (x * 2 for x in range(5))
                for num in numeros:
                    print(num)  # Saída: 0, 2, 4, 6, 8
                """
        },
        "gzip": {
            "significado": "Módulo que permite comprimir y descomprimir archivos en formato gzip.",
            "uso": "Se utiliza para trabajar con archivos comprimidos en el formato gzip, reduciendo su tamaño para almacenamiento o transmisión.",
            "exemplo": """
                import gzip
                with gzip.open('archivo.txt.gz', 'rb') as f:
                    contenido = f.read()
                    print(contenido)
                """
        },
        "graph": {
            "significado": "Estructura de datos que representa relaciones entre objetos a través de nodos y aristas.",
            "uso": "Se utiliza para representar relaciones complejas entre objetos, como en redes sociales o rutas de transporte.",
            "exemplo": """
                # Ejemplo básico de grafo
                grafo = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A'], 'D': ['B']}
                print(grafo)
                """
        },
        "grid": {
            "significado": "Estructura de datos o disposición de elementos en filas y columnas.",
            "uso": "Se utiliza para representar una cuadrícula, como en un tablero de ajedrez o una interfaz de usuario.",
            "exemplo": """
                grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
                for fila in grid:
                    print(fila)  # Saída: [1, 2, 3], [4, 5, 6], [7, 8, 9]
                """
        },
        "getopt": {
            "significado": "Módulo que proporciona una forma de analizar los argumentos de la línea de comandos.",
            "uso": "Se utiliza para gestionar opciones y parámetros pasados a un programa desde la línea de comandos.",
            "exemplo": """
                import getopt
                opciones, argumentos = getopt.getopt(['-f', 'archivo.txt'], 'f:')
                print(opciones)  # Saída: [('f', 'archivo.txt')]
                """
        },
        "gcd": {
            "significado": "Función que calcula el máximo común divisor de dos números.",
            "uso": "Se utiliza para encontrar el mayor número que divide a dos números sin dejar residuo.",
            "exemplo": """
                import math
                print(math.gcd(24, 36))  # Saída: 12
                """
        },
        "getpass": {
            "significado": "Función que lee una contraseña de manera oculta (sin mostrar caracteres al escribir).",
            "uso": "Se utiliza para leer contraseñas o entradas sensibles de forma segura en la terminal.",
            "exemplo": """
                import getpass
                password = getpass.getpass('Introduce tu contraseña: ')
                print(password)  # La contraseña no se muestra mientras se escribe
                """
        },
        "gradients": {
            "significado": "Cambio en el valor de una variable con respecto a otra, comúnmente utilizado en cálculo y machine learning.",
            "uso": "Se utiliza para calcular la dirección y la tasa de cambio de una función en relación con sus variables.",
            "exemplo": """
                # Ejemplo de gradiente en optimización
                def funcion(x):
                    return x**2
                gradiente = 2 * 3  # Gradiente de x^2 en x = 3
                print(gradiente)  # Saída: 6
                """
        },
        "graphlib": {
            "significado": "Módulo en Python que proporciona estructuras de datos para trabajar con grafos.",
            "uso": "Se utiliza para representar y manipular grafos de manera eficiente.",
            "exemplo": """
                import graphlib
                grafo = graphlib.TopologicalSorter({'A': ['B'], 'B': ['C'], 'C': []})
                print(list(grafo.static_order()))  # Saída: ['A', 'B', 'C']
                """
        },
        "get_event_loop": {
            "significado": "Función de la biblioteca `asyncio` que obtiene el bucle de eventos de la aplicación.",
            "uso": "Se utiliza para obtener el bucle de eventos principal en un programa asíncrono.",
            "exemplo": """
                import asyncio
                loop = asyncio.get_event_loop()
                print(loop)  # Saída: <_UnixSelectorEventLoop running=True closed=False pid=12345>
                """
        },
        "get_terminal_size": {
            "significado": "Función que obtiene el tamaño de la terminal en filas y columnas.",
            "uso": "Se utiliza para obtener la resolución de la terminal y ajustar el diseño de la salida.",
            "exemplo": """
                import shutil
                tamaño = shutil.get_terminal_size()
                print(tamaño)  # Saída: os.terminal_size(columns=80, lines=24)
                """
        },
        "getsizeof": {
            "significado": "Función del módulo `sys` que devuelve el tamaño de un objeto en bytes.",
            "uso": "Se utiliza para medir la memoria que ocupa un objeto en Python.",
            "exemplo": """
                import sys
                objeto = [1, 2, 3]
                print(sys.getsizeof(objeto))  # Saída: 72 (dependiendo del sistema)
                """
        },
        "google": {
            "significado": "Motor de búsqueda de internet, también utilizado como nombre de la empresa.",
            "uso": "Se utiliza para buscar información en la web a través de un navegador o API.",
            "exemplo": """
                # Buscando algo en Google
                # Se puede hacer a través de la interfaz web en www.google.com
                """
        },
        "getdefaultencoding": {
            "significado": "Método que devuelve el nombre de la codificación predeterminada utilizada por el sistema.",
            "uso": "Se utiliza para conocer la codificación de texto predeterminada en Python.",
            "exemplo": """
                import sys
                print(sys.getdefaultencoding())  # Saída: 'utf-8' (dependiendo del sistema)
                """
        },
        "geometry": {
            "significado": "Área de las matemáticas que se ocupa de las propiedades y relaciones de puntos, líneas, superficies y sólidos.",
            "uso": "Se utiliza en campos como la computación gráfica, ingeniería y arquitectura para describir formas y estructuras.",
            "exemplo": """
                # Ejemplo de geometría en programación
                import math
                area_circulo = math.pi * (5**2)  # Área de un círculo con radio 5
                print(area_circulo)  # Saída: 78.53981633974483
                """
        },
        "greenlet": {
            "significado": "Módulo que proporciona primitivas para el control de flujo cooperativo de hilos (lightweight threads).",
            "uso": "Se utiliza para ejecutar funciones concurrentemente sin la sobrecarga de los hilos tradicionales.",
            "exemplo": """
                from greenlet import greenlet
                def funcion1():
                    print('En la función 1')
                    g2.switch()
                def funcion2():
                    print('En la función 2')
                    g1.switch()
                g1 = greenlet(funcion1)
                g2 = greenlet(funcion2)
                g1.switch()  # Saída: En la función 1, En la función 2
                """
        },
        "gitignore": {
            "significado": "Archivo de configuración utilizado por Git para especificar qué archivos o directorios deben ser ignorados en el control de versiones.",
            "uso": "Se utiliza para evitar que ciertos archivos se incluyan en el repositorio Git, como archivos temporales o de configuración local.",
            "exemplo": """
                # Ejemplo de .gitignore
                *.log
                __pycache__/
                """
        },
        "grammar": {
            "significado": "Conjunto de reglas que describen la estructura de un lenguaje.",
            "uso": "Se utiliza para definir cómo se deben formar las oraciones o expresiones válidas en un lenguaje.",
            "exemplo": """
                # Ejemplo de gramática en programación
                def sumar(a, b):
                    return a + b
                # La sintaxis es la gramática de la función sumar
                """
        },
        "gettext": {
            "significado": "Función que traduce un texto a un idioma específico, a menudo utilizada en aplicaciones multilingües.",
            "uso": "Se utiliza para obtener una cadena de texto traducida según el idioma actual del sistema.",
            "exemplo": """
                import gettext
                traduccion = gettext.translation('mi_app', localedir='locales', languages=['es'])
                print(traduccion.gettext('Hello'))  # Saída: Hola
                """
        },
        "generate_tokens": {
            "significado": "Función que genera una secuencia de tokens a partir de un objeto de texto, utilizado para analizar y procesar código fuente.",
            "uso": "Se utiliza en la creación de analizadores léxicos para dividir un texto en unidades significativas.",
            "exemplo": """
                import token
                import tokenize
                codigo = 'print("Hola Mundo")'
                tokens = tokenize.generate_tokens(iter(codigo).__next__)
                for t in tokens:
                    print(t)
                """
        },
        "gevent": {
            "significado": "Biblioteca de Python para trabajar con concurrencia basada en hilos ligeros, utilizando corutinas.",
            "uso": "Se utiliza para manejar tareas concurrentes de manera eficiente sin la necesidad de múltiples hilos.",
            "exemplo": """
                import gevent
                def tarea():
                    print('Tarea completada')
                gevent.spawn(tarea).join()
                """
        },
        "gui": {
            "significado": "Interfaz gráfica de usuario, un sistema de interacción visual con los programas informáticos.",
            "uso": "Se utiliza para crear aplicaciones con interfaces visuales, facilitando la interacción del usuario.",
            "exemplo": """
                import tkinter as tk
                ventana = tk.Tk()
                ventana.title('Mi GUI')
                ventana.mainloop()
                """
        },
        "generator_function": {
            "significado": "Función que utiliza `yield` para devolver un generador.",
            "uso": "Se utiliza para crear funciones que devuelven un generador y permiten la iteración perezosa.",
            "exemplo": """
                def contar():
                    yield 1
                    yield 2
                    yield 3
                for numero in contar():
                    print(numero)  # Saída: 1, 2, 3
                """
        },
        "get_data": {
            "significado": "Método o función que obtiene datos de una fuente externa o interna.",
            "uso": "Se utiliza para recuperar datos desde bases de datos, APIs u otras fuentes.",
            "exemplo": """
                def obtener_datos():
                    return {'nombre': 'Juan', 'edad': 25}
                print(obtener_datos())  # Saída: {'nombre': 'Juan', 'edad': 25}
                """
        },
        "git_branch": {
            "significado": "Comando de Git que permite trabajar con ramas dentro de un repositorio.",
            "uso": "Se utiliza para crear, listar y cambiar entre diferentes ramas de un proyecto en Git.",
            "exemplo": """
                git branch  # Muestra las ramas existentes
                git checkout -b nueva_rama  # Crea y cambia a la nueva rama
                """
        },
        "governance": {
            "significado": "El proceso de toma de decisiones y gestión en una organización o sistema.",
            "uso": "Se utiliza para referirse a cómo se administra y regula un sistema o entidad.",
            "exemplo": """
                La gobernanza corporativa se refiere a las prácticas y estructuras organizacionales para la toma de decisiones.
                """
        },
        "gtts": {
            "significado": "Biblioteca de Python para convertir texto en voz usando el servicio Google Text-to-Speech.",
            "uso": "Se utiliza para generar archivos de audio a partir de texto en varios idiomas.",
            "exemplo": """
                from gtts import gTTS
                tts = gTTS('Hola, ¿cómo estás?', lang='es')
                tts.save('hola.mp3')
                """
        },
        "get_identity": {
            "significado": "Método o función que obtiene la identidad de un objeto o usuario.",
            "uso": "Se utiliza para obtener información sobre la identidad de un objeto o entidad, como un identificador único.",
            "exemplo": """
                def get_identity(usuario):
                    return usuario['id']
                usuario = {'id': 123, 'nombre': 'Juan'}
                print(get_identity(usuario))  # Saída: 123
                """
        },
        "get_status": {
            "significado": "Método o función que obtiene el estado de una operación, proceso o entidad.",
            "uso": "Se utiliza para verificar o recuperar el estado actual de un sistema o proceso.",
            "exemplo": """
                def get_status(operacion):
                    return operacion['estado']
                operacion = {'estado': 'completada'}
                print(get_status(operacion))  # Saída: completada
                """
        },
        "generator_instance": {
            "significado": "Instancia de un generador, que es un objeto que permite iterar sobre una secuencia de elementos.",
            "uso": "Se utiliza para manejar iteraciones de manera eficiente utilizando la palabra clave `yield`.",
            "exemplo": """
                def contador():
                    yield 1
                    yield 2
                    yield 3
                generador = contador()
                for numero in generador:
                    print(numero)  # Saída: 1, 2, 3
                """
        },
        "guess_encoding": {
            "significado": "Método que adivina la codificación de un archivo de texto, basado en su contenido.",
            "uso": "Se utiliza para detectar la codificación de archivos de texto que no tienen especificada una.",
            "exemplo": """
                import chardet
                with open('archivo.txt', 'rb') as f:
                    resultado = chardet.detect(f.read())
                print(resultado['encoding'])  # Saída: utf-8
                """
        },
        "git_commit": {
            "significado": "Comando de Git utilizado para registrar los cambios en el repositorio.",
            "uso": "Se utiliza para guardar un conjunto de cambios realizados en los archivos de un proyecto en el repositorio.",
            "exemplo": """
                git commit -m "Mensaje del commit"
                """
        },
        "gradient_descent": {
            "significado": "Método de optimización utilizado para minimizar funciones iterativamente, ajustando los parámetros en la dirección del gradiente negativo.",
            "uso": "Se utiliza principalmente en machine learning para encontrar los valores óptimos de los parámetros del modelo.",
            "exemplo": """
                # Ejemplo simplificado de gradiente descendente
                def gradiente_descendente(funcion, derivada, x_inicial, tasa_aprendizaje, iteraciones):
                    x = x_inicial
                    for _ in range(iteraciones):
                        x -= tasa_aprendizaje * derivada(x)
                    return x
                """
        },
        "get_referrers": {
            "significado": "Función que obtiene una lista de objetos que hacen referencia a un objeto dado.",
            "uso": "Se utiliza para rastrear las referencias hacia un objeto, útil para análisis de memoria.",
            "exemplo": """
                import sys
                referencia = sys.get_referrers(objeto)
                print(referencia)
                """
        },
        "get_window_extent": {
            "significado": "Método que obtiene las dimensiones de una ventana gráfica o área en la pantalla.",
            "uso": "Se utiliza para determinar el tamaño y las coordenadas de la ventana de una aplicación o gráfico.",
            "exemplo": """
                import matplotlib.pyplot as plt
                fig, ax = plt.subplots()
                extent = ax.get_window_extent()
                print(extent)
                """
        },
        "group": {
            "significado": "Método que agrupa elementos en una colección o estructura basada en algún criterio.",
            "uso": "Se utiliza para organizar datos en grupos o categorías.",
            "exemplo": """
                from itertools import groupby
                lista = [1, 1, 2, 2, 3]
                grupo = groupby(lista)
                for clave, valor in grupo:
                    print(clave, list(valor))  # Saída: 1 [1, 1], 2 [2, 2], 3 [3]
                """
        },
        "get_history": {
            "significado": "Método que obtiene el historial de operaciones o acciones previas.",
            "uso": "Se utiliza para recuperar las acciones anteriores realizadas en un sistema o aplicación.",
            "exemplo": """
                # Ejemplo de recuperación del historial en un sistema
                historial = get_history()
                print(historial)
                """
        },
        "gradient": {
            "significado": "El vector que indica la dirección y la tasa de cambio de una función en un punto dado.",
            "uso": "Se utiliza principalmente en el cálculo diferencial y en el entrenamiento de modelos en machine learning.",
            "exemplo": """
                # Ejemplo de gradiente de una función
                import numpy as np
                def funcion(x):
                    return x**2
                gradiente = 2 * 3  # Gradiente de x^2 en x = 3
                print(gradiente)  # Saída: 6
                """
        },
        "getfqdn": {
            "significado": "Función que obtiene el nombre de dominio completo (FQDN) de la máquina local.",
            "uso": "Se utiliza para obtener el nombre completo de dominio de la computadora en una red.",
            "exemplo": """
                import socket
                fqdn = socket.getfqdn()
                print(fqdn)  # Saída: ejemplo.local
                """
        },
        "get_url": {
            "significado": "Función que obtiene una URL específica, generalmente para acceder a un recurso en línea.",
            "uso": "Se utiliza para recuperar una URL desde una fuente externa o generar una URL para un recurso.",
            "exemplo": """
                import requests
                url = "http://example.com"
                respuesta = requests.get(url)
                print(respuesta.url)
                """
        },
        "get_line": {
            "significado": "Método que obtiene una línea específica de un archivo o conjunto de datos.",
            "uso": "Se utiliza para acceder a una línea específica dentro de un archivo o texto.",
            "exemplo": """
                with open('archivo.txt', 'r') as f:
                    linea = f.readline()
                    print(linea)
                """
        },
        "get_clock_info": {
            "significado": "Método que obtiene información sobre el reloj del sistema, como la frecuencia de actualización.",
            "uso": "Se utiliza para obtener detalles sobre el rendimiento y las características del reloj del sistema.",
            "exemplo": """
                import time
                info = time.get_clock_info('time')
                print(info)
                """
        },
        "getmtime": {
            "significado": "Función que obtiene la hora de la última modificación de un archivo.",
            "uso": "Se utiliza para obtener el tiempo de la última modificación de un archivo o directorio.",
            "exemplo": """
                import os
                ultima_modificacion = os.path.getmtime('archivo.txt')
                print(ultima_modificacion)
                """
        },
        "gettext_install": {
            "significado": "Comando o función que instala el paquete `gettext` para la internacionalización de aplicaciones.",
            "uso": "Se utiliza para instalar el paquete necesario para traducir cadenas de texto en aplicaciones de Python.",
            "exemplo": """
                # Ejemplo en la terminal
                pip install gettext
                """
        },
        "geometry_manager": {
            "significado": "Método utilizado para gestionar el tamaño y la ubicación de los widgets en interfaces gráficas.",
            "uso": "Se utiliza en bibliotecas de interfaces gráficas como Tkinter para controlar la disposición de los elementos.",
            "exemplo": """
                import tkinter as tk
                root = tk.Tk()
                label = tk.Label(root, text="Hola Mundo")
                label.pack()  # Usa el geometry manager 'pack'
                root.mainloop()
                """
        },
        "gcd_algorithm": {
            "significado": "Algoritmo para calcular el máximo común divisor (GCD) de dos números.",
            "uso": "Se utiliza para encontrar el mayor número que divide exactamente a dos números.",
            "exemplo": """
                import math
                gcd = math.gcd(24, 36)
                print(gcd)  # Saída: 12
                """
        },
        "googletrans": {
            "significado": "Biblioteca de Python que utiliza la API de Google Translate para traducir texto entre diferentes idiomas.",
            "uso": "Se utiliza para traducir texto automáticamente usando los servicios de Google Translate.",
            "exemplo": """
                from googletrans import Translator
                translator = Translator()
                traduccion = translator.translate('Hola, ¿cómo estás?', src='es', dest='en')
                print(traduccion.text)  # Saída: Hello, how are you?
                """
        },
        "get_dpi": {
            "significado": "Función que obtiene la densidad de píxeles por pulgada (DPI) de la pantalla.",
            "uso": "Se utiliza para obtener la resolución de la pantalla en términos de píxeles por pulgada.",
            "exemplo": """
                import tkinter as tk
                root = tk.Tk()
                dpi = root.winfo_fpixels('1i')  # Píxeles por pulgada
                print(dpi)
                """
        },
        "geolocation": {
            "significado": "Proceso de determinar la ubicación geográfica de un dispositivo.",
            "uso": "Se utiliza para obtener la latitud, longitud y otros detalles sobre la ubicación de un dispositivo.",
            "exemplo": """
                # Ejemplo usando geopy
                from geopy.geocoders import Nominatim
                geolocator = Nominatim(user_agent="mi_app")
                ubicacion = geolocator.geocode("1600 Pennsylvania Ave NW, Washington, DC 20500")
                print(ubicacion.address)
                """
        },
        "git_merge": {
            "significado": "Comando de Git que combina cambios de diferentes ramas en una sola.",
            "uso": "Se utiliza para fusionar las ramas de un repositorio en Git.",
            "exemplo": """
                git checkout master
                git merge rama-feature
                """
        },
        "get_tick_params": {
            "significado": "Función que obtiene los parámetros de los 'ticks' en un gráfico.",
            "uso": "Se utiliza en bibliotecas gráficas como Matplotlib para ajustar los valores de los ejes en los gráficos.",
            "exemplo": """
                import matplotlib.pyplot as plt
                fig, ax = plt.subplots()
                ticks = ax.get_xticks()
                print(ticks)
                """
        },
        "getrandbits": {
            "significado": "Método que devuelve un número aleatorio con una cantidad específica de bits.",
            "uso": "Se utiliza para generar números aleatorios binarios con un número determinado de bits.",
            "exemplo": """
                import random
                numero = random.getrandbits(8)  # 8 bits
                print(numero)  # Saída: número aleatorio de 8 bits
                """
        },
        "gui_toolkit": {
            "significado": "Conjunto de herramientas o bibliotecas utilizadas para desarrollar interfaces gráficas de usuario (GUI).",
            "uso": "Se utiliza para construir aplicaciones con interfaces visuales interactivas.",
            "exemplo": """
                # Ejemplo con Tkinter
                import tkinter as tk
                root = tk.Tk()
                label = tk.Label(root, text="Hola Mundo")
                label.pack()
                root.mainloop()
                """
        },
        "getpid": {
            "significado": "Función que obtiene el ID del proceso actual.",
            "uso": "Se utiliza para obtener el identificador único del proceso en ejecución.",
            "exemplo": """
                import os
                pid = os.getpid()
                print(pid)  # Saída: ID del proceso actual
                """
        },
        "get_event": {
            "significado": "Método que obtiene un evento específico en el contexto de un sistema o aplicación.",
            "uso": "Se utiliza para recuperar un evento de un sistema de gestión de eventos.",
            "exemplo": """
                # Ejemplo en un sistema de eventos
                evento = get_event("click")
                print(evento)
                """
        },
        "gmm": {
            "significado": "Modelo de Mezcla Gaussiana (GMM), un modelo probabilístico para la distribución de datos.",
            "uso": "Se utiliza en machine learning para modelar datos como una mezcla de distribuciones gaussianas.",
            "exemplo": """
                from sklearn.mixture import GaussianMixture
                gmm = GaussianMixture(n_components=2)
                gmm.fit(datos)
                """
        },
        "gather": {
            "significado": "Función utilizada para recopilar o juntar elementos o resultados en una estructura.",
            "uso": "Se utiliza para recoger resultados de operaciones paralelas o de múltiples fuentes.",
            "exemplo": """
                import asyncio
                async def tarea():
                    return 1
                async def main():
                    resultados = await asyncio.gather(tarea(), tarea())
                    print(resultados)
                asyncio.run(main())
                """
        },
        "get_statistics": {
            "significado": "Método que obtiene las estadísticas de un conjunto de datos.",
            "uso": "Se utiliza para calcular y recuperar métricas estadísticas como media, mediana, desviación estándar, etc.",
            "exemplo": """
                import statistics
                datos = [1, 2, 3, 4, 5]
                media = statistics.mean(datos)
                print(media)  # Saída: 3
                """
        },
        "get_user": {
            "significado": "Método que obtiene la información del usuario actual.",
            "uso": "Se utiliza para recuperar los detalles del usuario en un sistema.",
            "exemplo": """
                import os
                usuario = os.getlogin()
                print(usuario)  # Saída: nombre de usuario
                """
        },
        "get_unique": {
            "significado": "Función que obtiene los elementos únicos de un conjunto de datos.",
            "uso": "Se utiliza para recuperar los valores no repetidos de una lista o conjunto.",
            "exemplo": """
                import numpy as np
                datos = [1, 2, 2, 3, 4, 4]
                unicos = np.unique(datos)
                print(unicos)  # Saída: [1 2 3 4]
                """
        },
        "git_rebase": {
            "significado": "Comando de Git que permite aplicar cambios de una rama en otra, reescribiendo el historial.",
            "uso": "Se utiliza para integrar los cambios de una rama en otra de una manera más limpia, reorganizando los commits.",
            "exemplo": """
                git checkout feature-branch
                git rebase main
                """
        },
        "get_score": {
            "significado": "Método para obtener una puntuación o calificación basada en algún criterio o cálculo.",
            "uso": "Se utiliza en diversas aplicaciones para obtener la puntuación de un sistema, juego, examen, etc.",
            "exemplo": """
                score = game.get_score()
                print(score)  # Saída: puntuación actual
                """
        },
        "graph_data": {
            "significado": "Proceso de representar datos en forma de gráficos.",
            "uso": "Se utiliza para visualizar información y patrones mediante gráficos como barras, líneas, etc.",
            "exemplo": """
                import matplotlib.pyplot as plt
                datos = [1, 2, 3, 4, 5]
                plt.plot(datos)
                plt.show()
                """
        },
        "get_installed_distributions": {
            "significado": "Función que obtiene las distribuciones de paquetes instaladas en el entorno de Python.",
            "uso": "Se utiliza para obtener una lista de los paquetes instalados en un entorno Python.",
            "exemplo": """
                from pkg_resources import get_distribution
                distribuciones = get_installed_distributions()
                for distrib in distribuciones:
                    print(distrib)
                """
        },
        "geocode": {
            "significado": "Proceso de convertir una dirección en coordenadas geográficas (latitud y longitud).",
            "uso": "Se utiliza para obtener la ubicación geográfica de una dirección textual.",
            "exemplo": """
                from geopy.geocoders import Nominatim
                geolocator = Nominatim(user_agent="mi_app")
                ubicacion = geolocator.geocode("1600 Pennsylvania Ave NW, Washington, DC 20500")
                print(ubicacion.latitude, ubicacion.longitude)
                """
        },
        "get_type_hints": {
            "significado": "Función que obtiene las sugerencias de tipos de los parámetros y valores de retorno de una función.",
            "uso": "Se utiliza para obtener las anotaciones de tipo de una función.",
            "exemplo": """
                from typing import get_type_hints
                def ejemplo(x: int, y: str) -> bool:
                    return True
                print(get_type_hints(ejemplo))
                """
        },
        "genericpath": {
            "significado": "Módulo que proporciona funciones para trabajar con rutas de archivos y directorios de forma genérica.",
            "uso": "Se utiliza para manejar y manipular rutas de archivos y directorios.",
            "exemplo": """
                import genericpath
                archivo = "/ruta/a/archivo.txt"
                print(genericpath.exists(archivo))  # Saída: True o False
                """
        },
        "get_resource_path": {
            "significado": "Método que obtiene la ruta de un recurso dentro de un paquete o aplicación.",
            "uso": "Se utiliza para localizar recursos dentro de un entorno empaquetado.",
            "exemplo": """
                import pkg_resources
                ruta = pkg_resources.resource_filename('mi_paquete', 'recurso.txt')
                print(ruta)
                """
        },
        "git_pull": {
            "significado": "Comando de Git que actualiza el repositorio local con los cambios más recientes del repositorio remoto.",
            "uso": "Se utiliza para obtener los cambios más recientes desde el repositorio remoto y fusionarlos con la rama local.",
            "exemplo": """
                git pull origin master
                """
        },
        "get_cached_properties": {
            "significado": "Método para obtener propiedades que han sido almacenadas en caché.",
            "uso": "Se utiliza para acceder a propiedades previamente calculadas y almacenadas en memoria para mejorar la eficiencia.",
            "exemplo": """
                class MiClase:
                    @property
                    def propiedad(self):
                        if not hasattr(self, '_cached_propiedad'):
                            self._cached_propiedad = 42  # Ejemplo de cálculo
                        return self._cached_propiedad
                obj = MiClase()
                print(obj.propiedad)  # Saída: 42
                """
        },
        "geopandas": {
            "significado": "Biblioteca de Python para la manipulación y análisis de datos geoespaciales.",
            "uso": "Se utiliza para trabajar con datos espaciales, como mapas y coordenadas geográficas.",
            "exemplo": """
                import geopandas as gpd
                gdf = gpd.read_file('mapa.shp')
                gdf.plot()
                """
        },
        "get_open_files": {
            "significado": "Función que obtiene una lista de archivos abiertos en un sistema.",
            "uso": "Se utiliza para monitorear los archivos abiertos en un proceso o sistema.",
            "exemplo": """
                import psutil
                procesos = psutil.process_iter(['pid', 'name'])
                for proceso in procesos:
                    archivos = proceso.open_files()
                    for archivo in archivos:
                        print(archivo.path)
                """
        },
        "get_active_connections": {
            "significado": "Método que obtiene las conexiones activas en un sistema o red.",
            "uso": "Se utiliza para obtener las conexiones activas en una aplicación o sistema operativo.",
            "exemplo": """
                import psutil
                conexiones = psutil.net_connections()
                for conexion in conexiones:
                    print(conexion)
                """
        },
        "guess_language": {
            "significado": "Función que adivina el idioma de un texto dado.",
            "uso": "Se utiliza para determinar el idioma de una cadena de texto.",
            "exemplo": """
                from langdetect import detect
                idioma = detect("Hola, ¿cómo estás?")
                print(idioma)  # Saída: es
                """
        },
        "get_doc": {
            "significado": "Método que obtiene la documentación asociada a un objeto o función.",
            "uso": "Se utiliza para obtener la cadena de documentación (docstring) de un objeto o función.",
            "exemplo": """
                def ejemplo():
                    \"\"\"Esta es la documentación de la función\"\"\"
                    pass
                print(ejemplo.__doc__)
                """
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
