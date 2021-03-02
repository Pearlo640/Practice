# This is a sample Python script.

from prettytable import PrettyTable

l = [["Hassan", 21, "LUMS"], ["Ali", 22, "FAST"], ["Ahmed", 23, "UET"]]

table = PrettyTable(['Name', 'Age', 'University'])

for rec in l:
    table.add_row(rec)

print(table)

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


