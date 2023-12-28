f = open("adventOfCode\\2015\\input15.txt","r")
lignes = f.read().strip()
f.close()

house = 1
start = (0,0)
visited = set()

visited.add(start)

direction = {'>': (1,0), '^': (0,-1), 'v' : (0,1), '<':(-1,0)}

x,y = start
for dir in lignes:
    
    dirx, diry = direction[dir]
    x += dirx
    y += diry

    if (x,y) in visited:
        continue
    else: 
        visited.add((x,y))
        house += 1

print(house)