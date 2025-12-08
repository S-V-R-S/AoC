
import time
start_time = time.time()


def creer_matrice():
    with open('adventOfCode/2025/test.txt', encoding="UTF-8", mode= "r") as file:  
        lignes = file.read().splitlines()
        matrice = []
        for i, ligne in enumerate(lignes):
            matrice.append([])
            for j, letter in enumerate(ligne.split()):
                matrice[i].append(letter)
    return matrice



total = 0
matrice = creer_matrice()
print(matrice)
for colonne in range(len(matrice[0])):
    calcul = matrice[-1][colonne]
    if calcul == "*":
        somme = 1
    else:
        somme = 0
    print(calcul)
    for j in range(len(matrice)-1):
        print(int(matrice[j][colonne]))
        if calcul == "*":
            somme *= int(matrice[j][colonne])
            print(somme)
        else:
            somme += int(matrice[j][colonne])
        
    total += somme



print(total)
        
end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Le programme a dure {elapsed_time_ms:.2f} ms est la reponse est")
