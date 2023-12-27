def lectureDuFichier(chemin):
    f = open(chemin,"r")
    lignes = f.read()
    f.close()
    return lignes

def recupererInput(lignes):
    lignes = lignes.split("\n")
    data = []
    for l in lignes:
        l = l.split(" ")
        data.append([l[0], int(l[1])])
    return data


data = recupererInput(lectureDuFichier("adventOfCode\\2023\\input.txt"))

chemin = {(0,0): "F"}
minX = 0
minY  = 0
maxX = 0
maxY = 0
lastPoint = [0,0]
listDirection = [None]
taille = len(data)
for j,d in enumerate(data):

    direction = d[0]
    distance = d[1]
    lastX = lastPoint[0]
    lastY = lastPoint[1]
    caractere = "F"

    if direction == "U":
        lastPoint = [lastX, lastY-distance]
        for i in range(1, distance):
            chemin[(lastX, lastY - i)] = "|"
        if lastY - distance < minY:
            minY = lastY - distance
        if j+1 < taille:
            if data[j+1][0] == "R":
                chemin[(lastX, lastY - distance)] = "F"
            if data[j+1][0] == "L":
                chemin[(lastX, lastY - distance)] = "7"

    if direction == "D":
        lastPoint = [lastX, lastY+distance]
        for i in range(1, distance+1):
            chemin[(lastX, lastY + i)] = "|"
        if lastY + distance > maxY:
            maxY = lastY + distance
        if j+1 < taille:
            if data[j+1][0] == "R":
                chemin[(lastX, lastY + distance)] = "L"
            if data[j+1][0] == "L":
                chemin[(lastX, lastY + distance)] = "J"
            
    if direction == "R":
        lastPoint = [lastX+distance, lastY]
        for i in range(1, distance+1):
            chemin[(lastX+i, lastY)] = "-"
        if lastX + distance > maxX:
            maxX = lastX + distance
        if data[j+1][0] == "U":
                chemin[(lastX+ distance, lastY )] = "J"
        if data[j+1][0] == "D":
                chemin[(lastX+ distance, lastY)] = "7"
    if direction == "L":
        lastPoint = [lastX-distance, lastY]
        for i in range(1, distance+1):
            chemin[(lastX-i, lastY)] = "-"
        if lastX - distance < minX:
            minX = lastX - distance
        if data[j+1][0] == "U":
                chemin[(lastX - distance, lastY )] = "L"
        if data[j+1][0] == "D":
                chemin[(lastX - distance, lastY)] = "F"

matrice = []
for y in range(minY, maxY+1):
    matrice.append([])
    for x in range(minX, maxX+1):
        if (x,y) in chemin:
            matrice[y-minY].append(chemin[(x,y)]) 
        else:
            matrice[y-minY].append(".") 

for y in range(len(matrice)):
    exterieur = True
    for x in range(len(matrice[0])):
        if matrice[y][x] in ['J', '|', 'L']:
                exterieur = not(exterieur) 
        elif matrice[y][x] == ".":
            if not(exterieur):
                matrice[y][x] = "#"

for m in matrice:
     print(m)
count = 0
for y in range(len(matrice)):
    for x in range(len(matrice[0])):
        if matrice[y][x] != ".": count +=1
print(count)



# maniere elegante
# f = open("adventOfCode\\2023\\input18.txt","r")
# lignes = f.readlines()
# f.close()

# direction = {'R': (1,0), 'L': (-1,0), 'U': (0,-1), 'D': (0,1)}

# somme = 0
# b = 0
# chemin = [(0,0)]
# for ligne in lignes:
#     dir, dis, couleur = ligne.strip().split(" ")
#     dirx, diry = direction[dir]
#     dis = int(dis)
#     x,y = chemin[-1]
#     b += dis

#     chemin.append((x+ dis*dirx, y+dis*diry))

# del chemin[0]

# for i in range(len(chemin)-1):
#     somme += chemin[i][0]*chemin[i+1][1] - chemin[i+1][0]*chemin[i][1]

# aire = somme //2
# print(b)
# print(aire)
# i = aire + 1 - b //2

# print("Reponse:", i+b)