# Python100 days class end showcase project



ABC = "abc"
NUMBER = 0







# Section 1 - Built in functions

Absolute_value_def = "Absolute Value: returns the absolute value of a number.  abs().  "
# abs()
print(f"{Absolute_value_def},\n      abs(49.3) = {abs(49.3)}")


All_def = "All_def: Returns True if all items in an iterable object are true.  all().  "
# all()
mylist_ALL = [True, True, True]
print(f"{All_def},\n      mylist_ALL = [True, True, True]   all(mylist_ALL) = {all(mylist_ALL)}")

Any_def = "ANY: Returns True if any item in an iterable object is true"
mylist_ANY = [False, True, False]
# any()
print(f"{Any_def},\n      mylist_ANY = [False, True, False]   any(mylist_ANY) = {any(mylist_ANY)}")

Ascii_def = "ASCII: Returns a readable version of an object. Replaces none-ascii characters with escape character replaces foreign to English characters"
# ascii()
print(f"{Ascii_def},\n      ascii('My name is Ståle') = {ascii('My name is Ståle')}")

Binary_converter_def = "Binary Converter: Returns the binary version of a number. The result will always have the prefix 0b"
# bin()
print(f"{Binary_converter_def},\n      bin(37) = {bin(37)}")

Boolean_Checker_def = "Boolean Checker: Returns the boolean version of a specified object."
# bool()
print(f"{Boolean_Checker_def}{bool(1)},\n      bool(0) = {bool(0)}")


Byte_Array_converter_def = "Byte Array Converter: Returns an array of bytes"
# bytearray()
print(f"{Byte_Array_converter_def},\n      bytearray(4) = {bytearray(4)}")

Bytes_Converter_def = "Bytes Converter: Converts objects into bytes objects, or create empty bytes object of the specified size. The difference between bytes() and bytearray() is that bytes() returns an object that cannot be modified, and bytearray() returns an object that can be modified."
# bytes()
print(f"{Bytes_Converter_def},\n      bytes(4) = {bytes(4)}")

Callable_def = "Callable_def: The callable() function returns True if the specified object is callable, otherwise it returns False. Functions are callable vs Variables that are not"
# callable()
def callable_function_example():
    a = 5
callable_example_2 = 5
print(f"{Callable_def},\n      function def callable_function_example(): a = 5    = {callable(callable_function_example)}")
print(f"      callable_example_2 = 5      = {callable(callable_example_2)}")

Character_Unicoder_def = "Character Unicoder: The chr() function returns the character that represents the specified unicode"
# chr()
print(f"{Character_Unicoder_def},\n      chr(67) = {chr(67)}")
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


print(ClassMethod_Converter_def)
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



Compile_def = "Compile_def: The compile() function returns the specified source as a code object, ready to be executed."
# compile()
Compile_Example = compile('print(55)', 'test', 'eval')

print(f"{Compile_def},\n      compile('print(55)', 'test', 'eval') = ")
exec(Compile_Example)

# complex()
# print(f"{},\n      {}")
#
# delattr()
# print(f"{},\n      {}")
#
# dict()
# print(f"{},\n      {}")
#
# dir()
# print(f"{},\n      {}")
#
# divmod()
# print(f"{},\n      {}")
#
# enumerate()
# print(f"{},\n      {}")
#
# eval()
# print(f"{},\n      {}")
#
# exec()
# print(f"{},\n      {}")
#
# filter()
# print(f"{},\n      {}")
#
# float()
# print(f"{},\n      {}")
#
# format()
# print(f"{},\n      {}")
#
# frozenset()
# print(f"{},\n      {}")
#
# getattr()
# print(f"{},\n      {}")
#
# globals()
# print(f"{},\n      {}")
#
# hasattr()
# print(f"{},\n      {}")
#
# hash()
# print(f"{},\n      {}")
#
# help()
# print(f"{},\n      {}")
#
# hex()
# print(f"{},\n      {}")
#
# id()
# print(f"{},\n      {}")
#
# input()
# print(f"{},\n      {}")
#
# int()
# print(f"{},\n      {}")
#
# isinstance()
# print(f"{},\n      {}")
#
# issubclass()
# print(f"{},\n      {}")
#
# iter()
# print(f"{},\n      {}")
#
# len()
# print(f"{},\n      {}")
#
# list()
# print(f"{},\n      {}")
#
# locals()
# print(f"{},\n      {}")
#
# map()
# print(f"{},\n      {}")
#
# max()
# print(f"{},\n      {}")
#
# memoryview()
# print(f"{},\n      {}")
#
# min()
# print(f"{},\n      {}")
#
# next()
# print(f"{},\n      {}")
#
# object()
# print(f"{},\n      {}")
#
# oct()
# print(f"{},\n      {}")
#
# open()
# print(f"{},\n      {}")
#
# ord()
# print(f"{},\n      {}")
#
# pow()
# print(f"{},\n      {}")
#
# print()
# print(f"{},\n      {}")
#
# property()
# print(f"{},\n      {}")
#
# range()
# print(f"{},\n      {}")
#
# repr()
# print(f"{},\n      {}")
#
# reversed()
# print(f"{},\n      {}")
#
# round()
# print(f"{},\n      {}")
#
# set()
# print(f"{},\n      {}")
#
# setattr()
# print(f"{},\n      {}")
#
# slice()
# print(f"{},\n      {}")
#
# sorted()
# print(f"{},\n      {}")
#
# staticmethod()
# print(f"{},\n      {}")
#
# str()
# print(f"{},\n      {}")
#
# sum()
# print(f"{},\n      {}")
#
# super()
# print(f"{},\n      {}")
#
# tuple()
# print(f"{},\n      {}")
#
# type()
# print(f"{},\n      {}")
#
# vars()
# print(f"{},\n      {}")
#
# zip()
# print(f"{},\n      {}")
#
#
#
