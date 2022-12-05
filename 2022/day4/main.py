#  --- Day 4: Camp Cleanup ---
# Every section has a unique ID number, and each Elf is assigned a range of section IDs.

# many of the assignments overlap.
# To try to quickly find overlaps and reduce duplicated effort, the Elves pair up and
# make a big list of the section assignments for each pair (your puzzle input).

# In how many assignment pairs does one range fully contain the other?

# To begin, get your puzzle input.

# Prompt user for an input
def get_input():
    pair_assignments = input('Provide assignments: \n')
    pair_list = list(pair_assignments)
    return pair_list

def check_assignments(pair_list):
    for pair in pair_list:
        if (pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]) or (pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]):
            print("data calculation complete")

get_input()
check_assignments(pair_list)