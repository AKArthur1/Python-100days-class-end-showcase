### Morse Code Converter ###
import csv
from tkinter import Entry, messagebox
import pandas
import tkinter
from tkinter import scrolledtext
from pandas.core.config_init import styler_hrules
from prettytable import PrettyTable, HRuleStyle
from prettytable import from_csv
import pandas
import numpy as np


# Dictionary representing the morse code chart
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

USER_MESSAGE_TO_CONVERT = ""
USER_MESSAGE = ""
CONVERTED_USER_TEXT = []
PROGRAM_END = 0
history = pandas.read_csv("MorseCodeMessageHistory.csv")
CONVERTED_COLUMNS = ["USER_TEXT_TO_CONVERT", "CONVERTED_USER_TEXT"]
prettytable_default = PrettyTable()

# print(history)

# print(USER_TEXT_TO_CONVERT
def input_user_text():
    """Requests user text"""
    global CONVERTED_USER_TEXT
    global USER_MESSAGE
    global USER_MESSAGE_TO_CONVERT
    # USER_MESSAGE = input("Type Message to translate into Morse Code\n").upper()
    USER_MESSAGE = conversion_text_box.get().upper()
    USER_MESSAGE_LENGTH = 0


    for digit in USER_MESSAGE:
        digit_check = MORSE_CODE_DICT.get(digit)
        if USER_MESSAGE_LENGTH > 7:
            return
        else:
            if digit_check is not None:
                USER_MESSAGE_TO_CONVERT += str(digit)
                USER_MESSAGE_LENGTH += 1
            elif digit_check is None:
                pass
            else:
                pass

    # print(USER_MESSAGE_TO_CONVERT)


def digit_converter():
    """Converts Inputted digit into Morse Code then appends it to list of full converted statement"""
    global USER_MESSAGE
    global CONVERTED_USER_TEXT
    for digit in USER_MESSAGE:
        digit_check = MORSE_CODE_DICT.get(digit)
        if digit_check is not None:
            CONVERTED_USER_TEXT.append(digit_check)
        else:
            pass
    # print(', '.join(CONVERTED_USER_TEXT))
    # print(CONVERTED_USER_TEXT)


def save_converted_message_to_history():
    """Saves converted message into the history directory"""

    with open("MorseCodeMessageHistory.csv") as quicksave:
        message_history_save = pandas.DataFrame([[USER_MESSAGE, CONVERTED_USER_TEXT]])
        message_history_save.to_csv("MorseCodeMessageHistory.csv", mode="a", index=False, header=False)
        quicksave.close()


# def read_history():
#     post_convert_read_history = pandas.read_csv('MorseCodeMessageHistory.csv', mode='r')


def display_conversion_result():
    morse_code_results.config(text=f'Morse Code: {CONVERTED_USER_TEXT}')
    user_convertable_digits_results.config(text=f'Convertable Message: {USER_MESSAGE_TO_CONVERT}')



def clear_message_history():
    """Clears Messages History CSV file"""
    message_history_clear = pandas.DataFrame(columns=CONVERTED_COLUMNS)
    message_history_clear.to_csv("MorseCodeMessageHistory.csv", index=False)
    # print(history)

def delete_history_confirm():
    delete_query = messagebox.askquestion('Clear Save History File ',
                         'Clear ALL Morse Code History?')

    if delete_query == 'yes':
        clear_message_history()
    else:
        pass


def clear_message():
    """Clears current message for program auto loop"""
    global USER_MESSAGE_TO_CONVERT
    global CONVERTED_USER_TEXT
    USER_MESSAGE_TO_CONVERT = ""
    CONVERTED_USER_TEXT = []

def clear_entry_box():
    conversion_text_box.delete(0, tkinter.END)


def open_history():
    """Opens CSV Message History file"""
    # print(history)

# def program_running():
#     """Runs Program Loop"""
#     global PROGRAM_END
#     PROGRAM_END = 1
#     while PROGRAM_END:
#         # open_history()
#         input_user_text()
#         digit_converter()
#         save_converted_message_to_history()
#         clear_message()


        #button press toggles PROGRAM END VARIABLE to end program





### adding GUI using Tkinter
FONT = "Arial"
# convert = tkinter.StringVar()

window = tkinter.Tk()
window.title('Morse Code Converter')
# window.geometry("600x400")
window.minsize(width=500, height=300)
window.config(padx=10, pady=10)
window.resizable(width=False, height=False)


#Labels
title_label = tkinter.Label(text='Morse Code Converter', font=(FONT, 60, 'bold'))
title_label.grid(column=1, row=0)
title_label.config(padx=0, pady=30)

instructions_label = tkinter.Label(text='Type Message to translate into Morse Code', font=(FONT, 17))
instructions_label.grid(column=1, row=1)
instructions_label.config(padx=0, pady=10)

user_convertable_digits_results = tkinter.Label(text=str(USER_MESSAGE_TO_CONVERT), font=(FONT, 15))
user_convertable_digits_results.grid(column=1, row=5)
user_convertable_digits_results.config(padx=0, pady=10)

morse_code_results = tkinter.Label(text=str(CONVERTED_USER_TEXT), font=(FONT, 15))
morse_code_results.grid(column=1, row=6)
morse_code_results.config(padx=0, pady=10)

#Buttons
def button_exit():
    window.destroy()
    # pass

def button_convert_function():
    # convert = convert_var.get()
    # convert = conversion_text_box.get()
    clear_message()
    input_user_text()
    digit_converter()
    save_converted_message_to_history()
    # read_history()
    display_conversion_result()
    clear_entry_box()
    clear_message()


    # pass



def button_view_history():
    # read_history(mode="r")

    with open("MorseCodeMessageHistory.csv", "r", newline="") as MorseCodeMessageHistory:
        MorseCodeMessageHistory.flush()
        reader = csv.reader(MorseCodeMessageHistory)
        data = list(reader)

        ### Pretty Table ### --------------------------------------------------------------------------------------------------
        history_prettytable = PrettyTable()
        history_formatting = history
        # history_prettytable.hrules(styler_hrules=all)

        history_header = list(history.columns)
        history_data = list(map(list, np.array(history)))

        history_prettytable.field_names = history_header
        # history_prettytable.add_rows(history)
        for row in history_data:
            history_prettytable.add_row(row)
            history_prettytable.add_divider()

        # print(history_prettytable)


        # test = from_csv("MorseCodeMessageHistory.csv")

        ### Pretty Table ### --------------------------------------------------------------------------------------------------
        ### text window v02 ### -----------------------------------------------------------------------------------------------
        root = tkinter.Tk()
        text_area_scrollbar = tkinter.Scrollbar(root)
        save_history_pretty = tkinter.Text(root, height=40, width=200, font=(FONT, 7))
        text_area_scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        # text_area.grid(column=1, pady=0, padx=0)
        save_history_pretty.pack(side=tkinter.LEFT, fill=tkinter.Y)
        # save_history_pretty.grid(column=0, pady=0, padx=0)
        text_area_scrollbar.config(command=save_history_pretty.yview)
        save_history_pretty.config(yscrollcommand=text_area_scrollbar.set, wrap=None)
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
        MorseCodeMessageHistory.close()

    ### text window v02 ### -----------------------------------------------------------------------------------------------



def button_delete_history():
    clear_message_history()
    # pass

button_exit = tkinter.Button(text='EXIT',command=button_exit)
button_exit.grid(column=2, row=6)
# button_exit.config(padx=50, pady=50)

button_convert = tkinter.Button(text='CONVERT', command=button_convert_function)
button_convert.grid(column=1, row=4)

button_view_history = tkinter.Button(text='View History',command=button_view_history)
button_view_history.grid(column=0, row=4)

button_delete_history = tkinter.Button(text='Delete History',command=delete_history_confirm)
button_delete_history.grid(column=2, row=4)


#Entries
conversion_text_box = Entry(width=60, bg='dark grey', fg='black')
conversion_text_box.grid(column=1, row=3)









window.mainloop()