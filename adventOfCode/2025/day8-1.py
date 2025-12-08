
import time
start_time = time.time()


with open('adventOfCode/2025/test.txt', encoding="UTF-8", mode= "r") as file:  
        lignes = file.read().splitlines()

boitiers = []

for ligne in lignes:
        x,y,z = [int(i) for i in ligne.split(",")]
        boitiers.append((x,y,z))

distance_dict = {}
distances = set()
for i,b in enumerate(boitiers):
        for j in range(i+1, len(boitiers)):
                b2 = boitiers[j]
                d = ((b2[0] - b[0])**2 + (b2[1] - b[1])**2 + (b2[2] - b[2])**2) ** 0.5
                distances.add(d)
                if d in distance_dict:
                        print("pb")
                distance_dict[d] = (b, b2)

distances = sorted(distances)
print("sorted")
groupes = []
dico = {}

for i in range(1000):
        print(i)
        distance = distances[0]
        del distances[0]

        b, b1 = distance_dict[distance]

        if b in dico and not(b1 in dico):
            for liste in groupes:
                    if b in liste:
                            liste.append(b1)
                            dico[b1] = ""
                            break
            
        elif b1 in dico and not(b in dico):
            for liste in groupes:
                    if b1 in liste:
                            liste.append(b)
                            dico[b] = ""
                            break 
            
        elif b1 in dico and b in dico:
                total = []

                for j, liste in enumerate(groupes):
                    if b1 in liste:
                            l1 = liste
                            total += liste
                    
                    if b in liste:
                           l = liste
                           total += liste
                groupes.remove(l)
                if l != l1:
                    groupes.remove(l1)
                groupes.append(total)

                

        else:  
            dico[b] = ""
            dico[b1] = ""
            groupes.append([b, b1])

taille = [len(set(i)) for i in groupes]
taille.sort()
print(taille[-1]*taille[-2]*taille[-3])
end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Le programme a dure {elapsed_time_ms:.2f} ms est la reponse est")
