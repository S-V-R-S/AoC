with open('adventOfCode/2015/input.txt', encoding="UTF-8", mode= "r") as file:  
    moves = file.readline()
    
santa_position = (0,0)
robot_position = (0,0)
houses = {santa_position}

directions = {
    "v": (0,1),
    "<": (-1,0),
    ">" : (1,0),
    "^": (0,-1)
}

for i, move in enumerate(moves):
    dx, dy = directions[move]

    if i % 2 == 0:
        x, y = santa_position
        santa_position = (x + dx, y + dy)
        houses.add(santa_position)
    else:
        x, y = robot_position
        robot_position = (x + dx, y + dy)
        houses.add(robot_position)
    
print(len(houses))
    