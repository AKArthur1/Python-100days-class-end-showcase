### Morse Code Converter ###
import csv
from tkinter import Entry, Toplevel
import pandas
import tkinter
from tkinter import scrolledtext

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


# print(USER_TEXT_TO_CONVERT
def input_user_text():
    """Requests user text"""
    global CONVERTED_USER_TEXT
    global USER_MESSAGE
    global USER_MESSAGE_TO_CONVERT
    # USER_MESSAGE = input("Type Message to translate into Morse Code\n").upper()
    USER_MESSAGE = conversion_text_box.get().upper()


    for digit in USER_MESSAGE:
        digit_check = MORSE_CODE_DICT.get(digit)
        if digit_check is not None:
            USER_MESSAGE_TO_CONVERT += str(digit)
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
    message_history_save = pandas.DataFrame([[USER_MESSAGE, CONVERTED_USER_TEXT]])
    message_history_save.to_csv("MorseCodeMessageHistory.csv", mode="a",index=False , header=False)


def display_conversion_result():
    morse_code_results.config(text=f'Morse Code = {CONVERTED_USER_TEXT}')
    user_convertable_digits_results.config(text=f'Convertable Message = {USER_MESSAGE_TO_CONVERT}')




def clear_message_history():
    """Clears Messages History CSV file"""
    clear_history_query = input("Clear All History?\nyes or no\n")
    if clear_history_query.lower() == "yes":
        message_history_clear = pandas.DataFrame(columns=CONVERTED_COLUMNS)
        message_history_clear.to_csv("MorseCodeMessageHistory.csv", index=False)
        print("History Deleted")
    elif clear_history_query.lower() == "no":
        print("Returning to Previous Page")
        return
    else:
        return

    print(history)

def clear_message():
    """Clears current message for program auto loop"""
    global USER_MESSAGE_TO_CONVERT
    global CONVERTED_USER_TEXT
    USER_MESSAGE_TO_CONVERT = ""
    CONVERTED_USER_TEXT = []

    # CONVERTED_USER_TEXT.clear()

def open_history():
    """Opens CSV Message History file"""
    # print(history)

def program_running():
    """Runs Program Loop"""
    global PROGRAM_END
    PROGRAM_END = 1
    while PROGRAM_END:
        # open_history()
        input_user_text()
        digit_converter()
        save_converted_message_to_history()
        clear_message()


        #button press toggles PROGRAM END VARIABLE to end program




# input_user_text()
# digit_converter()
# save_converted_message_to_history()

# print(USER_TEXT_TO_CONVERT)
# program_running()
# open_history()
# clear_message_history()















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
    pass

def button_convert():
    # convert = convert_var.get()
    # convert = conversion_text_box.get()
    clear_message()
    input_user_text()
    digit_converter()
    save_converted_message_to_history()
    display_conversion_result()
    clear_message()
    # pass

def button_view_history():
    history_window = tkinter.Tk()
    history_window.title('History')
    history_window.minsize(width=200, height=600)
    history_window.config(padx=10, pady=10)
    # history_window.resizable(width=False, height=False)

    for i, converted_columns in enumerate(CONVERTED_COLUMNS, start=0):
        tkinter.Label(history_window, text=converted_columns).grid(row=0, column=i, padx=5)

    with open("MorseCodeMessageHistory.csv", "r", newline="") as MorseCodeMessageHistory:
        reader = csv.reader(MorseCodeMessageHistory)
        data = list(reader)

    entrieslist = []
    for i, row in enumerate(data, start=0):
        entrieslist.append(row[0])
        for col in range(0, 2):
            tkinter.Label(history_window, text=row[col]).grid(row=i, column=col)

    # Creating scrolled text
    # area widget
    text_area = scrolledtext.ScrolledText(history_window,
                                          wrap=tkinter.WORD,
                                          width=40,
                                          height=10,
                                          font=("Times New Roman",
                                                15))

    text_area.grid(column=0, pady=10, padx=10)

    # Placing cursor in the text area
    text_area.focus()


def button_delete_history():
    pass

button_exit = tkinter.Button(text='EXIT',command=button_exit)
button_exit.grid(column=2, row=6)
# button_exit.config(padx=50, pady=50)

button_convert = tkinter.Button(text='CONVERT',command=button_convert)
button_convert.grid(column=1, row=4)

button_view_history = tkinter.Button(text='View History',command=button_view_history)
button_view_history.grid(column=0, row=4)

button_delete_history = tkinter.Button(text='Delete History',command=button_delete_history)
button_delete_history.grid(column=2, row=4)


#Entries
conversion_text_box = Entry(width=60, bg='dark grey', fg='black')
conversion_text_box.grid(column=1, row=3)







window.mainloop()