#vicho
diccionario_eng = {
    "a": {
        "any": {
            "significado": ": Returns True if at least one of the elements in an iterable is true",
            "uso": "Verify if a condition is a true iterable",
            "ejemplo": '''values = [0, False, 2]
            print(any(values))  # True'''
        },
        "abs": {
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
    },
    "b": {
        "break": {
            "significado":"End a loop early",
            "uso": "to manually exit a loop",
            "ejemplo":'''while True:
            number = int(input("enter a number (enter a 0 for exit): "))
            if number == 0:
            break  # exit from the bucle if the user write 0
            print(f"the number entered is {number}")'''
        },
    },
    "c": {
        "_constains_": {
            "significado": "Defines how to check if one object contains another (for the in operator)",
            "uso": "Customize the behavior of the in operator when used with an object of a user-defined class",
            "ejemplo": '''class Box:
            def __init__(self, elements):
            self.elements = elements
            def __contains__(self, item):
            return item in self.elements
            box = Box([1, 2, 3])
            print(2 in box)  # True'''
        },
        "count": {
            "significado":"Returns the number of times an item appears in a list or string",
            "uso": "Count occurrences of a value in a collection",
            "ejemplo": '''list = [1, 2, 2, 3, 2, 4]
            print(list.count(2))  # 3'''
        },
        "clear": {
            "significado":" Delete all from a list or dictionary",
            "uso": "Empty the contents of a collection",
            "ejemplo": '''list = [1, 2, 3]
            list.clear()
            print(list)  # []'''
        },
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
        },
    "g": {
        # Aquí puedes agregar funciones que comiencen con la letra G
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
    },
    "m": {
        "max": {
            "significado": "Returns the largest value of an iterable",
            "usage": "find the max value",
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
    },
    "p": {
        "pop": {
            "significado":"Deletes and returns an item from a list in a specific index",
            "uso": "To remove a specific value from a list",
            "ejemplo": '''fruits = ["apple", "banana", "orange", "pear"]
            ultima_fruta = fruits.pop()
            print("Deleted last fruit:", last_fruit)  # exit: pera
            print("list later of pop:", fruits)  # exit: ['apple', 'banana', 'orange']'''
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
        }
    },
    "s": {
        "str": {
        "significado": "make a value into a text chain",
        "uso": " to make a value like a text",
        "ejemplo":''' # number
        number = 123
        number_like_str = str(number)
        print(type(number_like_str))  # exit: <class 'str'>
        print(number_like_str)        # exit: '123'''
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

