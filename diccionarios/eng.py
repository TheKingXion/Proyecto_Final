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
                parser.add_argument('--name', type=str, help='your name')
                args = parser.parse_args()
                print(f'Hello, {args.name}')
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
                text = "Hi, how are you?"
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

                p = Person('pepe', 30)
                print(p.name)  # Output: pepe
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
        },
     },
    "d": {
        "def": {
            "significado": "Python keyword used to define a function",
            "uso": "It is used to create a new function with a name and a block of code",
            "ejemplo": '''
                def Hello_world():
                    print('Hello World')

                Hello_world()  # Output: Hello World
                '''
        },
        "delattr": {
            "significado": "Function that removes an attribute from an object in Python",
            "uso": "It is used to exclude a specific attribute of an object",
            "ejemplo": '''
                class Person:
                    def __init__(self, name):
                        self.name = name

                p = Person('pepe')
                delattr(p, 'name')
                print(hasattr(p, 'name'))  # Output: False
                '''
        },
        "dataframe": {
            "significado": "Two-dimensional data structure in the Pandas library, similar to a table, which allows you to store data of different types",
            "uso": "It is used to manipulate large volumes of tabular data in Python",
            "ejemplo": '''
                import pandas as pd

                data = {'Name': ['pepe', 'age'], 'age': [28, 22]}
                df = pd.DataFrame(data)
                print(df)
                '''
        },
        "decode": {
            "significado": "A method used to decode binary data into a text format, usually in an encoding such as UTF-8",
            "uso": "It is used to convert binary data into readable text strings",
            "ejemplo": '''
                Encoded = b'Hello World'
                Decoded = Encoded.decode('utf-8')
                print(Decoded)  # Output: Hello World
                '''
        },
        "decimal": {
            "significado": "Python module that provides support for performing calculations with arbitrary precision decimals",
            "uso": "It is used to perform accurate arithmetic operations without the rounding errors typical of floating-point numbers",
            "ejemplo": '''
                from decimal import Decimal

                x = Decimal('0.1')
                y = Decimal('0.2')
                print(x + y)  # Output: 0.3
                '''
        },
        "device": {
            "significado": "General term to refer to any hardware device or system where a program runs",
            "uso": "It is used to refer to devices such as computers, mobile phones, etc",
            "ejemplo": '''
            import torch

            device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

            print(f'Using device: {device}')

            tensor = torch.randn(3, 3)
            tensor = tensor.to(device)

            print(f'Tensor: {tensor}')
            print(f'Tensor is on device: {tensor.device}')
            '''
        },
        "dict.get": {
            "significado": "Python dictionaries method that returns the value of a specified key or a default value if the key does not exist",
            "uso": "It is used to get the value associated with a key without generating an error if the key does not exist",
            "ejemplo": '''
                d = {'a': 1, 'b': 2}
                print(d.get('a'))  # Output: 1
                print(d.get('c', 'not found'))  # Output: not found
                '''
        },
        "dropna": {
            "significado": "Method in Pandas used to remove missing values (NaN) in a DataFrame or Series",
            "uso": "It is used to clean up data by removing rows or columns that contain null values",
            "ejemplo": '''
                import pandas as pd

                df = pd.DataFrame({'A': [1, 2, None], 'B': [None, 3, 4]})
                print(df.dropna())
                '''
        },
        "dtype": {
            "significado": "Property of arrays in Numpy or columns in a Pandas DataFrame that indicates the data type of the elements",
            "uso": "It is used to obtain or specify the type of data of an array or column",
            "ejemplo": '''
                import numpy as np

                arr = np.array([1, 2, 3])
                print(arr.dtype)  # Output: int64
                '''
        },
        "deque.appendleft": {
            "significado": "Method of the 'deck' data type in the 'collections' module that adds an element to the beginning of the deck",
            "uso": "It is used to insert a new element on the left side of a deck",
            "ejemplo": '''
                from collections import deque

                d = deque([2, 3, 4])
                d.appendleft(1)
                print(d)  # Output: deque([1, 2, 3, 4])
                '''
        },
        "dict.update": {
            "significado": "Python dictionaries method that updates a dictionary with the elements of another dictionary or iterable",
            "uso": "It is used to add or modify elements in a dictionary using another dictionary or iterate",
            "ejemplo": '''
                d1 = {'a': 1, 'b': 2}
                d2 = {'b': 3, 'c': 4}
                d1.update(d2)
                print(d1)  # Output: {'a': 1, 'b': 3, 'c': 4}
                '''
        },
        "del": {
            "significado": "Python keyword that removes an attribute or element from a collection",
            "uso": "It is used to remove elements from a list, an object's attribute, or a variable",
            "ejemplo": '''
                list = [1, 2, 3]
                del list[1]
                print(list)  # Output: [1, 3]
                '''
        },
        "dict": {
            "significado": "Type of data in Python that represents a dictionary, a collection of key-value pairs",
            "uso": "It is used to store and manipulate data efficiently by associating unique keys with values",
            "ejemplo": '''
                d = {'a': 1, 'b': 2}
                print(d['a'])  # Output: 1
                '''
        },
        "dir": {
            "significado": "Function that returns a list of an object's attributes and methods",
            "uso": "It is used to obtain information about the methods and attributes available for an object or module",
            "ejemplo": '''
                x = [1, 2, 3]
                print(dir(x))
                '''
        },
        "divmod": {
            "significado": "Function that takes two numbers and returns a tuple with the quotient and the rest of its division",
            "uso": "It is used to obtain both the quotient and the remainder of a division in a single operation",
            "ejemplo": '''
                result = divmod(9, 4)
                print(result)  # Output: (2, 1)
                '''
        },
        "deque": {
            "significado": "Type of data in the Python 'collections' module that represents a double-ended queue, allowing you to add and remove elements from both ends efficiently",
            "uso": "It is used to implement queues and stacks in an efficient manner",
            "ejemplo": '''
                from collections import deque

                d = deque([1, 2, 3])
                d.append(4)
                print(d)  # Output: deque([1, 2, 3, 4])
                '''
        },
        "defaultdict": {
            "significado": "Class in the 'collections' module that extends the default dictionary and allows you to set a default value for non-existent keys",
            "uso": "It is used to prevent errors when accessing non-existent keys by providing a default value",
            "ejemplo": '''
                from collections import defaultdict

                d = defaultdict(int)
                d['a'] += 1
                print(d)  # Output: defaultdict(<class 'int'>, {'a': 1})
                '''
        },
        "decode": {
            "significado": "Method used to convert binary data to text in a specific encoding",
            "uso": "It is used to decode a sequence of bytes into a text string in a specific encoding",
            "ejemplo": '''
                encoded = b'Hello World'
                decoded = encoded.decode('utf-8')
                print(decoded)  # Output: Hello Wolrd
                '''
        },
        "deflate": {
            "significado": "Lossless data compression algorithm, used to reduce file sizes",
            "uso": "It is used to compress data into a more efficient format",
            "ejemplo": '''
                import zlib

                data = b'Hello Wolrd'*100
                compressed = zlib.compress(data)
                print(compressed)
                '''
        },
        "deepcopy": {
            "significado": "Function of the 'copy' module that creates a deep copy of an object, i.e. copies all elements of the original object, including objects within objects",
            "uso": "It is used when it is necessary to make a complete and independent copy of an object",
            "ejemplo": '''
                import copy

                original = {'a': [1, 2, 3]}
                copy = copy.deepcopy(original)
                copy['a'][0] = 100
                print(original)  # Output: {'a': [1, 2, 3]}
                print(copy)     # Output: {'a': [100, 2, 3]}
                '''
        },
        "detach": {
            "significado": "Method used on objects in Python to unlink an object from its context or dataflow",
            "uso": "It is used to free up resources or unbind an object from its execution environment",
            "ejemplo": '''
                import torch

                tensor = torch.tensor([1, 2, 3])
                detached_tensor = tensor.detach()
                print(detached_tensor)  # Output: tensor([1, 2, 3])
                '''
        },
        "dump": {
            "significado": "Pickle library method that serializes an object and writes it to a file",
            "uso": "It is used to save an object to a file in serialized form",
            "ejemplo": '''
                import pickle

                data = {'a': 1, 'b': 2}
                with open('data.pkl', 'wb') as f:
                    pickle.dump(data, f)
                '''
        },
        "dumps": {
            "significado": "Pickle library method that serializes an object and returns it as a byte string",
            "uso": "It is used to convert an object into a string format for storage or transmission",
            "ejemplo": '''
                import pickle

                data = {'a': 1, 'b': 2}
                serialized = pickle.dumps(data)
                print(serialized)
                '''
        },
        "difference": {
            "significado": "Sets method in Python that returns the difference between two or more sets",
            "uso": "It is used to find the elements that are in one set but not in the others",
            "ejemplo": '''
                a = {1, 2, 3}
                b = {2, 3, 4}
                print(a.difference(b))  # Output: {1}
                '''
        },
        "difference_update": {
            "significado": "Sets method in Python that removes elements from one set that are present in another set",
            "uso": "It is used to modify a set by removing the elements that are in another set",
            "ejemplo": '''
                a = {1, 2, 3}
                b = {2, 3, 4}
                a.difference_update(b)
                print(a)  # Output: {1}
                '''
        },
        "decode_header": {
            "significado": "Function of the 'email.header' module that decodes an email header",
            "uso": "It is used to decode an email header that can be in different encodings",
            "ejemplo": '''
                from email.header import decode_header

                header = '=?utf-8?B?SG9sYSBNdW5kbyA8MTIzNDU+?='
                decoded, encoding = decode_header(header)[0]
                print(decoded.decode(encoding))  # Output: Hello World <12345>
                '''
        },
        "disk_usage": {
            "significado": "Function of the 'shutil' module that returns disk usage of a path or directory",
            "uso": "It is used to obtain information about the used and available space in a file system",
            "ejemplo": '''
                import shutil

                usage = shutil.disk_usage('/')
                print(usage)  # Output: usage(total=500000000, used=200000000, free=300000000)
                '''
        },
        "datetime": {
            "significado": "Python module that provides classes for working with dates and times",
            "uso": "It is used to manipulate and work with dates, times and times in general",
            "ejemplo": '''
                import datetime

                now = datetime.datetime.now()
                print(now)  # Output: 2024-11-22 12:00:00.123456
                '''
        },
        "disk_cache": {
            "significado": "Disk caching to improve data access speed or computational results",
            "uso": "It is used to temporarily store results or data on disk to avoid the need to recalculate or re-obtain the data",
            "ejemplo": '''
                import joblib

                result = joblib.Memory('cache_dir').cache(some_function)
                '''
        },
    },
    "e": {
       "enumerate": {
            "significado": "Built-in Python function that adds a counter to an iterable and returns it as an iterable tuple object",
            "uso": "It is used to obtain both the index and the value of elements in an iterable",
            "ejemplo": '''
                list = ['a', 'b', 'c']
                for index, value in enumerate(list):
                    print(index, value)
                # Output:
                # 0 a
                # 1 b
                # 2 c
                '''
        },
        "eval": {
            "significado": "Built-in Python function that evaluates a code string as a Python expression",
            "uso": "It is used to execute Python expressions contained in a string and return the result",
            "ejemplo": '''
                x = 2
                result = eval('x + 1')
                print(result)  # Output: 3
                '''
        },
        "exec": {
            "significado": "Built-in Python function that executes a code string as a complete code block",
            "uso": "It is used to execute Python code dynamically",
            "ejemplo": '''
                code = 'for i in range(3): print(i)'
                exec(code)
                # Output:
                # 0
                # 1
                # 2
                '''
        },
        "except": {
            "significado": "Python keyword used to handle exceptions within a try-except block",
            "uso": "It is used to catch and handle exceptions that occur in the try block",
            "ejemplo": '''
                try:
                    x = 1 / 0
                except ZeroDivisionError:
                    print('Error: divide by zero')
                # Output: Error: divide by zero
                '''
        },
        "else": {
            "significado": "Keyword in Python used in conditional control frameworks (if, try) to execute a block of code if the condition is not met or no exception occurs",
            "uso": "It is used to execute a block of code when the condition is not met or no exception occurs",
            "ejemplo": '''
                if 3 > 1:
                    print('Condition True')
                else:
                    print('Condition False')
                # Output: Condition True
                '''
        },
        "elif": {
            "significado": "Keyword in Python used in conditional structures to check for an additional condition if the previous ones are not met",
            "uso": "It is used to handle multiple conditions in an if-elif-else structure",
            "ejemplo": '''
                x = 3
                if x > 5:
                    print('Greater than 5')
                elif x == 3:
                    print('Same a 3')
                else:
                    print('Less than 3')
                # Output: Same a 3
                '''
        },
        "exit": {
            "significado": "Built-in Python function that terminates program execution",
            "uso": "It is used to exit a program or close an execution environment",
            "ejemplo": '''
                import sys
                sys.exit('Finishing the program')
                # The program ends with the message 'Ending the program'
                '''
        },
        "end": {
            "significado": "Keyword used in Python to specify the end of a block or the termination of a string",
            "uso": "It is mainly used in printing functions to control the output end",
            "ejemplo": '''
                print('Hello', end=' ')
                print('World')
                # Output: Hello World
                '''
        },
        "expandtabs": {
            "significado": "Strings method in Python that replaces tab characters with spaces",
            "uso": "It is used to align text by replacing tabs with a certain number of spaces",
            "ejemplo": '''
                text = 'Hello\tWorld'
                print(text.expandtabs(4))
                # Output: World   Hello
                '''
        },
        "encode": {
            "significado": "Strings method in Python that encodes a string into a byte sequence using a specific encoder",
            "uso": "It is used to convert a string into a sequence of bytes to be stored or transmitted in specific formats",
            "ejemplo": '''
                text = 'Hello World'
                encoded = text.encode('utf-8')
                print(encoded)
                # Output: b'Hello World'
                '''
        },
        "element": {
            "significado": "An individual item within a collection or data structure",
            "uso": "It is used to refer to an object within a list, set, dictionary, etc",
            "ejemplo": '''
                list = [1, 2, 3]
                print(list[0])  # Output: 1
                '''
        },
        "error": {
            "significado": "Anomalous condition in the execution of a program that interrupts its normal flow",
            "uso": "It is used to indicate that something has gone wrong during code execution",
            "ejemplo": '''
                try:
                    1 / 0
                except ZeroDivisionError as e:
                    print(f'Error: {e}')
                # Output: Error: divided by zero
                '''
        },
        "exception": {
            "significado": "Event that alters the normal flow of program execution, usually due to an error",
            "uso": "It is used to handle errors in code and perform specific actions when they occur",
            "ejemplo": '''
                try:
                    int('a')
                except ValueError:
                    print('Error: Cannot convert to integer')
                # Output: Error: Cannot convert to integer
                '''
        },
        "evaluate": {
            "significado": "Execute or calculate the value of an expression or function",
            "uso": "It is used to obtain the result of an expression",
            "ejemplo": '''
                x = 5
                result = eval('x + 2')
                print(result)  # Output: 7
                '''
        },
        "elements": {
            "significado": "Individual items or components within a set or collection",
            "uso": "It is used to refer to the parts of a data structure",
            "ejemplo": '''
                ensemble = {1, 2, 3}
                for element in ensemble:
                    print(element)
                # Output:
                # 1
                # 2
                # 3
                '''
        },
        "exponential": {
            "significado": "Related to the mathematical operation of exponentiation, which calculates the value of a base raised to an exponent",
            "uso": "It is used to perform exponential calculations",
            "ejemplo": '''
                import math
                result = math.exp(2)
                print(result)  # Output: 7.3890560989306495
                '''
        },
        "enumerations": {
            "significado": "A list or set of elements, often with an associated value or identifier",
            "uso": "It is used to represent a set of possible values of a variable",
            "ejemplo": '''
                from enum import Enum

                class Cor(Enum):
                    RED = 1
                    GREEN = 2
                    BLUE = 3

                print(Cor.RED)  # Output: Cor.RED
                '''
        },
        "encode_utf8": {
            "significado": "Encoding method that converts a string of characters into a sequence of bytes using the UTF-8 format",
            "uso": "It is used to convert text into a binary representation using UTF-8",
            "ejemplo": '''
                text = 'Hello World'
                encoded = text.encode('utf-8')
                print(encoded)  # Output: b'Hello World'
                '''
        },
        "execfile": {
            "significado": "Function that executes a Python file as if it were a script",
            "uso": "It is used to execute an external Python file",
            "ejemplo": '''
                # This command is only available in Python 2
                execfile('script.py')
                '''
        },
        "edit_distance": {
            "significado": "Measure that calculates the difference between two strings based on the operations required to convert one to the other",
            "uso": "It is used to compare how similar two strings are and to determine how many changes are needed to make them identical",
            "ejemplo": '''
                from nltk.metrics import edit_distance

                distance = edit_distance('kitten', 'sitting')
                print(distance)  # Output: 3
                '''
        },
        "eval_input": {
            "significado": "A function that evaluates user input, typically via the input() function",
            "uso": "It is used to obtain and evaluate a user-provided input",
            "ejemplo": '''
                entry = input('Enter a number: ')
                result = eval(entry)
                print(result)
                '''
        },
        "xceed": {
            "significado": "A term used to describe something that exceeds or exceeds a limit or expectation",
            "uso": "It is used to indicate that something has crossed a standard or threshold",
            "ejemplo": "The XCEED function is part of a set of functions that are used in data analysis or signal processing, but its name is not associated with a widely recognized standard function such as in common programming languages (such as Python, R, JavaScript, etc.). However, in some contexts, XCEED could refer to a custom function, some library, or even a function in some specific software"
        },
        "expected": {
            "significado": "Something anticipated or anticipated, based on expectations or forecasts",
            "uso": "It is used to describe what is expected to happen in a situation",
            "ejemplo": "The expected result was an increase in processing speed"
        },
        "encode_base64": {
            "significado": "Encoding method that converts binary data into a base-64 text representation",
            "uso": "It is used to encode binary data into a readable base-64 text string",
            "ejemplo": '''
                import base64
                encoded = base64.b64encode(b'Hello')
                print(encoded)  # Output: b'b2xh'
                '''
        },
        "execute": {
            "significado": "Perform or execute a set of instructions or a program",
            "uso": "It is used to put into practice an action or execute code",
            "ejemplo": '''
                def funtion():
                    print('Running...')
                funtion()  # Output: Running...
                '''
        },
        "exit_code": {
            "significado": "Value returned by a program or script when it is finished, indicating whether it was executed correctly or if an error occurred",
            "uso": "It is used to check if a program has completed successfully or if an error has occurred",
            "ejemplo": '''
                import sys
                sys.exit(0)  # Output: 0 indicates success, another number indicates error.
                '''
        },
        "evaluate_expression": {
            "significado": "Evaluate an expression to get its result",
            "uso": "It is used to calculate or obtain the value of a mathematical or logical expression",
            "ejemplo": '''
                result = eval('3 + 5')
                print(result)  # Output: 8
                '''
        },
        "environment": {
            "significado": "The context or set of conditions under which a program or application runs",
            "uso": "It is used to refer to the set of variables, settings, and features available to a program",
            "ejemplo": '''
                import os
                print(os.environ)  # Output: Shows system environment variables.
                '''
        },
        "environment_variable": {
            "significado": "Variable that stores information about the system or application environment",
            "uso": "It is used to store specific settings that affect the behavior of programs",
            "ejemplo": '''
                import os
                print(os.getenv('PATH'))  # Output: Shows the PATH environment variable.
                '''
        },
        "exp": {
            "significado": "A mathematical function that calculates the exponential of a number, that is, and raised to the power of that number",
            "uso": "It is used to perform exponential calculations",
            "ejemplo": '''
                import math
                result = math.exp(1)
                print(result)  # Output: 2.718281828459045
                '''
        },
        "exception_handling": {
            "significado": "Process of managing and responding to errors or exceptions that occur during the execution of a program",
            "uso": "It is used to catch and manage errors, ensuring that the program does not stop unexpectedly",
            "ejemplo": '''
                try:
                    value = 1 / 0
                except ZeroDivisionError as e:
                    print(f'Error: {e}')  # Output: Error: divided by zero
                '''
        },
        "expand": {
            "significado": "Enlarge or increase the size or reach of something",
            "uso": "It is used to do something bigger or include more information",
            "ejemplo": '''
                text = "Hello"
                print(text.expandtabs(4))  # Output: 'Hello' with enlarged tabs
                '''
        },
        "environment_config": {
            "significado": "Configuration related to the runtime of a program or system",
            "uso": "It is used to specify or adjust parameters that affect the operation of a program or application",
            "ejemplo": '''
                config = {
                    'host': 'localhost',
                    'port': 8080
                }
                print(config)  # Output: {'host': 'localhost', 'port': 8080}
                '''
        },
        "equal": {
            "significado": "Indicates that two elements are identical in value",
            "uso": "It is used to compare two values or expressions to see if they are the same",
            "ejemplo": '''
                a = 5
                b = 5
                print(a == b)  # Output: True
                '''
        },
        "error_handling": {
            "significado": "Process of managing errors and exceptions that occur during the execution of a program",
            "uso": "It is used to catch and manage errors in a controlled manner to prevent the program from terminating unexpectedly",
            "ejemplo": '''
                try:
                    value = 10 / 0
                except ZeroDivisionError:
                    print('Error de divide by zero')  # Output: Error divide by zero
                '''
        },
        "event": {
            "significado": "Action or event that can be detected and managed in a program",
            "uso": "It is used to manage and respond to activities or changes in a system or program",
            "ejemplo": '''
                import tkinter as tk
                def click():
                    print('Button pressed')
                root = tk.Tk()
                button = tk.Button(root, text="Click on me", command=click)
                button.pack()
                root.mainloop()  # Output: Shows a button that, when pressed, executes the click event
                '''
        },
        "event_loop": {
            "significado": "Continuous cycle that expects and manages asynchronous events or tasks in a program.",
            "uso": "It is used to execute tasks or respond to events in order, without blocking the main flow of execution.",
            "ejemplo": '''
                import asyncio
                async def hello():
                    print("Hello")
                asyncio.run(hello())  # Output: Hello
                '''
        },
        "exception_type": {
            "significado": "The specific type of an exception or error that occurs in a program",
            "uso": "It is used to identify what type of error has occurred and take appropriate action",
            "ejemplo": '''
                try:
                    value = 10 / 0
                except ZeroDivideError as e:
                    print(f"Error Type: {type(e)}")  # Output: Error Type: <class 'ZeroDivideError'>
                '''
        },
        "error_message": {
            "significado": "Message that describes the error or problem that occurred during the execution of a program",
            "uso": "It is used to provide details about what failed or caused an exception",
            "ejemplo": '''
                try:
                    x = int("abc")
                except ValueError as e:
                    print(f"Error message: {e}")  # Output: Error message: invalid literal for int() with base 10: 'abc'
                '''
        },
        "extract": {
            "significado": "Get a specific part of a dataset or insights",
            "uso": "It is used to extract or extract a specific component from a larger set of data",
            "ejemplo": '''
                text = 'Hello World'
                print(text[0:4])  # Output: Hello
                '''
        },
        "exit_status": {
            "significado": "Exit code that indicates whether a program or process has terminated correctly or in error",
            "uso": "It is used to check if a process or command has ended successfully or if an error has occurred",
            "ejemplo": '''
                import sys
                sys.exit(0)  # Output: 0 indicates success, any other number indicates error.
                '''
        },
        },
    "f": {
        "filemode": {
            "significado": "How to open a file that determines the operations that can be performed on it",
            "uso": "It is used to specify the type of access desired for a file (read, write, etc.).",
            "ejemplo": '''
                file = open('file.txt', 'r')  # 'r' indicates read-only mode
                print(file.mode)  # Output: 'r'
                '''
        },
        "frozen_set": {
            "significado": "Immutable set in Python, similar to a standard set, but without the possibility of modifying it after its creation",
            "uso": "It is used to create sets that should not be modified after they have been created",
            "ejemplo": '''
                ensemble = frozenset([1, 2, 3])
                print(ensemble)  # Output: frozenset({1, 2, 3})
                '''
        },
        "format_map": {
            "significado": "Method that returns a string formatted using a dictionary or similar object",
            "uso": "It is used to perform value substitutions in a string using a map (such as a dictionary)",
            "ejemplo": '''
                data = {'name': 'pepe', 'age': 30}
                text = 'Name: {name}, age: {age}'.format_map(data)
                print(text)  # Output: Name: pepe, age: 30
                '''
        },
        "find": {
            "significado": "A method that fetches a substring within a string and returns the index from the first occurrence",
            "uso": "It is used to find the position of one text within another",
            "ejemplo": '''
                text = 'Hello World'
                print(text.find('World'))  # Output: 5
                '''
        },
        "float32": {
            "significado": "Type of data in NumPy that represents a 32-bit floating-point number",
            "uso": "It is used to store numbers with decimals more efficiently in terms of memory",
            "ejemplo": '''
                import numpy as np
                number = np.float32(3.1415)
                print(number)  # Output: 3.1415
                '''
        },
        "float64": {
            "significado": "Type of data in NumPy that represents a 64-bit floating-point number",
            "uso": "It is used to store numbers with decimals with greater precision than the float32 type.",
            "ejemplo": '''
                import numpy as np
                number = np.float64(3.141592653589793)
                print(number)  # Output: 3.141592653589793
                '''
        },
        "formatting": {
            "significado": "The process of applying a format to date or strings, such as alignment, widths, and date types",
            "uso": "It is used to organize or display date in a more legible or specific way",
            "ejemplo": '''
                text = 'Name: {0:10}, age: {1:5}'.format('pepe', 30)
                print(text)  # Output: Name: pepe      , age: 30
                '''
        },
        "flush_output": {
            "significado": "Method used to empty the output buffer, forcing the data to be written immediately",
            "uso": "It is used when you want to ensure that all pending data in the output buffer is written to the destination",
            "ejemplo": '''
                import sys
                sys.stdout.write('Hello World')
                sys.stdout.flush()  # Output: 'Hello World' instanly
                '''
        },
        "function_definition": {
            "significado": "The process of creating a function in Python using the 'def' keyword",
            "uso": "It is used to declare reusable functions that execute a specific block of code",
            "ejemplo": '''
                def greet(name):
                    return f'Hello {name}'
                print(greet('pepe'))  # Output: Hello pepe
                '''
        },
        "filepath": {
            "significado": "Path or address of a file in the file system",
            "uso": "It is used to specify the location of a file in the file system",
            "ejemplo": '''
                import os
                path = os.path.join('folder', 'file.txt')
                print(path)  # Output: folder/file.txt
                '''
        },
        "flask": {
            "significado": "A Python micro-framework for web application development",
            "uso": "It is used to create web applications in a simple and fast way with routes, forms, and other features",
            "ejemplo": '''
                from flask import Flask
                app = Flask(__name__)

                @app.route('/')
                def hello():
                    return 'Hello World'

                app.run()  # Output: 'Hello World' in a web application
                '''
        },
        "filtering": {
            "significado": "Process of selecting elements from a collection that meet a specific condition",
            "uso": "It is used to extract elements from a list, ensemble, or any iterable based on a condition",
            "ejemplo": '''
                list = [1, 2, 3, 4, 5]
                result = filter(lambda x: x > 2, list)
                print(list(result))  # Output: [3, 4, 5]
                '''
        },
        "futures": {
            "significado": "Module that provides an interface to perform asynchronous and parallelized tasks",
            "uso": "It is used to execute functions concurrently using threads or processes",
            "ejemplo": '''
                from concurrent.futures import ThreadPoolExecutor

                def task(x):
                    return x * x

                with ThreadPoolExecutor() as executor:
                    results = executor.map(task, [1, 2, 3])
                    print(list(results))  # Output: [1, 4, 9]
                '''
        },
        "fold": {
            "significado": "Function that applies a cumulative operation on the elements of a sequence.",
            "uso": "It is used to reduce a sequence of elements to a single value by applying a binary operation",
            "ejemplo": '''
                from functools import reduce
                list = [1, 2, 3, 4]
                result = reduce(lambda x, y: x + y, list)
                print(result)  # Output: 10
                '''
        },
        "fromkeys": {
            "significado": "Dictionary method that creates a new dictionary with specified keys and default values",
            "uso": "It is used to create dictionaries from a list of keys with a default value",
            "ejemplo": '''
                dictionary = dict.fromkeys(['a', 'b', 'c'], 0)
                print(dictionary)  # Output: {'a': 0, 'b': 0, 'c': 0}
                '''
        },
        "flask_restful": {
            "significado": "Extension for Flask that simplifies the creation of RESTful APIs",
            "uso": "It is used to develop web applications that follow the REST architecture using",
            "ejemplo": '''
                from flask import Flask
                from flask_restful import Api, Resource

                app = Flask(__name__)
                api = Api(app)

                class HelloWorld(Resource):
                    def get(self):
                        return {'mensagge': 'Hello World'}

                api.add_resource(HelloWorld, '/')
                app.run()  # Output: 'Hello World' as API response
                '''
        },
        "fix": {
            "significado": "General term for correcting or adjusting something that doesn't work properly",
            "uso": "It is used when you make an adjustment or correction to the code or configuration of something",
            "ejemplo": '''
                # Example in the context of code: fix a syntax error
                def correct_error():
                    print('This is the corrected message')
                correct_error()
                '''
        },
        "float_conversion": {
            "significado": "Process of Converting Date from Other Types to Floating Type",
            "uso": "It is used to convert values to floating-point numbers (decimals)",
            "ejemplo": '''
                number = '3.14'
                result = float(number)
                print(result)  # Output: 3.14
                '''
        },
        "full_path": {
            "significado": "Full path to a file or directory in the file system",
            "uso": "It is used to specify the exact location of a file or directory from the root of the file system",
            "ejemplo": '''
                import os
                path_complet = os.path.abspath('file.txt')
                print(pah_complet)  # Output: /home/user/file.txt
                '''
        },
        "filter": {
            "significado": "Function that applies a condition to each element of an iterable and returns the elements that meet the condition",
            "uso": "It is used to select only those elements that meet a specific condition",
            "ejemplo": '''
                list = [1, 2, 3, 4, 5]
                result = filter(lambda x: x % 2 == 0, list)
                print(list(result))  # Output: [2, 4]
                '''
        },
        "float": {
            "significado": "Data type in Python to represent floating-point numbers (numbers with decimals)",
            "uso": "It is used to represent numbers that require decimals",
            "ejemplo": '''
                number = 3.14
                print(type(number))  # Output: <class 'float'>
                '''
        },
        "for": {
            "significado": "Python keyword used to iterate over the elements of an iterable",
            "uso": "It is used to execute a block of code repeatedly for each element of an iterable",
            "ejemplo": '''
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
            "significado": "Method used to format text strings by inserting values within them",
            "uso": "It is used to create more readable and dynamic text strings with variable values",
            "ejemplo": '''
                name = 'Juan'
                age = 30
                print('my name is {} and i am {} years old'.format(name, age))
                # Output: my name is Juan i am 30 years old
                '''
        },
        "from": {
            "significado": "Python keyword used to import modules or module-specific functions",
            "uso": "It is used to bring specific functionality from a module into the current namespace",
            "ejemplo": '''
                from math import sqrt
                print(sqrt(16))  # Output: 4.0
                '''
        },
        "function": {
            "significado": "Block of code designed to perform a specific task and that can be reused",
            "uso": "It is used to bundle related code that performs a common task, allowing for reusability and modularity",
            "ejemplo": '''
                def Greeting(name):
                    return f'Hello, {name}'
                
                print(Greeting('Juan'))  # Output: Hello, Juan
                '''
        },
        "fibonacci": {
            "significado": "Mathematical sequence where each number is the sum of the previous two",
            "uso": "It is used to generate the Fibonacci sequence, often in programming exercises or algorithms",
            "ejemplo": '''
                def fibonacci(n):
                    if n <= 1:
                        return n
                    else:
                        return fibonacci(n-1) + fibonacci(n-2)
                
                print(fibonacci(5))  # Output: 5
                '''
        },
        "file": {
            "significado": "Python object that allows you to interact with files in the file system",
            "uso": "It is used to open, read, write, and manipulate files",
            "ejemplo": '''
                with open('file.txt', 'r') as f:
                    Content = f.read()
                print(Content)
                '''
        },
        "fwrite": {
            "significado": "Function used to write date in a file",
            "uso": "It is used to write data binaries to an open file in write mode",
            "ejemplo": '''
                with open('file.bin', 'wb') as f:
                    f.write(b'Hello, World!')
                '''
        },
        "fread": {
            "significado": "Function Used to Read Date from a File",
            "uso": "It is used to read binary data from an open file in read mode",
            "ejemplo": '''
                with open('file.bin', 'rb') as f:
                    data = f.read()
                print(data)  # Output: b'Hello, World!'
                '''
        },
        "finally": {
            "significado": "Keyword in Python that defines a block of code that will run every time, regardless of whether an exception occurs or not",
            "uso": "It is used in try-except structures to ensure that a final block of code is executed, even if an error occurs",
            "ejemplo": '''
                try:
                    x = 1 / 0
                except ZeroDivisionError:
                    print('Divide by zero')
                finally:
                    print('This block always runs')
                '''
        },
        "freeze": {
            "significado": "Process of converting a mutable object to an immutable object",
            "uso": "It is used to prevent an object from being modified after it has been created",
            "ejemplo": '''
                # There is no explicit function called freeze, but in some cases such as with 'frozenset' you can achieve the same effect
                a = frozenset([1, 2, 3])
                print(a)  # Output: frozenset({1, 2, 3})
                '''
        },
        "flush": {
            "significado": "Method used to empty the buffers of a file, ensuring that all data are written to disk",
            "uso": "It is used when it is necessary to ensure that data stored in a buffer is immediately written to the file",
            "ejemplo": '''
                with open('file.txt', 'w') as f:
                    f.write('Hello')
                    f.flush()  # Ensures that the data are written to the file
                '''
        },
        "fstring": {
            "significado": "Text string that allows you to insert expressions within the string in a more readable and efficient way",
            "uso": "It is used to create interpolated text strings, where variables can be inserted directly into the string",
            "ejemplo": '''
                name = 'Juan'
                age = 30
                print(f'My name is {name} and i am {age} years old')
                # Output:My name is Juan and i am 30 years old
                '''
        },
        "factorial": {
            "significado": "A mathematical function that calculates the product of all positive integers up to a given number",
            "uso": "It is used to calculate the factorial of a number, often in combinatorics and probability algorithms",
            "ejemplo": '''
                import math
                print(math.factorial(5))  # Output: 120
                '''
        },
        "frozen": {
            "significado": "Immutable object that cannot be modified after its creation",
            "uso": "It is used to create objects that cannot be changed, such as a 'frozenset' in Python",
            "ejemplo": '''
                a = frozenset([1, 2, 3])
                print(a)  # Output: frozenset({1, 2, 3})
                '''
        },
        "filterfalse": {
            "significado": "Function that returns an iterator that filters the elements of an iterable, excluding those that return 'True' in the given function",
            "uso": "It is used to get the elements of an iterable for which the function returns 'False'",
            "ejemplo": '''
                from itertools import filterfalse
                result = filterfalse(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])
                print(list(result))  # Output: [1, 3, 5]
                '''
        },
        "fuzzy": {
            "significado": "Related to fuzzy logic, which allows you to deal with inaccurate or uncertain information",
            "uso": "It is used in systems that need to process approximate or uncertain dates",
            "ejemplo": '''
                # Example of a fuzzy logic library like 'fuzzywuzzy' (for fuzzy text matching)
                from fuzzywuzzy import fuzz
                print(fuzz.ratio('hello', 'Hello'))  # Output: 100
                '''
        },
        "fibonacci_sequence": {
            "significado": "Mathematical sequence where each number is the sum of the previous two.",
            "uso": "It is used to generate the Fibonacci sequence",
            "ejemplo": '''
                def fibonacci(n):
                    Sequence = [0, 1]
                    while len(Sequence) < n:
                        Sequence.append(Sequence[-1] + Sequence[-2])
                    return Sequence
                
                print(fibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
                '''
        },
        "format_spec": {
            "significado": "String used to define how values should be presented within a string format",
            "uso": "It is used to specify the format of values within a string, such as decimal precision, alignment, and more",
            "ejemplo": '''
                pi = 3.14159
                print(f'{pi:.2f}')  # Output: 3.14
                '''
        },
        "fork": {
            "significado": "Process of creating a new process, copied from the original process",
            "uso": "It is used in the programming of systems to create secondary processes",
            "ejemplo": '''
                import os
                pid = os.fork()
                if pid > 0:
                    print(f'Parent Process, PID: {pid}')
                else:
                    print(f'Child process, PID: {os.getpid()}')
                '''
        },
        "forking": {
            "significado": "Action of creating a new process or subprocess from a main process.",
            "uso": "It is used in operating systems to create additional processes that perform tasks concurrently",
            "ejemplo": '''
                import os
                pid = os.fork()
                # Similar to the example of 'fork', but encompassing the concept of 'forking''
                '''
        },
        "first": {
            "significado": "Getting the first element of a sequence or iterable",
            "uso": "It is used to access the first value of an iterable, such as a list or ensemble",
            "ejemplo": '''
                list = [1, 2, 3, 4]
                print(list[0])  # Output: 1
                '''
        },
        "float_format": {
            "significado": "Format that defines how floating-point numbers should be presented in a chain",
            "uso": "It is used to specify the number of decimal places to display in a floating-point number",
            "ejemplo": '''
                pi = 3.14159
                print(f'{pi:.2f}')  # Output: 3.14
                '''
        },
        "filter_none": {
            "significado": "Function that filters elements from an iterable by excluding None values.",
            "uso": "It is used to exclude 'None' values from a string.",
            "ejemplo": '''
                list = [1, None, 2, None, 3]
                result = filter(None, list)
                print(list(result))  # Output: [1, 2, 3]
                '''
        },
        "func_code": {
            "significado": "Attribute that contains the bytecode of the function in Python.",
            "uso": "It is used to access function code, usually in debugging or analysis contexts",
            "ejemplo": '''
                def ejemplo():
                    pass
                
                print(ejemplo.__code__)  # Output: <code object example at 0x...>
                '''
        },
        "float_power": {
            "significado": "Function that calculates a number raised to a floating power",
            "uso": "It is used to perform exponentiation with floating numbers",
            "ejemplo": '''
                print(pow(2, 3.5))  # Output: 11.313708498984761
                '''
        },
        "format_string": {
            "significado": "String that defines the structure of a value that you want to display, using format specifiers",
            "uso": "It is used to define how values should be displayed in a string, such as the number of decimal places or the alignment",
            "ejemplo": '''
                name = 'Juan'
                age = 25
                print(f'Name: {name}, age: {age}')  # Output: Name: Juan, age: 25
                '''
        },
        "filename": {
            "significado": "String representing the name of a file in the file system",
            "uso": "It is used to specify the name and location of a file that is to be manipulated",
            "ejemplo": '''
                file = 'document.txt'
                with open(file, 'r') as f:
                    print(f.read())
                '''
        },
        "file_object": {
            "significado": "object that represents a file opened in Python, through which it is possible to read, write, or manipulate the file",
            "uso": "It is used to interact with files opened in Python, accessing or modifying their contents",
            "ejemplo": '''
                with open('document.txt', 'r') as f:
                    Content = f.read()
                    print(Content)
                '''
        },
        "finally_clause": {
            "significado": "Part of a block of code that always executes after a 'try' statement, regardless of whether an exception is thrown or not.",
            "uso": "It is used to execute cleanup or finalization code, such as closing files or releasing resources.",
            "ejemplo": '''
                try:
                    file = open('document.txt', 'r')
                    Content = file.read()
                finally:
                    file.close()
                    print('File closed')
                '''
        },
        "file_read": {
            "significado": "Operation that allows you to read the contents of a file in Python.",
            "uso": "It is used to obtain the data stored in a file for processing or display.",
            "ejemplo": '''
                with open('document.txt', 'r') as file:
                    Content = file.read()
                    print(Content)
                '''
        },
        "form": {
            "significado": "Structure or template used to organize date in a specific way.",
            "uso": "It is used in user interfaces or web applications to capture and organize user data.",
            "ejemplo": '''
                form = {'name': 'Juan', 'age': 25}
                print(form)
                '''
        },
        "function_call": {
            "significado": "Invoke a function in code, passing the parameters needed to execute your task",
            "uso": "It is used to execute a function and obtain its result",
            "ejemplo": '''
                def sum(a, b):
                    return a + b
                result = sum(3, 4)
                print(result)  # Output: 7
                '''
        },
        "force": {
            "significado": "The action of imposing or forcing the execution of something, usually in the context of programming or manipulating objects",
            "uso": "It is used to force a specific behavior in a program, such as avoiding errors or performing an action regardless of the conditions",
            "ejemplo": '''
                # There is no direct force in Python, but you can use assert to force conditions
                assert 1 == 1, 'condition false'
                '''
        },
        "function_pointer": {
            "significado": "Reference to a function that can be passed and executed as an argument",
            "uso": "It is used in languages such as C or C++ to reference functions and pass them as parameters",
            "ejemplo": '''
                # In Python there is no direct function pointer, but functions can be passed as objects
                def Greeting():
                    print('Hello')
                function = Greeting
                function()  # Output: Hello
                '''
        },
        "float_precision": {
            "significado": "Number of digits used to accurately represent a floating number",
            "uso": "It is used to specify the number of decimal places to consider when performing operations with floating numbers",
            "ejemplo": '''
                number = 3.14159265359
                print(f'{number:.2f}')  # Output: 3.14
                '''
        },
        "format_error": {
            "significado": "Error that occurs when there is a problem formatting date, such as a poorly structured string",
            "uso": "It is used to handle errors related to incorrect date conversion or formatting",
            "ejemplo": '''
                try:
                    int('abc')
                except ValueError as e:
                    print(f'format error: {e}')
                '''
        },
        "file_write": {
            "significado": "Operation that allows you to write date to a file in Python.",
            "uso": "It is used to store information in a file, overwriting it or adding new data",
            "ejemplo": '''
                with open('document.txt', 'w') as file:
                    file.write('Hello, World!')
                '''
        },
        "fibonacci_search": {
            "significado": "Search method that uses Fibonacci numbers to divide the search space efficiently",
            "uso": "It is used as an alternative to the binary search algorithm to find an element in an array",
            "ejemplo": '''
                # Implementation of Fibonacci Search is not standard, but can be used as an alternative to binary search
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
            "significado": "Function that filters the elements of an iterable and then applies a mapping function to the remaining elements",
            "uso": "It is used to efficiently perform transformations and filtering on date sequences",
            "ejemplo": '''
                from itertools import filterfalse
                data = [1, 2, 3, 4, 5]
                result = map(lambda x: x * 2, filter(lambda x: x % 2 == 0, data))
                print(list(result))  # Output: [4, 8]
                '''
        },
        },
    "g": {
       "gather": {
    "example": "\n                import asyncio\n                async def task():\n                    return 1\n                async def main():\n                    results = await asyncio.gather(task(), task())\n                    print(results)\n                asyncio.run(main())\n                ",
    "meaning": "Function used to collect or group elements or results into a structure.",
    "usage": "It is used to gather results from parallel operations or multiple sources."
},
"gc": {
    "example": "\n                import gc\n                gc.collect()  # Force garbage collection\n                ",
    "meaning": "Garbage collection module that allows interaction with Python's garbage collector.",
    "usage": "It is used to manage memory and free unreferenced objects."
},
"gcd": {
    "example": "\n                import math\n                print(math.gcd(24, 36))  # Output: 12\n                ",
    "meaning": "Function that calculates the greatest common divisor (GCD) of two numbers.",
    "usage": "It is used to find the largest number that divides two numbers without leaving a remainder."
},
"gcd_algorithm": {
    "example": "\n                import math\n                gcd = math.gcd(24, 36)\n                print(gcd)  # Output: 12\n                ",
    "meaning": "Algorithm to calculate the greatest common divisor (GCD) of two numbers.",
    "usage": "It is used to find the largest number that divides two numbers exactly."
},
"generate_tokens": {
    "example": "\n                import token\n                import tokenize\n                code = 'print(\"Hello World\")'\n                tokens = tokenize.generate_tokens(iter(code).__next__)\n                for t in tokens:\n                    print(t)\n                ",
    "meaning": "Function that generates a sequence of tokens from a text object, used to analyze and process source code.",
    "usage": "It is used in creating lexical analyzers to split a text into meaningful units."
},
"generator": {
    "example": "\n                def count_to_three():\n                    yield 1\n                    yield 2\n                    yield 3\n                for num in count_to_three():\n                    print(num)  # Output: 1, 2, 3\n                ",
    "meaning": "Function that returns an iterator, allowing the generation of elements one by one during execution.",
    "usage": "It is used to create sequences of elements lazily (lazy evaluation), without having to store them all in memory."
},
"generator_expression": {
    "example": "\n                numbers = (x * 2 for x in range(5))\n                for num in numbers:\n                    print(num)  # Output: 0, 2, 4, 6, 8\n                ",
    "meaning": "Expression that allows generating a generator in a compact way, similar to a list comprehension.",
    "usage": "It is used to create generators efficiently without storing all elements."
},
"generator_function": {
    "example": "\n                def count():\n                    yield 1\n                    yield 2\n                    yield 3\n                for num in count():\n                    print(num)  # Output: 1, 2, 3\n                ",
    "meaning": "Function that uses `yield` to return a generator.",
    "usage": "It is used to create functions that return a generator and allow lazy iteration."
},
"generator_instance": {
    "example": "\n                def counter():\n                    yield 1\n                    yield 2\n                    yield 3\n                generator = counter()\n                for num in generator:\n                    print(num)  # Output: 1, 2, 3\n                ",
    "meaning": "Instance of a generator, which is an object that allows iteration over a sequence of elements.",
    "usage": "It is used to manage iterations efficiently using the `yield` keyword."
},
"genericpath": {
    "example": "\n                import genericpath\n                file = \"/path/to/file.txt\"\n                print(genericpath.exists(file))  # Output: True or False\n                ",
    "meaning": "Module that provides functions for working with file and directory paths in a generic way.",
    "usage": "It is used for manipulating file and directory paths."
},
"geocode": {
    "example": "\n                from geopy.geocoders import Nominatim\n                geolocator = Nominatim(user_agent=\"my_app\")\n                location = geolocator.geocode(\"1600 Pennsylvania Ave NW, Washington, DC 20500\")\n                print(location.latitude, location.longitude)\n                ",
    "meaning": "Process of converting an address into geographic coordinates (latitude and longitude).",
    "usage": "It is used to obtain the geographic location of a textual address."
},
"geolocation": {
    "example": "\n                # example using geopy\n                from geopy.geocoders import Nominatim\n                geolocator = Nominatim(user_agent=\"my_app\")\n                location = geolocator.geocode(\"1600 Pennsylvania Ave NW, Washington, DC 20500\")\n                print(location.address)\n                ",
    "meaning": "Process of determining the geographic location of a device.",
    "usage": "It is used to obtain the latitude, longitude, and other details about a device's location."
},
"geometry": {
    "example": "\n                # example of geometry in programming\n                import math\n                circle_area = math.pi * (5**2)  # Area of a circle with radius 5\n                print(circle_area)  # Output: 78.53981633974483\n                ",
    "meaning": "Area of mathematics that deals with the properties and relations of points, lines, surfaces, and solids.",
    "usage": "It is used in fields such as computer graphics, engineering, and architecture to describe shapes and structures."
},
"geometry_manager": {
    "example": "\n                import tkinter as tk\n                root = tk.Tk()\n                label = tk.Label(root, text=\"Hello World\")\n                label.pack()  # Uses the 'pack' geometry manager\n                root.mainloop()\n                ",
    "meaning": "Method used to manage the size and location of widgets in graphical user interfaces.",
    "usage": "It is used in GUI libraries like Tkinter to organize the layout of elements."
},
"geopandas": {
    "example": "\n                import geopandas as gpd\n                gdf = gpd.read_file('map.shp')\n                gdf.plot()\n                ",
    "meaning": "Python library for the manipulation and analysis of geospatial data.",
    "usage": "It is used for working with spatial data such as maps and geographic coordinates."
},
"get": {
    "example": "\n                dictionary = {'a': 1, 'b': 2}\n                print(dictionary.get('a'))  # Output: 1\n                print(dictionary.get('c', 'Not found'))  # Output: Not found\n                ",
    "meaning": "Method that retrieves the value of a key in a dictionary. If the key does not exist, it returns a default value.",
    "usage": "It is used to safely get the value associated with a key in a dictionary."
},
"get_active_connections": {
    "example": "\n                import psutil\n                connections = psutil.net_connections()\n                for connection in connections:\n                    print(connection)\n                ",
    "meaning": "Method that retrieves active connections in a system or network.",
    "usage": "It is used to get the active connections in an application or operating system."
},
"get_cached_properties": {
    "example": "\n                class MyClass:\n                    @property\n                    def property(self):\n                        if not hasattr(self, '_cached_property'):\n                            self._cached_property = 42  # Example calculation\n                        return self._cached_property\n                obj = MyClass()\n                print(obj.property)  # Output: 42\n                ",
    "meaning": "Method to retrieve properties that have been stored in cache.",
    "usage": "It is used to access properties that were previously calculated and stored in memory for efficiency."
}

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

