# Python100 days class end showcase project



ABC = "abc"
NUMBER = 0







# Section 1 - Built in functions

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
print("     Will take over the Run window")
print(f"help() = {help()}\n      help(print) = {help(print)}")

# hex()
# print(f"\n{},\n      {}")
#
# id()
# print(f"\n{},\n      {}")
#
# input()
# print(f"\n{},\n      {}")
#
# int()
# print(f"\n{},\n      {}")
#
# isinstance()
# print(f"\n{},\n      {}")
#
# issubclass()
# print(f"\n{},\n      {}")
#
# iter()
# print(f"\n{},\n      {}")
#
# len()
# print(f"\n{},\n      {}")
#
# list()
# print(f"\n{},\n      {}")
#
# locals()
# print(f"\n{},\n      {}")
#
# map()
# print(f"\n{},\n      {}")
#
# max()
# print(f"\n{},\n      {}")
#
# memoryview()
# print(f"\n{},\n      {}")
#
# min()
# print(f"\n{},\n      {}")
#
# next()
# print(f"\n{},\n      {}")
#
# object()
# print(f"\n{},\n      {}")
#
# oct()
# print(f"\n{},\n      {}")
#
# open()
# print(f"\n{},\n      {}")
#
# ord()
# print(f"\n{},\n      {}")
#
# pow()
# print(f"\n{},\n      {}")
#
# print()
# print(f"\n{},\n      {}")
#
# property()
# print(f"\n{},\n      {}")
#
# range()
# print(f"\n{},\n      {}")
#
# repr()
# print(f"\n{},\n      {}")
#
# reversed()
# print(f"\n{},\n      {}")
#
# round()
# print(f"\n{},\n      {}")
#
# set()
# print(f"\n{},\n      {}")
#
# setattr()
# print(f"\n{},\n      {}")
#
# slice()
# print(f"\n{},\n      {}")
#
# sorted()
# print(f"\n{},\n      {}")
#
# staticmethod()
# print(f"\n{},\n      {}")
#
# str()
# print(f"\n{},\n      {}")
#
# sum()
# print(f"\n{},\n      {}")
#
# super()
# print(f"\n{},\n      {}")
#
# tuple()
# print(f"\n{},\n      {}")
#
# type()
# print(f"\n{},\n      {}")
#
# vars()
# print(f"\n{},\n      {}")
#
# zip()
# print(f"\n{},\n      {}")
#
#
#
