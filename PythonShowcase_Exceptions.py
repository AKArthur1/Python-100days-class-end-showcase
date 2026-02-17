### Python Showcase Exceptions Methods ###
print("Beginning of the Python Exceptions Methods Showcase\n\n\n")


ArithmeticError_def = "ArithmeticError Exception: The ArithmeticError exception is the base exception for the three arithmetic error excpetions:    FloatingPointError.   OverflowError.   ZeroDivisionError     You can handle the ArithmeticError in a try...except statement,"
print(f"\n{ArithmeticError_def}")
print("    try:")
print("        print(10 / 0)")
print("    except ArithmeticError:")
print("        print('Error in calculation')")
print("    except:")
print("        print('Something else went wrong')")
print("=")
try:
  print(10 / 0)
except ArithmeticError:
  print('Error in calculation')
except:
  print('Something else went wrong')



AssertionError_def = "Assertion Error: The AssertionError exception occurs when an assert statement fails. You can handle the AssertionError in a try...except statement. "
print(f"\n{AssertionError_def}")
print("    AssertionError_x = 'hello'")
print("    try:")
print("        assert AssertionError_x == 'goodbye'")
print("    except AssertionError:")
print("        print('Error in assert statement')")
print("    except:")
print("        print('Something else went wrong')")
print("=")
AssertionError_x = 'hello'
try:
  assert AssertionError_x == 'goodbye'
except AssertionError:
  print('Error in assert statement')
except:
  print('Something else went wrong')



AttributeError_def = "Attribute Error: The AttributeError exception occurs when you try to execute a property or method that does not exist on the current object. You can handle the AttributeError in a try...except statement."

print(f"\n{AttributeError_def}")
print("    AttributeError_x = 'Hello'")
print("    try:")
print("        print(AttributeError_x.toUpperCase())")
print("    except AttributeError:")
print("        print('Opps! Strings do not have a toUpperCase method!')")
print("    except:")
print("        print('Something else went wrong')")
print("=")
AttributeError_x = 'Hello'
try:
  print(AttributeError_x.toUpperCase())
except AttributeError:
  print('Opps! Strings do not have a toUpperCase method!')
except:
  print('Something else went wrong')



ImportError_def = "Import Error: The ImportError exception occurs when you try to import a non-existing part of a module."
print(f"\n{ImportError_def}")
print("    from numpy import somethingstrange")
print("=")
print("    Traceback (most recent call last):\n            File './prog.py', line 1, in <module>\n            ImportError: cannot import name 'somethingstrange' from 'numpy' (/usr/local/lib/python3.12/dist-packages/numpy/__init__.py)")



IndentationError_def = "Indentation Error: The IndentationError exception occurs when indentitation is missing, or is wrong. You have to use the same number of spaces in the same block of code, otherwise you get an IndentationError."
print(f"\n{IndentationError_def}")
print("    if 5 > 2:")
print("        print('Five is greater than two!')")
print("         print('Makes sence!')")
print("=")
print("    File './prog.py', line 3, in < module >\n        print('Makes sence!')\n        IndentationError: unexpected indent")
# if 5 > 2:
#   print('Five is greater than two!')
#    print('Makes sence!')




IndexError_def = "Index Error: The IndexError exception occurs when you use an index on a sequence, like a list or a tuple, and the index is out of range. You can handle the IndexError in a try...except statement."
print(f"\n{IndexError_def}")
print("    IndexError_x = ['apple', 'banana', 'cherry']")
print("    try:")
print("        print(IndexError_x[5])")
print("    except IndexError:")
print("        print('You are trying to access a item that does not exist!')")
print("    except:")
print("        print('Something else went wrong')")
print("=")
IndexError_x = ['apple', 'banana', 'cherry']
try:
  print(IndexError_x[5])
except IndexError:
  print('You are trying to access a item that does not exist!')
except:
  print('Something else went wrong')





KeyError_def = "Key Error: The KeyError exception occurs when you use a key on a dictionary, and the key does not exist. You can handle the KeyError in a try...except statement."
print(f"\n{KeyError_def}")
print("    KeyError_fruit = {'name': 'apple', 'color': 'red'}")
print("    try:")
print("        print(KeyError_fruit['price'])")
print("    except KeyError:")
print("        print('You are trying to access a dictionary item that does not exist!')")
print("    except:")
print("        print('Something else went wrong')")
print("=")
KeyError_fruit = {'name': 'apple', 'color': 'red'}
try:
  print(KeyError_fruit['price'])
except KeyError:
  print('You are trying to access a dictionary item that does not exist!')
except:
  print('Something else went wrong')



NameError_def = "Name Error: The NameError exception occurs if you use a variable that is not defined. You can handle the NameError in a try...except statement."
print(f"\n{NameError_def}")
print("    try:")
print("        print(NameError_x)")
print("    except NameError:")
print("        print('Variable NameError_x is not defined')")
print("    except:")
print("        print('Something else went wrong')")
print("=")
try:
  print(NameError_x)
except NameError:
  print('Variable NameError_x is not defined')
except:
  print('Something else went wrong')




OverflowError_def = "Overflow Error: The OverflowError exception occurs when the result of a numeric calculation is too large. The OverflowError exception is one of three ArithmeticError You can handle the OverflowError in a try...except statement."
print(f"\n{OverflowError_def}")
print("    import math")
print("    try:")
print("        print(math.exp(999))")
print("    except OverflowError:")
print("        print('The number is too high')")
print("    except:")
print("        print('Something else went wrong')")
print("=")
import math
try:
  print(math.exp(999))
except OverflowError:
  print('The number is too high')
except:
  print('Something else went wrong')




TypeError_def = "Type Error: The TypeError exception occurs if an operation tries to perform an action with an unexpected data type. You can handle the TypeError in a try...except statement."
print(f"\n{TypeError_def}")
print("    try:")
print("        TypeError_x = 'hello' + 15")
print("    except TypeError:")
print("        print('Please convert to string before concatenate')")
print("    except:")
print("        print('Something else went wrong')")
print("=")
try:
  TypeError_x = 'hello' + 15
except TypeError:
  print('Please convert to string before concatenate')
except:
  print('Something else went wrong')




ValueError_def = "Value Error: The ValueError exception occurs if a function receives a value of wrong type. You can handle the ValueError in a try...except statement,"
print(f"\n{ValueError_def}")
print("    try:")
print("        ValueError_x = float('hello')")
print("    except ValueError:")
print("        print('The value has wrong format')")
print("    except:")
print("        BLANK")
print("=")
try:
  ValueError_x = float('hello')
except ValueError:
  print('The value has wrong format')
except:
  print('Something else went wrong')




ZeroDivisionError_def = "Zero Division Error: The ZeroDivisionError exception occurs when you try to devide a number with 0, and when you perform a modulo operation with 0. The ZeroDivisionError exception is one of three ArithmeticError You can handle the ZeroDivisionError in a try...except statement"

print(f"\n{ZeroDivisionError_def}")
print("    try:")
print("        print(10 / 0)")
print("    except ZeroDivisionError:")
print("        print('Error in calculation')")
print("    except:")
print("        print('Something else went wrong')")
print("=")
try:
  print(10 / 0)
except ZeroDivisionError:
  print('Error in calculation')
except:
  print('Something else went wrong')




print("\n\n\nEnd of the Python Exceptions Methods Showcase")

