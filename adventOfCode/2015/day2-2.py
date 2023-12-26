f = open("adventOfCode\\2015\\input2.txt","r")
lignes = f.readlines()
f.close()

total = 0

for ligne in lignes:
    dimension = [int(nbr) for nbr in ligne.strip().split("x")]

    ruban = 1
    for d in dimension: ruban *= d

    dimension = sorted(dimension)
    ruban += dimension[0]*2 + dimension[1]*2
    
    total += ruban

print(total)