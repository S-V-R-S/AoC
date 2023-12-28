import random
print("Happy Xmas")

f = open("adventOfCode\\2023\\input25.txt","r")
lignes = f.readlines()
f.close()

dico = {}
for l in lignes:
    n1, ns = l.strip().split(':')
    if n1 not in dico:
        dico[n1] = []
    for n in ns.strip().split(" "):
        if n not in dico:
            dico[n] = []
        dico[n1].append(n)
        dico[n].append(n1)

def compterNoeudsMemeComposant(depart):
    pile = [depart]
    visites = set()
    while pile:
        n = pile.pop()
        if n in visites: continue
        visites.add(n)
        for n1 in dico[n]:
            pile.append(n1)

    return len(visites)

cc= {}
cv = {}
def cheminBFS(d, a):
    pile = [d]
    visites = set()
    chemin = {}
    while pile:
        n = pile[0]
        del pile[0]
        if n in visites: continue
        if n == a:
            break
        visites.add(n)
        for n1 in dico[n]:
            if n1 not in visites:
                chemin[n1] = n
                pile.append(n1)
    c = []
    
    n = a
    while n != d:
        c.append(n)
        n1 = chemin[n]
        r = sorted([n, n1])
        if str(r) not in cc:
            cc[str(r)] = 1
        else: 
            cc[str(r)] += 1
        if n not in cv:
            cv[n] = 1
        else: 
            cv[n] += 1
        if n1 not in cv:
            cv[n1] = 1
        else: 
            cv[n1] += 1
        n = n1


noeuds = [n for n in dico.keys()]

nbrNoeuds = len(noeuds)

for i in range(10000):
        cheminBFS(noeuds[random.randint(0, nbrNoeuds-1)], noeuds[random.randint(0, nbrNoeuds-1)])

liensTriees = sorted(cc, key=cc.get, reverse=True)

liens = liensTriees[:3]

print(liens)
# ["['mnh', 'qnv']", "['ljh', 'tbg']", "['ffv', 'mfs']"]

print("Il y a", compterNoeudsMemeComposant("mnh"), "noeuds dans ce composant")

lien = [('mnh', 'qnv'), ('ljh', 'tbg'), ('ffv', 'mfs')]
for l in lien:
    n1,n2 = l
    dico[n1].remove(n2)
    dico[n2].remove(n1)

print("En enlevant ('mnh', 'qnv'), ('ljh', 'tbg'), ('ffv', 'mfs'), on a deux composants")
t1 = compterNoeudsMemeComposant("mnh")
t2 = compterNoeudsMemeComposant("qnv")
print("Il y a", t1 , "noeuds dans ce composant")
print("Il y a", t2 , "noeuds dans ce composant")
print("La reponse est", t1*t2)




