
with open('adventOfCode/2015/input.txt', encoding="UTF-8", mode= "r") as file:  
    line = file.read()

position = 0
floor = 0

for parenthesis in line:
    position += 1
    if parenthesis == "(":
        floor += 1
    else:
        floor -= 1
    if floor == -1:
        print(position)
        break