def faireMatrice():
    f = open("day13_input.txt","r")
    lignes = f.read()
    f.close()
    blocs = lignes.split("\n\n")
    matrices = []

    for i, bloc in enumerate(blocs):
        matrices.append([])
        for l, ligne in enumerate(bloc.split("\n")):
            matrices[i].append([])
            for ch in ligne:
                matrices[i][l].append(ch)
    return matrices


def calculerLignes(bloc):
    for i in range(1, len(bloc), 1):
        nbrEchange = min(i, len(bloc)-i)
        symetrique = True
        for j in range(nbrEchange):
            if nbrDiff(bloc[i-1-j],bloc[i+j]) != 0: 
                symetrique = False
        if symetrique: return i
    return 0

def calculerColonnes(bloc):
    for i in range(1, len(bloc[0]), 1):
        nbrEchange = min(i, len(bloc[0])-i)
        symetrique = True
        for j in range(nbrEchange):
            l1 = []
            l2 = []
            for l in bloc:
                l1.append(l[i-1-j])
                l2.append(l[i+j])
            if nbrDiff(l1,l2) != 0: 
                symetrique = False
        if symetrique: return i
    return 0

        
def nbrDiff(l1, l2):
    nbrDiff = 0
    for i in range(len(l1)): 
        
        if l1[i] != l2[i]: nbrDiff += 1
    return nbrDiff


sumLignes = 0
sumColonnes = 0
matrice = faireMatrice()
for m in matrice:
    sumLignes+=calculerLignes(m)
    sumColonnes+=calculerColonnes(m)

print("Score Lignes:",sumLignes)
print("Score Colonnes:",sumColonnes)
print("Score Global:",sumColonnes+sumLignes*100)

