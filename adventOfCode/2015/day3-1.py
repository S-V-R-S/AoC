# OUVERTURE DE L INPUT 

f = open("adventOfCode\\2015\\input15.txt","r")
lignes = f.read().strip()
f.close()

# INITIALISATION 
# ON A DEJA UNE MAISON 
house = 1
# EN POSITION 0,0 
start = (0,0)
visited = set()

# ON AJOUTE LA MAISON VISITEES A LA LISTE 
visited.add(start)

# DICTIONNAIRE DES DIRECTIONS POSSIBLES
direction = {'>': (1,0), '^': (0,-1), 'v' : (0,1), '<':(-1,0)}

x,y = start

# POUR CHAQUE ETAPE 
for dir in lignes:
    
    # ON RECUPERE LA DIRECTION 
    dirx, diry = direction[dir]

    # ON MET A JOUR LES COORDONNEES ACTUELS 
    x += dirx
    y += diry

    # ON SORT SI ON ATTEINT UNE MAISON DEJA VISITEE
    if (x,y) in visited:
        continue

    # SINON ON LA VISITE 
    else: 
        visited.add((x,y))
        house += 1

print(house)