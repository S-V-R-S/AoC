
import time
start_time = time.time()
import re 


robots = []
with open('adventOfCode/2024/input14.txt', encoding="UTF-8", mode= "r") as file:  
    lignes = file.read().splitlines()

col = 101
row = 103
second = 100
# p=3,0 v=-1,-2

for ligne in lignes:
    position, vitesse = ligne.split()
    x, y = list(map(int, re.findall(r"-?\d+", position)))
    vx, vy = list(map(int, re.findall(r"-?\d+", vitesse)))
    robots.append([x,y,vx,vy])

no, ne, so, se = [0,0,0,0]

for r in range(len(robots)):

    x,y,vx,vy = robots[r]
    for i in range(100):
        x = (x + vx) % col
        y = (y + vy) % row

        while x < 0:
            x = col + x
        
        while y < 0:
            y = row + y
    
    midx = col // 2
    midy = row // 2

    print(x,y)
    if x < midx and y < midy :
        no+=1
    elif x > midx and y < midy:
        so +=1
    elif x > midx and y > midy:
        se +=1
    elif x < midx and y > midy:
        ne +=1

print(ne,no,se,so)
print(ne*no*se*so)

        



    

 
end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Le programme a dure {elapsed_time_ms:.2f} ms est la reponse est")
