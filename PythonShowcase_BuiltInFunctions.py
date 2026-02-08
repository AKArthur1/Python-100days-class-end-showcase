### Python Showcase Built in Functions ###
print("Beginning of the Python Built in Functions Showcase\n\n\n")


Absolute_value_def = "Absolute Value: returns the absolute value of a number.  abs().  "
# abs()
print(f"\n{Absolute_value_def},\n      abs(49.3) = {abs(49.3)}")




All_def = "All_def: Returns True if all items in an iterable object are true.  all().  "
# all()
mylist_ALL = [True, True, True]
print(f"\n{All_def},\n      mylist_ALL = [True, True, True]   all(mylist_ALL) = {all(mylist_ALL)}")



Any_def = "ANY: Returns True if any item in an iterable object is true"
mylist_ANY = [False, True, False]
# any()
print(f"\n{Any_def},\n      mylist_ANY = [False, True, False]   any(mylist_ANY) = {any(mylist_ANY)}")



Ascii_def = "ASCII: Returns a readable version of an object. Replaces none-ascii characters with escape character replaces foreign to English characters"
# ascii()
print(f"\n{Ascii_def},\n      ascii('My name is Ståle') = {ascii('My name is Ståle')}")



Binary_converter_def = "Binary Converter: Returns the binary version of a number. The result will always have the prefix 0b"
# bin()
print(f"\n{Binary_converter_def},\n      bin(37) = {bin(37)}")



Boolean_Checker_def = "Boolean Checker: Returns the boolean version of a specified object."
# bool()
print(f"\n{Boolean_Checker_def}{bool(1)},\n      bool(0) = {bool(0)}")



Byte_Array_converter_def = "Byte Array Converter: Returns an array of bytes"
# bytearray()
print(f"\n{Byte_Array_converter_def},\n      bytearray(4) = {bytearray(4)}")



Bytes_Converter_def = "Bytes Converter: Converts objects into bytes objects, or create empty bytes object of the specified size. The difference between bytes() and bytearray() is that bytes() returns an object that cannot be modified, and bytearray() returns an object that can be modified."
# bytes()
print(f"\n{Bytes_Converter_def},\n      bytes(4) = {bytes(4)}")



Callable_def = "Callable_def: The callable() function returns True if the specified object is callable, otherwise it returns False. Functions are callable vs Variables that are not"
# callable()
def callable_function_example():
    a = 5
callable_example_2 = 5
print(f"\n{Callable_def},\n      function def callable_function_example(): a = 5    = {callable(callable_function_example)}")
print(f"      callable_example_2 = 5      = {callable(callable_example_2)}")



Character_Unicoder_def = "Character Unicoder: The chr() function returns the character that represents the specified unicode"
# chr()
print(f"\n{Character_Unicoder_def},\n      chr(67) = {chr(67)}")
print(f"      chr(167) = {chr(167)}")



ClassMethod_Converter_def = "Class Method converter: The built-in classmethod() function is a decorator that transforms a method into a class method. A class method receives the class itself as its first argument, enabling it to access or modify class-level data rather than instance data. This functionality is particularly useful for creating multiple constructors, which allow for different ways to instantiate the class:"
# classmethod()
class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def margherita(cls):
        return cls(["mozzarella", "tomatoes"])

    @classmethod
    def prosciutto(cls):
        return cls(["mozzarella", "tomatoes", "ham"])

    def __str__(self):
        return f"Pizza with {' and '.join(self.ingredients)}"

# print(
#     Pizza.margherita()
# )  # Output: Pizza with mozzarella and tomatoes
# print(
#     Pizza.prosciutto()
# )  # Output: Pizza with mozzarella and tomatoes and ham


print(f"\n{ClassMethod_Converter_def}")
print("      class Pizza:\n"
    "           def __init__(self, ingredients):\n"
        "               self.ingredients = ingredients\n"

    "           @classmethod\n"
    "           def margherita(cls):\n"
        "               return cls(['mozzarella', 'tomatoes'])\n"

    "           @classmethod\n"
    "           def prosciutto(cls):\n"
        "               return cls(['mozzarella', 'tomatoes', 'ham'])\n"

    "           def __str__(self):\n"
        "               return f'Pizza with {' and '.join(self.ingredients)}'\n"

"       print(Pizza.margherita())  # Output: Pizza with mozzarella and tomatoes\n"
"       print(Pizza.prosciutto())  # Output: Pizza with mozzarella and tomatoes and ham\n")





Compile_def = "Compile: The compile() function returns the specified source as a code object, ready to be executed."
# compile()
Compile_Example = compile('print(55)', 'test', 'eval')

print(f"\n{Compile_def},\n      compile('print(55)', 'test', 'eval') = ")
exec(Compile_Example)




Complex_def = "Complex: The complex() function returns a complex number by specifying a real number and an imaginary number."
# complex()
print(f"\n{Complex_def},\n      complex(3, 4) = {complex(3, 4)}")



Delete_Attribute_def = "Delete Attribute: The delattr() function will delete the specified attribute from the specified object."
# delattr()
class Person:
  name = "John"
  age = 36
  country = "Norway"
print(f"\n{Delete_Attribute_def},\n      class Person:\n        name = 'John'\n        age = 36\n        country = 'Norway'\n   delattr(Person, 'age')\n      {delattr(Person, 'age')}\n      {print(Person, 'age')}")



Dictionary_Converter_def = "Dictionary Convert: The dict() function creates a dictionary"
# dict()
print(f"\n{Dictionary_Converter_def},\n      dict(name = 'John', age = 36, country = 'Norway') = {dict(name = "John", age = 36, country = "Norway")}")



Dir_def = "Dir(): The dir() function returns all properties and methods of the specified object, without the values."
# dir()
class Person:
  name = "John"
  age = 36
  country = "Norway"
print(f"\n{Dir_def},\n      class Person:\n        name = 'John'\n        age = 36\n        country = 'Norway'\n   dir(Person)\n      {dir(Person)}")



Divided_Quotient_def = "Divided_Quotient: The divmod() function returns a tuple containing the quotient and the remainder when argument1 (dividend) is divided by argument2 (divisor)."
# divmod()
print(f"\n{Divided_Quotient_def},\n      divmod(5, 2) = {divmod(5, 2)}")



Enumerate_def = "Enumerate: The enumerate() function takes a collection/tuple and returns it as an enumerate object. It adds a counter as the key of the enumerate object."
# enumerate()
Enumerate_x = ('apple', 'banana', 'cherry')
Enumerate_y = enumerate(Enumerate_x)
print(f"\n{Enumerate_def},\n      Enumerate_x = ('apple', 'banana', 'cherry')\n      Enumerate_y = enumerate(Enumerate_x)\n          list(Enumerate_y) = {list(Enumerate_y)}")



Evaluation_def = "Evaluation:  The eval() function evaluates the specified expression, if the expression is a legal Python statement, it will be executed."
# eval()
Evaluation_x = 'print(55)'
print(f"\n{Evaluation_def}")
eval(Evaluation_x)



Execution_def = "Execution: The exec() function executes the specified Python code. It accepts large blocks of code, unlike the eval() function which only accepts a single expression."
# exec()
Execution_x = 'name = "John"\nprint(name)'
print(f"\n{Execution_def}")
exec(Execution_x)



Filter_def = "Filter: The filter() function returns an iterator where the items are filtered through a function to test if the item is accepted or not. "
# filter()
def Filter_starts_a(w):
    return w.startswith("a")

li = ["apple", "banana", "avocado", "cherry", "apricot"]
res = filter(Filter_starts_a, li)

print(f"\n{Filter_def},\n      def Filter_starts_a(w):\n                 return w.startswith('a')\n      li = ['apple', 'banana', 'avocado', 'cherry', 'apricot']\n      res = filter(Filter_starts_a, li)\n               = {list(res)}")



Float_convert_def = "Float: The float() function converts the specified value into a floating point number. It can be a number or a string."
# float()
print(f"\n{Float_convert_def},\n      float(3) = {float(3)}\n      float('3.500') = {float('3.500')}")



Format_def = "Format: The format() function formats a specified value into a specified format. Reference the Format list to see the many available formatting codes."
# format()
print(f"\n{Format_def},\n      format(0.5, '%') = {format(0.5, '%')}\n      format(255, 'x') = {format(255, 'x')}\n      format(1234567890, ',') = {format(1234567890, ',')}")



FrozenSet_def = "Frozen Set: The frozenset() function returns an unchangeable frozenset object (which is like a set object, only unchangeable)"
# frozenset()
Frozen_mylist = ['apple', 'banana', 'cherry']
print(f"\n{FrozenSet_def},\n      Frozen_mylist = ['apple', 'banana', 'cherry']\n           frozenset(Frozen_mylist) = {frozenset(Frozen_mylist)}")



Get_Attribute_def = "Get Attribute: The getattr() function returns the value of the specified attribute from the specified object. A 3rd parameter can be added as a message to display if this does not exist"
# getattr()
class Person:
  name = "John"
  age = 36
  country = "Norway"
print(f"\n{Get_Attribute_def},\n      class Person:\n        name = 'John'\n        age = 36\n        country = 'Norway'\n             getattr(Person, 'age') = {getattr(Person, 'age')}\n             getattr(Person, 'weight', 'THIS DOES NOT EXIST') = {getattr(Person, 'weight', 'THIS DOES NOT EXIST')}")



Globals_def = "Globals: The globals() function returns the global symbol table as a dictionary. A symbol table contains necessary information about the current program."
# globals()
print(f"\n{Globals_def},\n      globals() = {globals()}")



Has_Attribute_def = "Has Attribute: the hasattr() function returns True if the specified object has the specified attribute, otherwise False."
# hasattr()
class Person:
  name = "John"
  age = 36
  country = "Norway"
print(f"\n{Has_Attribute_def},\n      class Person:\n        name = 'John'\n        age = 36\n        country = 'Norway'\n             hasattr(Person, 'age') = {hasattr(Person, 'age')}")



Hash_def = "Hash: The hash() function in Python returns an integer hash value for an object"
# hash()
print(f"\n{Hash_def},\n      hash(10) = {hash(10)}\n      hash('python') = {hash('python')}")



Help_def = "Help: help() function in Python is a built-in function that provides information about modules, classes and functions. "
# help()

print(f"\n{Help_def})")
print("     ***Will take over the Run window***")
# print(f"help() = {help()}\n      help(print) = {help(print)}")



Hex_def = "Hex: The hex() function converts the specified number into a hexadecimal value. The return string always starts with the prefix 0x."
# hex()
print(f"\n{Hex_def},\n      hex(255) = {hex(255)}")



ID_def = "Id: The id() function returns a unique id for the specified object. The id is assigned to an object when it's created. It will be different everytime the program is run."
# id()
ID_x = ('apple', 'banana', 'cherry')

print(f"\n{ID_def},\n      ID_x = ('apple', 'banana', 'cherry')\n            id(ID_x) = {id(ID_x)}")



Input_def = "Input: The input() function allows user input"
# input()
# print("Enter your name:")
# Input_x = input()
# print("Hello, " + Input_x)
print(f"\n{Input_def},\n      print('Enter your name:')\n      Input_x = input()\n      print('Hello, ' + Input_x)\n            ***Output is __Hello Agyei__***")



Integer_def = "Integer: The int() function converts the specified Value into an integer number"
# int()
print(f"\n{Integer_def},\n      int(3.5) = {int(3.5)}\n      int('12') = {int('12')}")



Is_Instance_def = "Is Instance: The isinstance() function returns True if the specified object is of the specified type, otherwise False. If the type parameter is a tuple, this function will return True if the object is one of the types in the tuple."
# isinstance()
print(f"\n{Is_Instance_def},\n      isinstance(5, int) = {isinstance(5, int)}\n      isinstance('Hello', (float, int, str, list, dict, tuple)) = {isinstance('Hello', (float, int, str, list, dict, tuple))}\n      isinstance(68, str) = {isinstance(68, str)}")



Is_Subclass_def = "Is Subclass: The issubclass() function returns True if the specified object is a subclass of the specified object, otherwise False."
# issubclass()
class IsSubclass_myAge:
    age = 36
class IsSubclass_myObj(IsSubclass_myAge):
    name = "John"
    age = IsSubclass_myAge
class IsSubclass_myObj_2():
    name = "John"
    age = IsSubclass_myAge
print(f"\n{Is_Subclass_def},\n    class IsSubclass_myAge:\n        age = 36\n    class IsSubclass_myObj(IsSubclass_myAge):\n        name = 'John'\n        age = IsSubclass_myAge\n    class IsSubclass_myObj_2():\n        name = 'John'\n        age = IsSubclass_myAge\n             issubclass(IsSubclass_myObj, IsSubclass_myAge) = {issubclass(IsSubclass_myObj, IsSubclass_myAge)}\n             issubclass(IsSubclass_myObj_2, IsSubclass_myAge) = {issubclass(IsSubclass_myObj_2, IsSubclass_myAge)}")



Iterator_def = "Iterator: The iter() function returns an iterator object. Cannot go beyond the bounds of the list"
# iter()
Iterator_x = iter(["apple", "banana", "cherry"])
print(f"\n{Iterator_def},\n      Iterator_x = iter(['apple', 'banana', 'cherry'])\n           print(f'next(Iterator_x), next(Iterator_x), next(Iterator_x)') = {next(Iterator_x)}, {next(Iterator_x)}, {next(Iterator_x)}")



Length_def = "Length: The len() function returns the number of items in an object. When the object is a string, the len() function returns the number of the characters in the string."
# len()
Length_mylist = ["apple", "banana", "cherry"]
print(f"\n{Length_def},\n    Length_mylist = ['apple', 'banana', 'cherry']\n        len(Length_mylist) = {len(Length_mylist)}")




List_def = "List: The list() function creates a list object."
# list()
print(f"\n{List_def},\n      list(('apple', 'banana', 'cherry')) = {list(('apple', 'banana', 'cherry'))}")




Locals_def = "Locals: The locals() function returns the local symbol table as a dictionary."
# locals()
print(f"\n{Locals_def},\n      {locals()}")




Map_def = "Map: The map() function executes a specified function for each item in an iterable. The item is sent to the function as a papameter."
# map()
def Map_myfunc(n):
  return len(n)
Map_x = map(Map_myfunc, ('apple', 'banana', 'cherry'))
print(f"\n{Map_def},\n    def Map_myfunc(n):\n        return len(n)\n    Map_x = map(Map_myfunc, ('apple', 'banana', 'cherry'))\n    list(Map_x) = {list(Map_x)}")




Max_def = "Max: The max() function returns the item with the highest value, or the item with the highest value in an iterable. If the values are strings, an alphabetically comparison is done."
# max()
Max_a = (1, 5, 3, 9)
print(f"\n{Max_def},\n    max(5, 10) = {max(5, 10)}\n    max('Mike', 'John', 'Vicky') = {max('Mike', 'John', 'Vicky')}\n    Max_a = (1, 5, 3, 9)\n        max(Max_a) = {max(Max_a)}")




MemoryView_def = "Memory View: The memoryview() function returns a memory view object from a specified object."
# memoryview()
MemoryView_x = memoryview(b'Hello')
print(f"\n{MemoryView_def},\n    MemoryView_x = memoryview(b'Hello') = {MemoryView_x}\n    MemoryView_x[0] = {MemoryView_x[0]}\n    MemoryView_x[1] = {MemoryView_x[1]}")




Minimum_def = "Minimum: The min() function returns the item with the lowest value, or the item with the lowest value in an iterable. if the values are strings, an alphabetically comparison is done."
# min()
Minimum_a = (1, 5, 3, 9)
print(f"\n{Minimum_def},\n    min(5, 10) = {min(5, 10)}\n    min('Mike', 'John', 'Vicky') = {min('Mike', 'John', 'Vicky')}\n    Minimum_a = (1, 5, 3, 9)\n        min(Minimum_a) = {min(Minimum_a)}")




Next_def = "Next: The next() function returns the next item in an iterator. You can add a default return value, to return if the iterator has reached to it's end"
# next()
Next_mylist = iter(["apple", "banana", "cherry"])
print(f"\n{Next_def},\n    Next_mylist = iter(['apple', 'banana', 'cherry'])\n           print(f'next(Next_mylist), next(Next_mylist), next(Next_mylist)') = {next(Next_mylist)}, {next(Next_mylist)}, {next(Next_mylist)}")




Object_def = "Object: The object() function returns an empty object. You cannot add new properties or methods to this object. It is the base for all classes. "
# object()
Object_x = object()
print(f"\n{Object_def},\n     Object_x = object()\n     dir(Object_x) = {dir(Object_x)}")




Octal_convert_def = "Octal: The oct() function converts an integer into an octal string. Octal strings in Python are prefixed with 0o "
# oct()
print(f"\n{Octal_convert_def},\n      oct(12) = {oct(12)}")




Open_def = "Open: The open() function opens a file, and returns it as a file object. The Modes are 'r'-Read, 'a'-Append, 'w'-Write, 'x'-Create "
# open()
print(f"\n{Open_def},\n      *** This will open a file when run ***\n                  f = open('demofile.txt', 'r')\n                  print(f.read())")




Ord_def = "Ord: The ord() function returns the number representing the unicode code of a specified character."
# ord()
print(f"\n{Ord_def},\n    ord('h') = {ord('h')}\n    ord('y') = {ord('y')}")




PowerOf_def = "Power of: The pow() function returns the value of x to the power of y (x^y). If a third parameter is present, it returns x to the power of y, modulus z."
# pow()
print(f"\n{PowerOf_def},\n    pow(4, 3) = {pow(4, 3)}\n    pow(4, 3, 5) = {pow(4, 3, 5)}")




Print_def = "Print: The print() function prints the specified message to the screen, or other standard output device."
# print()
print(f"\n{Print_def},\n    print('Hello World') = Hello World")




Property_def = "Property: The property() function returns an object of the property class. It allows developers to create properties within a class, providing a way to control access to an attribute by defining getter, setter and deleter methods. This enhances encapsulation and ensures better control over class attributes."
# property()
class Property_Student:
    def __init__(self, name):
        self._name = name

    Property_name = property(lambda self: self._name)

Property_s = Property_Student("shakshi")
# print(s.Property_name)
print(f"\n{Property_def},\n    class Property_Student:\n        def __init__(self, name):\n            self._name = name\n        Property_name = property(lambda self: self._name)\n    Property_s = Property_Student('shakshi')\n    Property_s.Property_name = {Property_s.Property_name}")




Range_def = "Range: The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number."
# range()
Range_x = range(3, 20, 2)
Range_list = []
for Range_n in Range_x:
  Range_list.append(Range_n)
print(f"\n{Range_def},\n    Range_x = range(3, 20, 2)\n    Range_list = []\n    for Range_n in Range_x:\n        Range_list.append(Range_n)\n    print(Range_list) = {Range_list}")




Represent_def = "Represent: The repr() function returns a string representation of an object that can be used to recreate the object when passed to eval().It is mainly used for debugging and logging because it provides an unambiguous representation of an object. To understand more clearly, think of repr() as a blueprint for an object, while str() is a user-friendly description of it. Let's take an example: "
# repr()
Represent_text = "Hello\nWorld"
print(f"\n{Represent_def},\n    Represent_text = 'Hello***backslash N***World'\n        str(Represent_text) = {str(Represent_text)}\n        repr(Represent_text) = {repr(Represent_text)}")




Reversed_def = "Reversed: The reversed() function returns a reversed iterator object."
# reversed()
Reversed_alph = ["a", "b", "c", "d"]
Reversed_final_list = []
Reversed_ralph = reversed(Reversed_alph)
for Reversed_x in Reversed_ralph:
  Reversed_final_list.append(Reversed_x)
print(f"\n{Reversed_def},\n    Reversed_alph = ['a', 'b', 'c', 'd']\n    Reversed_final_list = []\n    Reversed_ralph = reversed(Reversed_alph)\n    for Reversed_x in Reversed_ralph:\n        Reversed_final_list.append(Reversed_x)\n    print(Reversed_final_list) = {Reversed_final_list}")




Round_def = "Round: The round() function returns a floating point number that is a rounded version of the specified number, with the specified number of decimals. "
# round()
print(f"\n{Round_def},\n    print(round(5.76543, 2)) = {round(5.76543, 2)}")




Set_Object_def = "Set Object: The set() function creates a set object. The items in a set list are unordered, so it will appear in random order. "
# set()
print(f"\n{Set_Object_def},\n      print(set(('apple', 'banana', 'cherry'))) = {set(('apple', 'banana', 'cherry'))}")




Set_Attribute_def = "SetAttribute: The setattr() function sets the value of the specified attribute of the specified object."
# setattr()
class Person:
  name = "John"
  age = 36
  country = "Norway"
setattr(Person, 'age', 40)
print(f"\n{Set_Attribute_def},\n    class Person:\n        name = 'John'\n        age = 36\n        country = 'Norway'\n    setattr(Person, 'age', 40)\n    print(getattr(Person, 'age')) = {getattr(Person, 'age')}")




Slice_def = "Slice: The slice() functino returns a slice object. You can specify where to begin and end the slicing. The step value is the third parameter."
# slice()
Slice_a = ("a", "b", "c", "d", "e", "f", "g", "h")
Slice_x = slice(0, 8, 3)
print(f"\n{Slice_def},\n    Slice_a = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')\n    Slice_x = slice(0, 8, 3)\n      print(Slice_a[Slice_x]) = {Slice_a[Slice_x]}")




Sorted_def = "Sorted: The sorted() function returns a sorted list of the specified iterable object. You can specify ascending or descending order. Strings are sorted alphabetically, and numbers are sorted numerically. You cannot sort a list that contains BOTH string values AND numeric values."
# sorted()
Sorted_a = ('b', 'g', 'a', 'd', 'f', 'c', 'h', 'e')
Sorted_x = sorted(Sorted_a)
print(f"\n{Sorted_def},\n    Sorted_a = ('b', 'g', 'a', 'd', 'f', 'c', 'h', 'e')\n    Sorted_x = sorted(Sorted_a)\n    print(Sorted_x) = {Sorted_x}")




StaticMethod_def = "Static Method: a method defined inside a class that does not depend on any instance or class data. It is used when a function logically belongs to a class but does not need access to self or cls. Static methods help organize related utility functions inside a class without creating objects."
# staticmethod()
class Person:
    @staticmethod
    def is_adult(age):
        return age >= 18
print(f"\n{StaticMethod_def},\n    class Person:\n        @staticmethod\n        def is_adult(age):\n            return age >= 18\n    print(Person.is_adult(16)) = {Person.is_adult(16)}\n    print(Person.is_adult(21)) = {Person.is_adult(21)}")




String_def = "String: The str() function converts the specified value into a string."
# str()
print(f"\n{String_def},\n    print(str(3.5)) = {str(3.5)}")




Sum_def = "Sum: The sum() function returns a numbers, the sum of all items in an iterable."
# sum()
Sum_a = (1, 2, 3, 4, 5)
print(f"\n{Sum_def},\n    Sum_a = (1, 2, 3, 4, 5)\n        print(sum(Sum_a)) = {sum(Sum_a)}\n        print(sum(Sum_a, 7)) = {sum(Sum_a, 7)}")



Super_def = "Super: The super() function is to give access to methods and properties of a parent or sibling class. Returns an object that represents the parent class."
# super()
class Parent:
  def __init__(self, txt):
    self.message = txt
  def printmessage(self):
    print(self.message)
class Child(Parent):
  def __init__(self, txt):
    super().__init__(txt)
x = Child('Hello, and welcome!')
print(f"\n{Super_def},\n    class Parent:\n        def __init__(self, txt):\n            self.message = txt\n        def printmessage(self):\n            print(self.message)\n    class Child(Parent):\n        def __init__(self, txt):\n            super().__init__(txt)\n    x = Child('Hello, and welcome!')")
print("print(x.printmessage()) =")
x.printmessage()




Tuple_def = "Tuple: The tuple() function creates a tuple object. Tuples are immutable"
# tuple()
Tuple_x = tuple(('apple', 'banana', 'cherry'))
print(f"\n{Tuple_def},\n    print(Tuple_x) = {Tuple_x}")



Type_def = "Type: The type() function returns the type of the specified object. "
# type()
Type_a = ('apple', 'banana', 'cherry')
Type_b = 'Hello World'
Type_c = 33
print(f"\n{Type_def},\n    Type_a = ('apple', 'banana', 'cherry')\n    Type_b = 'Hello World'\n    Type_c = 33\n    print(type(Type_a)) = {type(Type_a)}\n    print(type(Type_b)) = {type(Type_b)}\n    print(type(Type_c)) = {type(Type_c)}")




Vars_def = "Vars: The vars() function returns the __dict__ attribute of an object. The __dict__ attribute is a dictionary containing the object's changeable attributes."
# vars()
class Person:
  name = "John"
  age = 36
  country = "Norway"
print(f"\n{Vars_def},\n    class Person:\n        name = 'John'\n        age = 36\n        country = 'Norway'\n    print(vars(Person)) = {vars(Person)}")




Zip_def = "Zip: The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc. If the passed iterables have different lengths, the iterable with the least items decides the length of the new iterator. use the tuple() function to display a readable version of the result"
# zip()
Zip_a = ('John', 'Charles', 'Mike')
Zip_b = ('Jenny', 'Christy', 'Monica', 'Vicky')
Zip_x = zip(Zip_a, Zip_b)
print(f"\n{Zip_def},\n    Zip_a = ('John', 'Charles', 'Mike')\n    Zip_b = ('Jenny', 'Christy', 'Monica', 'Vicky')\n    Zip_x = zip(Zip_a, Zip_b)\n    print(tuple(Zip_x)) = {tuple(Zip_x)}")




print("\n\nEnd of the Python Built in Functions Showcase")