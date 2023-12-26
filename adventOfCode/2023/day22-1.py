from heapq import heappush, heappop
f = open("advent code 2023\\test.txt","r")
lignes = f.read()
f.close()

cubes = []
for l in lignes.split("\n"):
    p1, p2 = l.split("~")
    p1 = [int(v) for v in p1.split(',')]
    x1, y1, z1 = p1
    p2 = [int(v) for v in p2.split(',')]
    x2, y2, z2 = p2
    heappush(cubes, (z1, (x1,y1,z1), (x2, y2, z2)))

def recupererUnEtage(i):
    liste = []
    while True:
        p = heappop(cubes)
        if p[0] != i:
            heappush(cubes, p)
            break
        liste.append(p)
    return liste

incre = 1
liste = recupererUnEtage(incre)

while cubes:
    incre += 1
    nextStage = recupererUnEtage(incre)


    