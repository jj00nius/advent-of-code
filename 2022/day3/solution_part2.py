letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A","B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
total = 0
lines = []
with open("input.txt") as file:
    counter = 0
    start = 0
    stop = 3
    for line in file:
        lines.append(line.strip())
        curr_group = lines[start:stop]
        counter += 1

        if counter%3 == 0:
            for letter in curr_group[0]:
                if letter in curr_group[1]:
                    if letter in curr_group[2]:
                        total += letters.index(letter) + 1
                        break
            start += 3
            stop += 3

print(total)