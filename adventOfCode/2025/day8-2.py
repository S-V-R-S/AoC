
import time
start_time = time.time()


with open('adventOfCode/2025/test.txt', encoding="UTF-8", mode= "r") as file:  
        lignes = file.read().splitlines()

boitiers = []

groupes = {}
nb = 1
for ligne in lignes:
        x,y,z = [int(i) for i in ligne.split(",")]
        boitiers.append((x,y,z))
        groupes[(x,y,z)] = nb
        nb += 1

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

end = False

while not(end):
        distance = distances[0]
        del distances[0]

        b, b1 = distance_dict[distance]
        groupe = groupes[b1]
        groupes[b1] = groupes[b]

        for boitier in groupes.keys():
                if groupes[boitier] == groupe:
                        groupes[boitier] = groupes[b]

        same = True
        valeur = groupes[b]
        for boitier in groupes.keys():
            if groupes[boitier] != valeur:
                    same = False
                    break
        end = same

print(b[0]*b1[0])
end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Le programme a dure {elapsed_time_ms:.2f} ms est la reponse est")
