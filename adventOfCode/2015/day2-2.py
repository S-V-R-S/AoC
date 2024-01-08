# OUVERTURE DE L INPUT 
f = open("adventOfCode\\2015\\input2.txt","r")
lignes = f.readlines()
f.close()

# INITIALISATION DU TOTAL 
total = 0

# POUR CHAQUE CADEAU 
for ligne in lignes:
    # RECUPERATION DES DIFFERENTES MESURES
    dimension = [int(nbr) for nbr in ligne.strip().split("x")]

    # ON CALCUL LA VALEUR DU RUBAN NECESSAIRE 
    ruban = 1
    for d in dimension: ruban *= d

    # ON TRIE LES DIMENSIONS
    dimension = sorted(dimension)
    # ON RECUPERE LES DEUX PREMIERES VALEURS ET ON LES DOUBLE POUR LES AJOUTER AU RUBAN NECESSAIRE 
    ruban += dimension[0]*2 + dimension[1]*2
    
    # ON AJOUTE AU TOTAL 
    total += ruban

print(total)