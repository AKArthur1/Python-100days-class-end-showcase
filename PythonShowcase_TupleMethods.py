### Python Showcase Tuple Methods ###
print("Beginning of the Python Tuple Methods Showcase\n\n\n")


Count_def = "Count: The count() method returns the number of times a specified value appears in the tuple."
Count_thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
Count_x = Count_thistuple.count(5)
print(f"\n{Count_def}"
      f"\n    Count_thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)"
      f"\n    Count_x = Count_thistuple.count(5)"
      f"\n        print(Count_x) = {Count_x}")




Index_def = "Index: The index() method finds the first occurrence of the specified value. Raises an exception if the value is not found."
Index_thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
Index_x = Index_thistuple.index(8)
print(f"\n{Index_def}"
      f"\n    Index_thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)"
      f"\n    Index_x = Index_thistuple.index(8)"
      f"\n        print(Index_x) = {Index_x}")


print("\n\n\nEnd of the Python Tuple Methods Showcase")