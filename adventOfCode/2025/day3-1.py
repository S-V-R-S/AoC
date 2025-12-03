
import time
start_time = time.time()

# with open('adventOfCode/2025/input.txt', encoding="UTF-8", mode= "r") as file:  
with open('adventOfCode/2025/test.txt', encoding="UTF-8", mode= "r") as file:  
        lignes = file.read().strip()

somme = 0
for ligne in lignes.split("\n"):
        print(ligne)
        nbrs = [int(i) for i in ligne]
        nbr1 = max(nbrs[:-1])
        index = nbrs.index(nbr1)
        nbr2 = max(nbrs[index+1:])
        print(nbr1, index, nbr2)

        somme += int(str(nbr1)+str(nbr2))
print(somme)
end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Le programme a dure {elapsed_time_ms:.2f} ms est la reponse est")
