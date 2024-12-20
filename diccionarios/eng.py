#vicho
diccionario_eng = {
    "a": {
        "abs": {
            "ejemplo": "abs(-5)  # 5",
            "significado": "Returns the absolute value of a number",
            "uso": "It is used to obtain the absolute value of a number"
        },
        "absolute_import": {
            "ejemplo": "\n                from __future__ import absolute_import\n\n                # The global module always matters, not a local one with the same name\n                import math\n                ",
            "significado": "Policy used to enable absolute imports in Python 2.x and later versions",
            "uso": "It is used to avoid conflicts between local and global modules"
        },
        "add": {
            "ejemplo": "\n                # Sets\n                ensemble = {1, 2, 3}\n                ensemble.add(4)\n                print(ensemble)  # Output: {1, 2, 3, 4}\n\n                # NumPy\n                import numpy as np\n                result = np.add(2, 3)\n                print(result)  # Output: 5 ",
            "significado": "Method used to add an element to a set or perform a sum between arrays (depending on the context)",
            "uso": "It is used in sets to add elements or in NumPy to perform mathematical operations"
        },
        "all": {
            "ejemplo": "values = [1, 2, 3]\n            print(all(values))  # True",
            "significado": "Return True if all elements are true iterable",
            "uso": "Verifi is all contitions are true iterable"
        },
        "allclose": {
            "ejemplo": "\n                import numpy as np\n\n                a = [1.0, 2.001]\n                b = [1.0, 2.0009]\n                print(np.allclose(a, b, atol=0.01))  # Output: True ",
            "significado": "Verifies that all elements of two arrays are approximately equal",
            "uso": "It is used in NumPy to check the equality of elements with tolerance for small differences"
        },
        "allexcept": {
            "ejemplo": "\n                list = [1, 2, 3, 4]\n                result = [x for x in list if x != 2]  # Filters out all but 2\n                print(result)  # Output: [1, 3, 4]\n                ",
            "significado": "It is not a native Python term. It can refer to a logical approach that applies operations to all elements except for a few specific ones",
            "uso": "Usually implemented manually"
        },
        "any": {
            "ejemplo": "values = [0, False, 2]\n            print(any(values))  # True",
            "significado": ": Returns True if at least one of the elements in an iterable is true",
            "uso": "Verify if a condition is a true iterable"
        },
        "append": {
            "ejemplo": "\n                list = [1, 2, 3]\n                list.append(4)\n                print(list)  # Output: [1, 2, 3, 4]\n            ",
            "significado": "Adds an element to the end of a list",
            "uso": "It is used to add new elements to an existing list"
        },
        "apply": {
            "ejemplo": "\n                import pandas as pd\n\n                dice = pd.DataFrame({'A': [1, 2, 3]})\n                dice['B'] = dice['A'].apply(lambda x: x * 2)\n                print(dice)\n                # Output:\n                #    A  B\n                # 0  1  2\n                # 1  2  4\n                # 2  3  6\n                ",
            "significado": "Method used to apply a function to rows or columns of a DataFrame",
            "uso": "It is used to perform custom operations on rows or columns"
        },
        "arange": {
            "ejemplo": "\n                import numpy as np\n\n                result = np.arange(0, 10, 2)\n                print(result)  # Output: [0 2 4 6 8]\n                ",
            "significado": "Generates an array with equally spaced values within a range",
            "uso": "It is used in NumPy to create number sequences"
        },
        "arccos": {
            "ejemplo": "\n                import numpy as np\n\n                result = np.arccos(0.5)\n                print(result)  # Output: 1.0471975511965976 (equivalent a π/3)\n                ",
            "significado": "Returns the cosine arc (in radians) of a value",
            "uso": "It is used in trigonometric calculations with NumPy"
        },
        "arcsin": {
            "ejemplo": "\n                import numpy as np\n\n                result = np.arcsin(0.5)\n                print(result)  # Output: 0.5235987755982988 (equivalent a π/6)\n                ",
            "significado": "Returns the arc sine (in radians) of a value",
            "uso": "It is used in trigonometric calculations with NumPy"
        },
        "arctan": {
            "ejemplo": "\n                import numpy as np\n\n                result = np.arctan(1)\n                print(result)  # Output: 0.7853981633974483 (equivalent a π/4)\n                ",
            "significado": "Returns the tangent arc (in radians) of a value",
            "uso": "It is used in trigonometric calculations with NumPy"
        },
        "argmax": {
            "ejemplo": "\n                import numpy as np\n\n                numbers = [1, 5, 2, 9, 3]\n                print(np.argmax(numbers))  # Output: 3 (Value 9 Index)\n            ",
            "significado": "Returns the index of the maximum value in an array or iterable",
            "uso": "It is used in libraries such as NumPy to find the index of the highest value in data structures"
        },
        "argmin": {
            "ejemplo": "\n                import numpy as np\n\n                numbers = [1, 5, 2, 9, 3]\n                print(np.argmin(numbers))  # Output: 0 (Value 1 Index)\n            ",
            "significado": "Returns the index of the minimum value in an array or iterable",
            "uso": "It is used in libraries such as NumPy to find the index of the lowest value in data structures"
        },
        "argparse": {
            "ejemplo": "\n                import argparse\n\n                parser = argparse.ArgumentParser(description='ejemplo of argparse')\n                parser.add_argument('--name', type=str, help='your name')\n                args = parser.parse_args()\n                print(f'Hello, {args.name}')\n                ",
            "significado": "Python module used to manage arguments and command-line options",
            "uso": "It is used to create easy-to-use command-line interfaces"
        },
        "args": {
            "ejemplo": "\n                def numbers_sum(*args):\n                    return sum(args)\n\n                print(numbers_sum(1, 2, 3))  # Output: 6\n                ",
            "significado": "It is a parameter that allows it to receive a variable number of positional arguments in a function",
            "uso": "It is used to handle multiple arguments in a function without specifying each one individually"
        },
        "array": {
            "ejemplo": "\n                import numpy as np\n\n                numbers = np.array([1, 2, 3, 4])\n                print(numbers)  # Output: [1 2 3 4]\n            ",
            "significado": "It is a data structure that contains multiple elements of the same type, commonly used in libraries such as NumPy",
            "uso": "It is used to efficiently store and operate large amounts of homogeneous data"
        },
        "array_like": {
            "ejemplo": "\n                import numpy as np\n\n                list = [1, 2, 3]\n                array = np.array(list)  # list and array_like\n                print(array)  # Output: [1 2 3]\n                ",
            "significado": "Refers to any object that can be treated as an array, such as lists, tuples, or NumPy arrays",
            "uso": "It is used as input in NumPy or similar functions for operations with data"
        },
        "as": {
            "ejemplo": "\n                import numpy as np\n\n                with open('file.txt', 'r') as file:\n                    content = file.read()\n                ",
            "significado": "Keyword used to assign an alias to modules or in 'with' statements",
            "uso": "Makes it easy to reference long or specific names in code"
        },
        "as_tuple": {
            "ejemplo": "\n                from sympy import Point\n\n                p = Point(2, 3)\n                print(p.as_tuple())  # Output: (2, 3)\n                ",
            "significado": "Method that converts an object to a tuple (common in libraries such as SymPy)",
            "uso": "It is used to transform objects into tuple representations"
        },
        "ascii": {
            "ejemplo": "\n                text = \"Hi, how are you?\"\n                print(ascii(text))  # Output: 'Hi\\xe1, how are\\xea you\\xe1?'\n            ",
            "significado": "Returns a human-readable representation of an object using ASCII characters",
            "uso": "It is used to represent strings or characters in an ASCII-safe format by replacing non-ASCII characters with escape sequences"
        },
        "assert": {
            "ejemplo": "\n                x = 5\n                assert x > 0, 'x must be greater than 0'  # Does not generate error\n                assert x < 0, 'x must be less than 0'  # Generates AssertionError\n                ",
            "significado": "Evaluates an expression and throws an exception 'AssertionError' if the expression is false",
            "uso": "It is used to check conditions that must be met during program execution"
        },
        "assertAlmostEqual": {
            "ejemplo": "\n                import unittest\n\n                class Test(unittest.TestCase):\n                    def test_aprox(self):\n                        self.assertAlmostEqual(3.14159, 3.14, places=2)  # The test passes\n                ",
            "significado": "Checks whether two values are approximately equal to a specific number of decimal places in a unit test",
            "uso": "It is used in unit tests to validate values with tolerance to small differences"
        },
        "assertEqual": {
            "ejemplo": "\n                import unittest\n\n                class Test(unittest.TestCase):\n                    def test_sum(self):\n                        self.assertEqual(1 + 1, 2)  # The test passes\n                ",
            "significado": "Checks if two values are equal in a unit test",
            "uso": "It is used in unit tests to validate the equality of expected and actual values"
        },
        "assertIsNone": {
            "ejemplo": "\n                import unittest\n\n                class Test(unittest.TestCase):\n                    def test_value_none(self):\n                        self.assertIsNone(None)  # The test passes\n                ",
            "significado": "Checks if a value is None in a unit test",
            "uso": "It is used in unit tests to validate that a value is None"
        },
        "async": {
            "ejemplo": "\n                import asyncio\n\n                async def Greeting():\n                    print('Hello')\n                    await asyncio.sleep(1)\n                    print('Bye')\n\n                asyncio.run(Greeting())\n                ",
            "significado": "Defines an asynchronous function that can be used with 'await'",
            "uso": "It is used to implement asynchronous programming in Python"
        },
        "at": {
            "ejemplo": "\n                import pandas as pd\n\n                dices = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})\n                print(dices.at[0, 'A'])  # Output: 1\n                ",
            "significado": "Method used to access specific elements in structures such as DataFrames or arrays (usually in pandas)",
            "uso": "It is used to quickly access an individual value in a specific position"
        },
        "atleast_1d": {
            "ejemplo": "\n                import numpy as np\n\n                result = np.atleast_1d(5)\n                print(result)  # Output: [5]\n                ",
            "significado": "Converts inputs to arrays with at least one dimension",
            "uso": "It is used in NumPy to ensure that data has a minimum dimension"
        },
        "atleast_2d": {
            "ejemplo": "\n                import numpy as np\n\n                result = np.atleast_2d([1, 2, 3])\n                print(result)\n                # Output:\n                # [[1 2 3]]\n                ",
            "significado": "Converts inputs to arrays with at least two dimensions",
            "uso": "It is used in NumPy to work with data in array format"
        },
        "attribute": {
            "ejemplo": "\n                class Person:\n                    def __init__(self, name, age):\n                        self.name = name\n                        self.age = age\n\n                p = Person('pepe', 30)\n                print(p.name)  # Output: pepe\n                p.age = 31\n                print(p.age)  # Output: 31\n                ",
            "significado": "Refers to a property or characteristic associated with an object in Python",
            "uso": "It is used to access or modify properties of objects created from classes"
        },
        "attributeError": {
            "ejemplo": "\n                try:\n                    objet = 5\n                    objet.atribute = 10\n                except AttributeError as e:\n                    print('Error:', e)\n                # Output: Error: 'int' object has no attribute 'atribute'\n                ",
            "significado": "It is an exception that occurs when you try to access or assign an attribute that does not exist",
            "uso": "It is used to catch and handle errors related to invalid attributes"
        },
        "average": {
            "ejemplo": "\n                import numpy as np\n\n                values = [1, 2, 3, 4]\n                print(np.average(values))  # Output: 2.5\n                ",
            "significado": "Averages the elements of an array or list",
            "uso": "It is used in NumPy to calculate averages, with the possibility of weighting values"
        },
        "await": {
            "ejemplo": "\n                import asyncio\n\n                async def task():\n                    await asyncio.sleep(1)\n                    return 'Task ready'\n\n                async def main():\n                    result = await task()\n                    print(result)\n\n                asyncio.run(main())\n                ",
            "significado": "It is used to wait for the result of an asynchronous function.",
            "uso": "It is used within functions defined with 'async' to pause their execution until an asynchronous task is completed"
        }
    },
    "b": {
        "base64": {
            "ejemplo": "\n                import base64\n\n                encoded = base64.b64encode(b'abc')\n                print(encoded)  # Output: b'YWJj'\n                ",
            "significado": "Module that provides functions for encoding and decoding base64 data",
            "uso": "It is used to represent binary data in a string of ASCII characters"
        },
        "bin": {
            "ejemplo": "\n                number = 10\n                print(bin(number))  # Output: '0b1010'\n                ",
            "significado": "Converts a number in its binary representation as a string",
            "uso": "It is used to obtain the binary representation of an integer"
        },
        "binascii": {
            "ejemplo": "\n                import binascii\n\n                encoded = binascii.hexlify(b'abc')\n                print(encoded)  # Output: b'616263'\n                ",
            "significado": "Module that contains functions to convert between binary and different text representations",
            "uso": "It is used to perform conversions between text strings and binary data"
        },
        "binhex": {
            "ejemplo": "\n                import binhex\n\n                with open('file.bin', 'rb') as f:\n                    binhex.binhex(f, 'file.hex')\n                ",
            "significado": "Function to convert a binary file into hexadecimal format",
            "uso": "It is used to represent binary data in hexadecimal readable format"
        },
        "binomial": {
            "ejemplo": "\n                from scipy.special import comb\n\n                result = comb(5, 2)\n                print(result)  # Output: 10.0\n                ",
            "significado": "Function that calculates the binomial coefficient (n over k)",
            "uso": "It is used to calculate the number of ways to select k elements from a set of n elements"
        },
        "bit_length": {
            "ejemplo": "\n                number = 10\n                print(number.bit_length())  # Output: 4\n                ",
            "significado": "Returns the number of bits required to represent a binary number",
            "uso": "It is used to obtain the length in bits of an integer"
        },
        "bitarray": {
            "ejemplo": "\n                from bitarray import bitarray\n\n                a = bitarray('10101')\n                a.append('1')\n                print(a)  # Output: bitarray('101011')\n                ",
            "significado": "Module that implements an efficient data type for working with bit arrays",
            "uso": "It is used to efficiently manipulate and manage bit arrays"
        },
        "bitset": {
            "ejemplo": "\n                # ejemplo is not standard in Python, but one can use the 'bitarray' module to create bitsets\n                from bitarray import bitarray\n\n                bitset = bitarray('10101')\n                print(bitset)  # Output: bitarray('10101')\n                ",
            "significado": "Data structure that allows you to store a collection of bits",
            "uso": "It is used to represent sets of bits and perform efficient operations on them"
        },
        "bitwise_and": {
            "ejemplo": "\n                x = 5  # binary: 0101\n                y = 3  # binary: 0011\n                print(x & y)  # Output: 1 (binary: 0001)\n                ",
            "significado": "Operator that performs a bitwise AND operation between two numbers",
            "uso": "It is used to compare the corresponding bits of two numbers and return 1 only if both bits are 1"
        },
        "bitwise_left_shift": {
            "ejemplo": "\n                x = 5  # binary: 0101\n                print(x << 1)  # Output: 10 (binary: 1010)\n                ",
            "significado": "Operator that performs a bit shift to the left",
            "uso": "It is used to shift the bits of a number to the left by multiplying the value by powers of two"
        },
        "bitwise_not": {
            "ejemplo": "\n            x = 5  # binary: 0101\n            print(~x)  # Output: -6 (binary: 1010)\n            ",
            "significado": "Operator that performs a bitwise NOT operation on a number",
            "uso": "It is used to invert all the bits of a number"
        },
        "bitwise_or": {
            "ejemplo": "\n                x = 5  # binary: 0101\n                y = 3  # binary: 0011\n                print(x | y)  # Output: 7 (binary: 0111)\n                ",
            "significado": "Operator performing a bitwise OR operation between two numbers",
            "uso": "It is used to compare the corresponding bits of two numbers and return 1 if at least one of the bits is 1"
        },
        "bitwise_right_shift": {
            "ejemplo": "\n                x = 5  # binary: 0101\n                print(x >> 1)  # Output: 2 (binary: 0010)\n                ",
            "significado": "Operator that performs a bit shift to the right",
            "uso": "It is used to shift the bits of a number to the right, dividing the value by powers of two"
        },
        "bitwise_xor": {
            "ejemplo": "\n                x = 5  # binary: 0101\n                y = 3  # binary: 0011\n                print(x ^ y)  # Output: 6 (binary: 0110)\n                ",
            "significado": "Operator that performs a bitwise XOR operation between two numbers",
            "uso": "It is used to compare the matching bits of two numbers and return 1 if the bits are different"
        },
        "bool": {
            "ejemplo": "\n                value = bool(1)\n                print(value)  # Output: True\n                ",
            "significado": "Type of data representing Boolean values: True or False",
            "uso": "It is used to represent and operate with truth values"
        },
        "bool_": {
            "ejemplo": "\n                import numpy as np\n\n                value = np.bool_(True)\n                print(value)  # Output: True\n                ",
            "significado": "NumPy data type for boolean values, similar to Python's 'bool'",
            "uso": "It is used in operations with NumPy arrays to represent Boolean values"
        },
        "break": {
            "ejemplo": "while True:\n            number = int(input(\"enter a number (enter a 0 for Output): \"))\n            if number == 0:\n            break  # Output from the bucle if the user write 0\n            print(f\"the number entered is {number}\")",
            "significado": "End a loop early",
            "uso": "to manually Output a loop"
        },
        "breakpoint": {
            "ejemplo": "\n                def funtion():\n                    breakpoint()  # Interruption here\n                    print('Hi')\n                funtion()\n                ",
            "significado": "A function that establishes a breakpoint in the code by activating the debugger",
            "uso": "It is used to pause execution and enter the interactive debugger"
        },
        "broadcast": {
            "ejemplo": "\n                import numpy as np\n\n                a = np.array([1, 2, 3])\n                b = np.array([[1], [2], [3]])\n                result = a + b\n                print(result)\n                # Output:\n                # [[2 3 4]\n                #  [3 4 5]\n                #  [4 5 6]]\n                ",
            "significado": "Technique that allows arrays of different shapes to be aligned to perform element-wise operations",
            "uso": "It is mainly used in NumPy for operations with arrays of different sizes"
        },
        "buffer": {
            "ejemplo": "\n                buffer = memoryview(b'abc')\n                print(buffer[0])  # Output: 97 (equivalent 'a')\n                ",
            "significado": "A class in Python that provides a view of accessing an object's memory area",
            "uso": "It is used to access memory efficiently, especially in operations with large amounts of data"
        },
        "bytearray": {
            "ejemplo": "\n                b = bytearray([65, 66, 67])\n                b[0] = 90\n                print(b)  # Output: bytearray(b'ZBC')\n                ",
            "significado": "Mutable data type that represents a sequence of bytes",
            "uso": "It is used to modify byte sequences"
        },
        "byteorder": {
            "ejemplo": "\n                import sys\n\n                print(sys.byteorder)  # Output: 'little' or 'big'\n                ",
            "significado": "Indicates the order of bytes to represent numbers in memory",
            "uso": "It is used to manipulate the representation of numbers in systems with different architectures"
        },
        "bytes": {
            "ejemplo": "b = bytes([65, 66, 67])\n            print(b)  # Result: b'ABC",
            "significado": "Returns an immutable byte sequence object",
            "uso": "Working with Immutable Binary Data"
        },
        "byteswap": {
            "ejemplo": "\n                import numpy as np\n\n                a = np.array([1, 256], dtype=np.int16)\n                a = a.byteswap()\n                print(a)  # Output: [256 1]\n                ",
            "significado": "Method that swaps the order of bytes in an object",
            "uso": "It is used to change the order of bytes in a numeric data type"
        },
        "bz2": {
            "ejemplo": "\n                import bz2\n\n                with bz2.open('file.bz2', 'rb') as file:\n                    content = file.read()\n                    print(content)\n                ",
            "significado": "Module that provides compression and decompression using the bzip2 algorithm",
            "uso": "It is used to manipulate compressed files in the bzip2 format"
        }
    },
    "c": {
        "cProfile": {
            "ejemplo": "\n            import cProfile\n\n            def function():\n                for i in range(1000):\n                    pass\n\n            cProfile.run('function()')\n            ",
            "significado": "Module for performance profiling of Python programs.",
            "uso": "Used to profile code and analyze the efficiency of the program."
        },
        "call": {
            "ejemplo": "\n            def greeting():\n                return 'Hello'\n            \n            print(callable(greeting))  # Output: True\n            ",
            "significado": "Method used to invoke a callable object, like functions or classes.",
            "uso": "Used to call an object that can be executed."
        },
        "callable": {
            "ejemplo": "\n            def function():\n                return \"Hello\"\n            \n            print(callable(function))  # Output: True\n            print(callable(42))  # Output: False\n            ",
            "significado": "Checks if an object is callable (like a function or a class).",
            "uso": "Used to determine if an object can be called."
        },
        "capitalize": {
            "ejemplo": "\n            text = 'hello world'\n            print(text.capitalize())  # Output: 'Hello world'\n            ",
            "significado": "String method that capitalizes the first letter and makes the rest lowercase.",
            "uso": "Used to capitalize the first letter of a string."
        },
        "ceil": {
            "ejemplo": "\n            import math\n\n            number = 3.4\n            print(math.ceil(number))  # Output: 4\n            ",
            "significado": "Function in the `math` module that returns the smallest integer greater than or equal to a given number.",
            "uso": "Used to round a number up."
        },
        "center": {
            "ejemplo": "\n            text = 'hello'\n            print(text.center(10, '*'))  # Output: '**hello****'\n            ",
            "significado": "String method that centers a string within a specified length field.",
            "uso": "Used to align text in the center of a string with padding."
        },
        "chain": {
            "ejemplo": "\n            import itertools\n\n            a = [1, 2, 3]\n            b = [4, 5, 6]\n            result = list(itertools.chain(a, b))\n            print(result)  # Output: [1, 2, 3, 4, 5, 6]\n            ",
            "significado": "Function that combines multiple iterators into one.",
            "uso": "Used to concatenate multiple iterators."
        },
        "choice": {
            "ejemplo": "\n            import random\n\n            list1 = [1, 2, 3, 4, 5]\n            print(random.choice(list1))  # Output: a random value from the list\n            ",
            "significado": "Function in the `random` module that selects a random element from a sequence.",
            "uso": "Used to select a random value from a list or sequence."
        },
        "chr": {
            "ejemplo": "\n            print(chr(65))  # Output: 'A'\n            print(chr(8364))  # Output: '€'\n            ",
            "significado": "Returns the Unicode character corresponding to an integer number.",
            "uso": "Used to convert a Unicode code point into its character representation."
        },
        "clamp": {
            "ejemplo": "\n            def clamp(value, minimum, maximum):\n                return max(minimum, min(value, maximum))\n\n            print(clamp(5, 1, 10))  # Output: 5\n            ",
            "significado": "Function that restricts a value within a specified range.",
            "uso": "Used to ensure a value stays within a given range."
        },
        "class": {
            "ejemplo": "\n            class Person:\n                def __init__(self, name):\n                    self.name = name\n                \n                def greet(self):\n                    print(f\"Hello, my name is {self.name}\")\n            \n            p = Person(\"Juan\")\n            p.greet()  # Output: Hello, my name is Juan\n            ",
            "significado": "Keyword used to define a class in Python.",
            "uso": "Used to create custom objects with attributes and methods."
        },
        "classmethod": {
            "ejemplo": "\n            class MyClass:\n                counter = 0\n\n                @classmethod\n                def increment(cls):\n                    cls.counter += 1\n            \n            MyClass.increment()\n            print(MyClass.counter)  # Output: 1\n            ",
            "significado": "Defines a class method that takes the class as the first argument instead of an instance.",
            "uso": "Used to create methods that affect the class in general."
        },
        "clear": {
            "ejemplo": "\n            list1 = [1, 2, 3]\n            list1.clear()\n            print(list1)  # Output: []\n            ",
            "significado": "Removes all elements from a list or dictionary.",
            "uso": "Used to clear the contents of a list or dictionary."
        },
        "cmath": {
            "ejemplo": "\n            import cmath\n\n            number = cmath.sqrt(-1)\n            print(number)  # Output: 1j\n            ",
            "significado": "Module that provides mathematical functions for working with complex numbers.",
            "uso": "Used to perform mathematical operations on complex numbers."
        },
        "collections": {
            "ejemplo": "\n            from collections import deque\n\n            queue = deque([1, 2, 3])\n            queue.append(4)\n            print(queue)  # Output: deque([1, 2, 3, 4])\n            ",
            "significado": "Module that implements specialized data types like `Counter`, `deque`, `OrderedDict`, among others.",
            "uso": "Used to work with collections of data efficiently."
        },
        "compile": {
            "ejemplo": "\n            code = \"print('Hello World')\"\n            compiled = compile(code, '<string>', 'exec')\n            exec(compiled)  # Output: Hello World\n            ",
            "significado": "Compiles a string of code into an executable Python object.",
            "uso": "Used to compile dynamic code from text or files."
        },
        "complex": {
            "ejemplo": "\n            c = complex(2, 3)\n            print(c)  # Output: (2+3j)\n            print(c.real, c.imag)  # Output: 2.0 3.0\n            ",
            "significado": "Creates a complex number in Python.",
            "uso": "Used to represent complex numbers with real and imaginary parts."
        },
        "continue": {
            "ejemplo": "\n            for i in range(5):\n                if i == 2:\n                    continue\n                print(i)  # Output: 0 1 3 4\n            ",
            "significado": "Keyword that skips to the next iteration of a loop.",
            "uso": "Used to skip the rest of the code in the current iteration."
        },
        "copy": {
            "ejemplo": "\n            import copy\n\n            list1 = [1, 2, [3, 4]]\n            copy1 = copy.copy(list1)\n            print(copy1)  # Output: [1, 2, [3, 4]]\n            ",
            "significado": "Creates a shallow copy of an object.",
            "uso": "Used to duplicate data structures without duplicating nested objects."
        },
        "copyreg": {
            "ejemplo": "\n            import copyreg\n\n            def create_person(name, age):\n                return {'name': name, 'age': age}\n\n            copyreg.pickle(dict, create_person)\n            ",
            "significado": "Module that provides functions for registering objects for copying and unpickling.",
            "uso": "Used to customize the behavior of object copying and storing."
        },
        "coroutine": {
            "ejemplo": "\n            async def task():\n                print(\"Start\")\n                await asyncio.sleep(1)\n                print(\"End\")\n            \n            import asyncio\n            asyncio.run(task())  # Output: Start... End\n            ",
            "significado": "Object representing a suspended asynchronous function.",
            "uso": "Used to manage asynchronous tasks with `async` and `await`."
        },
        "count": {
            "ejemplo": "\n            list1 = [1, 2, 2, 3]\n            print(list1.count(2))  # Output: 2\n            ",
            "significado": "Returns the number of occurrences of an element in a collection.",
            "uso": "Used to count the number of times an element appears in a list or string."
        },
        "counter": {
            "ejemplo": "\n            from collections import Counter\n\n            counter = Counter([1, 2, 2, 3, 3, 3])\n            print(counter)  # Output: Counter({3: 3, 2: 2, 1: 1})\n            ",
            "significado": "Class in the `collections` module that counts hashable elements in a sequence.",
            "uso": "Used to count the frequency of elements in an iterable."
        },
        "csv": {
            "ejemplo": "\n            import csv\n\n            with open('file.csv', mode='w', newline='') as file:\n                writer = csv.writer(file)\n                writer.writerow(['Name', 'Age'])\n                writer.writerow(['Ana', 30])\n            ",
            "significado": "Module to read and write CSV (Comma Separated Values) files.",
            "uso": "Used to handle CSV files."
        }
    },
    "d": {
        "dataframe": {
            "ejemplo": "\n                import pandas as pd\n\n                data = {'Name': ['pepe', 'age'], 'age': [28, 22]}\n                df = pd.DataFrame(data)\n                print(df)\n                ",
            "significado": "Two-dimensional data structure in the Pandas library, similar to a table, which allows you to store data of different types",
            "uso": "It is used to manipulate large volumes of tabular data in Python"
        },
        "datetime": {
            "ejemplo": "\n                import datetime\n\n                now = datetime.datetime.now()\n                print(now)  # Output: 2024-11-22 12:00:00.123456\n                ",
            "significado": "Python module that provides classes for working with dates and times",
            "uso": "It is used to manipulate and work with dates, times and times in general"
        },
        "decimal": {
            "ejemplo": "\n                from decimal import Decimal\n\n                x = Decimal('0.1')\n                y = Decimal('0.2')\n                print(x + y)  # Output: 0.3\n                ",
            "significado": "Python module that provides support for performing calculations with arbitrary precision decimals",
            "uso": "It is used to perform accurate arithmetic operations without the rounding errors typical of floating-point numbers"
        },
        "decode": {
            "ejemplo": "\n                encoded = b'Hello World'\n                decoded = encoded.decode('utf-8')\n                print(decoded)  # Output: Hello Wolrd\n                ",
            "significado": "Method used to convert binary data to text in a specific encoding",
            "uso": "It is used to decode a sequence of bytes into a text string in a specific encoding"
        },
        "decode_header": {
            "ejemplo": "\n                from email.header import decode_header\n\n                header = '=?utf-8?B?SG9sYSBNdW5kbyA8MTIzNDU+?='\n                decoded, encoding = decode_header(header)[0]\n                print(decoded.decode(encoding))  # Output: Hello World <12345>\n                ",
            "significado": "Function of the 'email.header' module that decodes an email header",
            "uso": "It is used to decode an email header that can be in different encodings"
        },
        "deepcopy": {
            "ejemplo": "\n                import copy\n\n                original = {'a': [1, 2, 3]}\n                copy = copy.deepcopy(original)\n                copy['a'][0] = 100\n                print(original)  # Output: {'a': [1, 2, 3]}\n                print(copy)     # Output: {'a': [100, 2, 3]}\n                ",
            "significado": "Function of the 'copy' module that creates a deep copy of an object, i.e. copies all elements of the original object, including objects within objects",
            "uso": "It is used when it is necessary to make a complete and independent copy of an object"
        },
        "def": {
            "ejemplo": "\n                def Hello_world():\n                    print('Hello World')\n\n                Hello_world()  # Output: Hello World\n                ",
            "significado": "Python keyword used to define a function",
            "uso": "It is used to create a new function with a name and a block of code"
        },
        "defaultdict": {
            "ejemplo": "\n                from collections import defaultdict\n\n                d = defaultdict(int)\n                d['a'] += 1\n                print(d)  # Output: defaultdict(<class 'int'>, {'a': 1})\n                ",
            "significado": "Class in the 'collections' module that extends the default dictionary and allows you to set a default value for non-existent keys",
            "uso": "It is used to prevent errors when accessing non-existent keys by providing a default value"
        },
        "deflate": {
            "ejemplo": "\n                import zlib\n\n                data = b'Hello Wolrd'*100\n                compressed = zlib.compress(data)\n                print(compressed)\n                ",
            "significado": "Lossless data compression algorithm, used to reduce file sizes",
            "uso": "It is used to compress data into a more efficient format"
        },
        "del": {
            "ejemplo": "\n                list = [1, 2, 3]\n                del list[1]\n                print(list)  # Output: [1, 3]\n                ",
            "significado": "Python keyword that removes an attribute or element from a collection",
            "uso": "It is used to remove elements from a list, an object's attribute, or a variable"
        },
        "delattr": {
            "ejemplo": "\n                class Person:\n                    def __init__(self, name):\n                        self.name = name\n\n                p = Person('pepe')\n                delattr(p, 'name')\n                print(hasattr(p, 'name'))  # Output: False\n                ",
            "significado": "Function that removes an attribute from an object in Python",
            "uso": "It is used to exclude a specific attribute of an object"
        },
        "deque": {
            "ejemplo": "\n                from collections import deque\n\n                d = deque([1, 2, 3])\n                d.append(4)\n                print(d)  # Output: deque([1, 2, 3, 4])\n                ",
            "significado": "Type of data in the Python 'collections' module that represents a double-ended queue, allowing you to add and remove elements from both ends efficiently",
            "uso": "It is used to implement queues and stacks in an efficient manner"
        },
        "deque.appendleft": {
            "ejemplo": "\n                from collections import deque\n\n                d = deque([2, 3, 4])\n                d.appendleft(1)\n                print(d)  # Output: deque([1, 2, 3, 4])\n                ",
            "significado": "Method of the 'deck' data type in the 'collections' module that adds an element to the beginning of the deck",
            "uso": "It is used to insert a new element on the left side of a deck"
        },
        "detach": {
            "ejemplo": "\n                import torch\n\n                tensor = torch.tensor([1, 2, 3])\n                detached_tensor = tensor.detach()\n                print(detached_tensor)  # Output: tensor([1, 2, 3])\n                ",
            "significado": "Method used on objects in Python to unlink an object from its context or dataflow",
            "uso": "It is used to free up resources or unbind an object from its execution environment"
        },
        "device": {
            "ejemplo": "\n            import torch\n\n            device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')\n\n            print(f'Using device: {device}')\n\n            tensor = torch.randn(3, 3)\n            tensor = tensor.to(device)\n\n            print(f'Tensor: {tensor}')\n            print(f'Tensor is on device: {tensor.device}')\n            ",
            "significado": "General term to refer to any hardware device or system where a program runs",
            "uso": "It is used to refer to devices such as computers, mobile phones, etc"
        },
        "dict": {
            "ejemplo": "\n                d = {'a': 1, 'b': 2}\n                print(d['a'])  # Output: 1\n                ",
            "significado": "Type of data in Python that represents a dictionary, a collection of key-value pairs",
            "uso": "It is used to store and manipulate data efficiently by associating unique keys with values"
        },
        "dict.get": {
            "ejemplo": "\n                d = {'a': 1, 'b': 2}\n                print(d.get('a'))  # Output: 1\n                print(d.get('c', 'not found'))  # Output: not found\n                ",
            "significado": "Python dictionaries method that returns the value of a specified key or a default value if the key does not exist",
            "uso": "It is used to get the value associated with a key without generating an error if the key does not exist"
        },
        "dict.update": {
            "ejemplo": "\n                d1 = {'a': 1, 'b': 2}\n                d2 = {'b': 3, 'c': 4}\n                d1.update(d2)\n                print(d1)  # Output: {'a': 1, 'b': 3, 'c': 4}\n                ",
            "significado": "Python dictionaries method that updates a dictionary with the elements of another dictionary or iterable",
            "uso": "It is used to add or modify elements in a dictionary using another dictionary or iterate"
        },
        "difference": {
            "ejemplo": "\n                a = {1, 2, 3}\n                b = {2, 3, 4}\n                print(a.difference(b))  # Output: {1}\n                ",
            "significado": "Sets method in Python that returns the difference between two or more sets",
            "uso": "It is used to find the elements that are in one set but not in the others"
        },
        "difference_update": {
            "ejemplo": "\n                a = {1, 2, 3}\n                b = {2, 3, 4}\n                a.difference_update(b)\n                print(a)  # Output: {1}\n                ",
            "significado": "Sets method in Python that removes elements from one set that are present in another set",
            "uso": "It is used to modify a set by removing the elements that are in another set"
        },
        "dir": {
            "ejemplo": "\n                x = [1, 2, 3]\n                print(dir(x))\n                ",
            "significado": "Function that returns a list of an object's attributes and methods",
            "uso": "It is used to obtain information about the methods and attributes available for an object or module"
        },
        "disk_cache": {
            "ejemplo": "\n                import joblib\n\n                result = joblib.Memory('cache_dir').cache(some_function)\n                ",
            "significado": "Disk caching to improve data access speed or computational results",
            "uso": "It is used to temporarily store results or data on disk to avoid the need to recalculate or re-obtain the data"
        },
        "disk_usage": {
            "ejemplo": "\n                import shutil\n\n                usage = shutil.disk_usage('/')\n                print(usage)  # Output: usage(total=500000000, used=200000000, free=300000000)\n                ",
            "significado": "Function of the 'shutil' module that returns disk usage of a path or directory",
            "uso": "It is used to obtain information about the used and available space in a file system"
        },
        "divmod": {
            "ejemplo": "\n                result = divmod(9, 4)\n                print(result)  # Output: (2, 1)\n                ",
            "significado": "Function that takes two numbers and returns a tuple with the quotient and the rest of its division",
            "uso": "It is used to obtain both the quotient and the remainder of a division in a single operation"
        },
        "dropna": {
            "ejemplo": "\n                import pandas as pd\n\n                df = pd.DataFrame({'A': [1, 2, None], 'B': [None, 3, 4]})\n                print(df.dropna())\n                ",
            "significado": "Method in Pandas used to remove missing values (NaN) in a DataFrame or Series",
            "uso": "It is used to clean up data by removing rows or columns that contain null values"
        },
        "dtype": {
            "ejemplo": "\n                import numpy as np\n\n                arr = np.array([1, 2, 3])\n                print(arr.dtype)  # Output: int64\n                ",
            "significado": "Property of arrays in Numpy or columns in a Pandas DataFrame that indicates the data type of the elements",
            "uso": "It is used to obtain or specify the type of data of an array or column"
        },
        "dump": {
            "ejemplo": "\n                import pickle\n\n                data = {'a': 1, 'b': 2}\n                with open('data.pkl', 'wb') as f:\n                    pickle.dump(data, f)\n                ",
            "significado": "Pickle library method that serializes an object and writes it to a file",
            "uso": "It is used to save an object to a file in serialized form"
        },
        "dumps": {
            "ejemplo": "\n                import pickle\n\n                data = {'a': 1, 'b': 2}\n                serialized = pickle.dumps(data)\n                print(serialized)\n                ",
            "significado": "Pickle library method that serializes an object and returns it as a byte string",
            "uso": "It is used to convert an object into a string format for storage or transmission"
        }
    },
    "e": {
        "edit_distance": {
            "ejemplo": "\n                from nltk.metrics import edit_distance\n\n                distance = edit_distance('kitten', 'sitting')\n                print(distance)  # Output: 3\n                ",
            "significado": "Measure that calculates the difference between two strings based on the operations required to convert one to the other",
            "uso": "It is used to compare how similar two strings are and to determine how many changes are needed to make them identical"
        },
        "element": {
            "ejemplo": "\n                list = [1, 2, 3]\n                print(list[0])  # Output: 1\n                ",
            "significado": "An individual item within a collection or data structure",
            "uso": "It is used to refer to an object within a list, set, dictionary, etc"
        },
        "elements": {
            "ejemplo": "\n                ensemble = {1, 2, 3}\n                for element in ensemble:\n                    print(element)\n                # Output:\n                # 1\n                # 2\n                # 3\n                ",
            "significado": "Individual items or components within a set or collection",
            "uso": "It is used to refer to the parts of a data structure"
        },
        "elif": {
            "ejemplo": "\n                x = 3\n                if x > 5:\n                    print('Greater than 5')\n                elif x == 3:\n                    print('Same a 3')\n                else:\n                    print('Less than 3')\n                # Output: Same a 3\n                ",
            "significado": "Keyword in Python used in conditional structures to check for an additional condition if the previous ones are not met",
            "uso": "It is used to handle multiple conditions in an if-elif-else structure"
        },
        "else": {
            "ejemplo": "\n                if 3 > 1:\n                    print('Condition True')\n                else:\n                    print('Condition False')\n                # Output: Condition True\n                ",
            "significado": "Keyword in Python used in conditional control frameworks (if, try) to execute a block of code if the condition is not met or no exception occurs",
            "uso": "It is used to execute a block of code when the condition is not met or no exception occurs"
        },
        "encode": {
            "ejemplo": "\n                text = 'Hello World'\n                encoded = text.encode('utf-8')\n                print(encoded)\n                # Output: b'Hello World'\n                ",
            "significado": "Strings method in Python that encodes a string into a byte sequence using a specific encoder",
            "uso": "It is used to convert a string into a sequence of bytes to be stored or transmitted in specific formats"
        },
        "encode_base64": {
            "ejemplo": "\n                import base64\n                encoded = base64.b64encode(b'Hello')\n                print(encoded)  # Output: b'b2xh'\n                ",
            "significado": "Encoding method that converts binary data into a base-64 text representation",
            "uso": "It is used to encode binary data into a readable base-64 text string"
        },
        "encode_utf8": {
            "ejemplo": "\n                text = 'Hello World'\n                encoded = text.encode('utf-8')\n                print(encoded)  # Output: b'Hello World'\n                ",
            "significado": "Encoding method that converts a string of characters into a sequence of bytes using the UTF-8 format",
            "uso": "It is used to convert text into a binary representation using UTF-8"
        },
        "end": {
            "ejemplo": "\n                print('Hello', end=' ')\n                print('World')\n                # Output: Hello World\n                ",
            "significado": "Keyword used in Python to specify the end of a block or the termination of a string",
            "uso": "It is mainly used in printing functions to control the output end"
        },
        "enumerate": {
            "ejemplo": "\n                list = ['a', 'b', 'c']\n                for index, value in enumerate(list):\n                    print(index, value)\n                # Output:\n                # 0 a\n                # 1 b\n                # 2 c\n                ",
            "significado": "Built-in Python function that adds a counter to an iterable and returns it as an iterable tuple object",
            "uso": "It is used to obtain both the index and the value of elements in an iterable"
        },
        "enumerations": {
            "ejemplo": "\n                from enum import Enum\n\n                class Cor(Enum):\n                    RED = 1\n                    GREEN = 2\n                    BLUE = 3\n\n                print(Cor.RED)  # Output: Cor.RED\n                ",
            "significado": "A list or set of elements, often with an associated value or identifier",
            "uso": "It is used to represent a set of possible values of a variable"
        },
        "environment": {
            "ejemplo": "\n                import os\n                print(os.environ)  # Output: Shows system environment variables.\n                ",
            "significado": "The context or set of conditions under which a program or application runs",
            "uso": "It is used to refer to the set of variables, settings, and features available to a program"
        },
        "environment_config": {
            "ejemplo": "\n                config = {\n                    'host': 'localhost',\n                    'port': 8080\n                }\n                print(config)  # Output: {'host': 'localhost', 'port': 8080}\n                ",
            "significado": "Configuration related to the runtime of a program or system",
            "uso": "It is used to specify or adjust parameters that affect the operation of a program or application"
        },
        "environment_variable": {
            "ejemplo": "\n                import os\n                print(os.getenv('PATH'))  # Output: Shows the PATH environment variable.\n                ",
            "significado": "Variable that stores information about the system or application environment",
            "uso": "It is used to store specific settings that affect the behavior of programs"
        },
        "equal": {
            "ejemplo": "\n                a = 5\n                b = 5\n                print(a == b)  # Output: True\n                ",
            "significado": "Indicates that two elements are identical in value",
            "uso": "It is used to compare two values or expressions to see if they are the same"
        },
        "error": {
            "ejemplo": "\n                try:\n                    1 / 0\n                except ZeroDivisionError as e:\n                    print(f'Error: {e}')\n                # Output: Error: divided by zero\n                ",
            "significado": "Anomalous condition in the execution of a program that interrupts its normal flow",
            "uso": "It is used to indicate that something has gone wrong during code execution"
        },
        "error_handling": {
            "ejemplo": "\n                try:\n                    value = 10 / 0\n                except ZeroDivisionError:\n                    print('Error de divide by zero')  # Output: Error divide by zero\n                ",
            "significado": "Process of managing errors and exceptions that occur during the execution of a program",
            "uso": "It is used to catch and manage errors in a controlled manner to prevent the program from terminating unexpectedly"
        },
        "error_message": {
            "ejemplo": "\n                try:\n                    x = int(\"abc\")\n                except ValueError as e:\n                    print(f\"Error message: {e}\")  # Output: Error message: invalid literal for int() with base 10: 'abc'\n                ",
            "significado": "Message that describes the error or problem that occurred during the execution of a program",
            "uso": "It is used to provide details about what failed or caused an exception"
        },
        "eval": {
            "ejemplo": "\n                x = 2\n                result = eval('x + 1')\n                print(result)  # Output: 3\n                ",
            "significado": "Built-in Python function that evaluates a code string as a Python expression",
            "uso": "It is used to execute Python expressions contained in a string and return the result"
        },
        "eval_input": {
            "ejemplo": "\n                entry = input('Enter a number: ')\n                result = eval(entry)\n                print(result)\n                ",
            "significado": "A function that evaluates user input, typically via the input() function",
            "uso": "It is used to obtain and evaluate a user-provided input"
        },
        "evaluate": {
            "ejemplo": "\n                x = 5\n                result = eval('x + 2')\n                print(result)  # Output: 7\n                ",
            "significado": "Execute or calculate the value of an expression or function",
            "uso": "It is used to obtain the result of an expression"
        },
        "evaluate_expression": {
            "ejemplo": "\n                result = eval('3 + 5')\n                print(result)  # Output: 8\n                ",
            "significado": "Evaluate an expression to get its result",
            "uso": "It is used to calculate or obtain the value of a mathematical or logical expression"
        },
        "event": {
            "ejemplo": "\n                import tkinter as tk\n                def click():\n                    print('Button pressed')\n                root = tk.Tk()\n                button = tk.Button(root, text=\"Click on me\", command=click)\n                button.pack()\n                root.mainloop()  # Output: Shows a button that, when pressed, executes the click event\n                ",
            "significado": "Action or event that can be detected and managed in a program",
            "uso": "It is used to manage and respond to activities or changes in a system or program"
        },
        "event_loop": {
            "ejemplo": "\n                import asyncio\n                async def hello():\n                    print(\"Hello\")\n                asyncio.run(hello())  # Output: Hello\n                ",
            "significado": "Continuous cycle that expects and manages asynchronous events or tasks in a program.",
            "uso": "It is used to execute tasks or respond to events in order, without blocking the main flow of execution."
        },
        "except": {
            "ejemplo": "\n                try:\n                    x = 1 / 0\n                except ZeroDivisionError:\n                    print('Error: divide by zero')\n                # Output: Error: divide by zero\n                ",
            "significado": "Python keyword used to handle exceptions within a try-except block",
            "uso": "It is used to catch and handle exceptions that occur in the try block"
        },
        "exception": {
            "ejemplo": "\n                try:\n                    int('a')\n                except ValueError:\n                    print('Error: Cannot convert to integer')\n                # Output: Error: Cannot convert to integer\n                ",
            "significado": "Event that alters the normal flow of program execution, usually due to an error",
            "uso": "It is used to handle errors in code and perform specific actions when they occur"
        },
        "exception_handling": {
            "ejemplo": "\n                try:\n                    value = 1 / 0\n                except ZeroDivisionError as e:\n                    print(f'Error: {e}')  # Output: Error: divided by zero\n                ",
            "significado": "Process of managing and responding to errors or exceptions that occur during the execution of a program",
            "uso": "It is used to catch and manage errors, ensuring that the program does not stop unexpectedly"
        },
        "exception_type": {
            "ejemplo": "\n                try:\n                    value = 10 / 0\n                except ZeroDivideError as e:\n                    print(f\"Error Type: {type(e)}\")  # Output: Error Type: <class 'ZeroDivideError'>\n                ",
            "significado": "The specific type of an exception or error that occurs in a program",
            "uso": "It is used to identify what type of error has occurred and take appropriate action"
        },
        "exec": {
            "ejemplo": "\n                code = 'for i in range(3): print(i)'\n                exec(code)\n                # Output:\n                # 0\n                # 1\n                # 2\n                ",
            "significado": "Built-in Python function that executes a code string as a complete code block",
            "uso": "It is used to execute Python code dynamically"
        },
        "execfile": {
            "ejemplo": "\n                # This command is only available in Python 2\n                execfile('script.py')\n                ",
            "significado": "Function that executes a Python file as if it were a script",
            "uso": "It is used to execute an external Python file"
        },
        "execute": {
            "ejemplo": "\n                def funtion():\n                    print('Running...')\n                funtion()  # Output: Running...\n                ",
            "significado": "Perform or execute a set of instructions or a program",
            "uso": "It is used to put into practice an action or execute code"
        },
        "exit": {
            "ejemplo": "\n                import sys\n                sys.exit('Finishing the program')\n                # The program ends with the message 'Ending the program'\n                ",
            "significado": "Built-in Python function that terminates program execution",
            "uso": "It is used to exit a program or close an execution environment"
        },
        "exit_code": {
            "ejemplo": "\n                import sys\n                sys.exit(0)  # Output: 0 indicates success, another number indicates error.\n                ",
            "significado": "Value returned by a program or script when it is finished, indicating whether it was executed correctly or if an error occurred",
            "uso": "It is used to check if a program has completed successfully or if an error has occurred"
        },
        "exit_status": {
            "ejemplo": "\n                import sys\n                sys.exit(0)  # Output: 0 indicates success, any other number indicates error.\n                ",
            "significado": "Exit code that indicates whether a program or process has terminated correctly or in error",
            "uso": "It is used to check if a process or command has ended successfully or if an error has occurred"
        },
        "exp": {
            "ejemplo": "\n                import math\n                result = math.exp(1)\n                print(result)  # Output: 2.718281828459045\n                ",
            "significado": "A mathematical function that calculates the exponential of a number, that is, and raised to the power of that number",
            "uso": "It is used to perform exponential calculations"
        },
        "expand": {
            "ejemplo": "\n                text = \"Hello\"\n                print(text.expandtabs(4))  # Output: 'Hello' with enlarged tabs\n                ",
            "significado": "Enlarge or increase the size or reach of something",
            "uso": "It is used to do something bigger or include more information"
        },
        "expandtabs": {
            "ejemplo": "\n                text = 'Hello\tWorld'\n                print(text.expandtabs(4))\n                # Output: World   Hello\n                ",
            "significado": "Strings method in Python that replaces tab characters with spaces",
            "uso": "It is used to align text by replacing tabs with a certain number of spaces"
        },
        "expected": {
            "ejemplo": "The expected result was an increase in processing speed",
            "significado": "Something anticipated or anticipated, based on expectations or forecasts",
            "uso": "It is used to describe what is expected to happen in a situation"
        },
        "exponential": {
            "ejemplo": "\n                import math\n                result = math.exp(2)\n                print(result)  # Output: 7.3890560989306495\n                ",
            "significado": "Related to the mathematical operation of exponentiation, which calculates the value of a base raised to an exponent",
            "uso": "It is used to perform exponential calculations"
        },
        "extract": {
            "ejemplo": "\n                text = 'Hello World'\n                print(text[0:4])  # Output: Hello\n                ",
            "significado": "Get a specific part of a dataset or insights",
            "uso": "It is used to extract or extract a specific component from a larger set of data"
        },
        "xceed": {
            "ejemplo": "The XCEED function is part of a set of functions that are used in data analysis or signal processing, but its name is not associated with a widely recognized standard function such as in common programming languages (such as Python, R, JavaScript, etc.). However, in some contexts, XCEED could refer to a custom function, some library, or even a function in some specific software",
            "significado": "A term used to describe something that exceeds or exceeds a limit or expectation",
            "uso": "It is used to indicate that something has crossed a standard or threshold"
        }
    },
    "f": {
        "factorial": {
            "ejemplo": "\n                import math\n                print(math.factorial(5))  # Output: 120\n                ",
            "significado": "A mathematical function that calculates the product of all positive integers up to a given number",
            "uso": "It is used to calculate the factorial of a number, often in combinatorics and probability algorithms"
        },
        "fibonacci": {
            "ejemplo": "\n                def fibonacci(n):\n                    if n <= 1:\n                        return n\n                    else:\n                        return fibonacci(n-1) + fibonacci(n-2)\n                \n                print(fibonacci(5))  # Output: 5\n                ",
            "significado": "Mathematical sequence where each number is the sum of the previous two",
            "uso": "It is used to generate the Fibonacci sequence, often in programming exercises or algorithms"
        },
        "fibonacci_search": {
            "ejemplo": "\n                # Implementation of Fibonacci Search is not standard, but can be used as an alternative to binary search\n                def fibonacci_search(arr, x):\n                    fib_m_minus_2 = 0\n                    fib_m_minus_1 = 1\n                    fib_m = fib_m_minus_1 + fib_m_minus_2\n                    while(fib_m < len(arr)):\n                        fib_m_minus_2 = fib_m_minus_1\n                        fib_m_minus_1 = fib_m\n                        fib_m = fib_m_minus_1 + fib_m_minus_2\n                ",
            "significado": "Search method that uses Fibonacci numbers to divide the search space efficiently",
            "uso": "It is used as an alternative to the binary search algorithm to find an element in an array"
        },
        "fibonacci_sequence": {
            "ejemplo": "\n                def fibonacci(n):\n                    Sequence = [0, 1]\n                    while len(Sequence) < n:\n                        Sequence.append(Sequence[-1] + Sequence[-2])\n                    return Sequence\n                \n                print(fibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]\n                ",
            "significado": "Mathematical sequence where each number is the sum of the previous two.",
            "uso": "It is used to generate the Fibonacci sequence"
        },
        "file": {
            "ejemplo": "\n                with open('file.txt', 'r') as f:\n                    Content = f.read()\n                print(Content)\n                ",
            "significado": "Python object that allows you to interact with files in the file system",
            "uso": "It is used to open, read, write, and manipulate files"
        },
        "file_object": {
            "ejemplo": "\n                with open('document.txt', 'r') as f:\n                    Content = f.read()\n                    print(Content)\n                ",
            "significado": "object that represents a file opened in Python, through which it is possible to read, write, or manipulate the file",
            "uso": "It is used to interact with files opened in Python, accessing or modifying their contents"
        },
        "file_read": {
            "ejemplo": "\n                with open('document.txt', 'r') as file:\n                    Content = file.read()\n                    print(Content)\n                ",
            "significado": "Operation that allows you to read the contents of a file in Python.",
            "uso": "It is used to obtain the data stored in a file for processing or display."
        },
        "file_write": {
            "ejemplo": "\n                with open('document.txt', 'w') as file:\n                    file.write('Hello, World!')\n                ",
            "significado": "Operation that allows you to write date to a file in Python.",
            "uso": "It is used to store information in a file, overwriting it or adding new data"
        },
        "filemode": {
            "ejemplo": "\n                file = open('file.txt', 'r')  # 'r' indicates read-only mode\n                print(file.mode)  # Output: 'r'\n                ",
            "significado": "How to open a file that determines the operations that can be performed on it",
            "uso": "It is used to specify the type of access desired for a file (read, write, etc.)."
        },
        "filename": {
            "ejemplo": "\n                file = 'document.txt'\n                with open(file, 'r') as f:\n                    print(f.read())\n                ",
            "significado": "String representing the name of a file in the file system",
            "uso": "It is used to specify the name and location of a file that is to be manipulated"
        },
        "filepath": {
            "ejemplo": "\n                import os\n                path = os.path.join('folder', 'file.txt')\n                print(path)  # Output: folder/file.txt\n                ",
            "significado": "Path or address of a file in the file system",
            "uso": "It is used to specify the location of a file in the file system"
        },
        "filter": {
            "ejemplo": "\n                list = [1, 2, 3, 4, 5]\n                result = filter(lambda x: x % 2 == 0, list)\n                print(list(result))  # Output: [2, 4]\n                ",
            "significado": "Function that applies a condition to each element of an iterable and returns the elements that meet the condition",
            "uso": "It is used to select only those elements that meet a specific condition"
        },
        "filter_map": {
            "ejemplo": "\n                from itertools import filterfalse\n                data = [1, 2, 3, 4, 5]\n                result = map(lambda x: x * 2, filter(lambda x: x % 2 == 0, data))\n                print(list(result))  # Output: [4, 8]\n                ",
            "significado": "Function that filters the elements of an iterable and then applies a mapping function to the remaining elements",
            "uso": "It is used to efficiently perform transformations and filtering on date sequences"
        },
        "filter_none": {
            "ejemplo": "\n                list = [1, None, 2, None, 3]\n                result = filter(None, list)\n                print(list(result))  # Output: [1, 2, 3]\n                ",
            "significado": "Function that filters elements from an iterable by excluding None values.",
            "uso": "It is used to exclude 'None' values from a string."
        },
        "filterfalse": {
            "ejemplo": "\n                from itertools import filterfalse\n                result = filterfalse(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])\n                print(list(result))  # Output: [1, 3, 5]\n                ",
            "significado": "Function that returns an iterator that filters the elements of an iterable, excluding those that return 'True' in the given function",
            "uso": "It is used to get the elements of an iterable for which the function returns 'False'"
        },
        "filtering": {
            "ejemplo": "\n                list = [1, 2, 3, 4, 5]\n                result = filter(lambda x: x > 2, list)\n                print(list(result))  # Output: [3, 4, 5]\n                ",
            "significado": "Process of selecting elements from a collection that meet a specific condition",
            "uso": "It is used to extract elements from a list, ensemble, or any iterable based on a condition"
        },
        "finally": {
            "ejemplo": "\n                try:\n                    x = 1 / 0\n                except ZeroDivisionError:\n                    print('Divide by zero')\n                finally:\n                    print('This block always runs')\n                ",
            "significado": "Keyword in Python that defines a block of code that will run every time, regardless of whether an exception occurs or not",
            "uso": "It is used in try-except structures to ensure that a final block of code is executed, even if an error occurs"
        },
        "finally_clause": {
            "ejemplo": "\n                try:\n                    file = open('document.txt', 'r')\n                    Content = file.read()\n                finally:\n                    file.close()\n                    print('File closed')\n                ",
            "significado": "Part of a block of code that always executes after a 'try' statement, regardless of whether an exception is thrown or not.",
            "uso": "It is used to execute cleanup or finalization code, such as closing files or releasing resources."
        },
        "find": {
            "ejemplo": "\n                text = 'Hello World'\n                print(text.find('World'))  # Output: 5\n                ",
            "significado": "A method that fetches a substring within a string and returns the index from the first occurrence",
            "uso": "It is used to find the position of one text within another"
        },
        "first": {
            "ejemplo": "\n                list = [1, 2, 3, 4]\n                print(list[0])  # Output: 1\n                ",
            "significado": "Getting the first element of a sequence or iterable",
            "uso": "It is used to access the first value of an iterable, such as a list or ensemble"
        },
        "fix": {
            "ejemplo": "\n                # Example in the context of code: fix a syntax error\n                def correct_error():\n                    print('This is the corrected message')\n                correct_error()\n                ",
            "significado": "General term for correcting or adjusting something that doesn't work properly",
            "uso": "It is used when you make an adjustment or correction to the code or configuration of something"
        },
        "flask": {
            "ejemplo": "\n                from flask import Flask\n                app = Flask(__name__)\n\n                @app.route('/')\n                def hello():\n                    return 'Hello World'\n\n                app.run()  # Output: 'Hello World' in a web application\n                ",
            "significado": "A Python micro-framework for web application development",
            "uso": "It is used to create web applications in a simple and fast way with routes, forms, and other features"
        },
        "flask_restful": {
            "ejemplo": "\n                from flask import Flask\n                from flask_restful import Api, Resource\n\n                app = Flask(__name__)\n                api = Api(app)\n\n                class HelloWorld(Resource):\n                    def get(self):\n                        return {'mensagge': 'Hello World'}\n\n                api.add_resource(HelloWorld, '/')\n                app.run()  # Output: 'Hello World' as API response\n                ",
            "significado": "Extension for Flask that simplifies the creation of RESTful APIs",
            "uso": "It is used to develop web applications that follow the REST architecture using"
        },
        "float": {
            "ejemplo": "\n                number = 3.14\n                print(type(number))  # Output: <class 'float'>\n                ",
            "significado": "Data type in Python to represent floating-point numbers (numbers with decimals)",
            "uso": "It is used to represent numbers that require decimals"
        },
        "float32": {
            "ejemplo": "\n                import numpy as np\n                number = np.float32(3.1415)\n                print(number)  # Output: 3.1415\n                ",
            "significado": "Type of data in NumPy that represents a 32-bit floating-point number",
            "uso": "It is used to store numbers with decimals more efficiently in terms of memory"
        },
        "float64": {
            "ejemplo": "\n                import numpy as np\n                number = np.float64(3.141592653589793)\n                print(number)  # Output: 3.141592653589793\n                ",
            "significado": "Type of data in NumPy that represents a 64-bit floating-point number",
            "uso": "It is used to store numbers with decimals with greater precision than the float32 type."
        },
        "float_conversion": {
            "ejemplo": "\n                number = '3.14'\n                result = float(number)\n                print(result)  # Output: 3.14\n                ",
            "significado": "Process of Converting Date from Other Types to Floating Type",
            "uso": "It is used to convert values to floating-point numbers (decimals)"
        },
        "float_format": {
            "ejemplo": "\n                pi = 3.14159\n                print(f'{pi:.2f}')  # Output: 3.14\n                ",
            "significado": "Format that defines how floating-point numbers should be presented in a chain",
            "uso": "It is used to specify the number of decimal places to display in a floating-point number"
        },
        "float_power": {
            "ejemplo": "\n                print(pow(2, 3.5))  # Output: 11.313708498984761\n                ",
            "significado": "Function that calculates a number raised to a floating power",
            "uso": "It is used to perform exponentiation with floating numbers"
        },
        "float_precision": {
            "ejemplo": "\n                number = 3.14159265359\n                print(f'{number:.2f}')  # Output: 3.14\n                ",
            "significado": "Number of digits used to accurately represent a floating number",
            "uso": "It is used to specify the number of decimal places to consider when performing operations with floating numbers"
        },
        "flush": {
            "ejemplo": "\n                with open('file.txt', 'w') as f:\n                    f.write('Hello')\n                    f.flush()  # Ensures that the data are written to the file\n                ",
            "significado": "Method used to empty the buffers of a file, ensuring that all data are written to disk",
            "uso": "It is used when it is necessary to ensure that data stored in a buffer is immediately written to the file"
        },
        "flush_output": {
            "ejemplo": "\n                import sys\n                sys.stdout.write('Hello World')\n                sys.stdout.flush()  # Output: 'Hello World' instanly\n                ",
            "significado": "Method used to empty the output buffer, forcing the data to be written immediately",
            "uso": "It is used when you want to ensure that all pending data in the output buffer is written to the destination"
        },
        "fold": {
            "ejemplo": "\n                from functools import reduce\n                list = [1, 2, 3, 4]\n                result = reduce(lambda x, y: x + y, list)\n                print(result)  # Output: 10\n                ",
            "significado": "Function that applies a cumulative operation on the elements of a sequence.",
            "uso": "It is used to reduce a sequence of elements to a single value by applying a binary operation"
        },
        "for": {
            "ejemplo": "\n                for i in range(5):\n                    print(i)\n                # Output:\n                # 0\n                # 1\n                # 2\n                # 3\n                # 4\n                ",
            "significado": "Python keyword used to iterate over the elements of an iterable",
            "uso": "It is used to execute a block of code repeatedly for each element of an iterable"
        },
        "force": {
            "ejemplo": "\n                # There is no direct force in Python, but you can use assert to force conditions\n                assert 1 == 1, 'condition false'\n                ",
            "significado": "The action of imposing or forcing the execution of something, usually in the context of programming or manipulating objects",
            "uso": "It is used to force a specific behavior in a program, such as avoiding errors or performing an action regardless of the conditions"
        },
        "fork": {
            "ejemplo": "\n                import os\n                pid = os.fork()\n                if pid > 0:\n                    print(f'Parent Process, PID: {pid}')\n                else:\n                    print(f'Child process, PID: {os.getpid()}')\n                ",
            "significado": "Process of creating a new process, copied from the original process",
            "uso": "It is used in the programming of systems to create secondary processes"
        },
        "forking": {
            "ejemplo": "\n                import os\n                pid = os.fork()\n                # Similar to the example of 'fork', but encompassing the concept of 'forking''\n                ",
            "significado": "Action of creating a new process or subprocess from a main process.",
            "uso": "It is used in operating systems to create additional processes that perform tasks concurrently"
        },
        "form": {
            "ejemplo": "\n                form = {'name': 'Juan', 'age': 25}\n                print(form)\n                ",
            "significado": "Structure or template used to organize date in a specific way.",
            "uso": "It is used in user interfaces or web applications to capture and organize user data."
        },
        "format": {
            "ejemplo": "\n                name = 'Juan'\n                age = 30\n                print('my name is {} and i am {} years old'.format(name, age))\n                # Output: my name is Juan i am 30 years old\n                ",
            "significado": "Method used to format text strings by inserting values within them",
            "uso": "It is used to create more readable and dynamic text strings with variable values"
        },
        "format_error": {
            "ejemplo": "\n                try:\n                    int('abc')\n                except ValueError as e:\n                    print(f'format error: {e}')\n                ",
            "significado": "Error that occurs when there is a problem formatting date, such as a poorly structured string",
            "uso": "It is used to handle errors related to incorrect date conversion or formatting"
        },
        "format_map": {
            "ejemplo": "\n                data = {'name': 'pepe', 'age': 30}\n                text = 'Name: {name}, age: {age}'.format_map(data)\n                print(text)  # Output: Name: pepe, age: 30\n                ",
            "significado": "Method that returns a string formatted using a dictionary or similar object",
            "uso": "It is used to perform value substitutions in a string using a map (such as a dictionary)"
        },
        "format_spec": {
            "ejemplo": "\n                pi = 3.14159\n                print(f'{pi:.2f}')  # Output: 3.14\n                ",
            "significado": "String used to define how values should be presented within a string format",
            "uso": "It is used to specify the format of values within a string, such as decimal precision, alignment, and more"
        },
        "format_string": {
            "ejemplo": "\n                name = 'Juan'\n                age = 25\n                print(f'Name: {name}, age: {age}')  # Output: Name: Juan, age: 25\n                ",
            "significado": "String that defines the structure of a value that you want to display, using format specifiers",
            "uso": "It is used to define how values should be displayed in a string, such as the number of decimal places or the alignment"
        },
        "formatting": {
            "ejemplo": "\n                text = 'Name: {0:10}, age: {1:5}'.format('pepe', 30)\n                print(text)  # Output: Name: pepe      , age: 30\n                ",
            "significado": "The process of applying a format to date or strings, such as alignment, widths, and date types",
            "uso": "It is used to organize or display date in a more legible or specific way"
        },
        "fread": {
            "ejemplo": "\n                with open('file.bin', 'rb') as f:\n                    data = f.read()\n                print(data)  # Output: b'Hello, World!'\n                ",
            "significado": "Function Used to Read Date from a File",
            "uso": "It is used to read binary data from an open file in read mode"
        },
        "freeze": {
            "ejemplo": "\n                # There is no explicit function called freeze, but in some cases such as with 'frozenset' you can achieve the same effect\n                a = frozenset([1, 2, 3])\n                print(a)  # Output: frozenset({1, 2, 3})\n                ",
            "significado": "Process of converting a mutable object to an immutable object",
            "uso": "It is used to prevent an object from being modified after it has been created"
        },
        "from": {
            "ejemplo": "\n                from math import sqrt\n                print(sqrt(16))  # Output: 4.0\n                ",
            "significado": "Python keyword used to import modules or module-specific functions",
            "uso": "It is used to bring specific functionality from a module into the current namespace"
        },
        "fromkeys": {
            "ejemplo": "\n                dictionary = dict.fromkeys(['a', 'b', 'c'], 0)\n                print(dictionary)  # Output: {'a': 0, 'b': 0, 'c': 0}\n                ",
            "significado": "Dictionary method that creates a new dictionary with specified keys and default values",
            "uso": "It is used to create dictionaries from a list of keys with a default value"
        },
        "frozen": {
            "ejemplo": "\n                a = frozenset([1, 2, 3])\n                print(a)  # Output: frozenset({1, 2, 3})\n                ",
            "significado": "Immutable object that cannot be modified after its creation",
            "uso": "It is used to create objects that cannot be changed, such as a 'frozenset' in Python"
        },
        "frozen_set": {
            "ejemplo": "\n                ensemble = frozenset([1, 2, 3])\n                print(ensemble)  # Output: frozenset({1, 2, 3})\n                ",
            "significado": "Immutable set in Python, similar to a standard set, but without the possibility of modifying it after its creation",
            "uso": "It is used to create sets that should not be modified after they have been created"
        },
        "fstring": {
            "ejemplo": "\n                name = 'Juan'\n                age = 30\n                print(f'My name is {name} and i am {age} years old')\n                # Output:My name is Juan and i am 30 years old\n                ",
            "significado": "Text string that allows you to insert expressions within the string in a more readable and efficient way",
            "uso": "It is used to create interpolated text strings, where variables can be inserted directly into the string"
        },
        "full_path": {
            "ejemplo": "\n                import os\n                path_complet = os.path.abspath('file.txt')\n                print(pah_complet)  # Output: /home/user/file.txt\n                ",
            "significado": "Full path to a file or directory in the file system",
            "uso": "It is used to specify the exact location of a file or directory from the root of the file system"
        },
        "func_code": {
            "ejemplo": "\n                def ejemplo():\n                    pass\n                \n                print(ejemplo.__code__)  # Output: <code object example at 0x...>\n                ",
            "significado": "Attribute that contains the bytecode of the function in Python.",
            "uso": "It is used to access function code, usually in debugging or analysis contexts"
        },
        "function": {
            "ejemplo": "\n                def Greeting(name):\n                    return f'Hello, {name}'\n                \n                print(Greeting('Juan'))  # Output: Hello, Juan\n                ",
            "significado": "Block of code designed to perform a specific task and that can be reused",
            "uso": "It is used to bundle related code that performs a common task, allowing for reusability and modularity"
        },
        "function_call": {
            "ejemplo": "\n                def sum(a, b):\n                    return a + b\n                result = sum(3, 4)\n                print(result)  # Output: 7\n                ",
            "significado": "Invoke a function in code, passing the parameters needed to execute your task",
            "uso": "It is used to execute a function and obtain its result"
        },
        "function_definition": {
            "ejemplo": "\n                def greet(name):\n                    return f'Hello {name}'\n                print(greet('pepe'))  # Output: Hello pepe\n                ",
            "significado": "The process of creating a function in Python using the 'def' keyword",
            "uso": "It is used to declare reusable functions that execute a specific block of code"
        },
        "function_pointer": {
            "ejemplo": "\n                # In Python there is no direct function pointer, but functions can be passed as objects\n                def Greeting():\n                    print('Hello')\n                function = Greeting\n                function()  # Output: Hello\n                ",
            "significado": "Reference to a function that can be passed and executed as an argument",
            "uso": "It is used in languages such as C or C++ to reference functions and pass them as parameters"
        },
        "futures": {
            "ejemplo": "\n                from concurrent.futures import ThreadPoolExecutor\n\n                def task(x):\n                    return x * x\n\n                with ThreadPoolExecutor() as executor:\n                    results = executor.map(task, [1, 2, 3])\n                    print(list(results))  # Output: [1, 4, 9]\n                ",
            "significado": "Module that provides an interface to perform asynchronous and parallelized tasks",
            "uso": "It is used to execute functions concurrently using threads or processes"
        },
        "fuzzy": {
            "ejemplo": "\n                # Example of a fuzzy logic library like 'fuzzywuzzy' (for fuzzy text matching)\n                from fuzzywuzzy import fuzz\n                print(fuzz.ratio('hello', 'Hello'))  # Output: 100\n                ",
            "significado": "Related to fuzzy logic, which allows you to deal with inaccurate or uncertain information",
            "uso": "It is used in systems that need to process approximate or uncertain dates"
        },
        "fwrite": {
            "ejemplo": "\n                with open('file.bin', 'wb') as f:\n                    f.write(b'Hello, World!')\n                ",
            "significado": "Function used to write date in a file",
            "uso": "It is used to write data binaries to an open file in write mode"
        }
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
    "h": {},
    "i": {
        "_init_": {
            "ejemplo": "class Person:\n            def __init__(self, name, age):\n            self.name = name\n            self.age = age",
            "significado": "It's a special method in Python classes that's called when you create a new instance of the",
            "uso": " To initialize object attributes."
        },
        "if": {
            "ejemplo": "if x > 10: print('greater than 10')",
            "significado": "Condition that is assessed as true or false",
            "uso": "Used to make decisions in the flow of a program"
        },
        "index": {
            " ejemplo": "list = [10, 20, 30, 40]\n            print(list.index(30))  # 2",
            "significado": "Returns the index of the first occurrence of a value in a list or string",
            "uso": " Search the position of a element inside of a iterable"
        },
        "input": {
            "ejemplo": "input('write a number')",
            "significado": "Reads user-written data",
            "uso": "It is used to interact with the user and obtain information"
        },
        "int": {
            "ejemplo": "int(\"10\")  # 10",
            "significado": "Turn a string into a whole number",
            "uso": "It is used to convert numerical strings into integer values"
        }
    },
    "j": {
        "join": {
            "ejemplo": "words = [\"Hello\", \"world\"]\n            result = \" \".join(words)\n            print(result)  ",
            "significado": "Join the elements of an iterable in a string, using a specific delimiter",
            "uso": "Combine items from a list or tuple into a single string"
        }
    },
    "k": {},
    "l": {
        "lambda": {
            "ejemplo": "square = lambda x: x**2\n            print(square(4))  # print 16",
            "significado": "Anonymous (unnamed) function that can be defined on a single line",
            "uso": " Define simple functions to use in a single expression"
        },
        "len()": {
            "ejemplo": "text = \"Hello word\"\n            longitude = longitude (text)\n            print(f\"the longitude of the chain is: {longitude}\")",
            "significado": "Returns the length of an object (such as a list or string)",
            "uso": "To count elements in a sequence"
        },
        "locals()": {
            "ejemplo": "def ejemplo():\n            b = 20\n            print(locals())  # Result: {'b': 20}\n            ejemplo()",
            "significado": "Returns a dictionary that represents the current local namespace",
            "uso": "Get the local context of variables within a function or module"
        }
    },
    "m": {
        "map": {
            "ejemplo": "map(lambda x: x * 2, [1, 2, 3])  # [2, 4, 6]",
            "significado": "Apply a function to each element of an iterable",
            "uso": "It is used to apply an operation to all the elements of an iterable."
        },
        "max": {
            "ejemplo": "max([1, 2, 3])  # 3",
            "significado": "Returns the largest value of an iterable",
            "uso": "find the max value"
        }
    },
    "n": {},
    "o": {
        "open()": {
            "ejemplo": "file = open(\"ejemplo.txt\", \"w\")\n            file.write(\"Hello world\")\n            file.close()",
            "significado": "Opens a file and returns it as a file object",
            "uso": "read or write files"
        },
        "ord": {
            "ejemplo": "ord('A')  # Result: 65",
            "significado": "Converts a character to its ASCII code",
            "uso": "Getting the numeric value of a character"
        },
        "os": {
            "ejemplo": "import os\n            Current_Directory = os.getcwd()\n            print(f\"Current Directory: {Current_Directory}\")\n            os.mkdir(\"new_ directory\")\n            files = os.listdir(Current_Directory)\n            print(f\"files in the directory: {files}\")\n            os.rmdir(\"new_directory\")",
            "significado": " The module allows you to interact with the operating system, such as manipulating files, directories, obtaining information about the system, etc",
            "uso": "It is useful for performing low-level operations on the system, such as browsing directories or deleting files"
        }
    },
    "p": {
        "parseInt": {
            "ejemplo": "parseInt(\"10\");  // 10",
            "significado": "Convert a string to an integer",
            "uso": "Used to convert text strings representing numbers to integer values"
        },
        "pathlib": {
            "ejemplo": "from pathlib import Path\n            route = Path(\"my_directory/my_file.txt\")\n            if route.exists():\n            print(f\"The file {route} exist.\")\n            else:\n            print(f\"The file {route} no exist.\")\n            Path(\"new_directory\").mkdir(parents=True, exist_ok=True)\n            content = route.read_text()\n            print(content)",
            "significado": "Pathlib is a module that facilitates the handling of file and directory paths in a more readable and modern way",
            "uso": "It is used to handle paths more easily and to perform file operations efficiently"
        },
        "pop": {
            "ejemplo": "fruits = [\"apple\", \"banana\", \"orange\", \"pear\"]\n            ultima_fruta = fruits.pop()\n            print(\"Deleted last fruit:\", last_fruit)  # Output: pera\n            print(\"list later of pop:\", fruits)  # Output: ['apple', 'banana', 'orange']",
            "significado": "Deletes and returns an item from a list in a specific index",
            "uso": "To remove a specific value from a list"
        }
    },
    "q": {},
    "r": {
        "range": {
            "ejemplo": "for i in range(5):\n            print(i)",
            "significado": "Returns a sequence of numbers, ussualy in loops.",
            "uso": "To create a range of numbers that can be iterated"
        },
        "reduce()": {
            "ejemplo": "from functools import reduce\n            numbers = [1, 2, 3, 4]\n            results = reduce(lambda x, y: x + y, numbers)\n            print(resuls)  # 10",
            "significado": "The reduce() function applies a cumulative function to the elements of an iterable, reducing it to a single value",
            "uso": "It is used to perform cumulative operations, such as adding or multiplying all the items in a list"
        },
        "return": {
            "ejemplo": "def multiplicate(a, b):\n            return a * b\n            result = multiplicate(3, 4)",
            "significado": "Value that a function returns to the person who invokes it",
            "uso": "Get the result of executing a function"
        },
        "reversed": {
            "ejemplo": "reversed([1, 2, 3])  # [3, 2, 1]",
            "significado": "Return the iterable invested",
            "uso": "Serves to reverse the order of the elements of an iterable"
        }
    },
    "s": {
        " shutil": {
            "ejemplo": "pimport shutil\n            shutil.copy(\"origin.txt\", \"destiny.txt\")\n            shutil.move(\"origin.txt\", \"new_directory/origin.txt\")\n            shutil.remove(\"destiny.txt\")",
            "significado": " Shutil is a module that provides a way to copy, move, or delete files and directories",
            "uso": "Used for high-level operations with files and directories, such as copying a file or moving an entire directory"
        },
        "sorted": {
            "ejemplo": "list = [4, 1, 3, 2]\n            print(sorted(list))  # [1, 2, 3, 4]",
            "significado": "Returns a new list with the items of an iterable sorted",
            "uso": "Sort a list or tuple in ascending or descending order"
        },
        "split": {
            "ejemplo": "text = \"Hello word Python\"\n        words = text.split()\n        print(words)",
            "significado": "Divides a string into a list of substrings.",
            "uso": " It is the first parameter of any instance method of a class"
        },
        "str": {
            "ejemplo": " # number\n        number = 123\n        number_like_str = str(number)\n        print(type(number_like_str))  # Output: <class 'str'>\n        print(number_like_str)        # Output: '123",
            "significado": "make a value into a text chain",
            "uso": " to make a value like a text"
        },
        "sum": {
            "ejemplo": "sum([1, 2, 3])  # 6",
            "significado": "Returns the sum of the elements of an iterable",
            "uso": "Add up items in a list or tuple"
        },
        "super() ": {
            "ejemplo": "class Animal:\n            def speak(self):\n            return \"The animal make a sound\"\n            class dog(Animal):\n            def speak(self):\n            return super().speak() + \" and the dog barks.\"\n            my_dog = dog()\n            print(my_dog.speak())  # The animal make a sound. and the dog barks.",
            "significado": "Using super() allows you to call a base class method from a derived class",
            "uso": "Used when a child class needs to extend or modify the behavior of a method of the base class"
        }
    },
    "t": {
        "type": {
            "ejemplo": "type(10)  # <class 'int'>",
            "significado": "Returns the type of an object",
            "uso": "It is used to verify the type of a variable"
        }
    },
    "u": {},
    "v": {},
    "w": {
        "with": {
            "ejemplo": "try:\n            with open(\"file.txt\", \"r\") as file:\n            content = file.read()\n            print(content)\n            except FileNotFoundError:\n            print(\"the file not exist\")",
            "significado": "Used to handle resources such as files, databases, network connections, etc., efficiently",
            "uso": " Ensures that resources are closed correctly, even if an exception occurs"
        }
    },
    "x": {},
    "y": {},
    "z": {
        "zip": {
            "ejemplo": "zip([1, 2], [\"a\", \"b\"])  # [(1, \"a\"), (2, \"b\")]",
            "significado": "Join multiple iterables into a single tuple sequence",
            "uso": "Combine lists or tuples so that their items are paired"
        }
    }
}