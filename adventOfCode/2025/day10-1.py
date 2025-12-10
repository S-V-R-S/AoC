import itertools
import time
start_time = time.time()

with open('adventOfCode/2025/test.txt', encoding="UTF-8", mode= "r") as file:  
        lignes = file.read().splitlines()


total = 0
for ligne in lignes:
        parties = ligne.split(" ")
        voyants = parties[0]
        tension = parties[-1]
        boutons = parties[1:-1]
        print(voyants)
        print(tension)
        print(boutons)
        objectif = [i for i in voyants[1:-1]]
        print(objectif)
        
        trouve = False
        nbr = 1
        while not(trouve):
                print("nbr",nbr)
                combinaisons = list(itertools.combinations(boutons, nbr))
                print(combinaisons)
                for sequence in combinaisons:
                        depart = ["." for i in range(len(voyants)-2)]
                        for s in sequence:
                                btns = [int(x) for x in s.strip("()").split(",")]
                                for btn in btns:
                                        if depart[btn] == ".":
                                                depart[btn] = "#"
                                        else:
                                                depart[btn] = "."
                        print(depart, objectif)
                        if depart == objectif:
                                total += nbr
                                trouve = True
                                print(trouve)
                                break
                print(trouve)
                if trouve:
                        continue                
                nbr +=1



print(total)


end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Le programme a dure {elapsed_time_ms:.2f} ms est la reponse est")
