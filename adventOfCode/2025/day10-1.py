
import time
start_time = time.time()

with open('adventOfCode/2025/test.txt', encoding="UTF-8", mode= "r") as file:  
        lignes = file.read().splitlines()

appuie = 0

for ligne in lignes:
        parties = ligne.split(" ")
        voyants = parties[0]
        tension = parties[-1]
        boutons = parties[1:-1]
        print(voyants)
        print(tension)
        print(boutons)
        departs = ["." for i in range(len(voyants))]


end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Le programme a dure {elapsed_time_ms:.2f} ms est la reponse est")
