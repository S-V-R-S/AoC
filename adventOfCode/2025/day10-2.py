import pulp


with open('adventOfCode/2025/test.txt', encoding="UTF-8", mode= "r") as file:  
        lignes = file.read().splitlines()


total = 0
for ligne in lignes:
        parties = ligne.split(" ")

        objectif = [int(i) for i in parties[-1][1:-1].split(",")]
        boutons = parties[1:-1]

# creation du pb
        prob = pulp.LpProblem("", pulp.LpMinimize)

# creation des variables qui sont mes boutons 
        inconnues = {}
        for bouton in boutons:
               inconnues[bouton] = pulp.LpVariable(bouton, lowBound=0, cat=pulp.LpInteger)
        
# ajout les variables a la somme quil faut minimiser 
        prob += pulp.lpSum(inconnues.values())
        
# creer les equations a resoudre
        for i, o in enumerate(objectif):
               
               resultat = 0
# ajouter tous les boutons qui appuie sur le led en position i 
               for b in boutons:
                      if str(i) in b:
                             resultat += inconnues[b]

                            #  ajout de lequation
               prob += o == resultat
# redsoudre le pb 
        prob.solve()

        # ajouter la somme quil fallait minimiser au total 
        total += pulp.value(prob.objective)
print(total)