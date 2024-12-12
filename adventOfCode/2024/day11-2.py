
import time
start_time = time.time()

with open('adventOfCode/2024/input11.txt', encoding="UTF-8", mode= "r") as file:  
    ligne = list(map(int,file.read().splitlines()[0].split()))

print(ligne)
cache = {}



def recursif(nbr, step):
    
    if (nbr, step) in cache:
        return cache[(nbr, step)]
    
    if step == 0: 
        return 1

    if nbr == 0: 
        reponse = recursif(1, step -1)
        cache[(nbr, step)] = reponse
        return reponse

    if len(str(nbr)) % 2 == 0:
        nbr = str(nbr)
        taille = len(nbr)
        mid = taille // 2 
        nbr1, nbr2 = int(nbr[:mid]), int(nbr[mid:])

        reponse = recursif(nbr1, step -1) + recursif(nbr2, step-1)
        cache[(nbr, step)] = reponse
        return reponse


    reponse = recursif(nbr*2024, step - 1)
    cache[(nbr, step)] = reponse
    return reponse

total = 0

for nbr in ligne:
    total += recursif(nbr, 75)
        

print(total)

        

        
            


end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Le programme a dure {elapsed_time_ms:.2f} ms est la reponse est")


# 172484