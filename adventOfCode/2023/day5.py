import re
import math

def contient_des_lettres(ligne):
    for caractere in ligne:
        if caractere.isalpha():
            return True
    return False

def read_input(nom: str) -> list[str]:
    with open(nom) as f:
        lines = f.read().splitlines()
    return lines

def soil(nom: str):
    cles = []
    with open(nom, encoding="UTF-8", mode="r") as file: 
        dico = {}
        lignes = file.readlines()
        starters = lignes[0].split(" ")
        del starters[0]
        del lignes[0]
        for ligne in lignes: 
            if(contient_des_lettres(ligne)):
                newCle = ligne.split(' ')[0]
                dico[newCle] = {}
                cles.append(newCle)
                
            elif len(ligne)>1:
                numbers = re.findall("\d+", ligne)   
                for i in range(int(numbers[2])):
                    dico[newCle][int(numbers[1])+i] = int(numbers[0]) + i
        
        distance = []
        for start in starters:
            start = int(start)
            for cle in cles:
                if( start in dico[cle]):
                    start = dico[cle][start]
            distance.append(start)              


    return min(distance)
# print(soil("input.txt"))

def dico(nom: str):
    cles = []
    with open(nom, encoding="UTF-8", mode="r") as file: 
        dico = {}
        lignes = file.readlines()
        starters = lignes[0].split(" ")
        del starters[0]
        del lignes[0]
        for ligne in lignes: 
            if(contient_des_lettres(ligne)):
                newCle = ligne.split(' ')[0]
                dico[newCle] = []
                cles.append(newCle)
                
            elif len(ligne)>1:
                numbers = re.findall("\d+", ligne)   
                dico[newCle].append({'start': int(numbers[1]), 'end':int(numbers[1])+int(numbers[2]) -1, 'range': int(numbers[0])-int(numbers[1])})
        
        distance = []
        for start in starters:
            start = int(start)
            for cle in cles:
                for poss in dico[cle]:
                    if(start>= poss['start'] and start<= poss['end']):
                        start = start +poss['range']
                        break
            distance.append(start)

        return min(distance)


def dico2(nom: str):
    cles = []
    dico = {}
    starters = {}

    lignes = read_input(nom)
    
    starters = re.findall("\d+", lignes[0])
    del lignes[0]
    for ligne in lignes: 
        if(contient_des_lettres(ligne)):
            newCle = ligne.split(' ')[0]
            dico[newCle] = []
            cles.append(newCle)
            
        elif len(ligne)>1:
            numbers = re.findall("\d+", ligne)   
            dico[newCle].append({'start': int(numbers[1]), 'end':int(numbers[1])+int(numbers[2]) -1, 'range': int(numbers[0])-int(numbers[1])})
    
    distance = math.inf

    for i in range(0, len(starters), 2):
        print(i)
        for j in range(int(starters[i+1])):
            start = int(starters[i])+j
            for cle in cles:
                for poss in dico[cle]:
                    if(start>= poss['start'] and start<= poss['end']):
                        start = start + poss['range']
                        break
            distance = min(distance, start)

    return distance


    



print(dico2("test.txt"))