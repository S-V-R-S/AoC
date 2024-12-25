
import time
start_time = time.time()
import copy

with open('adventOfCode/2024/input24.txt', encoding="UTF-8", mode= "r") as file:  
    lignes = file.read().splitlines()          

goal = "1011110000000011011110100010110111100010110000"
dico = {}
dico_operation = {}
liste_z = []

for ligne in lignes:
    if ":" in ligne:
        porte, valeur = ligne.split(": ")
        dico[porte] = int(valeur)
    if "-" in ligne:
        p1, op, p2, f, p3 = ligne.split()
        dico_operation[p3] = [p1, op, p2]
        if p3[0] == "z":
             liste_z.append(p3)
             
liste_z = sorted(liste_z)       
echange = []
score = 0

def calcul(p3):
    p1, op, p2 = dico_operation[p3]
    if p1 in dico and p2 in dico:
        if op == "AND":
            if dico[p1] == 1 and dico[p2] == 1:
                dico[p3] = 1
            else:
                dico[p3] = 0
        elif op == "OR":
            if dico[p1] == 1 or dico[p2] == 1:
                dico[p3] = 1
            else:
                dico[p3] = 0
        elif op == "XOR":
            if dico[p1] == 1 and dico[p2] == 0 or dico[p1] == 0 and dico[p2] == 1:
                dico[p3] = 1
            else:
                dico[p3] = 0
        return
    if p1 not in dico:
        calcul(p1)
    if p2 not in dico:
        calcul(p2)
    calcul(p3)

echanges = []

def score(numero):
    score = 0
    for i in range(numero + 1):
        attendu = int(goal[-1-i])
        z = liste_z[i]
        calcul(z)
        if attendu == dico[z]:
            score +=1
    return score

def parents_z(point):
    parents = []
    to_explore = [point]
    x_haut = 0
    while to_explore:
        p = to_explore.pop()
        p1, op, p2 = dico_operation[p]
        if p1[0] in "x,y":
            parents.append(p1)
            if int(p1[1:]) > x_haut:
                x_haut = int(p1[1:])
        elif p1 not in parents and p1 not in to_explore:
            to_explore.append(p1)
            parents.append(p1)
        if p2[0] in "x,y":
            parents.append(p2)
        elif p2 not in parents and p2 not in to_explore:
            to_explore.append(p2)
            parents.append(p2)
    return x_haut



def difference(z1, z2):
    l1 = parents_z(z1)
    l2 = parents_z(z2)
    resultat = list(set(l1) - set(l2))
    return resultat

def enfants(liste):
    print("l", liste)
    enfs = []
    while liste:
        enfant = liste.pop()
        p1, op, p2 = dico_operation[enfant]
        if p1 in liste or p1 in enfs or p2 in liste or p2 in enfs:
            enfs.append(enfant)
            
    return enfs
# print(enfants(difference("z10", "z09")))
#10  kmb/z10, kks/10
    # 15 {('tvp', 'z15'), ('qts', 'z15'), ('kvg', 'z15'), ('jkh', 'z15'), }
# print(enfants(difference("z15", "z14")))
# print(enfants(difference("z25", "z24")))

z_problem = []   
for z in liste_z:
    if dico_operation[z][1] != "XOR" and z[1:] != "45":
        z_problem.append(z)
  
potentiel = [] 
for cle in dico_operation.keys():
    if dico_operation[cle][1] == "XOR" and dico_operation[cle][0][0] not in "xy" and cle[0] != "z":
        potentiel.append(cle)
        
a_tester = z_problem + potentiel
print(a_tester)

# //todo trier les kmb tvp dpg en trouvent le z le plus haut
print(parents_z("kmb"))  
# 10 
print(parents_z("tvp"))       
# 15
print(parents_z("dpg"))  
# 25
        
echanges = [["kmb", "z10"],["tvp", "z15"],["dpg", "z25"]]

for e in echanges:
    x, y = e
    dico_operation[x], dico_operation[y] = dico_operation[y], dico_operation[x]
    

resultat = score(45)
possible = []
a = 0

while a+1 == score(a)  :
    a += 1
    
a = 35
p1, o, p2 = dico_operation["z35"]
print(p1, p2)
for cle in dico_operation.keys():
    x, o, y = dico_operation[cle]
    if (x == "x35" and y == "y35" or x == "y35" and y == "x35") and o == "XOR":
        print(cle)
        # vdk
        echanges.append([cle, "mmf"])
        break


dico_operation["mmf"], dico_operation[cle] = dico_operation[cle], dico_operation["mmf"]


dico = {}
for ligne in lignes:
    if ":" in ligne:
        porte, valeur = ligne.split(": ")
        dico[porte] = int(valeur)
        

if score(45) == 46:
    final = []
    for echange in echanges:
        e,c = echange
        final.append(e)
        final.append(c)
    print(",".join(sorted(final)))

# dpg,kmb,mmf,tvp,vdk,z10,z15,z25

# end_time = time.time()
# elapsed_time_ms = (end_time - start_time) * 1000
# print(f"Le programme a dure {elapsed_time_ms:.2f} ms est la reponse est")
# dpg,kmb,mmf,tvp,vdk,z10,z15,z25

# kmb,z10,
# tvp,z15,
# z25,dpg,
# vdk,mmf