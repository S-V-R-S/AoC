
import time
start_time = time.time()

directions = [[0 , -1], [0, 1], (1, 0), (-1, 0)]
parcelles = set()


# creation de la matrice 
with open('adventOfCode/2024/input12.txt', encoding="UTF-8", mode= "r") as file:  
    lignes = file.read().splitlines()
    matrice = []
    for i, ligne in enumerate(lignes):
        matrice.append([])
        for j, letter in enumerate(ligne):
            matrice[i].append(letter)
            parcelles.add((j,i))

# exploration de chaque parcelle 
prix = 0
# tant qu'un point n a pas ete explore 
while len(parcelles) != 0:
    p = parcelles.pop()
    same = [p]
    to_explore = [p]

    # forme un groupe 
    while to_explore:
        point = to_explore.pop()
        x, y = point

        for dir in directions:
            x1 = x + dir[0]
            y1 = y + dir[1]
            if 0 <= x1 < len(matrice[0]) and 0 <= y1 < len(matrice):
                if matrice[y1][x1] == matrice[y][x] and (x1,y1) not in same:
                    same.append((x1, y1))
                    to_explore.append((x1, y1))
                    parcelles.remove((x1,y1))
    
    # pour chaque groupe recuperation des frontieres en 4 groupes : haut, bas, droite, gauche     
    f_h = []
    f_b = []
    f_d = []
    f_g = []

    for parcelle in same:
        perimetre = 0
        x,y = parcelle
        for dir in directions:
            x1 = x + dir[0]
            y1 = y + dir[1]
            if 0 <= x1 < len(matrice[0]) and 0 <= y1 < len(matrice):
                if (x1,y1) not in same:
                    if dir == [0 , -1]:
                        f_h.append(parcelle)
                    if dir == [0, 1] :
                        f_b.append(parcelle)
                    if dir == (1, 0) :
                        f_d.append(parcelle)
                    if dir == (-1, 0) :
                        f_g.append(parcelle)


            else:
                if x1 <0 :
                    f_g.append(parcelle)
                if x1 >= len(matrice[0]):
                    f_d.append(parcelle)

                if y1 <0 :
                    f_h.append(parcelle)
                if y1 >= len(matrice):
                    f_b.append(parcelle)


    nbr_frontieres = 0

    # calcul le nombre des frontieres pour chaque cote 
    # pour haut
    dico_x = {}
    for point in f_h:
        y = point[1]
        if y not in dico_x:
            dico_x[y] = []
        dico_x[y].append(point[0])

    for liste_x in dico_x.values():
        liste_x.sort()
        x = liste_x[0]
        nbx = 1
        for i in range(1, len(liste_x)):
            if liste_x[i] - x > 1:
                nbx += 1
            x = liste_x[i]
        nbr_frontieres += nbx

    # pour Bas
    dico_x = {}
    for point in f_b:
        y = point[1]
        if y not in dico_x:
            dico_x[y] = []
        dico_x[y].append(point[0])

    for liste_x in dico_x.values():
        liste_x.sort()
        x = liste_x[0]
        nbx = 1
        for i in range(1, len(liste_x)):
            if liste_x[i] - x > 1:
                nbx += 1
            x = liste_x[i]
        nbr_frontieres += nbx
    

    # pour gauche
    dico_y = {}
    for point in f_g:
        x = point[0]
        if x not in dico_y:
            dico_y[x] = []
        dico_y[x].append(point[1])

    for liste_y in dico_y.values():
        liste_y.sort()
        y = liste_y[0]
        nby = 1
        for i in range(1, len(liste_y)):
            if liste_y[i] - y > 1:
                nby += 1
            y = liste_y[i]
        nbr_frontieres += nby
   
    # pour droite
    dico_y = {}
    for point in f_d:
        x = point[0]
        if x not in dico_y:
            dico_y[x] = []
        dico_y[x].append(point[1])

    for liste_y in dico_y.values():
        liste_y.sort()
        y = liste_y[0]
        nby = 1
        for i in range(1, len(liste_y)):
            if liste_y[i] - y > 1:
                nby += 1
            y = liste_y[i]
        nbr_frontieres += nby


    prix += nbr_frontieres * len(same)

    
                
                    


print(prix)
end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Le programme a dure {elapsed_time_ms:.2f} ms est la reponse est prix")
# 893676