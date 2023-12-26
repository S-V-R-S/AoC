
grille = []
f = open("input.txt","r")
lignes = f.readlines()
f.close()

for i, l in enumerate(lignes):
    grille.append([])
    for c in l.strip():
        grille[i].append(c)

def rotationNord(grille):
    coords = recupCoor(grille)
    for coord in coords:
        l = coord[0]
        c = coord[1]
        for k in range (0,len(grille)):    
            if(l==0):
                break
            if grille[l-1][c] == '.':
                grille[l-1][c]='O'
                grille[l][c]='.'
                l -= 1
            else:
                break

def rotationSud(grille):
    for k in range (0,len(grille)):
        for i in range(0,len(grille)-1):
            for j in range(len(grille[i])):
                if grille[i+1][j] in '.' and grille[i][j] in 'O':
                    grille[i+1][j]='O'
                    grille[i][j]='.'

def rotationOuest(grille):
    for k in range (0,len(grille[0])):
        for i in range(0,len(grille)):
            for j in range(1,len(grille[i])):
                if grille[i][j-1] in '.' and grille[i][j] in 'O':
                    grille[i][j-1]='O'
                    grille[i][j]='.'
    

def rotationEst(grille):
    for k in range (0,len(grille[0])):
        for i in range(0,len(grille)):
            for j in range(0,len(grille[i])-1):
                if grille[i][j+1] in '.' and grille[i][j] in 'O':
                    grille[i][j+1]='O'
                    grille[i][j]='.'

def recupCoor(grille):
    coords = []
    for l in range(len(grille)):
        for c in range(len(grille[0])):
            if grille[l][c] == "O":
                coords.append((l,c))
    return coords

def somme(grille):
    c = 1
    sumo = 0
    for i in range(len(grille)-1,-1,-1):
        for j in range(len(grille[i])):
            if grille[i][j] in 'O':
                sumo = sumo + c
        c+=1
    return sumo

nbrTour = 1000000000

def tour(nbrTour, grille):
    nbr = 1
    historique = {}
    find = False
    while nbr<nbrTour:
        print(nbr)
        rotationNord(grille)
        rotationOuest(grille)
        rotationSud(grille)
        rotationEst(grille)
        if str(grille) in historique and not(find):
            cycle = abs(historique[str(grille)] - nbr)
            nbrCycle = (nbrTour-historique[str(grille)])//cycle
            nbr = historique[str(grille)] + nbrCycle*cycle
            find = True
        else:
            historique[str(grille)] = nbr
            nbr+=1
    


tour(nbrTour, grille)
print(somme(grille))
