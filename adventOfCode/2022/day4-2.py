def lire(nom: str):

    with open(nom, encoding="UTF-8", mode= "r") as file:  
            lignes = file.readlines()
    return lignes

score = 0

for ligne in lire('adventOfCode/2022/input.txt'):
    if(ligne.strip() != ""):
       first, second = ligne.strip().split(',')
       first = first.split('-')
       second = second.split('-')
       
       if (int(first[0]) <= int(second[0]) and int(first[1]) >= int(second[0])) or (int(first[0]) >= int(second[0]) and int(first[0]) <= int(second[1])):
            print(first,second)
            score += 1

print(score)


