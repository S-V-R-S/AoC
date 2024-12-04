
def creer_matrice():
    with open('adventOfCode/2024/input.txt', encoding="UTF-8", mode= "r") as file:  
        lignes = file.read().splitlines()
        matrice = []
        for i, ligne in enumerate(lignes):
            matrice.append([])
            for j, letter in enumerate(ligne):
                matrice[i].append(letter)
    return matrice


score = 0
matrice = creer_matrice()

# y descend x a droite
def chercher_xmas(matrice, point):
     nbr = 0
     x,y = point[0], point[1]
     
    #  a droite
     if x < len(matrice) - 3:
          if matrice[y][x] == 'X' and matrice[y][x+1] == 'M' and matrice[y][x+2] == 'A' and matrice[y][x+3] == 'S':
               nbr +=1
     # a gauche
     if x > 2:
          if matrice[y][x] == 'X' and matrice[y][x-1] == 'M' and matrice[y][x-2] == 'A' and matrice[y][x-3] == 'S':
               nbr +=1
    #  a droite
     if y < len(matrice[0]) - 3:
          if matrice[y][x] == 'X' and matrice[y+1][x] == 'M' and matrice[y+2][x] == 'A' and matrice[y+3][x] == 'S':
               nbr +=1
     # a gauche
     if y > 2:
          if matrice[y][x] == 'X' and matrice[y-1][x] == 'M' and matrice[y-2][x] == 'A' and matrice[y-3][x] == 'S':
               nbr +=1
     # en bas a droite 
     if x < len(matrice) - 3 and y < len(matrice[0]) - 3:
          if matrice[y][x] == 'X' and matrice[y+1][x+1] == 'M' and matrice[y+2][x+2] == 'A' and matrice[y+3][x+3] == 'S':
               nbr +=1
     # en haut a gauche
     if x > 2 and y > 2:
          if matrice[y][x] == 'X' and matrice[y-1][x-1] == 'M' and matrice[y-2][x-2] == 'A' and matrice[y-3][x-3] == 'S':
               nbr +=1

    # en bas a gauche
     if x > 2 and y < len(matrice[0]) - 3:
          if matrice[y][x] == 'X' and matrice[y+1][x-1] == 'M' and matrice[y+2][x-2] == 'A' and matrice[y+3][x-3] == 'S':
               nbr +=1
     # en bas a gauche
     if x < len(matrice) - 3 and y > 2:
          if matrice[y][x] == 'X' and matrice[y-1][x+1] == 'M' and matrice[y-2][x+2] == 'A' and matrice[y-3][x+3] == 'S':
               nbr +=1
               



     return nbr


for i in range(len(matrice)):
     for j in range(len(matrice[0])):
            score += chercher_xmas(matrice, [i,j])

print(score)