
import time
start_time = time.time()

with open('adventOfCode/2025/input.txt', encoding="UTF-8", mode= "r") as file:  
# with open('adventOfCode/2025/test.txt', encoding="UTF-8", mode= "r") as file:  
        lignes = file.read().strip()


frais = set()
nombres = set()

for s, ligne in enumerate(lignes.split("\n")):
        if "-" in ligne:
                continue
        elif ligne.strip() != "":
                nombres.add(int(ligne)) 


somme = 0
for s, ligne in enumerate(lignes.split("\n")):
        if "-" in ligne:
                start, end = [int(j) for j in ligne.split("-")]

                for n in nombres:
                        if n >= start and n<= end:
                             frais.add(n)
      

print(len(frais))

end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Le programme a dure {elapsed_time_ms:.2f} ms est la reponse est")
