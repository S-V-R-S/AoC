
import time
start_time = time.time()

with open('adventOfCode/2024/input11.txt', encoding="UTF-8", mode= "r") as file:  
    ligne = list(map(int,file.read().splitlines()[0].split()))

print(ligne)

blink = 25

for i in range(blink):
    add = 0
    ligneTemp = ligne.copy()
    for j, nbr in enumerate(ligneTemp):
        if nbr == 0 : ligne[j+add] = 1
        elif len(str(nbr)) % 2 == 0:
            nbr = str(nbr)
            taille = len(nbr)
            mid = taille // 2 
            nbr1, nbr2 = int(nbr[:mid]), int(nbr[mid:])
            ligne[j+add] = nbr1
            ligne.insert(j+1+add,nbr2)
            add +=1
        else:
            ligne[j+add] = nbr*2024

print(len(ligne))

        

        
            


end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Le programme a dure {elapsed_time_ms:.2f} ms est la reponse est")
