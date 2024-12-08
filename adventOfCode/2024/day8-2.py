dico = {}
antennes = set()

antinodes = set()

with open('adventOfCode/2024/input.txt', encoding="UTF-8", mode= "r") as file:  
    lignes = file.read().splitlines()
    matrice = []
    for i, ligne in enumerate(lignes):
        matrice.append([])
        for j, letter in enumerate(ligne):
            matrice[i].append(letter)
            if letter != ".":
                if letter not in dico:
                    dico[letter] = []
                antennes.add((j,i))
                dico[letter].append([j,i])

print(len(matrice), "-", len(matrice[0]))

def create_antinodes(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    antinodes.add((x1,y1))
    antinodes.add((x2,y2))

    dx = x1 - x2
    dy = y1 - y2

    x = dx + x1
    y = dy + y1

    while (0<= x < len(matrice[0])) and (0<= y < len(matrice)):
        

        if (0<= x < len(matrice[0])) and (0<= y < len(matrice)):
            antinodes.add((x,y))
        x = dx + x
        y = dy + y
    
    dx = x2 - x1
    dy = y2 - y1

    x = x2 + dx
    y = y2 + dy

    while (0<= x < len(matrice[0])) and (0<= y < len(matrice)):
        
        if (0<= x < len(matrice[0])) and (0<= y < len(matrice)):
            antinodes.add((x,y))
        x = x + dx
        y = y + dy


for type in dico.keys():
    for point1 in dico[type]:
        for point2 in dico[type]:

            if point1!=point2:
                # print("couple", point1, "-", point2)
                create_antinodes(point1, point2)


print(antinodes)
print(len(antinodes))



