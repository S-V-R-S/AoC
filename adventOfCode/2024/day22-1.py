
import time
start_time = time.time()

with open('adventOfCode/2024/input22.txt', encoding="UTF-8", mode= "r") as file:  
    lignes = file.read().splitlines()

def elaguer(nbr):
    return nbr % 16777216

def melanger(a,b):
    return a ^ b

def transformer(nbr):
    nbr = elaguer(melanger(nbr*64,nbr))
    nbr = elaguer(melanger(nbr//32, nbr))
    nbr = elaguer(melanger(nbr*2048, nbr))
    return nbr

def plurieurs_fois(nbr, fois):
    for i in range(fois):
        nbr = transformer(nbr)
    return nbr

somme = 0

for number in lignes:
    somme += plurieurs_fois(int(number), 2000)

print(somme)


end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Le programme a dure {elapsed_time_ms:.2f} ms est la reponse est")
