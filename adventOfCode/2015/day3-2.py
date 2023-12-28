f = open("adventOfCode\\2015\\input15.txt","r")
lignes = f.read().strip()
f.close()

house = 1
start = (0,0)
visited = set()

visited.add(start)

direction = {'>': (1,0), '^': (0,-1), 'v' : (0,1), '<':(-1,0)}

xs, ys = start
xr, yr = start 
tour = True
for dir in lignes:
    if tour:
        dirx, diry = direction[dir]
        xs += dirx
        ys += diry

        if (xs,ys) in visited:
            tour = not(tour)
            continue
        else: 
            visited.add((xs,ys))
            house += 1
    else:
        dirx, diry = direction[dir]
        xr += dirx
        yr += diry

        if (xr,yr) in visited:
            tour = not(tour)
            continue
        else: 
            visited.add((xr,yr))
            house += 1
    tour = not(tour)

print(house)