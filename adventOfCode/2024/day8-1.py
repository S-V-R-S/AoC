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

    x = x1 - x2
    y = y1 - y2

    x = x + x1
    y = y + y1

    if (0<= x < len(matrice)) and (0<= y < len(matrice[0])):
        antinodes.add((x,y))
    
    x = x2 - x1
    y = y2 - y1

    x = x2 + x
    y = y2 + y

    if (0<= x < len(matrice)) and (0<= y < len(matrice[0])):
        antinodes.add((x,y))


for type in dico.keys():
    for point1 in dico[type]:
        for point2 in dico[type]:

            if point1!=point2:
                # print("couple", point1, "-", point2)
                create_antinodes(point1, point2)


# print(antinodes)
print(len(antinodes))



