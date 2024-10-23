def lire(nom: str):

    with open(nom, encoding="UTF-8", mode= "r") as file:  
            lignes = file.readlines()
    return lignes

score = 0
strategy = {"A": {"X" : "Z", "Y": "X", "Z": "Y"},
            "B": {"X" : "X", "Y": "Y", "Z": "Z"},
            "C": {"X" : "Y", "Y": "Z", "Z": "X"}}

dico = {"X": {"point": 1, "A" : 3, "B": 0, "C": 6},
        "Y": {"point": 2, "A" : 6, "B": 3, "C": 0},
        "Z": {"point": 3, "A" : 0, "B": 6, "C": 3}}
for ligne in lire('adventOfCode/2022/input.txt'):
    if(ligne.strip() != ""):
        opponent, issue = ligne.strip().split(" ")
        play = strategy[opponent][issue]
        score += dico[play]["point"] + dico[play][opponent]

print(score)


