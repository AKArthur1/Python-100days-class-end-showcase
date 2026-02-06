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

# enumerate()
# print(f"\n{},\n      {}")
#
# eval()
# print(f"\n{},\n      {}")
#
# exec()
# print(f"\n{},\n      {}")
#
# filter()
# print(f"\n{},\n      {}")
#
# float()
# print(f"\n{},\n      {}")
#
# format()
# print(f"\n{},\n      {}")
#
# frozenset()
# print(f"\n{},\n      {}")
#
# getattr()
# print(f"\n{},\n      {}")
#
# globals()
# print(f"\n{},\n      {}")
#
# hasattr()
# print(f"\n{},\n      {}")
#
# hash()
# print(f"\n{},\n      {}")
#
# help()
# print(f"\n{},\n      {}")
#
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
