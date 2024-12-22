
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
    return nbr, nbr%10

def plurieurs_fois(nbr, fois):
    reste = [nbr%10]
    for i in range(fois):
        nbr, r = transformer(nbr)
        reste.append(r)

    return reste

somme = 0

dico = {}
for j, nbr in enumerate(lignes):
    verif = set()
    restes = plurieurs_fois(int(nbr),2000)
    s = [0,0,0,0]
    for i in range(len(restes)):
        del s[0]
        s.append(restes[i]-restes[i-1])
        if i>=4:
            if tuple(s) not in verif:
                verif.add(tuple(s))
                if tuple(s) not in dico:
                    dico[tuple(s)] = 0
                dico[tuple(s)] += restes[i]

print(max(dico.values()))

end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Le programme a dure {elapsed_time_ms:.2f} ms est la reponse est")
 