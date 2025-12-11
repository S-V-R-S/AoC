
import time
start_time = time.time()

with open('adventOfCode/2025/test.txt', encoding="UTF-8", mode= "r") as file:  
        lignes = file.read().splitlines()



def allerOut(dico, porte, step):
        somme = 0
        for s in dico[porte]:
                if s != "out":
                        somme += allerOut(dico, s, step +1)
                else:
                    return 1

        return somme 
        
        


dico = {}
for ligne in lignes:
        entree, sorties = ligne.split(":")
        sortiesList =  []
        for s in sorties.strip().split(' '):
                sortiesList.append(s)
        dico[entree] = sortiesList

print(dico)
print(allerOut(dico, "you", 0))


                



end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Le programme a dure {elapsed_time_ms:.2f} ms est la reponse est")


# aaa: you hhh
# you: bbb ccc
# bbb: ddd eee
# ccc: ddd eee fff
# ddd: ggg
# eee: out
# fff: out
# ggg: out
# hhh: ccc fff iii
# iii: out