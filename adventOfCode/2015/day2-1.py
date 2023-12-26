f = open("adventOfCode\\2015\\input2.txt","r")
lignes = f.readlines()
f.close()

total = 0

for ligne in lignes:
    l,w,h = [int(nbr) for nbr in ligne.strip().split("x")]
    surface = [l*w, w*h, h*l]
    total += min(surface)
    for s in surface: total += 2*s

print(total)