import re
import os


def joindre(tab: []):
    tableau = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    nbr = ""
    if(tab[0] in tableau):    
        nbr += str(int(tableau.index(tab[0]))+1)
    else:
         nbr+= tab[0]
    if(tab[-1] in tableau):    
        nbr += str(int(tableau.index(tab[-1]))+1)
    else:
         nbr+= tab[-1]
    return int(nbr)

def regex(var: str):
    taille = len(var)
    tab = [""]*taille
    incr = 0
    for i in range(taille):
        tableau = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        if(var[i].isdigit()):
            tab[incr] = var[i]
        for nbr in tableau:
            if(var[i:min(i+len(nbr),taille-1)] == nbr):
                tab[incr] = var[i:min(i+len(nbr),taille-1)]
        incr += 1
    new_tab = [valeur for valeur in tab if valeur != '']
    return new_tab  

def calibre(nom: str):
    with open(nom, encoding="UTF-8", mode= "r") as file:  
            somme = 0
            for ligne in file: 
                nbr = re.findall("\d", ligne)
                somme+= joindre(nbr)
    return somme

def calibre2(nom: str):
    with open(nom, encoding="UTF-8", mode= "r") as file:  
            somme = 0
            for ligne in file: 
                nbr =regex(ligne)
                somme+= joindre(nbr)
    return somme

print(calibre2("input.txt"))
