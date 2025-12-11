
import time
start_time = time.time()

with open('adventOfCode/2025/test.txt', encoding="UTF-8", mode= "r") as file:  
        lignes = file.read().splitlines()


dico = {}



def allerOut(porte, fft, dac):
        global dico
        somme = 0
        for s in dico[porte]:
                if s != "out":
                            if "fft" == s:
                                fft = True
                            if "dac" == s:
                                dac = True
                          
                            somme += allerOut(s, fft, dac)
                else:
                       if fft and dac:
                            somme += 1
        return somme 
        
        


for ligne in lignes:
        entree, sorties = ligne.split(":")
        sortiesList =  []
        for s in sorties.strip().split(' '):
                sortiesList.append(s)
        dico[entree] = sortiesList

print(allerOut("svr", False, False))


                



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