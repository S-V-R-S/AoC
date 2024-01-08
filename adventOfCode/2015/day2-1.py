# OUVERTURE DE L INPUT 
f = open("adventOfCode\\2015\\input2.txt","r")
lignes = f.readlines()
f.close()

# INITIALISATION DU TOTAL 
total = 0

# POUR CHAQUE CADEAU 
for ligne in lignes:

    # RECUPERATION DES DIFFERENTES MESURES
    l,w,h = [int(nbr) for nbr in ligne.strip().split("x")]

    # CALCUL DES SURFACES
    surface = [l*w, w*h, h*l]

    # ON AJOUTE LA VALEUR DE LA PLUS PETITE SURFACE 
    total += min(surface)

    # ON LES AJOUTE TOUTES 
    for s in surface: total += 2*s

print(total)