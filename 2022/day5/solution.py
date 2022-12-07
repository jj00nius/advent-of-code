# [V]     [B]                     [C]
# [C]     [N] [G]         [W]     [P]
# [W]     [C] [Q] [S]     [C]     [M]
# [L]     [W] [B] [Z]     [F] [S] [V]
# [R]     [G] [H] [F] [P] [V] [M] [T]
# [M] [L] [R] [D] [L] [N] [P] [D] [W]
# [F] [Q] [S] [C] [G] [G] [Z] [P] [N]
# [Q] [D] [P] [L] [V] [D] [D] [C] [Z]
#  1   2   3   4   5   6   7   8   9 

import re

stacks = [['Q','F','M','R','L','W','C','V'],
['D','Q','L'],
['P','S','R','G','W','C','N','B'],
['L','C','D','H','B','Q','G'],['V','G',
'L','F','Z','S'],
['D','G','N','P'],
['D','Z','P','V','F','C','W'],
['C','P','D','M','S'],
['Z','N','W','T','V','M','P','C']]

def crane(crates: int, source: int, destination: int) -> None:
    source = source -1
    destination =  destination -1
    move = stacks[source][-crates:]
    # Comment out for part two
    # move.reverse()
    stacks[destination].extend(move)
    del stacks[source][-crates:]
    return None

def read_from_file(file_name:str)-> None:
    with open(file_name) as f:
        fs = f.read().splitlines() 
        for i in fs:
            test = re.findall("move (\d+) from (\d+) to (\d+)",i)
            new_int = tuple(int(item) for item in test[0])
            crane(*new_int)

def output():
    read_from_file("input.txt")
    string_output = ''
    for i in stacks:
        string_output += i[-1:][0]
    print(string_output)

output()

