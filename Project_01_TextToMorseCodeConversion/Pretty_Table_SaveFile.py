from prettytable import PrettyTable
from prettytable import from_csv
import pandas
import numpy as np

history_prettytable = PrettyTable()
history = pandas.read_csv("MorseCodeMessageHistory.csv")

history_header = list(history.columns)
history_data = list(map(list, np.array(history)))


history_prettytable.field_names = history_header
for row in history_data:
    history_prettytable.add_row(row)
# print(history_prettytable)