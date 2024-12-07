import itertools

with open('adventOfCode/2024/input.txt', encoding="UTF-8", mode= "r") as file:  
    lignes = file.read().splitlines()

operateurs = ["+","*"]
somme = 0
for ligne in lignes:
    reponse, consignes = ligne.strip().split(":")
    reponse = int(reponse)
    consignes = list(map(int, consignes.split()))
    
    combinations = list(itertools.product(operateurs, repeat=len(consignes)-1))
    combinations_list = [''.join(comb) for comb in combinations]

    for combinaison in combinations_list:
        resultat = consignes[0]
        for j in range(len(consignes)-1):
            if combinaison[j] == "+":
                resultat = resultat + consignes[j+1]
            else:
                resultat = resultat * consignes[j+1]

        if resultat == reponse:
            somme += resultat
            break

# 5540634308362
print(somme)

        

