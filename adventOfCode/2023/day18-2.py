f = open("adventOfCode\\2023\\input18.txt","r")
lignes = f.readlines()
f.close()

direction = {'0': (1,0), '2': (-1,0), '3': (0,-1), '1': (0,1)}

somme = 0
b = 0
chemin = [(0,0)]
for ligne in lignes:
    dir, dis, couleur = ligne.strip().split(" ")
    dir = couleur[-2]
    dis = couleur[2:len(couleur)-2]
    dis = int(dis, 16)
    dirx, diry = direction[dir]
    dis = int(dis)
    x,y = chemin[-1]
    b += dis

    chemin.append((x+ dis*dirx, y+dis*diry))

del chemin[0]

for i in range(len(chemin)-1):
    somme += chemin[i][0]*chemin[i+1][1] - chemin[i+1][0]*chemin[i][1]

aire = somme //2
print("contour",b)
print("aire",aire)
i = aire + 1 - b //2

print("Reponse:", i+b)
