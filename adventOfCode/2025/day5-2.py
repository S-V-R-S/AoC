
import time
start_time = time.time()

with open('adventOfCode/2025/input.txt', encoding="UTF-8", mode= "r") as file:  
# with open('adventOfCode/2025/test.txt', encoding="UTF-8", mode= "r") as file:  
        lignes = file.read().strip()


frais = []

averifier = True

somme = 0

for s, ligne in enumerate(lignes.split("\n")):
        if "-" in ligne:
                start, end = [int(j) for j in ligne.split("-")]
                chevauchement = False
                print("test" , start, end)
                starts = [start]
                ends = [end]
                for i, plage in enumerate(frais):
                        so, eo = plage
                        if start <= eo and start >= so or end >= so and end <= eo or start <= so and end >= eo:
                                starts.append(so)
                                ends.append(eo)
                                frais[i] = [-1,-1]
                
                frais.append([min(starts), max(ends)])
                        
for plage in frais:
        start, end = plage
        if start != -1:
            somme += end - start +1


print(frais)
print(somme)

end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Le programme a dure {elapsed_time_ms:.2f} ms est la reponse est")
