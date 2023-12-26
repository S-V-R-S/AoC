
print("Happy Xmas")

f = open("advent code 2023\\test.txt","r")
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

def scoreCorrespondance(n1, n2):
    l1 = set()
    l1.add(n1)
    for n in dico[n1]:
        l1.add(n)
    l2 = set()
    l2.add(n2)
    for n in dico[n2]:
        l2.add(n)

    return len(l1 & l2)

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

    # c.append(d)
    # c.reverse()
    # print(c)



noeuds = [n for n in dico.keys()]

print(cc)
for n in noeuds:
    for n2 in noeuds:
        print(n, n2)
        cheminBFS(n, n2)
print(cc)


print("Il y a", compterNoeudsMemeComposant("cmg"), "noeuds dans ce composant")

lien = [('hfx','pzl'), ('bvb','cmg'), ('nvd','jqt')]
for l in lien:
    n1,n2 = l
    dico[n1].remove(n2)
    dico[n2].remove(n1)

print("En enlevant hfx/pzl, bvb/cmg et nvd/jqt, on a deux composants")
t1 = compterNoeudsMemeComposant("cmg")
t2 = compterNoeudsMemeComposant("bvb")
print("Il y a", t1 , "noeuds dans ce composant")
print("Il y a", t2 , "noeuds dans ce composant")
print("La reponse est", t1*t2)




print(cv)