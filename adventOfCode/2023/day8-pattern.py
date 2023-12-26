from functools import reduce
from math import gcd


def contient_des_lettres(ligne):
    for caractere in ligne:
        if caractere.isalpha():
            return True
    return False

def se_termine_par_Z(lieu: str):
    return lieu[-1] == "Z"

def plus_petit_multiple(a, b):
    return abs(a * b) // gcd(a, b)

def ppm_pour_une_liste(zendliste):
    return reduce(plus_petit_multiple, zendliste)

f = open("input.txt","r")
lignes = f.readlines()
f.close()

instruction = lignes[0][:-1]
del lignes[0]
dico = {} 
noeuds = []
for ligne in lignes: 
    if(contient_des_lettres(ligne)):
        ligne = ligne.split("=")
        dico[ligne[0].strip()] = {"L": ligne[1].split(',')[0][2:], "R": ligne[1].split(',')[1][1:4]}
        if(ligne[0].strip()[2]=="A"):
            noeuds.append(ligne[0].strip())

step = 0
incre = 0
zend = 0

zendliste = []

for i in range(len(noeuds)):
    zend=0
    incre=0
    step=0

    while(1 != zend):    
        step += 1
        noeuds[i] = dico[noeuds[i]][instruction[incre]]
        if(se_termine_par_Z(noeuds[i])):
            zend +=1
            zendliste.append(step)
        
        incre +=1
        if(incre == len(instruction)):
            incre = 0

print(ppm_pour_une_liste(zendliste))

