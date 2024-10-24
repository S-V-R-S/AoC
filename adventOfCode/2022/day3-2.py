def lire(nom: str):

    with open(nom, encoding="UTF-8", mode= "r") as file:  
            lignes = file.readlines()
    return lignes

score = 0
index = 0
bags = [""]*3
for ligne in lire('adventOfCode/2022/input.txt'):
    if(ligne.strip() != ""):
        bags[index] = ligne.strip()
        
    if index == 2:
        index = 0
        sameLetter = "".join(set(bags[0]).intersection(set(bags[1])).intersection(set(bags[2])))

        if sameLetter.islower():
             score += ord(sameLetter) + 1 - ord("a")
             print(sameLetter)
        else:
             score += ord(sameLetter) + 27 - ord("A")
             print(sameLetter)
    else:
        index +=1

print(score)


