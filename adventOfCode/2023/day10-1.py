import re 

# def etiquetteMinimale(distance, noeudsAExplorer):
#     min = float("inf")
#     noeud = None
   
#     for x in range(len(distance)):
#         for y in range(len(distance[x])):
#             if([y,x] in noeudsAExplorer):
#                 if(distance[x][y] != "." and distance[x][y]<min):
#                     min = distance[x][y]
#                     noeud = [y,x]
#     return noeud

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


