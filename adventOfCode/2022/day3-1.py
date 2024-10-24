def lire(nom: str):

    with open(nom, encoding="UTF-8", mode= "r") as file:  
            lignes = file.readlines()
    return lignes

score = 0

for ligne in lire('adventOfCode/2022/input.txt'):
    if(ligne.strip() != ""):
        letters = ligne.strip()
        length = len(letters)
        middle = length//2
        sameLetter = "".join(set(letters[0:middle]).intersection(set(letters[middle:])))
        if sameLetter.islower():
             score += ord(sameLetter) + 1 - ord("a")
             print(sameLetter)
        else:
             score += ord(sameLetter) + 27 - ord("A")
             print(sameLetter)

print(score)


