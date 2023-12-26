import re

def contains_bigger(nbr: int, liste: list):
     contains = False
     for i in liste:
        if(int(i)>int(nbr)):
             contains = True
             break
     return contains

def sumGames(nom: str):
    with open(nom, encoding="UTF-8", mode= "r") as file:  
            somme = 0
            incre = 1
            for ligne in file: 
                ligne = ligne.split(":")[1]
                tirage = ligne.split(";")
                print(ligne)
                for col in tirage:
                    erreur = False
                    couleur = col.split(",")
                    for possibility in couleur:
                         if(len(re.findall("red", possibility))>0 and contains_bigger(12,re.findall("\d+", possibility))
                            or len(re.findall("blue", possibility))>0 and contains_bigger(14,re.findall("\d+", possibility))
                            or len(re.findall("green", possibility))>0 and contains_bigger(13,re.findall("\d+", possibility))):
                              erreur = True
                              break
                    if(erreur):                                                 
                         break
                if(not(erreur)):
                    print(incre) 
                    somme +=incre
                
                incre += 1
    return somme
def puissance(nom: str):
    with open(nom, encoding="UTF-8", mode= "r") as file:  
            somme = 0
            for ligne in file: 
                ligne = ligne.split(":")[1]
                tirage = ligne.split(";")
                maxPerCol = [0,0,0]
                for col in tirage:
                    couleur = col.split(",")
                    for possibility in couleur:
                        if(len(re.findall("red", possibility))>0 and contains_bigger(maxPerCol[0],re.findall("\d+", possibility))):
                            maxPerCol[0] = int(re.findall("\d+", possibility)[0])
                        if(len(re.findall("blue", possibility))>0 and contains_bigger(maxPerCol[1],re.findall("\d+", possibility))):
                            maxPerCol[1] = int(re.findall("\d+", possibility)[0])
                        if(len(re.findall("green", possibility))>0 and contains_bigger(maxPerCol[2],re.findall("\d+", possibility))):
                            maxPerCol[2] = int(re.findall("\d+", possibility)[0])
                somme += maxPerCol[0]*maxPerCol[1]*maxPerCol[2]
    return somme
print(puissance("input.txt"))