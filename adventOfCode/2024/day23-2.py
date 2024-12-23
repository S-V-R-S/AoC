
import time
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
good = set()
taille = max(len(t) for t in dico.values())

def tester(group):
        for a in group:
            for b in group:
                if a != b:
                    if a not in dico[b]:
                        return False
        return True
    
    
def groupe(o, taille):
    listes = list(combinations(dico[o], taille))
    for group in listes:
        if tester(group):
            return True
        
def groupe2(o, taille):
    listes = list(combinations(dico[o], taille))
    for group in listes:
        if tester(group):
            return group    
    return False

print(taille)            
while taille != 0:    
    found = False 
    print(taille)           
    for o in ordinateurs:
        if groupe(o, taille):
            print(o, taille)
            print(",".join(sorted(list(groupe2(o, taille)))))
            found = True
            break
    if found:
        break
    taille -= 1

print('fin')
    
end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Le programme a dure {elapsed_time_ms:.2f} ms est la reponse est")
# bw,dr,du,ha,mm,ov,pj,qh,tz,uv,vq,wq,xw
