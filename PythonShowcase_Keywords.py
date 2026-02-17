### Python Showcase Keyword Methods ###
print("Beginning of the Python Keywords Showcase\n\n\n")


And_def = "And: The and keyword is a logical operator. Logical operators are used to combine conditional statements. The return value will only be True if both statements return True, otherwise it will return False."
And_x = (5 > 3 and 5 < 10)
print(f"\n{And_def}")
print("    And_x = (5 > 3 and 5 < 10)")
print(f"        print(And_x) = {And_x}")




As_def = "As: The as keyword is used to create an alias. In the example above, we create an alias, c, when importing the calendar module, and now we can refer to the calendar module by using c instead of calendar."
import calendar as As_c
print(f"\n{As_def}")
print("    import calendar as As_c")
print(f"        print(As_c.month_name[1]) = {As_c.month_name[1]}")




Assert_def = "Assert: The assert keyword is used when debugging code. The assert keyword lets you test if a condition in your code returns True, if not, the program will raise an AssertionError. You can write a message to be written if the code returns False, check the example below."
Assert_x = 'welcome'
#if condition returns False, AssertionError is raised:
# assert Assert_x != 'welcome', 'x should not be welcome'
print(f"\n{Assert_def}")
print("    Assert_x = 'welcome'")
print("    #if condition returns False, AssertionError is raised:")
print("    assert Assert_x != 'welcome', 'x should not be welcome'")
print("        Traceback (most recent call last):\n            File 'demo_ref_keyword_assert2.py', line 4, in <module>\n            assert x !='welcome', 'x should not be 'welcome''\n            AssertionError: x should not be 'welcome'")
# print(f"        print() = {BLANK}")



Async_def = "Async: The async keyword declares a function as asynchronous (a coroutine), allowing use of await inside it. Asynchronous functions run within an event loop (for example using asyncio.run())."
import asyncio
async def Async_greet():
  return '                                          Hello'
async def Async_main():
  msg = await Async_greet()
  print(msg)
print(f"\n{Async_def}")
print("    import asyncio")
print("    async def Async_greet():")
print("        return 'Hello'")
print("    async def Async_main():")
print("        msg = await Async_greet()")
print("        print(msg)")
print(f"    print(asyncio.run(Async_main())) = ")
asyncio.run(Async_main())




Await_def = "Await: The await keyword pauses execution in an async function until the awaited object (coroutine / awaitable) returns a result. await can only be used inside functions declared with async."
import asyncio
async def Await_greet():
  return '                                  Hi'
async def Await_main():
  msg = await Await_greet()
  print(msg)

print(f"\n{Await_def}")
print("    import asyncio")
print("    async def Await_greet():")
print("        return 'Hi'")
print("    async def Await_main():")
print("        msg = await Await_greet()")
print("        print(msg)")
print("    asyncio.run(Await_main()) = ")
asyncio.run(Await_main())




Break_def = "Break: The break keyword is used to break out a for loop, or a while loop."
print(f"\n{Break_def}")
print("    for Break_i in range(9):")
print("        if Break_i > 3:")
print("            break")
print("        print(Break_i)")
print("=")
for Break_i in range(9):
  if Break_i > 3:
    break
  print(Break_i)





Case_def = "Case: The case keyword is used in combination with the match keyword to define a pattern to match against a subject value. When a case pattern matches, the corresponding block of code is executed. The first matching case wins. match/case is Python's structural pattern matching feature, introduced in Python 3.10."
print(f"\n{Case_def}")
print("    Case_command = 'start'")
print("    match Case_command:")
print("        case 'start':")
print("            print('Starting...')")
print("        case 'stop':")
print("            print('Stopping...')")
print("        case _:")
print("            print('Unknown command')")
print("    =")
Case_command = 'start'
match Case_command:
  case 'start':
    print('Starting...')
  case 'stop':
    print('Stopping...')
  case _:
    print('Unknown command')




Class_def = "Class: The class keyword is used to create a class. A class is like an object constructor. See the example below to see how we can use it to create an object."
class Class_Person:
  name = 'John'
  age = 36
print(f"\n{Class_def}")
print("    class Class_Person:")
print("        name = 'John'")
print("        age = 36")
print(f"        print(Class_Person.name) = {Class_Person.name}")




Continue_def = "Continue: The continue keyword is used to end the current iteration in a for loop (or a while loop), and continues to the next iteration."
print(f"\n{Continue_def}")
print("    for Continue_i in range(9):")
print("        if Continue_i == 3:")
print("            continue")
print("        print(Continue_i)")
print("=")
for Continue_i in range(9):
  if Continue_i == 3:
    continue
  print(Continue_i)




Define_def = "Define: The def keyword is used to create, (or define) a function."
def Define_my_function():
 print('                              Hello from a function')
print(f"\n{Define_def}")
print("    def Define_my_function():")
print("        print('Hello from a function')")
print(f"        print(Define_my_function()) = ")
Define_my_function()




Delete_def = "Delete: The del keyword is used to delete objects. In Python everything is an object, so the del keyword can also be used to delete variables, lists, or parts of a list etc."
Del_x = ['apple', 'banana', 'cherry']
del Del_x[0]
print(f"\n{Delete_def}")
print("    Del_x = ['apple', 'banana', 'cherry']")
print("    del Del_x[0]")
print(f"        print(Del_x) = {Del_x}")




Elif_def = "Elif: The elif keyword is used in conditional statements (if statements), and is short for else if."
print(f"\n{Elif_def}")
print("    for Elif_i in range(-5, 5):")
print("        if Elif_i > 0:")
print("            print('YES')")
print("        elif Elif_i == 0:")
print("            print('WHATEVER')")
print("        else:")
print("            print('NO')")
print("=")
for Elif_i in range(-5, 5):
  if Elif_i > 0:
    print('YES')
  elif Elif_i == 0:
    print('WHATEVER')
  else:
    print('NO')




Else_def = "Else: The else keyword is used in conditional statements (if statements), and decides what to do if the condition is False. The else keyword can also be use in try...except blocks."
print(f"\n{Else_def}")
print("    Else_x = 2")
print("    if Else_x > 3:")
print("        print('YES')")
print("    else:")
print("        print('NO')")
print("=")
Else_x = 2
if Else_x > 3:
  print('YES')
else:
  print('NO')



Except_def = "Except: The except keyword is used in try...except blocks. It defines a block of code to run if the try block raises an error. You can define different blocks for different error types, and blocks to execute if nothing went wrong."
print(f"\n{Except_def}")
print("    # (x > 3) will raise an error because x is not defined:")
print("    try:")
print("        Except_x > 3")
print("    except:")
print("        print('Something went wrong')")
print("    print('Even if it raised an error, the program keeps running')")
# # (x > 3) will raise an error because x is not defined:
# try:
#   Except_x > 3
# except:
#   print('Something went wrong')
# print('Even if it raised an error, the program keeps running')
print("=")
print("Something went wrong     Even if it raised an error, the program keeps running")



False_def = "False: The False keyword is a Boolean value, and result of a comparison operation. The False keyword is the same as 0 (True is the same as 1)."
print(f"\n{False_def}")
print(f"    print(print(5 > 6)) ")
print("=")
print(5 > 6)




Finally_def = "Finally: The finally keyword is used in try...except blocks. It defines a block of code to run when the try...except...else block is final. The finally block will be executed no matter if the try block raises an error or not. This can be useful to close objects and clean up resources."

print(f"\n{Finally_def}")
print("    try:")
print("        Finally_x > 3")
print("    except:")
print("        print('Something went wrong')")
print("    else:")
print("        print('Nothing went wrong')")
print("    finally:")
print("        print('The try...except block is finished')")
print("=")
try:
  Finally_x > 3
except:
  print('Something went wrong')
else:
  print('Nothing went wrong')
finally:
  print('The try...except block is finished')




For_def = "For: The for keyword is used to create a for loop. It can be used to iterate through a sequence, like a list, tuple, etc."
print(f"\n{For_def}")
print("    for For_x in range(1, 9):")
print("        print(For_x)")
print("=")
for For_x in range(1, 9):
  print(For_x)





From_def = "From: The from keyword is used to import only a specified section from a module."
from datetime import time
From_x = time(hour=15)
print(f"\n{From_def}")
print("    from datetime import time")
print("    From_x = time(hour=15)")
print(f"    print(From_x) = {From_x}")





Global_def = "Global: The global keyword is used to create global variables from a no-global scope, e.g. inside a function."
def Global_myfunction():
  global Global_x
  Global_x = 'hello'
Global_myfunction()
print(f"\n{Global_def}")
print("    def Global_myfunction():")
print("        global Global_x")
print("        Global_x = 'hello'")
print("    Global_myfunction()")
print("    #Global_x should now be global, and accessible in the global scope.")
print(f"        print() = {Global_x}")




If_def = "If: The if keyword is used to create conditional statements (if statements), and allows you to execute a block of code only if a condition is True. Use the else keyword to execute code if the condition is False."
print(f"\n{If_def}")
print("    If_x = 5")
print("    if If_x > 3:")
print("        print('YES')")
print("=")
If_x = 5
if If_x > 3:
  print('YES')




Import_def = "Import: The import keyword is used to import modules."
import datetime
Import_x = datetime.datetime.now()
print(f"\n{Import_def}")
print("    import datetime")
print("    Import_x = datetime.datetime.now()")
print(f"        print(Import_x) = {Import_x}")




In_def = "In: The in keyword has two purposes: The in keyword is used to check if a value is present in a sequence (list, range, string etc.). The in keyword is also used to iterate through a sequence in a for loop:"
print(f"\n{In_def}")
print("    In_fruits = ['apple', 'banana', 'cherry']")
print("    if 'banana' in In_fruits:")
print("        print('yes')")
print("=")
In_fruits = ['apple', 'banana', 'cherry']
if 'banana' in In_fruits:
  print('yes')




Is_def = "Is: The is keyword is used to test if two variables refer to the same object. The test returns True if the two objects are the same object. The test returns False if they are not the same object, even if the two objects are 100% equal. Use the == operator to test if two variables are equal."
Is_x = ['apple', 'banana', 'cherry']
Is_y = ['apple', 'banana', 'cherry']
print(f"\n{Is_def}")
print("    Is_x = ['apple', 'banana', 'cherry']")
print("    Is_y = ['apple', 'banana', 'cherry']")
print(f"        print(Is_x is Is_y) = {Is_x is Is_y}")




Lambda_def = "Lambda: The lambda keyword is used to create small anonymous functions. A lambda function can take any number of arguments, but can only have one expression. The expression is evaluated and the result is returned."
Lambda_x = lambda a : a + 10
print(Lambda_x(5))
print(f"\n{Lambda_def}")
print("    Lambda_x = lambda a : a + 10")
print(f"        print(Lambda_x(5)) = {Lambda_x(5)}")




Match_def = "Match: The match keyword starts a structural pattern matching statement, introduced in Python 3.10. It compares a subject value against one or more case patterns and executes the first matching case's block.    You can use:    Literal patterns (numbers, strings).   OR-patterns with |.   Wildcard _ to match anything (default case).   Guards with if for extra conditions.  Sequence, mapping, and class patterns (advanced)"
print(f"\n{Match_def}")
print("    Match_role = 'editor'")
print("    match Match_role:")
print("        case 'admin':")
print("            print('Full access')")
print("        case 'editor':")
print("            print('Edit content')")
print("        case 'viewer':")
print("            print('Read-only')")
print("=")
Match_role = 'editor'
match Match_role:
  case 'admin':
    print('Full access')
  case 'editor':
    print('Edit content')
  case 'viewer':
    print('Read-only')



None_def = "None: The None keyword is used to define a null value, or no value at all. None is not the same as 0, False, or an empty string. None is a data type of its own (NoneType) and only None can be None."
None_x = None
print(f"\n{None_def}")
print("    None_x = None")
print(f"        print(None_x) = {None_x}")




Nonlocal_def = "Nonlocal: The nonlocal keyword is used to work with variables inside nested functions, where the variable should not belong to the inner function. Use the keyword nonlocal to declare that the variable is not local."
def Nonlocal_myfunc1():
  Nonlocal_x = 'John'
  def Nonlocal_myfunc2():
    nonlocal Nonlocal_x
    Nonlocal_x = 'hello'
  Nonlocal_myfunc2()
  return Nonlocal_x
print(f"\n{Nonlocal_def}")
print("    def Nonlocal_myfunc1():")
print("        Nonlocal_x = 'John'")
print("        def Nonlocal_myfunc2():")
print("            nonlocal Nonlocal_x")
print("            Nonlocal_x = 'hello'")
print("        Nonlocal_myfunc2() ")
print("        return Nonlocal_x")
print(f"        print(Nonlocal_myfunc1()) = {Nonlocal_myfunc1()}")




Not_def = "Not: The not keyword is a logical operator. The return value will be True if the statement(s) are not True, otherwise it will return False."
Not_x = False
print(f"\n{Not_def}")
print("    Not_x = False")
print(f"        print(not Not_x) = {not Not_x}")




Or_def = "Or: The or keyword is a logical operator. Logical operators are used to combine conditional statements. The return value will be True if one of the statements return True, otherwise it will return False."
Or_x = (5 > 3 or 5 > 10)
print(f"\n{Or_def}")
print("    Or_x = (5 > 3 or 5 > 10)")
print(f"        print(Or_x) = {Or_x}")




Pass_def = "Pass: The pass statement is used as a placeholder for future code. When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed. Empty code is not allowed in loops, function definitions, class definitions, or in if statements."
for Pass_x in [0, 1, 2]:
  pass
print(f"\n{Pass_def}")
print("    for Pass_x in [0, 1, 2]:")
print("        pass")
# print("=")




Raise_def = "Raise: The raise keyword is used to raise an exception. You can define what kind of error to raise, and the text to print to the user."
# Raise_x = -1
# if Raise_x < 0:
#   raise Exception('Sorry, no numbers below zero')
print(f"\n{Raise_def}")
print("    Raise_x = -1")
print("    if Raise_x < 0:")
print("        raise Exception('Sorry, no numbers below zero')")
print("=")
print("    Traceback (most recent call last):\n       File 'demo_ref_keyword_raise.py', line 4, in <module>\n       raise Exception('Sorry, no numbers below zero')\n       Exception: Sorry, no numbers below zero")




Return_def = "Return: The return keyword is to exit a function and return a value."
def Return_myfunction():
  return 3+3
  # code inside the function, but after the return line will not be executed
  print('Hello, World!')
print(f"\n{Return_def}")
print("    def Return_myfunction():")
print("        return 3+3")
print("        # code inside the function, but after the return line will not be executed")
print("        print('Hello, World!')")
print(f"        print(Return_myfunction())) = {Return_myfunction()}")




True_def = "True: The True keyword is a Boolean value, and result of a comparison operation. The True keyword is the same as 1 (False is the same as 0)."
print(f"\n{True_def}")
print(f"        print(7 > 6) = {7 > 6}")




Try_def = "Try: The try keyword is used in try...except blocks. It defines a block of code test if it contains any errors. You can define different blocks for different error types, and blocks to execute if nothing went wrong, see examples belo"
print(f"\n{Try_def}")
print("    try:")
print("        Try_x > 3")
print("    except:")
print("        print('Something went wrong')")
print("=")
try:
  Try_x > 3
except:
  print('Something went wrong')
print('Even if it raised an error, the program keeps running')





While_def = "While: The while keyword is used to create a while loop. A while loop will continue until the statement is false."
print(f"\n{While_def}")
print("    While_x = 0")
print("    while While_x < 9:")
print("        print(While_x)")
print("        While_x = While_x + 1")
print("=")
While_x = 0
while While_x < 9:
  print(While_x)
  While_x = While_x + 1






With_def = "With: The with keyword wraps a block of code using a context manager. It ensures setup and cleanup logic (__enter__ / __exit__) happen automatically, simplifying resource management and exce"
print(f"\n{With_def}")
print("    import contextlib")
print("    with contextlib.nullcontext('resource') as With_r:")
print("        print('Using', With_r)")
print("=")
import contextlib
with contextlib.nullcontext('resource') as With_r:
  print('Using', With_r)





Yield_def = "Yield: The yield keyword turns a function into a function generator. The function generator returns an iterator. The code inside the function is not executed when they are first called, but are divided into steps, one step for each yield, and each step is only executed when iterated upon. Unlike the return keyword which stops further execution of the function, the yield keyword returns the result so far, and continues to the next step. The return value will be a list of values, one item for each yield. "
print(f"\n{Yield_def}")
print("    def Yield_myFunc():")
print("        yield 'Hello'")
print("        yield 51")
print("        yield 'Good Bye'")
print("    Yield_x = Yield_myFunc()")
print("    for Yield_z in Yield_x:")
print("        print(Yield_z)")
print("=")
def Yield_myFunc():
  yield 'Hello'
  yield 51
  yield 'Good Bye'
Yield_x = Yield_myFunc()
for Yield_z in Yield_x:
  print(Yield_z)




print("\n\n\nEnd of the Python Keyword Showcase")