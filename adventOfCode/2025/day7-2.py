
import time
start_time = time.time()



with open('adventOfCode/2025/test.txt', encoding="UTF-8", mode= "r") as file:  
    lignes = file.read().split("\n")
    matrice = []
    for i, ligne in enumerate(lignes):
        matrice.append([])
        for j, letter in enumerate(ligne):
            matrice[i].append(letter)
            if letter =="S":
                matrice[i][j] = 1
            if letter == ".":
                 matrice[i][j] = 0


for i in range(len(matrice)-1):
    for j in range(len(matrice[0])):
        if matrice[i][j] != "^":
            if matrice[i+1][j] != "^":
                matrice[i+1][j] += matrice[i][j]
            elif matrice[i+1][j] == "^":
                if matrice[i+1][j-1] != "^":
                    matrice[i+1][j-1]  += matrice[i][j]
                if matrice[i+1][j+1] != "^":
                    matrice[i+1][j+1]  += matrice[i][j]

somme = 0
for i in matrice[-1]:
    if i != "^":
        somme += i

print(somme)      
end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Le programme a dure {elapsed_time_ms:.2f} ms est la reponse est")
# 12 minutes
# total = 25