with open('adventOfCode/2015/input.txt', encoding="UTF-8", mode= "r") as file:  
    moves = file.readline()
    
position = (0,0)
houses = {position}

directions = {
    "v": (0,1),
    "<": (-1,0),
    ">" : (1,0),
    "^": (0,-1)
}

for move in moves:
    x, y = position
    dx, dy = directions[move]
    position = (x + dx, y + dy)

    houses.add(position)
    
print(len(houses))
    