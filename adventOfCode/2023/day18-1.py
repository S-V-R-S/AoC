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

data = recupererInput(lectureDuFichier("test.txt"))

# def lectureDuFichier(chemin):
#     f = open(chemin,"r")
#     lignes = f.read()
#     f.close()
#     return lignes

# def recupererInput(lignes):
#     lignes = lignes.split("\n")
#     data = []
#     for l in lignes:
#         l = l.split(" ")
#         data.append(l[2])
#     return data


# dataIngest = recupererInput(lectureDuFichier("test.txt"))
# data = []
# dico  = {"0":"R", "1":"D", "2": "L", "3": "U"}
# for i in dataIngest:
#      direction = dico[i[-2]]
#      distance = i[2:-2]
#      distance = int(distance, 16)
#      data.append([direction, distance])

def appartenir(y, tab):
    print(tab)
    for t in tab:
            if y >= t[0] and y<= t[1]:
                return True
    return False
chemin = {(0,0): "F"}
minX = 0
minY  = 0
maxX = 0
maxY = 0
lastPoint = [0,0]
matrice = {}
taille = len(data)
for j,d in enumerate(data):

    direction = d[0]
    distance = d[1]
    lastX = lastPoint[0]
    lastY = lastPoint[1]
    caractere = "F"

    if direction == "U":
        lastPoint = [lastX, lastY-distance]
        if lastY - distance < minY:
            minY = lastY - distance
        if lastX not in matrice:
            matrice[lastX]= [sorted([lastY - 1, lastY - distance +1])]
        else:
            matrice[lastX].append(sorted([lastY - 1, lastY - distance +1]))

    if direction == "D":
        lastPoint = [lastX, lastY+distance]
        if lastY + distance > maxY:
            maxY = lastY + distance
        if lastX not in matrice:
            matrice[lastX]= [sorted([lastY + 1, lastY + distance])]
        else:
            matrice[lastX].append(sorted([lastY + 1, lastY + distance]))
            
    if direction == "R":
        lastPoint = [lastX+distance, lastY]
        if lastX + distance > maxX:
            maxX = lastX + distance
        if data[j+1][0] == "U":

            if (lastX+ distance) not in matrice:
                matrice[lastX + distance ]= [[lastY,lastY]]
            else:
                matrice[lastX + distance].append([lastY,lastY])

    if direction == "L":
        lastPoint = [lastX-distance, lastY]
        if lastX - distance < minX:
            minX = lastX - distance
        if data[j+1][0] == "U":
            if (lastX - distance) not in matrice:
                matrice[lastX - distance]= [[lastY,lastY]]
            else:
                matrice[lastX - distance].append([lastY,lastY])

for x, m in matrice.items():
    print(x,m)


count = 0
