import itertools

with open('adventOfCode/2024/input.txt', encoding="UTF-8", mode= "r") as file:  
    lignes = file.read().splitlines()

operateurs = ["+","*"]
somme = 0
for ligne in lignes:
    reponse, consignes = ligne.strip().split(":")
    reponse = int(reponse)
    consignes = list(consignes.split())
    
    combinations = list(itertools.product(operateurs, repeat=len(consignes)-1))
    combinations_list = [''.join(comb) for comb in combinations]

    for combinaison in combinations_list:
        resultat = consignes[0]

        for j in range(len(consignes)-1):
            resultat = resultat + combinaison[j] + consignes[j+1]

        additions = resultat.split("+")
        calcul = 0
        for addition in additions:
            multiplications = list(map(int,addition.split("*")))
            result_multiplications = 1

            for i in multiplications:
                    result_multiplications *= i
            calcul += result_multiplications

        if calcul == reponse:
            somme += calcul


print(somme)

        

