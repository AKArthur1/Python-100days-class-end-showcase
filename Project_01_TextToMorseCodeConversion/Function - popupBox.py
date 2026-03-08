# Python program to create

### Yes/No Pop up ### ---------------------------------------------------------------------------------------------

import tkinter as tk
from tkinter import *
from tkinter import messagebox

def clear_message_history():
    """Clears Messages History CSV file"""
    message_history_clear = pandas.DataFrame(columns=CONVERTED_COLUMNS)
    message_history_clear.to_csv("MorseCodeMessageHistory.csv", index=False)
    # clear_history_query = input("Clear All History?\nyes or no\n")
    # if clear_history_query.lower() == "yes":
    #     message_history_clear = pandas.DataFrame(columns=CONVERTED_COLUMNS)
    #     message_history_clear.to_csv("MorseCodeMessageHistory.csv", index=False)
    #     print("History Deleted")
    # elif clear_history_query.lower() == "no":
    #     print("Returning to Previous Page")
    #     return
    # else:
    #     return

    print(history)

def delete_history_confirm():
    delete_query = messagebox.askquestion('Clear Save History File ',
                         'Clear ALL Morse Code History?')

    if delete_query == 'yes':
        clear_message_history()
    else:
        root.destroy()



PADDING_buttons = 50
# Driver's code
root = tk.Tk()
popup_canvas = tk.Canvas(root,
                         width=350,
                         height=200,
                         )
root.title('Clear ALL Morse Code History?')
root.resizable(width=False, height=False)
# popup_canvas.grid()
Yes_del = Button(root,
                 text='YES',
                 command=delete_history_confirm)
Yes_del.grid(column=0, row=0, padx=PADDING_buttons, pady=PADDING_buttons)
No_del = Button(root,
                 text='NO',
                 command=root.destroy)
No_del.grid(column=1, row=0, padx=PADDING_buttons, pady=PADDING_buttons)
# popup_canvas.create_window(100, 100,
#                            window=Yes_del)

root.mainloop()

### Yes/No Pop up ### ---------------------------------------------------------------------------------------------
