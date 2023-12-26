import re
def carteGagnante(nom: str):
    with open(nom, encoding="UTF-8", mode="r") as file: 
        scoreTotal = 0 
        for ligne in file: 
            print(ligne)
            ligne = ligne.split(":")[1].split("|")
            reponse = set(re.findall("\d+", ligne[0]))
            prop = set(re.findall("\d+", ligne[1]))
            commun = reponse.intersection(prop)
            if (len(commun)>0):
                scoreTotal += 1 *2**(len(commun)-1)
    return scoreTotal

def nombreDeCarte(nom: str):
    with open(nom, encoding="UTF-8", mode="r") as file: 
        dico = {}
        incre = 1
        nombreTotal = 0 
        for ligne in file: 
            if(incre in dico):
                dico[incre] += 1
            else:
                dico[incre] = 1
            ligne = ligne.split(":")[1].split("|")
            reponse = set(re.findall("\d+", ligne[0]))
            prop = set(re.findall("\d+", ligne[1]))
            score = len(reponse.intersection(prop))
            for i in range(score):
                card = incre +1 +i
                if(card in dico):
                    dico[card] += dico[incre]
                else:
                    dico[card] = dico[incre]
            incre += 1
        for number in dico.values():
            nombreTotal += number
    return nombreTotal
 

print(nombreDeCarte("input.txt"))