import tkinter

from prettytable import PrettyTable
from prettytable import from_csv
import pandas
import numpy as np

history = pandas.read_csv("MorseCodeMessageHistory.csv")
### Pretty Table ### --------------------------------------------------------------------------------------------------
history_prettytable = PrettyTable()
# history = pandas.read_csv("MorseCodeMessageHistory.csv")

history_header = list(history.columns)
history_data = list(map(list, np.array(history)))

history_prettytable.field_names = history_header
for row in history_data:
    history_prettytable.add_row(row)

### Pretty Table ### --------------------------------------------------------------------------------------------------


### text window v02 ### -----------------------------------------------------------------------------------------------
root = tkinter.Tk()
text_area_scrollbar = tkinter.Scrollbar(root)
save_history_pretty = tkinter.Text(root, height=4, width=50)
text_area_scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
# text_area.grid(column=1, pady=0, padx=0)
save_history_pretty.pack(side=tkinter.LEFT, fill=tkinter.Y)
# save_history_pretty.grid(column=0, pady=0, padx=0)
text_area_scrollbar.config(command=save_history_pretty.yview)
save_history_pretty.config(yscrollcommand=text_area_scrollbar.set)
# quote = """HAMLET: To be, or not to be--that is the question:
# Whether 'tis nobler in the mind to suffer
# The slings and arrows of outrageous fortune
# Or to take arms against a sea of troubles
# And by opposing end them. To die, to sleep--
# No more--and by a sleep to say we end
# The heartache, and the thousand natural shocks
# That flesh is heir to. 'Tis a consummation
# Devoutly to be wished."""
save_history_pretty.insert(tkinter.END, history_prettytable)
tkinter.mainloop()

### text window v02 ### -----------------------------------------------------------------------------------------------





### Python Showcase BLANK Methods ###
# print("Beginning of the Python BLANK Methods Showcase\n\n\n")




# DEF = ""
#
# print(f"\n{_ref}")
# print("    BLANK")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")
# print(f"        print() = {BLANK}")



# print("\n\n\nEnd of the Python BLANK Methods Showcase")





















#
# fruits = {'apple', 'banana', 'cherry'}
#
# fruits.discard()
#
# print(f"\Math_Comb_n{_def}")
# print("    fruits = {'apple', 'banana', 'cherry'}")
# print("    fruits.discard()")
# print(f"        print(fruits) = {fruits}")


#
# _a = {'apple', 'banana', 'cherry'}
# _b = {'google', 'microsoft', 'apple'}
# _c = {'cherry', 'micra', 'bluebird'}
# _d = {'pink', 'black', 'orange'}
# _a.BLANK(_b, _c, _d)
# print(f"\Math_Comb_n{_def}")
# print("    _a = {'apple', 'banana', 'cherry'}")
# print("    _b = {'google', 'microsoft', 'apple'}")
# print("    _c = {'cherry', 'micra', 'bluebird'}")
# print("    _d = {'pink', 'black', 'orange'}")
# print("    _a.BLANK(_b, _c, _d)")
# print(f"        print(_a) = {_a}")




# Symmetric_Difference_Update_x = {'apple', 'banana', 'cherry'}
# Symmetric_Difference_Update_y = {'google', 'microsoft', 'apple'}
# Symmetric_Difference_Update_z = Symmetric_Difference_Update_x.symmetric_difference_update(Symmetric_Difference_Update_y)
# Symmetric_Difference_Update_x ^= Symmetric_Difference_Update_y
# print(f"\Math_Comb_n{Symmetric_Difference_Update_def}")
# print("    Symmetric_Difference_Update_x = {'apple', 'banana', 'cherry'}")
# print("    Symmetric_Difference_Update_y = {'google', 'microsoft', 'apple'}")
# print("    Symmetric_Difference_Update_z = Symmetric_Difference_Update_x.symmetric_difference_update(Symmetric_Difference_Update_y)")
# print("    Symmetric_Difference_Update_x ^= Symmetric_Difference_Update_y")
# print(f"        print(Symmetric_Difference_Update_z) = {Symmetric_Difference_Update_z}")
# print(f"        print(Symmetric_Difference_Update_x) = {Symmetric_Difference_Update_x}")













# DEF = ""
#
# print(f"\Math_Comb_n{Add_ref}")
# print("    BLANK")
# print("    BLANK")
# print("    BLANK")






# print("=")



