
import time
from itertools import product
from itertools import combinations
start_time = time.time()



with open('adventOfCode/2024/input23.txt', encoding="UTF-8", mode= "r") as file:  
    lignes = file.read().splitlines()


dico = {}
for connexions in lignes:  
    ord1, ord2 = connexions.split("-")
    
    if ord1 not in dico:
        dico[ord1] = set()
        dico[ord1].add(ord1)
        
    if ord2 not in dico:
        dico[ord2] = set()
        dico[ord2].add(ord2)

    dico[ord2].add(ord1)  
    dico[ord1].add(ord2)      
    

ordinateurs = dico.keys()
# listes_de_trois = list(combinations(ordinateurs, 3))
good = set()

for o in ordinateurs:
    if o[0] == 't':
        listes_de_trois = list(combinations(dico[o], 3))
        
        for trio in listes_de_trois:
            a,b,c = trio
            if a in dico[b] and a in dico[c] and b in dico[a] and b in dico[c] and c in dico[b] and c in dico[a]:
                if 't' == a[0] or 't' == b[0] or 't' == c[0]:
                    trio = sorted(trio)
                    good.add(tuple(trio))
    

for t in good:
    print(t)
print(len(good))
end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Le programme a dure {elapsed_time_ms:.2f} ms est la reponse est")
# 231309103124520
