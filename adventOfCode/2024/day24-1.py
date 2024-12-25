
import time
start_time = time.time()

with open('adventOfCode/2024/input24.txt', encoding="UTF-8", mode= "r") as file:  
    lignes = file.read().splitlines()          

dico = {}
operation = []
z = []
for ligne in lignes:
    if ":" in ligne:
        porte, valeur = ligne.split(": ")
        dico[porte] = int(valeur)
    if "-" in ligne:
        p1, op, p2, f, p3 = ligne.split()
        operation.append([p1, op, p2, f, p3])
        if p1[0] == "z":
            z.append(p1)
        if p2[0] == "z":
             z.append(p2)
        if p3[0] == "z":
             z.append(p3)

for ope in operation:
    p1, op, p2, f, p3 = ope

    if p1 in dico and p2 in dico:
        if op == "AND":
            if dico[p1] == 1 and dico[p2] == 1:
                dico[p3] = 1
            else:
                dico[p3] = 0
        elif op == "OR":
            if dico[p1] == 1 or dico[p2] == 1:
                dico[p3] = 1
            else:
                dico[p3] = 0
        elif op == "XOR":
            if dico[p1] == 1 and dico[p2] == 0 or dico[p1] == 0 and dico[p2] == 1:
                dico[p3] = 1
            else:
                dico[p3] = 0
        else:
            print("erreur", p1, op, p2)
    else:
        operation.append(ope)

reponse = []
for i in range(len(z)):
    reponse.append(0)
for ze in z:
    reponse[int(ze[1:])] = dico[ze]
reponse.reverse()
chaine_binaire = ''.join(map(str, reponse))
decimal = int(chaine_binaire, 2)

print(decimal)       
# 51715173446832   
end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Le programme a dure {elapsed_time_ms:.2f} ms est la reponse est")
