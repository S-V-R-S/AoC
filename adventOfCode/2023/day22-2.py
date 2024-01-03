from heapq import heappush, heappop
f = open("adventOfCode\\2023\\input22.txt","r")
lignes = f.read()
f.close()

def recupereInput(lignes):
    cubes = []
    for l in lignes.split("\n"):
        p1, p2 = l.split("~")
        p1 = [int(v) for v in p1.split(',')]
        x1, y1, z1 = p1
        p2 = [int(v) for v in p2.split(',')]
        x2, y2, z2 = p2
        cubes.append([[x1,y1,z1], [x2, y2, z2]])

    cubes.sort(key=lambda cube: cube[0][2])
    return cubes

def superposition(c1 , c2):
    return max(c1[0][0], c2[0][0]) <= min(c1[1][0],c2[1][0]) and max(c1[0][1], c2[0][1]) <= min(c1[1][1],c2[1][1])

def faireTomber(cubes):
    for i, cube in enumerate(cubes):
        z = 1
        for c in cubes[:i]:
            if superposition(cube, c):
                z = max(c[1][2] + 1, z)
        taille = cube[1][2] - cube[0][2] 
        cube[0][2] = z
        cube[1][2] = z + taille
        cubes.sort(key=lambda cube: cube[0][2])
    return cubes


cubes = recupereInput(lignes)
cubes = faireTomber(cubes)

supporte = {i: [] for i in range(len(cubes))}
estSupporte = {i: [] for i in range(len(cubes))}


for i, porteur in enumerate(cubes):
    for j in range(i+1, len(cubes)):
        if superposition(cubes[i], cubes[j]) and cubes[i][1][2] == cubes[j][0][2] - 1:
            supporte[i].append(j)
            estSupporte[j].append(i)


destruction = 0

for i in range(len(cubes)):
    destroy = []
    aDetruire = [i]
    while aDetruire:
        cube = aDetruire[0]
        del aDetruire[0]
        destroy.append(cube)
        for j in supporte[cube]:
                if all(k in destroy for k in estSupporte[j]):
                    destruction += 1
                    aDetruire.append(j)



print(destruction)


