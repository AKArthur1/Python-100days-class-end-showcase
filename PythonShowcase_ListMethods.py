### Python Showcase List Methods ###
print("Beginning of the Python List Methods Showcase\n\n\n")


Append_def = "Append: The append() method appends an element to the end of the list"
Append_fruits = ['apple', 'banana', 'cherry']
Append_fruits.append('orange')
print(f"\n{Append_def}"
      f"\n    Append_fruits = ['apple', 'banana', 'cherry']"
      f"\n        print(Append_fruits.append('orange')) = {Append_fruits.append('orange')}")




Clear_def = "Clear: The clear() method removes all the elements from a list"
Clear_fruits = ['apple', 'banana', 'cherry', 'orange']
Clear_fruits.clear()
print(f"\n{Clear_def}"
      f"\n    Clear_fruits = ['apple', 'banana', 'cherry', 'orange']"
      f"\n    Clear_fruits.clear()"
      f"\n        print(Clear_fruits) = {Clear_fruits}")



Copy_def = "Copy: The copy() method returns a copy of the specified list."
Copy_fruits = ['apple', 'banana', 'cherry', 'orange']
Copy_fruits_v2 = Copy_fruits.copy()
print(f"\n{Copy_def}"
      f"\n    Copy_fruits = ['apple', 'banana', 'cherry', 'orange']"
      f"\n    Copy_fruits_v2 = Copy_fruits.copy()"
      f"\n        print(Copy_fruits_v2) = {Copy_fruits_v2}")



Count_def = "Count: The count() method returns the number of elements with the specified value."
Count_fruits = ['apple', 'banana', 'cherry']
Count_x = Count_fruits.count('cherry')
print(f"\n{Count_def}"
      f"\n    Count_fruits = ['apple', 'banana', 'cherry']"
      f"\n    Count_x = Count_fruits.count('cherry')"
      f"\n        print(Count_x) = {Count_x}")



Extend_def = "Extend: The extend() method adds the specified list elements (or any iterable) to the end of the current list."
Extend_fruits = ['apple', 'banana', 'cherry']
Extend_cars = ['Ford', 'BMW', 'Volvo']
Extend_fruits.extend(Extend_cars)
print(f"\n{Extend_def}"
      f"\n    Extend_fruits = ['apple', 'banana', 'cherry']"
      f"\n    Extend_cars = ['Ford', 'BMW', 'Volvo']"
      f"\n    Extend_fruits.extend(Extend_cars)"
      f"\n        print(Extend_fruits) = {Extend_fruits}")



Index_def = "Index: The index() method returns the position at the first occurrence of the specified value. "
Index_fruits = ['apple', 'banana', 'cherry']
print(f"\n{Index_def}"
      f"\n    Index_fruits = ['apple', 'banana', 'cherry']"
      f"\n        print(Index_fruits.index('cherry')) = {Index_fruits.index('cherry')}")



Insert_def = "Insert: The insert() method inserts the specified value at the specified position."
Insert_fruits = ['apple', 'banana', 'cherry']
Insert_fruits.insert(1, 'orange')
print(f"\n{Insert_def}"
      f"\n    Insert_fruits = ['apple', 'banana', 'cherry']"
      f"\n    Insert_fruits.insert(1, 'orange')"
      f"\n        print(Insert_fruits) = {Insert_fruits}")



Pop_def = "Pop: The pop() method removes the element at the specified position."
Pop_fruits = ['apple', 'banana', 'cherry']
Pop_fruits.pop(1)
print(f"\n{Pop_def}"
      f"\n    Pop_fruits = ['apple', 'banana', 'cherry']"
      f"\n    Pop_fruits.pop(1)"
      f"\n        print(Pop_fruits) = {Pop_fruits}")



Remove_def = "Remove: The remove() method removes the first occurance of the element with the specified value."
Remove_fruits = ['apple', 'banana', 'cherry']
Remove_fruits.remove('banana')
print(f"\n{Remove_def}"
      f"\n    Remove_fruits = ['apple', 'banana', 'cherry']"
      f"\n    Remove_fruits.remove('banana')"
      f"\n        print(Remove_fruits) = {Remove_fruits}")



Reverse_def = "Reverse: The reverse() method reverses the sorting order of the elements."
Reverse_fruits = ['apple', 'banana', 'cherry']
Reverse_fruits.reverse()
print(f"\n{Reverse_def}"
      f"\n    Reverse_fruits = ['apple', 'banana', 'cherry']"
      f"\n    Reverse_fruits.reverse()"
      f"\n        print(Reverse_fruits) = {Reverse_fruits}")




Sort_def = "Sort: The sort() method sorts the list ascending by defaulft. You can also make a function to decide the sorting criteria. # A function that returns the length of the value"
def Sort_myFunc(Sort_e):
  return len(Sort_e)
Sort_cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
Sort_cars.sort(reverse=True, key=Sort_myFunc)
print(f"\n{Sort_def}"
      f"\n    def Sort_myFunc(Sort_e):"
      f"\n        return len(Sort_e)"
      f"\n    Sort_cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']"
      f"\n    Sort_cars.sort(reverse=True, key=Sort_myFunc)"
      f"\n        print(Sort_cars) = {Sort_cars}")




print("\n\n\nEnd of the Python List Methods Showcase")