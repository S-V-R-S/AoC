
import time
start_time = time.time()
import re 


robots = []
with open('adventOfCode/2024/input14.txt', encoding="UTF-8", mode= "r") as file:  
    lignes = file.read().splitlines()

# col = 11
# row = 7

col = 101
row = 103
# second = 100
# p=3,0 v=-1,-2

for ligne in lignes:
    position, vitesse = ligne.split()
    x, y = list(map(int, re.findall(r"-?\d+", position)))
    vx, vy = list(map(int, re.findall(r"-?\d+", vitesse)))
    robots.append([x,y,vx,vy])


groupe = []
startx = col // 2 - 20 
starty = row // 2 - 20 

for i in range(40):
    for y in range(40):
        groupe.append((startx+i, starty+y))

for i in range(10000):
    coord = []
    new = []
    for r in range(len(robots)):

        x,y,vx,vy = robots[r]
        positions_prises = []
    
        x = (x + vx) % col
        y = (y + vy) % row

        while x < 0:
            x = col + x
        
        while y < 0:
            y = row + y
        
        new.append([x,y,vx,vy])
        coord.append((x,y))
    robots = new

    intersection = set(coord)
    intersection.intersection_update(groupe)

    if len(intersection) >= 200:
        print(i+1)



end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Le programme a dure {elapsed_time_ms:.2f} ms est la reponse est")
