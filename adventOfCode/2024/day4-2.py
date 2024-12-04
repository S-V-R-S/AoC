
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


def chercher_xmas(matrice, point):
     nbr = 0
     x,y = point[0], point[1]

     if x < len(matrice) - 1 and y > 0 and x > 0 and y < len(matrice[0]) - 1:

            if matrice[y][x] == 'A' and matrice[y-1][x+1] == 'S' and matrice[y+1][x+1] == 'S' and matrice[y-1][x-1] == 'M' and matrice[y+1][x-1] == 'M':
                nbr +=1
            if matrice[y][x] == 'A' and matrice[y-1][x+1] == 'M' and matrice[y+1][x+1] == 'M' and matrice[y-1][x-1] == 'S' and matrice[y+1][x-1] == 'S':
                nbr +=1
            if matrice[y][x] == 'A' and matrice[y-1][x+1] == 'M' and matrice[y+1][x+1] == 'S' and matrice[y-1][x-1] == 'M' and matrice[y+1][x-1] == 'S':
                nbr +=1
            if matrice[y][x] == 'A' and matrice[y-1][x+1] == 'S' and matrice[y+1][x+1] == 'M' and matrice[y-1][x-1] == 'S' and matrice[y+1][x-1] == 'M':
                nbr +=1

     return nbr


for i in range(len(matrice)):
     for j in range(len(matrice[0])):
            score += chercher_xmas(matrice, [i,j])

print(score)