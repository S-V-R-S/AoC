import re

def lire(nom: str):

    with open(nom, encoding="UTF-8", mode= "r") as file:  
            lignes = file.readlines()
    return lignes

# fct qui fait les changements
def move(dico, consigne):
     nbrBlocs, origine, destination = map(int, re.findall(r'\d+', consigne))
     blocs = dico[origine][-nbrBlocs:]
     dico[origine] = dico[origine][:-nbrBlocs]
     dico[destination] = dico[destination] + blocs
     return dico




# construction du dico 
lignes = lire('adventOfCode/2022/input.txt')
nbrColonnes = (len(lignes[0]))//4
dico = {}
for i in range(1,nbrColonnes+1):
     dico[i] = []

for ligne in lignes:
    # si c'est une ligne du depart qui permet de representer letat initial
    if(ligne[0] != "m" and (len(ligne)> 1 and ligne[1] != "1") and ligne.strip() != ""):
         for i in range(1,nbrColonnes+1):
              if (ligne[1 + 4*(i-1)] != " "):
                   dico[i].insert(0,(ligne[1 + 4*(i-1)]))
    # sinon c'est une ligne de mouvement 
    elif(ligne[0] == "m"):
       move(dico, ligne)
    



reponse = ""
# print les premiers sacs de chaque colonne
for i in range(1, nbrColonnes+1):
     reponse += dico[i][-1]

print(reponse)