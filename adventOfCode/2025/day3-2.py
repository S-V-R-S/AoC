
import time
start_time = time.time()

with open('adventOfCode/2025/input.txt', encoding="UTF-8", mode= "r") as file:  
# with open('adventOfCode/2025/test.txt', encoding="UTF-8", mode= "r") as file:  
        lignes = file.read().strip()

somme = 0
for ligne in lignes.split("\n"):
        nbrs = [int(i) for i in ligne]
        total = ""
        for i in range(12):
            nbr1 = max(nbrs[:len(nbrs)-12+i+1])
            index = nbrs.index(nbr1)
            nbrs = nbrs[index+1:]
            total += str(nbr1)
        print(total)
        somme += int(total)

print(somme)
end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Le programme a dure {elapsed_time_ms:.2f} ms est la reponse est")
