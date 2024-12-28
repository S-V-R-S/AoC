import re
with open('adventOfCode/2015/input.txt', encoding="UTF-8", mode= "r") as file:  
    instructions = file.readlines()
    
grid = [[0] * 1000 for _ in range(1000)]
    
for instruction in instructions:
    start_x, start_y, end_x, end_y = map(int, re.findall(r"\d+", instruction))
    
    for i in range(start_x, end_x+1):
        for j in range(start_y, end_y+1):
            if instruction.startswith("turn off"):
                if grid[j][i] > 0:
                    grid[j][i] -= 1
            elif instruction.startswith("turn on"):
                grid[j][i] += 1
            elif instruction.startswith("toggle"):
                grid[j][i] += 2

print(sum(sum(row) for row in grid))