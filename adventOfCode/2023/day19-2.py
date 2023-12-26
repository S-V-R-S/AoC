import re


f = open("advent code 2023\\input.txt","r")
lignes = f.read()
f.close()
lignes= lignes.split("\n\n")

workflow_data = lignes[0].split("\n")

workflows = {}
for w in workflow_data:
    w =  w[:-1]
    key, regle = w.split("{")
    regles =  regle.split(',')
    liste = []
    fin = ""
    for r in regles: 
        if ":" in r:
            cond, suite = r.split(":")
            liste.append((cond[0], cond[1], int(cond[2:]), suite))
        else:
            fin = r
    workflows[key] = ((liste), fin)


def compterPossibilites(ranges, cle):
    if cle == "R": return 0
    if cle == "A":
        combinaison = 1
        for bornInf, bornSup in ranges.values():
            combinaison *= bornSup - bornInf + 1
        return combinaison
    
    regles, fin = workflows[cle]

    total = 0

    for lettre, compa, nbr, target in regles:
        binf, bsup = ranges[lettre]
        if compa == "<":
            T = (binf, min(nbr - 1, bsup))
            F = (max(nbr, binf), bsup)
        else:
            T = (max(nbr + 1, binf), bsup)
            F = (binf, min(nbr, bsup))
        # si c'est vrai on change de regles et on s'assure que T n'est pas vide
        if T[0] <= T[1]:
            copy = dict(ranges)
            copy[lettre] = T
            total += compterPossibilites(copy, target)
        # sinon on poursuit si f pas vide
        if F[0] <= F[1]:
            ranges[lettre] = F

    total += compterPossibilites(ranges, fin)
            
    return total

print("Resultat")
print(compterPossibilites({lettre: (1, 4000) for lettre in 'xmas'}, "in"))

# 121464316215623