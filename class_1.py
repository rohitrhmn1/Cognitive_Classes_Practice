# String Operations
# import string
#
# a = "This is a string"
# b = a.upper()
# print(b)
# asc = string.ascii_letters
# print(asc)
# Numbers = "0123456"
# print(Numbers[::2])
# print("0123456".find('1'))
# Letters = "ABCDEFGHIJK"
# print(Letters[0:4])
# Good = "GsoAo+d"
# print(Good[::2])
# print("uppercase".upper())

# Tuples and Lists
# Files
# with open("./FileOne/Files/test_1.txt", "w") as file1:
#     file1.write("Your text goes here")
# file1.close()

# Working with Pandas

import pandas as pd

csv_path = "File1.csv"
# df = pd.read_csv(csv_path)  # df stands for DataFrame
# df.head()
df = pd.DataFrame({'a': [11, 21, 31], 'b': [21, 22, 23]})
print(df.head(3))
print(df['b'])
