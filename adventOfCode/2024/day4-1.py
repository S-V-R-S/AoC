

with open('adventOfCode/2024/input.txt', encoding="UTF-8", mode= "r") as file:  
     matrice = file.read().splitlines()
score = 0
direction = [-1,0,1]

# y descend x a droite

def chercher_xmas(matrice, point):
     nbr = 0
     x, y = point[0], point[1]
     
     for dx in direction:
          for dy in direction:
               if 0 <= x + 3*dx < len(matrice) and 0 <= y + 3*dy < len(matrice[0]):
                    word = ""
                    for k in range(4):
                         word += matrice[y + dy*k][x + dx*k]
                    if word == 'XMAS':
                         nbr += 1
     return nbr


for i in range(len(matrice)):
     for j in range(len(matrice[0])):
            score += chercher_xmas(matrice, [i,j])

print(score)