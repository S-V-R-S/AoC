def lire(nom: str):

    with open(nom, encoding="UTF-8", mode= "r") as file:  
            lignes = file.readlines()
    return lignes

score = 0
dico = {"X": {"point": 1, "A" : 3, "B": 0, "C": 6},
        "Y": {"point": 2, "A" : 6, "B": 3, "C": 0},
        "Z": {"point": 3, "A" : 0, "B": 6, "C": 3}}
for ligne in lire('adventOfCode/2022/input.txt'):
    if(ligne.strip() != ""):
        opponent, mine = ligne.strip().split(" ")
        score += dico[mine]["point"] + dico[mine][opponent]

print(score)


