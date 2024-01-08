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

# LE PERE NOEL ET LE ROBOT COMMENCENT A LA MEME POSITION 
xs, ys = start
xr, yr = start 

# SI TOUR == TRUE CEST AU PERE DE NOEL DE SE DEPLACER SINON CEST AU ROBOT 
tour = True

# POUR CHAQUE ETAPE 
for dir in lignes:
    # ON REGARDE SI CEST AU PERE NOEL OU NON 
    if tour:
        # RECUPERATION DE LA DIRECTION
        dirx, diry = direction[dir]
        # MISE A JOUR DE LA POSITION 
        xs += dirx
        ys += diry

        # ON VISITE LA MAISON SI CE NEST PAS DEJA FAIT 
        if (xs,ys) in visited:
            tour = not(tour)
            continue
        else: 
            visited.add((xs,ys))
            house += 1
    else:
        # RECUPERATION DE LA DIRECTION
        dirx, diry = direction[dir]
        # MISE A JOUR DE LA POSITION 
        xr += dirx
        yr += diry

        # ON VISITE LA MAISON SI CE NEST PAS DEJA FAIT     
        if (xr,yr) in visited:
            tour = not(tour)
            continue
        else: 
            visited.add((xr,yr))
            house += 1
    tour = not(tour)

print(house)