### Python Showcase Dictionary Methods ###
# print("Beginning of the Python Dictionary Methods Showcase\n\n\n")




Clear_def = "Clear: The clear() method removes all the elements from a dictionary."
Clear_car = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
Clear_car.clear()
print(f"\n{Clear_def}")
print("    Clear_car = {\n        'brand': 'Ford',\n        'model': 'Mustang',\n        'year': 1964}")
print(f"    Clear_car.clear()"
      f"\n        print(Clear_car) = {Clear_car}")




Copy_def = "Copy: The copy() method returns a copy of a specified dictionary."
Copy_car = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
Copy_x = Copy_car.copy()
print(f"\n{Copy_def}")
print("    Copy_car = {\n        'brand': 'Ford',\n        'model': 'Mustang',\n        'year': 1964}")
print(f"    Copy_x = Copy_car.copy()"
      f"\n        print(Copy_x) = {Copy_x}")





FromKeys_def = "From keys: The fromkeys() method returns a dictionary with the specified keys and the specified value."
FromKeys_x = ('key1', 'key2', 'key3')
FromKeys_y = 0
FromKeys_thisdict = dict.fromkeys(FromKeys_x, FromKeys_y)
print(f"\n{FromKeys_def}"
      f"\n    FromKeys_x = ('key1', 'key2', 'key3')"
      f"\n    FromKeys_y = 0"
      f"\n    FromKeys_thisdict = dict.fromkeys(FromKeys_x, FromKeys_y)"
      f"\n        print(FromKeys_thisdict) = {FromKeys_thisdict}")




Get_def = "The get() method returns the value of the item with the specified key."
Get_car = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
Get_x = Get_car.get('price', 15000)
print(f"\n{Get_def}")
print("    Get_car = {\n"
      "        'brand': 'Ford',\n"
      "        'model': 'Mustang',\n"
      "        'year': 1964\n"
      "}")
print(f"    Get_x = Get_car.get('price', 15000)"
      f"\n        print(Get_x) = {Get_x}")




Items_def = "Items: The items() method returns a view object. The view object contains the key-value pairs of the dictionary, as tuples in a list. The view object will reflect any changes done to the dictionary."
Items_car = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}

Items_x = Items_car.items()

Items_car['year'] = 2018
print(f"\n{Items_def}")
print("    Items_car = {\n"
      "        'brand': 'Ford',\n"
      "        'model': 'Mustang',\n"
      "        'year': 1964\n"
      "}")
print("    Items_car['year'] = 2018"
      f"\n        print(Items_x) = {Items_x}")




Keys_def = "Keys: The keys() method returns a view object. The view object contains the keys of the dictionary, as a list. The view object will reflect any changes done to the dictionary. When an item is added in the dictionary, the view object also gets updated."
Keys_car = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
Keys_x = Keys_car.keys()
Keys_car['color'] = 'white'
print(f"\n{Keys_def}")
print("    Keys_car = {"
      "\n        'brand': 'Ford',"
      "\n        'model': 'Mustang',"
      "\n        'year': 1964"
      "\n}")
print(f"\n    Keys_x = Keys_car.keys()"
      f"\n    Keys_car['color'] = 'white'"
      f"\n        print(Keys_x) = {Keys_x}")







Pop_def = "Pop: The pop() method removes the specified item from the dictionary. The value of the removed item is the return value of the pop() method."
Pop_car = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
Pop_car.pop('model')
print(f"\n{Pop_def}")
print("    Pop_car = {"
      "\n        'brand': 'Ford',"
      "\n        'model': 'Mustang',"
      "\n        'year': 1964"
      "\n}")
print(f"\n    Pop_car.pop('model')"
      f"\n        print(Pop_car) = {Pop_car}")







# DEF = ""
#
# print(f"\n{DEF}"
#       f"\n    BLANK"
#       f"\n        print() = {BLANK}")







# DEF = ""
#
# print(f"\n{DEF}"
#       f"\n    BLANK"
#       f"\n        print() = {BLANK}")







# DEF = ""
#
# print(f"\n{DEF}"
#       f"\n    BLANK"
#       f"\n        print() = {BLANK}")







# DEF = ""
#
# print(f"\n{DEF}"
#       f"\n    BLANK"
#       f"\n        print() = {BLANK}")





# print("\n\n\nEnd of the Python Dictionary Methods Showcase")