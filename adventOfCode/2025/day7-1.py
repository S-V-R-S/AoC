
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
                start = [i,j]
                matrice[i][j] = "|"

division = 0
for i in range(len(matrice)-1):
    for j in range(len(matrice[0])):
        if matrice[i][j] == "|":
            print(i,j)
            if matrice[i+1][j] == ".":
                matrice[i+1][j] = "|"
            elif matrice[i+1][j] == "^":
                division += 1
                if matrice[i+1][j-1] == ".":
                    matrice[i+1][j-1] = "|"
                if matrice[i+1][j+1] == ".":
                    matrice[i+1][j+1] = "|"

print(division)


        
end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Le programme a dure {elapsed_time_ms:.2f} ms est la reponse est")
# 13 minutes