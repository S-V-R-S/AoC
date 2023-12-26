import re 

f = open("input.txt","r")
lignes = f.readlines()
f.close()

historique = []

somme = 0

for ligne in lignes:
    historique.append([ int(h) for h in ligne.strip().split(" ") ])

tableau = []
for mesure in historique:
    tab = []
    mesure.reverse()
    tab.append(mesure)
    while(not(all(s==0 for s in tab[-1]))):
        tab.append([])
        for i in range(len(tab[-2])-1):
            tab[-1].append(tab[-2][i] - tab[-2][i+1])

    tableau.append(tab)

for tab in tableau:
    for i in range(len(tab)):
        if(i==0):
            tab[-1].append(0)
        else:
            tab[-1-i].append(-tab[-i][-1]+tab[-1-i][-1])


for tab in tableau:
    somme += tab[0][-1]

print(somme)


