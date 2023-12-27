# EXERCICE 1

def etiquetteMinimale(distance, noeudsAExplorer):
    min = float("inf")
    noeudMin = None
    for noeud in noeudsAExplorer:
        if(distance[noeud[1]][noeud[0]]<min):
            noeudMin = noeud
            min = distance[noeud[1]][noeud[0]]
    return noeudMin

def noeudsAccessibles(x,y,grille):
    noeuds = []
    if(x!=0):
        if(grille[y][x-1] in  ["-", "L", "F"] and (grille[y][x]=="S" or grille[y][x] in ['-',"J","7"])):
            # print("je peux aller a gauche")
            noeuds.append([x-1,y])
    if(x!=len(grille[y])-1):
         if(grille[y][x+1] in  ["-", "7", "J"] and (grille[y][x]=="S" or grille[y][x] in ["-", "L", "F"])):
            # print("je peux aller a droite")
            noeuds.append([x+1,y])
    if(y!=0):
         if(grille[y-1][x] in  ["|", "7", "F"] and (grille[y][x]=="S" or grille[y][x] in ["|", "L", "J"])):
            # print("je peux aller en haut")
            noeuds.append([x,y-1])
    if(y!=len(grille)-1):
         if(grille[y+1][x] in  ["|", "L", "J"] and (grille[y][x]=="S" or grille[y][x] in ["|", "7", "F"])):
            # print("je peux aller en bas")
            noeuds.append([x,y+1])  
    return noeuds

f = open("input.txt","r")
lignes = f.readlines()
f.close()
        
grille = []
distance = []
depart = [0,0]
noeudsAExplorer = []
distanceMax = 0

for y in range(len(lignes)):
    distance.append([])
    grille.append([])
    ligne = lignes[y].strip()
    for x in range(len(ligne)):
        grille[y].append(ligne[x])
        if ligne[x] == "S":
            depart = [x,y]
            noeudsAExplorer.append(depart)
            distance[y].append(0)
        elif( ligne[x] == "."):
            distance[y].append(".")
        else:
            distance[y].append(float("inf"))

noeudsExplores = []

while len(noeudsAExplorer) != 0:

    noeudActuel = etiquetteMinimale(distance, noeudsAExplorer)
    noeudsExplores.append(noeudActuel)
    x = noeudActuel[0]
    y = noeudActuel[1]
    noeuds = noeudsAccessibles(x,y, grille)
    for noeud in noeuds:
        if(noeud not in noeudsExplores):
            noeudsAExplorer.append(noeud)
        if(distance[noeud[1]][noeud[0]]> distance[y][x] +1):
            distance[noeud[1]][noeud[0]] = distance[y][x] +1
            if(distance[y][x] +1>distanceMax):
                distanceMax = distance[y][x] +1 
                
    del noeudsAExplorer[noeudsAExplorer.index(noeudActuel)]


print(distanceMax)

# EXERCICE 2 


grille = []
chemin = set()

# CONSTRUCTION GRILLE ET RECUPERATION DU DEPART
for i in range(len(lignes)):
    grille.append(lignes[i].strip())
    if("S" in lignes[i].strip()):
        depart = (lignes[i].strip().index("S"), i)
        chemin.add(depart)

# CONVERSION DU S EN BOUT DE CHEMIN POUR FERMER LA BOUCLE


x = depart[0]
y = depart[1]


deuxieme = noeudsAccessibles(x, y, grille)
directionDeuxieme = []


for point in deuxieme:
    if(point[0] == x-1 and point[1] == y):
        directionDeuxieme.append("h")
    if(point[0] == x+1 and point[1] == y):
        directionDeuxieme.append("b")
    if(point[0] == x and point[1]-1 == y):
        directionDeuxieme.append("d")
    if(point[0] == x and point[1]+1 == y):
        directionDeuxieme.append("g")

if('h' in directionDeuxieme and 'd' in directionDeuxieme):
    grille[y] = grille[y][:x] + "L" + grille[y][x + 1:]
    print("L")

if('h' in directionDeuxieme and 'b' in directionDeuxieme):
    grille[y] = grille[y][:x] + "|" + grille[y][x + 1:]
    print("|")

if('h' in directionDeuxieme and 'g' in directionDeuxieme):
    grille[y] = grille[y][:x] + "J" + grille[y][x + 1:]
    print("J")

if('b' in directionDeuxieme and 'd' in directionDeuxieme):
    grille[y] = grille[y][:x] + "F" + grille[y][x + 1:]
    print("F")
if('b' in directionDeuxieme and 'g' in directionDeuxieme):
    grille[y] = grille[y][:x] + "7" + grille[y][x + 1:]
    print("7")

if('d' in directionDeuxieme and 'g' in directionDeuxieme):
    grille[y] = grille[y][:x] + "-" + grille[y][x + 1:]
    print("-")


exterieur = True
verticalMur = ['J', 'L', '|']
# OU
# verticalMur = ['7', 'F', '|']

for y in range(len(grille)):
    for x in range(len(grille[0])):
        if(not(isinstance(distance[y][x] , int)) and not(exterieur)):
            grille[y] = grille[y][:x] + "o" + grille[y][x + 1:]

        if(grille[y][x] in verticalMur and isinstance(distance[y][x] , int)):
            exterieur = not(exterieur)
    exterieur = True


compteur = 0

for y in range(len(grille)):
    for x in range(len(grille[0])):
        if(grille[y][x] == 'o'):
            compteur += 1
print(compteur)
