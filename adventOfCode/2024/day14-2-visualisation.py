
import time
start_time = time.time()
import re 
import numpy as np
import matplotlib
matplotlib.use('Qt5Agg') 
import matplotlib.pyplot as plt

robots = []
with open('adventOfCode/2024/input14.txt', encoding="UTF-8", mode= "r") as file:  
    lignes = file.read().splitlines()

# col = 11
# row = 7

col = 101
row = 103

for ligne in lignes:
    position, vitesse = ligne.split()
    x, y = list(map(int, re.findall(r"-?\d+", position)))
    vx, vy = list(map(int, re.findall(r"-?\d+", vitesse)))
    robots.append([x,y,vx,vy])



for i in range(8000):
    coord = []
    matrix = np.zeros((col, row))
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

    if(i >= 7000):
        for x, y in coord:
            matrix[x, y] = 1  
        cmap = plt.cm.colors.ListedColormap(['blue', 'green'])

        plt.figure(figsize=(10, 10))
        plt.imshow(matrix, cmap=cmap, origin='upper')
        plt.colorbar(ticks=[0, 1], label='Couleurs (0 = Bleu, 1 = Vert)')
        plt.title(f"Matrice Colorée {i}")
        plt.xlabel("Colonnes")
        plt.ylabel("Lignes")
        plt.show()

    





        



    

 
end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Le programme a dure {elapsed_time_ms:.2f} ms est la reponse est")
