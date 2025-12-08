
import time
start_time = time.time()


def creer_matrice():
    with open('adventOfCode/2025/test.txt', encoding="UTF-8", mode= "r") as file:  
        lignes = file.read().split("\n")
        matrice = []
        for i, ligne in enumerate(lignes):
            matrice.append([])
            for j, letter in enumerate(ligne):
                matrice[i].append(letter)
    return matrice



total = 0
matrice = creer_matrice()
print(matrice)
increment = 0
while increment<len(matrice[0]):
    tour = 1
    calcul = matrice[-1][increment]
    
    while  increment + tour < len(matrice[0]) and matrice[-1][increment + tour] == ' ':
        tour += 1
    
    if tour + increment == len(matrice[0]):
        tour +=1
    nombres = []
    for i in range(tour-1):
        nombre = ""
        for j in range(len(matrice)-1):
            if matrice[j][increment+i] != " ":
                nombre += matrice[j][increment+i]
        nombres.append(int(nombre))
    if calcul == "*":
        somme = 1
    else:
        somme = 0

    for l in nombres:
        if calcul == "*":
            somme *= int(l)
        else:
            somme += int(l)
    print(nombres)
    print(somme)      
    total += somme
    increment += tour



print(total)
        
end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Le programme a dure {elapsed_time_ms:.2f} ms est la reponse est")
