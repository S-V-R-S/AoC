import re


def nombre(nbr: int,liste:list):
    score = 0
    for i in liste:
        if(nbr==i):
            score += 1
    return score

def lettreJ(lettre: str,liste:list):
    score = 0
    for i in liste:
        if(lettre==i):
            score += 1
    return score

f = open("day7-input.txt","r")
lignes = f.readlines()
f.close()

liste = []
for i in lignes:
    liste.append([i.split(" ")[0], int(i.split(" ")[1])])

possibilite = ['five', 'four','full', 'three', 'two', 'one', 'high']
cartes = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
cartesRang = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

mains = [""]*len(liste)


for main in range(len(liste)):
    jeu = liste[main][0]
    score = [0]*len(cartes)
    j = lettreJ("J", jeu)
    for lettre in jeu:
        for carte in cartes:
            if(lettre==carte):
                score[cartes.index(carte)] += 1
    
    if(5 in score or j>= 4 or 3 in score and j == 2 or 2 in score and j == 3 or 4 in score and j == 1):
        mains[main] = 'five'
    elif(4 in score or 3 in score and j == 1 or 2 in score and j == 2 or j == 3):
        mains[main] = 'four'
    elif(3 in score and 2 in score or nombre(2,score)==2 and j == 1):
        mains[main] = 'full'
    elif(3 in score or j == 2):
        mains[main] = 'three'
    elif(nombre(2,score)==2):
        mains[main] = 'two'
    elif(2 in score and j == 1):
        mains[main] = 'three'
    elif(2 in score or j ==1):
        mains[main] = 'one'
    else:
        mains[main] = 'high'

for r in range(len(liste)):
    chaine = str(possibilite.index(mains[r]))
    for lettre in liste[r][0]:
        chaine += alphabet[cartesRang.index(lettre)]
    liste[r][0] = chaine

liste_triee = sorted(liste, key=lambda x: x[0])

reponse = 0
for i in range(len(liste)):
    reponse += (len(liste)-i)*int(liste_triee[i][1])

print(reponse)


    


