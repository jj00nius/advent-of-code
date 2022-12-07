# import re

# def read_from_file(file_name:str)-> None:
#     with open(file_name) as f:
#         fs = f.read().splitlines()
#         for i in fs:
#             test = re.findall()
# for i in range(0, len(string)):
#     count = 1
#     for count in range(i+1, len(string)):
#         if (string[i] == string[count] and string[1] != ' '):
#             count = count + 1
#     # setting the string count to 0 to avoid printing the characters already taken 
#     string = string[:count] + '0' + string[count+1:]; 
#     # If the count is greater than 1, the character is considered as duplicate 
#     if(count > 1 and string[i] != '0'): 
#         print(string[i]," - ",count)
INPUT = 'input.txt'

with open(INPUT) as f:
    d = f.readline().strip()

PART1_MSG_SIZE = 4
PART2_MSG_SIZE = 14
part_1_found = False
part_2_found = False

for c in range(len(d)): 
    if not part_1_found:
        msg_1 = [d[i] for i in range(c, c + PART1_MSG_SIZE)]
        if len(set(msg_1)) == PART1_MSG_SIZE:
            part_1 = c + PART1_MSG_SIZE
            part_1_found = True
    if not part_2_found:
        msg_2 = [d[i] for i in range(c, c + PART2_MSG_SIZE)]
        if len(set(msg_2)) == PART2_MSG_SIZE:
            part_2 = c + PART2_MSG_SIZE
            part_2_found = True
    if part_1_found and part_2_found:
        break

print('part 1:', part_1)
print('part 2:', part_2)
