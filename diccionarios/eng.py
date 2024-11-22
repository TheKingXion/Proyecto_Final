#vicho
diccionario_eng = {
    "a": {
        "any": {
            "significado": ": Returns True if at least one of the elements in an iterable is true",
            "uso": "Verify if a condition is a true iterable",
            "ejemplo": '''values = [0, False, 2]
            print(any(values))  # True'''
        },
        "all": {
            "significado": "Return True if all elements are true iterable",
            "uso": "Verifi is all contitions are true iterable",
            "ejemplo": '''values = [1, 2, 3]
            print(all(values))  # True'''
        },
        "abs": {
            "significado":"Returns the absolute value of a number",
            "uso": "It is used to obtain the absolute value of a number",
            "ejemplo": '''abs(-5)  # 5'''
        },
        "absolute_import": {
            "significado": "Policy used to enable absolute imports in Python 2.x and later versions",
            "uso": "It is used to avoid conflicts between local and global modules",
            "ejemplo": '''
                from __future__ import absolute_import

                # The global module always matters, not a local one with the same name
                import math
                '''
        },
        "add": {
            "significado": "Method used to add an element to a set or perform a sum between arrays (depending on the context)",
            "uso": "It is used in sets to add elements or in NumPy to perform mathematical operations",
            "ejemplo": '''
                # Sets
                ensemble = {1, 2, 3}
                ensemble.add(4)
                print(ensemble)  # Output: {1, 2, 3, 4}

                # NumPy
                import numpy as np
                result = np.add(2, 3)
                print(result)  # Output: 5 '''
        },
        "allclose": {
            "significado": "Verifies that all elements of two arrays are approximately equal",
            "uso": "It is used in NumPy to check the equality of elements with tolerance for small differences",
            "ejemplo": '''
                import numpy as np

                a = [1.0, 2.001]
                b = [1.0, 2.0009]
                print(np.allclose(a, b, atol=0.01))  # Output: True '''
        },
        "allexcept": {
            "significado": "It is not a native Python term. It can refer to a logical approach that applies operations to all elements except for a few specific ones",
            "uso": "Usually implemented manually",
            "ejemplo": '''
                list = [1, 2, 3, 4]
                result = [x for x in list if x != 2]  # Filters out all but 2
                print(result)  # Output: [1, 3, 4]
                '''
        },
         "append": {
            "significado": "Adds an element to the end of a list",
            "uso": "It is used to add new elements to an existing list",
            "ejemplo": '''
                list = [1, 2, 3]
                list.append(4)
                print(list)  # Output: [1, 2, 3, 4]
            '''
        },
        "apply": {
            "significado": "Method used to apply a function to rows or columns of a DataFrame",
            "uso": "It is used to perform custom operations on rows or columns",
            "ejemplo": '''
                import pandas as pd

                dice = pd.DataFrame({'A': [1, 2, 3]})
                dice['B'] = dice['A'].apply(lambda x: x * 2)
                print(dice)
                # Output:
                #    A  B
                # 0  1  2
                # 1  2  4
                # 2  3  6
                '''
        },
        "argmin": {
            "significado": "Returns the index of the minimum value in an array or iterable",
            "uso": "It is used in libraries such as NumPy to find the index of the lowest value in data structures",
            "ejemplo": '''
                import numpy as np

                numbers = [1, 5, 2, 9, 3]
                print(np.argmin(numbers))  # Output: 0 (Value 1 Index)
            '''
        },
        "array": {
            "significado": "It is a data structure that contains multiple elements of the same type, commonly used in libraries such as NumPy",
            "uso": "It is used to efficiently store and operate large amounts of homogeneous data",
            "ejemplo": '''
                import numpy as np

                numbers = np.array([1, 2, 3, 4])
                print(numbers)  # Output: [1 2 3 4]
            '''
        },
        "args": {
            "significado": "It is a parameter that allows it to receive a variable number of positional arguments in a function",
            "uso": "It is used to handle multiple arguments in a function without specifying each one individually",
            "ejemplo": '''
                def numbers_sum(*args):
                    return sum(args)

                print(numbers_sum(1, 2, 3))  # Output: 6
                '''
        },
        "arccos": {
            "significado": "Returns the cosine arc (in radians) of a value",
            "uso": "It is used in trigonometric calculations with NumPy",
            "ejemplo": '''
                import numpy as np

                result = np.arccos(0.5)
                print(result)  # Output: 1.0471975511965976 (equivalent a π/3)
                '''
        },
        "arcsin": {
            "significado": "Returns the arc sine (in radians) of a value",
            "uso": "It is used in trigonometric calculations with NumPy",
            "ejemplo": '''
                import numpy as np

                result = np.arcsin(0.5)
                print(result)  # Output: 0.5235987755982988 (equivalent a π/6)
                '''
        },
        "arctan": {
            "significado": "Returns the tangent arc (in radians) of a value",
            "uso": "It is used in trigonometric calculations with NumPy",
            "ejemplo": '''
                import numpy as np

                result = np.arctan(1)
                print(result)  # Output: 0.7853981633974483 (equivalent a π/4)
                '''
        },
        "argparse": {
            "significado": "Python module used to manage arguments and command-line options",
            "uso": "It is used to create easy-to-use command-line interfaces",
            "ejemplo": '''
                import argparse

                parser = argparse.ArgumentParser(description='ejemplo of argparse')
                parser.add_argument('--nome', type=str, help='your name')
                args = parser.parse_args()
                print(f'Hello, {args.nome}')
                '''
        },
        "array_like": {
            "significado": "Refers to any object that can be treated as an array, such as lists, tuples, or NumPy arrays",
            "uso": "It is used as input in NumPy or similar functions for operations with data",
            "ejemplo": '''
                import numpy as np

                list = [1, 2, 3]
                array = np.array(list)  # list and array_like
                print(array)  # Output: [1 2 3]
                '''
        },
        "arange": {
            "significado": "Generates an array with equally spaced values within a range",
            "uso": "It is used in NumPy to create number sequences",
            "ejemplo": '''
                import numpy as np

                result = np.arange(0, 10, 2)
                print(result)  # Output: [0 2 4 6 8]
                '''
        },
        "argmax": {
            "significado": "Returns the index of the maximum value in an array or iterable",
            "uso": "It is used in libraries such as NumPy to find the index of the highest value in data structures",
            "ejemplo": '''
                import numpy as np

                numbers = [1, 5, 2, 9, 3]
                print(np.argmax(numbers))  # Output: 3 (Value 9 Index)
            '''
        },
        "as": {
            "significado": "Keyword used to assign an alias to modules or in 'with' statements",
            "uso": "Makes it easy to reference long or specific names in code",
            "ejemplo": '''
                import numpy as np

                with open('file.txt', 'r') as file:
                    content = file.read()
                '''
        },
        "assert": {
            "significado": "Evaluates an expression and throws an exception 'AssertionError' if the expression is false",
            "uso": "It is used to check conditions that must be met during program execution",
            "ejemplo": '''
                x = 5
                assert x > 0, 'x must be greater than 0'  # Does not generate error
                assert x < 0, 'x must be less than 0'  # Generates AssertionError
                '''
        },
        "async": {
            "significado": "Defines an asynchronous function that can be used with 'await'",
            "uso": "It is used to implement asynchronous programming in Python",
            "ejemplo": '''
                import asyncio

                async def Greeting():
                    print('Hello')
                    await asyncio.sleep(1)
                    print('Bye')

                asyncio.run(Greeting())
                '''
        },
        "assertEqual": {
            "significado": "Checks if two values are equal in a unit test",
            "uso": "It is used in unit tests to validate the equality of expected and actual values",
            "ejemplo": '''
                import unittest

                class Test(unittest.TestCase):
                    def test_sum(self):
                        self.assertEqual(1 + 1, 2)  # The test passes
                '''
        },
        "assertIsNone": {
            "significado": "Checks if a value is None in a unit test",
            "uso": "It is used in unit tests to validate that a value is None",
            "ejemplo": '''
                import unittest

                class Test(unittest.TestCase):
                    def test_value_none(self):
                        self.assertIsNone(None)  # The test passes
                '''
        },
        "assertAlmostEqual": {
            "significado": "Checks whether two values are approximately equal to a specific number of decimal places in a unit test",
            "uso": "It is used in unit tests to validate values with tolerance to small differences",
            "ejemplo": '''
                import unittest

                class Test(unittest.TestCase):
                    def test_aprox(self):
                        self.assertAlmostEqual(3.14159, 3.14, places=2)  # The test passes
                '''
        },
        "as_tuple": {
            "significado": "Method that converts an object to a tuple (common in libraries such as SymPy)",
            "uso": "It is used to transform objects into tuple representations",
            "ejemplo": '''
                from sympy import Point

                p = Point(2, 3)
                print(p.as_tuple())  # Output: (2, 3)
                '''
        },
        "ascii": {
            "significado": "Returns a human-readable representation of an object using ASCII characters",
            "uso": "It is used to represent strings or characters in an ASCII-safe format by replacing non-ASCII characters with escape sequences",
            "ejemplo": '''
                texto = "Hi, how are you?"
                print(ascii(text))  # Output: 'Hi\\xe1, how are\\xea you\\xe1?'
            '''
        },
        "at": {
            "significado": "Method used to access specific elements in structures such as DataFrames or arrays (usually in pandas)",
            "uso": "It is used to quickly access an individual value in a specific position",
            "ejemplo": '''
                import pandas as pd

                dices = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
                print(dices.at[0, 'A'])  # Output: 1
                '''
        },
        "attribute": {
            "significado": "Refers to a property or characteristic associated with an object in Python",
            "uso": "It is used to access or modify properties of objects created from classes",
            "ejemplo": '''
                class Person:
                    def __init__(self, name, age):
                        self.name = name
                        self.age = age

                p = Person('João', 30)
                print(p.name)  # Output: João
                p.age = 31
                print(p.age)  # Output: 31
                '''
        },
        "attributeError": {
            "significado": "It is an exception that occurs when you try to access or assign an attribute that does not exist",
            "uso": "It is used to catch and handle errors related to invalid attributes",
            "ejemplo": '''
                try:
                    objet = 5
                    objet.atribute = 10
                except AttributeError as e:
                    print('Error:', e)
                # Output: Error: 'int' object has no attribute 'atribute'
                '''
        },
        "atleast_1d": {
            "significado": "Converts inputs to arrays with at least one dimension",
            "uso": "It is used in NumPy to ensure that data has a minimum dimension",
            "ejemplo": '''
                import numpy as np

                result = np.atleast_1d(5)
                print(result)  # Output: [5]
                '''
        },
        "atleast_2d": {
            "significado": "Converts inputs to arrays with at least two dimensions",
            "uso": "It is used in NumPy to work with data in array format",
            "ejemplo": '''
                import numpy as np

                result = np.atleast_2d([1, 2, 3])
                print(result)
                # Output:
                # [[1 2 3]]
                '''
        },
        "average": {
            "significado": "Averages the elements of an array or list",
            "uso": "It is used in NumPy to calculate averages, with the possibility of weighting values",
            "ejemplo": '''
                import numpy as np

                values = [1, 2, 3, 4]
                print(np.average(values))  # Output: 2.5
                '''
        },
        "await": {
            "significado": "It is used to wait for the result of an asynchronous function.",
            "uso": "It is used within functions defined with 'async' to pause their execution until an asynchronous task is completed",
            "ejemplo": '''
                import asyncio

                async def task():
                    await asyncio.sleep(1)
                    return 'Task ready'

                async def main():
                    result = await task()
                    print(result)

                asyncio.run(main())
                '''
        },
    },
    "b": {
        "break": {
            "significado":"End a loop early",
            "uso": "to manually Output a loop",
            "ejemplo":'''while True:
            number = int(input("enter a number (enter a 0 for Output): "))
            if number == 0:
            break  # Output from the bucle if the user write 0
            print(f"the number entered is {number}")'''
        },
        "bytes": {
            "significado": "Returns an immutable byte sequence object",
            "uso": "Working with Immutable Binary Data",
            "ejemplo": '''b = bytes([65, 66, 67])
            print(b)  # Result: b'ABC'''
        },
        "bin": {
            "significado": "Converts a number in its binary representation as a string",
            "uso": "It is used to obtain the binary representation of an integer",
            "ejemplo": '''
                number = 10
                print(bin(number))  # Output: '0b1010'
                '''
        },
        "bool": {
            "significado": "Type of data representing Boolean values: True or False",
            "uso": "It is used to represent and operate with truth values",
            "ejemplo": '''
                value = bool(1)
                print(value)  # Output: True
                '''
        },
        "bytearray": {
            "significado": "Mutable data type that represents a sequence of bytes",
            "uso": "It is used to modify byte sequences",
            "ejemplo": '''
                b = bytearray([65, 66, 67])
                b[0] = 90
                print(b)  # Output: bytearray(b'ZBC')
                '''
        },
        "byteswap": {
            "significado": "Method that swaps the order of bytes in an object",
            "uso": "It is used to change the order of bytes in a numeric data type",
            "ejemplo": '''
                import numpy as np

                a = np.array([1, 256], dtype=np.int16)
                a = a.byteswap()
                print(a)  # Output: [256 1]
                '''
        },
        "buffer": {
            "significado": "A class in Python that provides a view of accessing an object's memory area",
            "uso": "It is used to access memory efficiently, especially in operations with large amounts of data",
            "ejemplo": '''
                buffer = memoryview(b'abc')
                print(buffer[0])  # Output: 97 (equivalent 'a')
                '''
        },
        "base64": {
            "significado": "Module that provides functions for encoding and decoding base64 data",
            "uso": "It is used to represent binary data in a string of ASCII characters",
            "ejemplo": '''
                import base64

                encoded = base64.b64encode(b'abc')
                print(encoded)  # Output: b'YWJj'
                '''
        },
        "bitwise_and": {
            "significado": "Operator that performs a bitwise AND operation between two numbers",
            "uso": "It is used to compare the corresponding bits of two numbers and return 1 only if both bits are 1",
            "ejemplo": '''
                x = 5  # binary: 0101
                y = 3  # binary: 0011
                print(x & y)  # Output: 1 (binary: 0001)
                '''
        },
        "bitwise_or": {
            "significado": "Operator performing a bitwise OR operation between two numbers",
            "uso": "It is used to compare the corresponding bits of two numbers and return 1 if at least one of the bits is 1",
            "ejemplo": '''
                x = 5  # binary: 0101
                y = 3  # binary: 0011
                print(x | y)  # Output: 7 (binary: 0111)
                '''
        },
        "bitwise_xor": {
            "significado": "Operator that performs a bitwise XOR operation between two numbers",
            "uso": "It is used to compare the matching bits of two numbers and return 1 if the bits are different",
            "ejemplo": '''
                x = 5  # binary: 0101
                y = 3  # binary: 0011
                print(x ^ y)  # Output: 6 (binary: 0110)
                '''
        },
        "bitwise_not": {
        "significado": "Operator that performs a bitwise NOT operation on a number",
        "uso": "It is used to invert all the bits of a number",
        "ejemplo": '''
            x = 5  # binary: 0101
            print(~x)  # Output: -6 (binary: 1010)
            '''
        },
        "binomial": {
            "significado": "Function that calculates the binomial coefficient (n over k)",
            "uso": "It is used to calculate the number of ways to select k elements from a set of n elements",
            "ejemplo": '''
                from scipy.special import comb

                result = comb(5, 2)
                print(result)  # Output: 10.0
                '''
        },
        "binascii": {
            "significado": "Module that contains functions to convert between binary and different text representations",
            "uso": "It is used to perform conversions between text strings and binary data",
            "ejemplo": '''
                import binascii

                encoded = binascii.hexlify(b'abc')
                print(encoded)  # Output: b'616263'
                '''
        },
        "byteorder": {
            "significado": "Indicates the order of bytes to represent numbers in memory",
            "uso": "It is used to manipulate the representation of numbers in systems with different architectures",
            "ejemplo": '''
                import sys

                print(sys.byteorder)  # Output: 'little' or 'big'
                '''
        },
        "bit_length": {
            "significado": "Returns the number of bits required to represent a binary number",
            "uso": "It is used to obtain the length in bits of an integer",
            "ejemplo": '''
                number = 10
                print(number.bit_length())  # Output: 4
                '''
        },
        "breakpoint": {
            "significado": "A function that establishes a breakpoint in the code by activating the debugger",
            "uso": "It is used to pause execution and enter the interactive debugger",
            "ejemplo": '''
                def funtion():
                    breakpoint()  # Interruption here
                    print('Hi')
                funtion()
                '''
        },
        "binhex": {
            "significado": "Function to convert a binary file into hexadecimal format",
            "uso": "It is used to represent binary data in hexadecimal readable format",
            "ejemplo": '''
                import binhex

                with open('file.bin', 'rb') as f:
                    binhex.binhex(f, 'file.hex')
                '''
        },
        "bitset": {
            "significado": "Data structure that allows you to store a collection of bits",
            "uso": "It is used to represent sets of bits and perform efficient operations on them",
            "ejemplo": '''
                # ejemplo is not standard in Python, but one can use the 'bitarray' module to create bitsets
                from bitarray import bitarray

                bitset = bitarray('10101')
                print(bitset)  # Output: bitarray('10101')
                '''
        },
        "broadcast": {
            "significado": "Technique that allows arrays of different shapes to be aligned to perform element-wise operations",
            "uso": "It is mainly used in NumPy for operations with arrays of different sizes",
            "ejemplo": '''
                import numpy as np

                a = np.array([1, 2, 3])
                b = np.array([[1], [2], [3]])
                result = a + b
                print(result)
                # Output:
                # [[2 3 4]
                #  [3 4 5]
                #  [4 5 6]]
                '''
        },
        "bitarray": {
            "significado": "Module that implements an efficient data type for working with bit arrays",
            "uso": "It is used to efficiently manipulate and manage bit arrays",
            "ejemplo": '''
                from bitarray import bitarray

                a = bitarray('10101')
                a.append('1')
                print(a)  # Output: bitarray('101011')
                '''
        },
        "buffer": {
            "significado": "A class in Python that provides a view of accessing an object's memory area",
            "uso": "It is used to access memory efficiently, especially in operations with large amounts of data",
            "ejemplo": '''
                buffer = memoryview(b'abc')
                print(buffer[0])  # Output: 97 (equivalent 'a')
                '''
        },
        "bitwise_left_shift": {
            "significado": "Operator that performs a bit shift to the left",
            "uso": "It is used to shift the bits of a number to the left by multiplying the value by powers of two",
            "ejemplo": '''
                x = 5  # binary: 0101
                print(x << 1)  # Output: 10 (binary: 1010)
                '''
        },
        "bitwise_right_shift": {
            "significado": "Operator that performs a bit shift to the right",
            "uso": "It is used to shift the bits of a number to the right, dividing the value by powers of two",
            "ejemplo": '''
                x = 5  # binary: 0101
                print(x >> 1)  # Output: 2 (binary: 0010)
                '''
        },
        "bz2": {
            "significado": "Module that provides compression and decompression using the bzip2 algorithm",
            "uso": "It is used to manipulate compressed files in the bzip2 format",
            "ejemplo": '''
                import bz2

                with bz2.open('file.bz2', 'rb') as file:
                    content = file.read()
                    print(content)
                '''
        },
        "bool_": {
            "significado": "NumPy data type for boolean values, similar to Python's 'bool'",
            "uso": "It is used in operations with NumPy arrays to represent Boolean values",
            "ejemplo": '''
                import numpy as np

                value = np.bool_(True)
                print(value)  # Output: True
                '''
        },
    },
    "c": {
        {
    "callable": {
        "significado": "Checks if an object is callable (like a function or a class).",
        "uso": "Used to determine if an object can be called.",
        "ejemplo": '''
            def function():
                return "Hello"
            
            print(callable(function))  # Output: True
            print(callable(42))  # Output: False
            '''
    },
    "chr": {
        "significado": "Returns the Unicode character corresponding to an integer number.",
        "uso": "Used to convert a Unicode code point into its character representation.",
        "ejemplo": '''
            print(chr(65))  # Output: 'A'
            print(chr(8364))  # Output: '€'
            '''
    },
    "class": {
        "significado": "Keyword used to define a class in Python.",
        "uso": "Used to create custom objects with attributes and methods.",
        "ejemplo": '''
            class Person:
                def __init__(self, name):
                    self.name = name
                
                def greet(self):
                    print(f"Hello, my name is {self.name}")
            
            p = Person("Juan")
            p.greet()  # Output: Hello, my name is Juan
            '''
    },
    "classmethod": {
        "significado": "Defines a class method that takes the class as the first argument instead of an instance.",
        "uso": "Used to create methods that affect the class in general.",
        "ejemplo": '''
            class MyClass:
                counter = 0

                @classmethod
                def increment(cls):
                    cls.counter += 1
            
            MyClass.increment()
            print(MyClass.counter)  # Output: 1
            '''
    },
    "compile": {
        "significado": "Compiles a string of code into an executable Python object.",
        "uso": "Used to compile dynamic code from text or files.",
        "ejemplo": '''
            code = "print('Hello World')"
            compiled = compile(code, '<string>', 'exec')
            exec(compiled)  # Output: Hello World
            '''
    },
    "complex": {
        "significado": "Creates a complex number in Python.",
        "uso": "Used to represent complex numbers with real and imaginary parts.",
        "ejemplo": '''
            c = complex(2, 3)
            print(c)  # Output: (2+3j)
            print(c.real, c.imag)  # Output: 2.0 3.0
            '''
    },
    "continue": {
        "significado": "Keyword that skips to the next iteration of a loop.",
        "uso": "Used to skip the rest of the code in the current iteration.",
        "ejemplo": '''
            for i in range(5):
                if i == 2:
                    continue
                print(i)  # Output: 0 1 3 4
            '''
    },
    "copy": {
        "significado": "Creates a shallow copy of an object.",
        "uso": "Used to duplicate data structures without duplicating nested objects.",
        "ejemplo": '''
            import copy

            list1 = [1, 2, [3, 4]]
            copy1 = copy.copy(list1)
            print(copy1)  # Output: [1, 2, [3, 4]]
            '''
    },
    "coroutine": {
        "significado": "Object representing a suspended asynchronous function.",
        "uso": "Used to manage asynchronous tasks with `async` and `await`.",
        "ejemplo": '''
            async def task():
                print("Start")
                await asyncio.sleep(1)
                print("End")
            
            import asyncio
            asyncio.run(task())  # Output: Start... End
            '''
    },
    "count": {
        "significado": "Returns the number of occurrences of an element in a collection.",
        "uso": "Used to count the number of times an element appears in a list or string.",
        "ejemplo": '''
            list1 = [1, 2, 2, 3]
            print(list1.count(2))  # Output: 2
            '''
    },
    "clear": {
        "significado": "Removes all elements from a list or dictionary.",
        "uso": "Used to clear the contents of a list or dictionary.",
        "ejemplo": '''
            list1 = [1, 2, 3]
            list1.clear()
            print(list1)  # Output: []
            '''
    },
    "cmath": {
        "significado": "Module that provides mathematical functions for working with complex numbers.",
        "uso": "Used to perform mathematical operations on complex numbers.",
        "ejemplo": '''
            import cmath

            number = cmath.sqrt(-1)
            print(number)  # Output: 1j
            '''
    },
    "chain": {
        "significado": "Function that combines multiple iterators into one.",
        "uso": "Used to concatenate multiple iterators.",
        "ejemplo": '''
            import itertools

            a = [1, 2, 3]
            b = [4, 5, 6]
            result = list(itertools.chain(a, b))
            print(result)  # Output: [1, 2, 3, 4, 5, 6]
            '''
    },
    "csv": {
        "significado": "Module to read and write CSV (Comma Separated Values) files.",
        "uso": "Used to handle CSV files.",
        "ejemplo": '''
            import csv

            with open('file.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Name', 'Age'])
                writer.writerow(['Ana', 30])
            '''
    },
    "copyreg": {
        "significado": "Module that provides functions for registering objects for copying and unpickling.",
        "uso": "Used to customize the behavior of object copying and storing.",
        "ejemplo": '''
            import copyreg

            def create_person(name, age):
                return {'name': name, 'age': age}

            copyreg.pickle(dict, create_person)
            '''
    },
    "counter": {
        "significado": "Class in the `collections` module that counts hashable elements in a sequence.",
        "uso": "Used to count the frequency of elements in an iterable.",
        "ejemplo": '''
            from collections import Counter

            counter = Counter([1, 2, 2, 3, 3, 3])
            print(counter)  # Output: Counter({3: 3, 2: 2, 1: 1})
            '''
    },
    "cProfile": {
        "significado": "Module for performance profiling of Python programs.",
        "uso": "Used to profile code and analyze the efficiency of the program.",
        "ejemplo": '''
            import cProfile

            def function():
                for i in range(1000):
                    pass

            cProfile.run('function()')
            '''
    },
    "capitalize": {
        "significado": "String method that capitalizes the first letter and makes the rest lowercase.",
        "uso": "Used to capitalize the first letter of a string.",
        "ejemplo": '''
            text = 'hello world'
            print(text.capitalize())  # Output: 'Hello world'
            '''
    },
    "center": {
        "significado": "String method that centers a string within a specified length field.",
        "uso": "Used to align text in the center of a string with padding.",
        "ejemplo": '''
            text = 'hello'
            print(text.center(10, '*'))  # Output: '**hello****'
            '''
    },
    "ceil": {
        "significado": "Function in the `math` module that returns the smallest integer greater than or equal to a given number.",
        "uso": "Used to round a number up.",
        "ejemplo": '''
            import math

            number = 3.4
            print(math.ceil(number))  # Output: 4
            '''
    },
    "call": {
        "significado": "Method used to invoke a callable object, like functions or classes.",
        "uso": "Used to call an object that can be executed.",
        "ejemplo": '''
            def greeting():
                return 'Hello'
            
            print(callable(greeting))  # Output: True
            '''
    },
    "clamp": {
        "significado": "Function that restricts a value within a specified range.",
        "uso": "Used to ensure a value stays within a given range.",
        "ejemplo": '''
            def clamp(value, minimum, maximum):
                return max(minimum, min(value, maximum))

            print(clamp(5, 1, 10))  # Output: 5
            '''
    },
    "choice": {
        "significado": "Function in the `random` module that selects a random element from a sequence.",
        "uso": "Used to select a random value from a list or sequence.",
        "ejemplo": '''
            import random

            list1 = [1, 2, 3, 4, 5]
            print(random.choice(list1))  # Output: a random value from the list
            '''
    },
    "collections": {
        "significado": "Module that implements specialized data types like `Counter`, `deque`, `OrderedDict`, among others.",
        "uso": "Used to work with collections of data efficiently.",
        "ejemplo": '''
            from collections import deque

            queue = deque([1, 2, 3])
            queue.append(4)
            print(queue)  # Output: deque([1, 2, 3, 4])
            '''
    }
}

     },
    "d": {
        "del": {
            "significado": "Remove a object or variable",
            "uso": "Delete a object, variable or element from a colletion",
            "ejemplo": '''list = [1, 2, 3]
            del list[0]
            print(list)  # [2, 3]'''
        },
    },
    "e": {
       "enumerate": {
            "significado":" Returns an enumerated object, i.e., an index and its value",
            "uso": "It is used to obtain both the index and the value of an iterable in a loop",
            "ejemplo": '''for idx, val in enumerate(["a", "b", "c"]):
            print(idx, val)'''
            },
        "except": {
            "significado": "Error or unexpected event that interrupts the normal flow of the program",
            "uso": " Handling errors and unforeseen situations",
            "ejemplo": '''try:
            result = 10 / 0
            except ZeroDivisionError:
            print("cannot be divided by zero")'''
        },
        },
      "f": {
         "format": {
            "significado": "Allows values to be inserted within a text string in a more readable and flexible way",
            "uso": "It is used to format strings dynamically, inserting values in specific places",
            "ejemplo": '''name = "Juan"
            age = 30
            message = "Hi, my name is {} and i am {} years old.".format(name, age)
            print(mensaje)  # "Hello, my name is Juan and i am 30 years old"'''
        },
        "float": {
            "significado":"make a chain of numbers into a real numbers",
            "uso": "work for make a chain number into a float numbers",
            "ejemplo": '''float("10.5")  # 10.5'''
        },
        "find": {
            "significado":"refers to the definition or concept of something within the programming language",
            "uso": " refers to how a concept is implemented or employed within a program",
            "ejemplo": '''def plus(a, b):
            return a + b
            result = plus(3, 4)
            print(result)  # This will print 7'''
        },
        },
    "g": {
       "global": {
            "significado":" a Variable away from all funtions and classes",
            "uso": " Make a variable accessible from anywhere in your code",
            "ejemplo": '''x = 10
            def funtion():
            global x
            x = 20'''
        },
    },
    "h": {
        # Aquí puedes agregar funciones que comiencen con la letra H
    },
    "i": {
        "if": {
            "significado": "Condition that is assessed as true or false",
            "uso": "Used to make decisions in the flow of a program",
            "ejemplo": "if x > 10: print('greater than 10')"
        },
        "input": {
            "significado":"Reads user-written data",
            "uso": "It is used to interact with the user and obtain information",
            "ejemplo": "input('write a number')"
        },
        "_init_": {
            "significado": "It's a special method in Python classes that's called when you create a new instance of the",
            "uso": " To initialize object attributes.",
            "ejemplo": '''class Person:
            def __init__(self, name, age):
            self.name = name
            self.age = age'''
        },
        "index": {
            "significado":"Returns the index of the first occurrence of a value in a list or string",
            "uso": " Search the position of a element inside of a iterable",
            " ejemplo": '''list = [10, 20, 30, 40]
            print(list.index(30))  # 2'''
        },
        "int": {
            "significado":"Turn a string into a whole number",
            "uso": "It is used to convert numerical strings into integer values",
            "ejemplo": '''int("10")  # 10'''
        },
    },
    "j": {
        "join": {
            "significado": "Join the elements of an iterable in a string, using a specific delimiter",
            "uso": "Combine items from a list or tuple into a single string",
            "ejemplo": '''words = ["Hello", "world"]
            result = " ".join(words)
            print(result)  '''
        },
    },
    "k": {
        # Aquí puedes agregar funciones que comiencen con la letra K
    },
    "l": {
         "len()": {
            "significado": "Returns the length of an object (such as a list or string)",
            "uso": "To count elements in a sequence",
            "ejemplo": '''text = "Hello word"
            longitude = longitude (text)
            print(f"the longitude of the chain is: {longitude}")'''
        },
        "lambda": {
            "significado":"Anonymous (unnamed) function that can be defined on a single line",
            "uso": " Define simple functions to use in a single expression",
            "ejemplo": '''square = lambda x: x**2
            print(square(4))  # print 16'''
        },
        "locals()": {
            "significado": "Returns a dictionary that represents the current local namespace",
            "uso": "Get the local context of variables within a function or module",
            "ejemplo": '''def ejemplo():
            b = 20
            print(locals())  # Result: {'b': 20}
            ejemplo()'''
        },
    },
    "m": {
        "max": {
            "significado": "Returns the largest value of an iterable",
            "uso": "find the max value",
            "ejemplo": '''max([1, 2, 3])  # 3'''
        },
        "map": {
            "significado":"Apply a function to each element of an iterable",
            "uso": "It is used to apply an operation to all the elements of an iterable.",
            "ejemplo": '''map(lambda x: x * 2, [1, 2, 3])  # [2, 4, 6]'''
        },
    },
    "n": {
        # Aquí puedes agregar funciones que comiencen con la letra N
    },
    "o": {
        "os": {
            "significado":" The module allows you to interact with the operating system, such as manipulating files, directories, obtaining information about the system, etc",
            "uso": "It is useful for performing low-level operations on the system, such as browsing directories or deleting files",
            "ejemplo": '''import os
            Current_Directory = os.getcwd()
            print(f"Current Directory: {Current_Directory}")
            os.mkdir("new_ directory")
            files = os.listdir(Current_Directory)
            print(f"files in the directory: {files}")
            os.rmdir("new_directory")'''
        },
         "ord": {
            "significado": "Converts a character to its ASCII code",
            "uso": "Getting the numeric value of a character",
            "ejemplo": '''ord('A')  # Result: 65'''
        },
         "open()": {
            "significado": "Opens a file and returns it as a file object",
            "uso": "read or write files",
            "ejemplo": '''file = open("ejemplo.txt", "w")
            file.write("Hello world")
            file.close()'''
        },
    },
    "p": {
        "pop": {
            "significado":"Deletes and returns an item from a list in a specific index",
            "uso": "To remove a specific value from a list",
            "ejemplo": '''fruits = ["apple", "banana", "orange", "pear"]
            ultima_fruta = fruits.pop()
            print("Deleted last fruit:", last_fruit)  # Output: pera
            print("list later of pop:", fruits)  # Output: ['apple', 'banana', 'orange']'''
        },
         "parseInt": {
            "significado":"Convert a string to an integer",
            "uso": "Used to convert text strings representing numbers to integer values",
            "ejemplo": '''parseInt("10");  // 10'''
        },
        "pathlib": {
            "significado":"Pathlib is a module that facilitates the handling of file and directory paths in a more readable and modern way",
            "uso": "It is used to handle paths more easily and to perform file operations efficiently",
            "ejemplo": '''from pathlib import Path
            route = Path("my_directory/my_file.txt")
            if route.exists():
            print(f"The file {route} exist.")
            else:
            print(f"The file {route} no exist.")
            Path("new_directory").mkdir(parents=True, exist_ok=True)
            content = route.read_text()
            print(content)'''
        },
    },
    "q": {
        # Aquí puedes agregar funciones que comiencen con la letra Q
    },
    "r": {
        "range": {
        "significado": "Returns a sequence of numbers, ussualy in loops.",
        "uso": "To create a range of numbers that can be iterated",
        "ejemplo": '''for i in range(5):
            print(i)'''
        },
        "reversed": {
            "significado": "Return the iterable invested",
            "uso": "Serves to reverse the order of the elements of an iterable",
            "ejemplo": '''reversed([1, 2, 3])  # [3, 2, 1]'''
        },
        "reduce()": {
            "significado":"The reduce() function applies a cumulative function to the elements of an iterable, reducing it to a single value",
            "uso": "It is used to perform cumulative operations, such as adding or multiplying all the items in a list",
            "ejemplo": '''from functools import reduce
            numbers = [1, 2, 3, 4]
            results = reduce(lambda x, y: x + y, numbers)
            print(resuls)  # 10'''
        },
        "return": {
            "significado": "Value that a function returns to the person who invokes it",
            "uso": "Get the result of executing a function",
            "ejemplo": '''def multiplicate(a, b):
            return a * b
            result = multiplicate(3, 4)'''
        },
    },
    "s": {
        "str": {
        "significado": "make a value into a text chain",
        "uso": " to make a value like a text",
        "ejemplo":''' # number
        number = 123
        number_like_str = str(number)
        print(type(number_like_str))  # Output: <class 'str'>
        print(number_like_str)        # Output: '123'''
        },
        "split": {
        "significado":"Divides a string into a list of substrings.",
        "uso": " It is the first parameter of any instance method of a class",
        "ejemplo": '''text = "Hello word Python"
        words = text.split()
        print(words)'''
        },
        "sorted": {
            "significado":"Returns a new list with the items of an iterable sorted",
            "uso": "Sort a list or tuple in ascending or descending order",
            "ejemplo": '''list = [4, 1, 3, 2]
            print(sorted(list))  # [1, 2, 3, 4]'''
        },
        "sum": {
            "significado":"Returns the sum of the elements of an iterable",
            "uso": "Add up items in a list or tuple",
            "ejemplo": '''sum([1, 2, 3])  # 6'''
        },
        " shutil": {
            "significado":" Shutil is a module that provides a way to copy, move, or delete files and directories",
            "uso": "Used for high-level operations with files and directories, such as copying a file or moving an entire directory",
            "ejemplo": '''pimport shutil
            shutil.copy("origin.txt", "destiny.txt")
            shutil.move("origin.txt", "new_directory/origin.txt")
            shutil.remove("destiny.txt")'''
        },
        "super() ": {
            "significado":"Using super() allows you to call a base class method from a derived class",
            "uso": "Used when a child class needs to extend or modify the behavior of a method of the base class",
            "ejemplo": '''class Animal:
            def speak(self):
            return "The animal make a sound"
            class dog(Animal):
            def speak(self):
            return super().speak() + " and the dog barks."
            my_dog = dog()
            print(my_dog.speak())  # The animal make a sound. and the dog barks.'''
        },
    },
    "t": {
        "type": {
            "significado":"Returns the type of an object",
            "uso": "It is used to verify the type of a variable",
            "ejemplo": '''type(10)  # <class 'int'>'''
        },
    },
    "u": {
        # Aquí puedes agregar funciones que comiencen con la letra U
    },
    "v": {
        # Aquí puedes agregar funciones que comiencen con la letra V
    },
    "w": {
        "with": {
            "significado":"Used to handle resources such as files, databases, network connections, etc., efficiently",
            "uso": " Ensures that resources are closed correctly, even if an exception occurs",
            "ejemplo": '''try:
            with open("file.txt", "r") as file:
            content = file.read()
            print(content)
            except FileNotFoundError:
            print("the file not exist")'''
        },
    },
    "x": {
        # Aquí puedes agregar funciones que comiencen con la letra X
    },
    "y": {
        # Aquí puedes agregar funciones que comiencen con la letra Y
    },
    "z": {
        "zip": {
            "significado":"Join multiple iterables into a single tuple sequence",
            "uso": "Combine lists or tuples so that their items are paired",
            "ejemplo": '''zip([1, 2], ["a", "b"])  # [(1, "a"), (2, "b")]'''
        },
    },
}

