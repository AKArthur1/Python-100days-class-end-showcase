### Python Showcase Set Methods ###
print("Beginning of the Python Set Methods Showcase\n\n\n")




Add_ref = "Add: The add() method adds an element to the set. If the element already exists, the add() method does not add the element."
Add_fruits = {'apple', 'banana', 'cherry'}
Add_fruits.add('apple')
print(f"\n{Add_ref}")
print("    Add_fruits = {'apple', 'banana', 'cherry'}")
print("    Add_fruits.add('apple')")
print(f"        print(Add_fruits) = {Add_fruits}")




Clear_def = "Clear: The clear() method removes all elements in a set."
Clear_fruits = {'apple', 'banana', 'cherry'}
Clear_fruits.clear()
print(f"\n{Clear_def}")
print("    Clear_fruits = {'apple', 'banana', 'cherry'}")
print("    Clear_fruits.clear()")
print(f"        print(Clear_fruits) = {Clear_fruits}")




Copy_def = "Copy: The copy() method copies the set."
Copy_fruits = {'apple', 'banana', 'cherry'}
Copy_fruits_v2 = Copy_fruits.copy()
print(f"\n{Copy_def}")
print("    Copy_fruits = {'apple', 'banana', 'cherry'}")
print("    Copy_fruits_v2 = Copy_fruits.copy()")
print(f"        print(Copy_fruits_v2) = {Copy_fruits_v2}")




Difference_def = "Difference: The difference() method returns a set that contains the difference between two sets. Meaning: The returned set contains items that exist only in the first set, and not in both sets. As a shortcut, you can use the - operator instead, see example below."
Difference_x = {'apple', 'banana', 'cherry'}
Difference_y = {'google', 'microsoft', 'apple'}
Difference_z = Difference_x.difference(Difference_y)
print(f"\n{Difference_def}")
print("    Difference_x = {'apple', 'banana', 'cherry'}")
print("    Difference_y = {'google', 'microsoft', 'apple'}")
print("    Difference_z = Difference_x.difference(Difference_y)")
print(f"        print(Difference_z) = {Difference_z}")




DifferenceUpdate_def = "DifferenceUpdate: The difference_update() method removes the items that exist in both sets. It is different from the difference() method, because the difference() method returns a newset, without the unwanted items, and the difference_update() method removes the unwanted items from the original set. As a shortcut you can use the, -=, operator instead."
DifferenceUpdate_a = {'apple', 'banana', 'cherry'}
DifferenceUpdate_b = {'google', 'microsoft', 'apple'}
DifferenceUpdate_c = {'cherry', 'micra', 'bluebird'}
DifferenceUpdate_d = {'pink', 'black', 'orange'}
DifferenceUpdate_a.difference_update(DifferenceUpdate_b, DifferenceUpdate_c, DifferenceUpdate_d)
print(f"\n{DifferenceUpdate_def}")
print("    DifferenceUpdate_a = {'apple', 'banana', 'cherry'}")
print("    DifferenceUpdate_b = {'google', 'microsoft', 'apple'}")
print("    DifferenceUpdate_c = {'cherry', 'micra', 'bluebird'}")
print("    DifferenceUpdate_d = {'pink', 'black', 'orange'}")
print("    DifferenceUpdate_a.difference_update(DifferenceUpdate_b, DifferenceUpdate_c, DifferenceUpdate_d)")
print(f"        print(DifferenceUpdate_a) = {DifferenceUpdate_a}")




Discard_def = "Discard: The discard() method removes the specified item from the set. This method is different from the remove() method, because the remove() method will raise an error if the specified item does not exist, and the discard() method will not."
Discard_fruits = {'apple', 'banana', 'cherry'}
Discard_fruits.discard('banana')
print(f"\n{Discard_def}")
print("    Discard_fruits = {'apple', 'banana', 'cherry'}")
print("    Discard_fruits.discard('banana')")
print(f"        print(Discard_fruits) = {Discard_fruits}")




Intersection_def = "Intersection: The intersection() method returns a set that contains the similarity between two or more sets. The returned set contains only items that exist in both sets, or in all sets if the comparison is done with more than two sets. As a shortcut, you can use the, & ,operator instead"
Intersection_a = {'apple', 'banana', 'cherry'}
Intersection_b = {'google', 'microsoft', 'apple'}
Intersection_c = {'cherry', 'micra', 'bluebird', 'apple'}
Intersection_d = {'pink', 'black', 'orange', 'apple'}
Intersection_z = Intersection_a.intersection(Intersection_b, Intersection_c, Intersection_d)
print(f"\n{Intersection_def}")
print("    Intersection_a = {'apple', 'banana', 'cherry'}")
print("    Intersection_b = {'google', 'microsoft', 'apple'}")
print("    Intersection_c = {'cherry', 'micra', 'bluebird', 'apple'}")
print("    Intersection_d = {'pink', 'black', 'orange', 'apple'}")
print("    Intersection_z = Intersection_a.intersection(Intersection_b, Intersection_c, Intersection_d)")
print(f"        print(Intersection_z) = {Intersection_z}")




IntersectionUpdate_def = "Intersection Update: The intersection_update() method removes the items that is not present in both sets (or in all sets if the comparison is done between more than two sets). The intersection_update() method is different from the intersection() method, because the intersection() method returns a new set, without the unwanted items, and the intersection_update() method removes the unwanted items from the original set. As a shortcut, you can use the &= operator instead"
IntersectionUpdate_a = {'apple', 'banana', 'cherry'}
IntersectionUpdate_b = {'google', 'microsoft', 'apple'}
IntersectionUpdate_c = {'cherry', 'micra', 'bluebird', 'apple'}
IntersectionUpdate_d = {'pink', 'black', 'orange', 'apple'}
IntersectionUpdate_a.intersection_update(IntersectionUpdate_b, IntersectionUpdate_c, IntersectionUpdate_d)
print(f"\n{IntersectionUpdate_def}")
print("    IntersectionUpdate_a = {'apple', 'banana', 'cherry'}")
print("    IntersectionUpdate_b = {'google', 'microsoft', 'apple'}")
print("    IntersectionUpdate_c = {'cherry', 'micra', 'bluebird', 'apple'}")
print("    IntersectionUpdate_d = {'pink', 'black', 'orange', 'apple'}")
print("    IntersectionUpdate_a.intersection_update(IntersectionUpdate_b, IntersectionUpdate_c, IntersectionUpdate_d)")
print(f"        print(IntersectionUpdate_a) = {IntersectionUpdate_a}")




IsDisjoint_def = "Is Disjoint: The isdisjoint() method returns True if none of the items are present in both sets, otherwise it returns False."
IsDisjoint_x = {'apple', 'banana', 'cherry'}
IsDisjoint_y = {'google', 'microsoft', 'facebook'}
IsDisjoint_z = IsDisjoint_x.isdisjoint(IsDisjoint_y)
print(f"\n{IsDisjoint_def}")
print("    IsDisjoint_x = {'apple', 'banana', 'cherry'}")
print("    IsDisjoint_y = {'google', 'microsoft', 'facebook'}")
print("    IsDisjoint_z = IsDisjoint_x.isdisjoint(IsDisjoint_y)")
print(f"        print(IsDisjoint_z) = {IsDisjoint_z}")




IsSubset_def = "Is Subset: The issubset() method returns True if all items in the set exists in the specified set, otherwise it returns False. As a shortcut, you can use the <= operator instead"
IsSubset_x = {'a', 'b', 'c'}
IsSubset_y = {'f', 'e', 'd', 'c', 'b', 'a'}
IsSubset_z = IsSubset_x.issubset(IsSubset_y)
print(f"\n{IsSubset_def}")
print("    IsSubset_x = {'a', 'b', 'c'}")
print("    IsSubset_y = {'f', 'e', 'd', 'c', 'b', 'a'}")
print("    IsSubset_z = IsSubset_x.issubset(IsSubset_y)")
print(f"        print(IsSubset_z) = {IsSubset_z}")




IsSuperSet_def = "Is Super Set: The issuperset() method returns True if all items in the specified set exists in the original set, otherwise it returns False. As a shortcut, you can use the >= operator instead"
IsSuperSet_x = {'f', 'e', 'd', 'c', 'b', 'a'}
IsSuperSet_y = {'a', 'b', 'c'}
IsSuperSet_z = IsSuperSet_x.issuperset(IsSuperSet_y)
print(f"\n{IsSuperSet_def}")
print("    IsSuperSet_x = {'f', 'e', 'd', 'c', 'b', 'a'}")
print("    IsSuperSet_y = {'a', 'b', 'c'}")
print("    IsSuperSet_z = IsSuperSet_x.issuperset(IsSuperSet_y)")
print(f"        print(IsSuperSet_z) = {IsSuperSet_z}")




Pop_DEF = "Pop: The pop() method removes a random item from the set. This method returns the removed item."
Pop_fruits = {'apple', 'banana', 'cherry'}
Pop_fruits.pop()
print(f"\n{Pop_DEF}")
print("    Pop_fruits = {'apple', 'banana', 'cherry'}")
print("    Pop_fruits.pop()")
print(f"        print(Pop_fruits) = {Pop_fruits}")




Remove_def = "Remove: The remove() method removes the specified element from the set. This method is different from the discard() method, because the remove() method will raise an error if the specified item does not exist, and the discard() method will not."
Remove_fruits = {'apple', 'banana', 'cherry'}
Remove_fruits.remove('banana')
print(f"\n{Remove_def}")
print("    Remove_fruits = {'apple', 'banana', 'cherry'}")
print("    Remove_fruits.remove('banana')")
print(f"        print(Remove_fruits) = {Remove_fruits}")




Symmetric_Difference_def = "Symmetric_difference: The symmetric_difference() method returns a set that contains all items from both set, but not the items that are present in both sets. Meaning: The returned set contains a mix of items that are not present in both sets. As a shortcut, you can use the ^ operator instead"
Symmetric_Difference_x = {'apple', 'banana', 'cherry'}
Symmetric_Difference_y = {'google', 'microsoft', 'apple'}
Symmetric_Difference_z = Symmetric_Difference_x.symmetric_difference(Symmetric_Difference_y)
Symmetric_Difference_shortcut_z = Symmetric_Difference_x ^ Symmetric_Difference_y
print(f"\n{Symmetric_Difference_def}")
print("    Symmetric_Difference_x = {'apple', 'banana', 'cherry'}")
print("    Symmetric_Difference_y = {'google', 'microsoft', 'apple'}")
print("    Symmetric_Difference_z = Symmetric_Difference_x.symmetric_difference(Symmetric_Difference_y)")
print("    Symmetric_Difference_shortcut_z = Symmetric_Difference_x ^ Symmetric_Difference_y")
print(f"        print(Symmetric_Difference_z) = {Symmetric_Difference_z}")
print(f"        print(Symmetric_Difference_shortcut_z) = {Symmetric_Difference_shortcut_z}")




Symmetric_Difference_Update_def = "Symmetric_Difference_Update: The symmetric_difference_update() method updates the original set by removing items that are present in both sets, and inserting the other items. As a shortcut, you can use the ^= operator instead"

Symmetric_Difference_Update_x = {'apple', 'banana', 'cherry'}
Symmetric_Difference_Update_y = {'google', 'microsoft', 'apple'}
Symmetric_Difference_Update_x.symmetric_difference_update(Symmetric_Difference_Update_y)
Symmetric_Difference_Update_x ^= Symmetric_Difference_Update_y
print(f"\n{Symmetric_Difference_Update_def}")
print("    Symmetric_Difference_Update_x = {'apple', 'banana', 'cherry'}")
print("    Symmetric_Difference_Update_y = {'google', 'microsoft', 'apple'}")
print("    Symmetric_Difference_Update_x.symmetric_difference_update(Symmetric_Difference_Update_y)")
print("    Symmetric_Difference_Update_x ^= Symmetric_Difference_Update_y")
print(f"        print(Symmetric_Difference_Update_x) = {Symmetric_Difference_Update_x}")
print(f"        print(Symmetric_Difference_Update_x) = {Symmetric_Difference_Update_x}")




Union_def = "Union: The union() method returns a set that contains all items from the original set, and all items from the specified set(s). You can specify as many sets you want, separated by commas. It does not have to be a set, it can be any iterable object. If an item is present in more than one set, the result will contain only one appearance of this item. As a shortcut, you can use the | operator instead"
Union_x = {'a', 'b', 'c'}
Union_y = {'f', 'd', 'a'}
Union_z = {'c', 'd', 'e'}
Union_result = Union_x.union(Union_y, Union_z)
Union_shortcut_result = Union_x | Union_y | Union_z
print(f"\n{Union_def}")
print("    Union_x = {'a', 'b', 'c'}")
print("    Union_y = {'f', 'd', 'a'}")
print("    Union_z = {'c', 'd', 'e'}")
print("    Union_result = Union_x.union(Union_y, Union_z)")
print("    Union_shortcut_result = Union_x | Union_y | Union_z")
print(f"        print(Union_result) = {Union_result}")
print(f"        print(Union_shortcut_result) = {Union_shortcut_result}")




Update_def = "Update: The update() method updates the current set, by adding items from another set (or any other iterable). If an item is present in both sets, only one appearance of this item will be present in the updated set. As a shortcut, you can use the |= operator instead"
Update_x = {'apple', 'banana', 'cherry'}
Update_y = {'google', 'microsoft', 'apple'}
Update_z = {'cherry', 'micra', 'bluebird'}
Update_x |= Update_y | Update_z
print(f"\n{Update_def}")
print("    Update_x = {'apple', 'banana', 'cherry'}")
print("    Update_y = {'google', 'microsoft', 'apple'}")
print("    Update_z = {'cherry', 'micra', 'bluebird'}")
print("    Update_x.update(Update_y, Update_z)")
print(f"        print(Update_x) = {Update_x}")
print(f"        print(Update_x |= Update_y | Update_z) = {Update_x}")




print("\n\n\nEnd of the Python Set Methods Showcase")