import csv
# [V]     [B]                     [C]
# [C]     [N] [G]         [W]     [P]
# [W]     [C] [Q] [S]     [C]     [M]
# [L]     [W] [B] [Z]     [F] [S] [V]
# [R]     [G] [H] [F] [P] [V] [M] [T]
# [M] [L] [R] [D] [L] [N] [P] [D] [W]
# [F] [Q] [S] [C] [G] [G] [Z] [P] [N]
# [Q] [D] [P] [L] [V] [D] [D] [C] [Z]
#  1   2   3   4   5   6   7   8   9 

puzzle_input = [['Q','F','M','R','L','W','C','V'],['D','Q','L'],['P','S','R','G','W','C','N','B'],
['L','C','D','H','B','Q','G'],['V','G','L','F','Z','S'],['D','G','N','P'],['D','Z','P','V','F','C','W'],
['C','P','D','M','S'],['Z','N','W','T','V','M','P','C']]

# importing the pandas library
import pandas as pd
import csv
from collections import defaultdict
 
# reading the csv file using read_csv
# storing the data frame in variable called df
df = pd.read_csv('input.csv')
 
# creating a list of column names by
# calling the .columns
list_of_column_names = list(df.columns)
 
# displaying updated list of column names
# print(list_of_column_names)

columns = defaultdict(list) # each value in each column is appended to a list

with open('input.csv') as format:
    # read rows into a dictionary format
    reader = csv.DictReader(format)
    # read a row as {column1: value1, column2: value2,...}
    for row in reader:
    # go over each column name and value 
        for (column_name, value) in row.items():
            # append the value into the appropriate list
            columns[column_name].append(value)

# Evaluate first row to create a list
string_input = [columns['AMOUNT'][0],columns['SOURCE'][0],columns['DESTINATION'][0]]

# Convert list to numerical
num_input = [eval(i) for i in string_input]

# Print numerical list
# print(num_input)

amount = range(num_input[0])
source = puzzle_input[num_input[1] - 1]
destination = puzzle_input[num_input[2] - 1]
print(source, destination)

print(source[-1])
print(destination[-1])
for i in amount:
    crate = (source[-1])
    destination.append(crate)
    source.pop(-1)
    print(source, destination)

# puzzle_input.append()
# puzzle_input.pop()