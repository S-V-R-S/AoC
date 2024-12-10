import time

start_time = time.time()
dico = {}
antinodes = set()

with open('adventOfCode/2024/input8.txt', encoding="UTF-8", mode= "r") as file:  
    lignes = file.read().splitlines()
    matrice = []
    for i, ligne in enumerate(lignes):
        matrice.append([])
        for j, letter in enumerate(ligne):
            matrice[i].append(letter)
            if letter != ".":
                if letter not in dico:
                    dico[letter] = []
                dico[letter].append([j,i])

def add_nodes(x,y,dx,dy):
    x = dx + x
    y = dy + y
    if (0<= x < len(matrice[0])) and (0<= y < len(matrice)):
        antinodes.add((x,y))
        

def create_antinodes(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    dx = x1 - x2
    dy = y1 - y2

    add_nodes(x1,y1,dx,dy)
    add_nodes(x2,y2,-dx,-dy)


for type in dico.keys():
    for p, point1 in enumerate(dico[type]):
        for i in range (p+1, len(dico[type])):
            create_antinodes(point1, dico[type][i])

# 409
end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Le programme a duré {elapsed_time_ms:.2f} ms est la réponse est", len(antinodes))



