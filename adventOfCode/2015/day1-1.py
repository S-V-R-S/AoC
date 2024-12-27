
with open('adventOfCode/2015/input.txt', encoding="UTF-8", mode= "r") as file:  
    line = file.read()

 
floor = 0

for parenthesis in line:
    if parenthesis == "(":
        floor += 1
    else:
        floor -= 1
        
        
print(floor)