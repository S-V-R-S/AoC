import re

def lire(nom: str):

    with open(nom, encoding="UTF-8", mode= "r") as file:  
            lignes = file.readlines()
    return lignes

def recuperer_enfants(parent: str):
     to_explore = []
     to_explore.append(parent)
     liste_enfants = []

     while len(to_explore) != 0 : 
          for enfant in dossiers[to_explore[0]].keys():
               if dossiers[to_explore[0]][enfant] == "dir":
                    if enfant not in liste_enfants:
                         liste_enfants.append(enfant)
                         to_explore.append(enfant)

          del(to_explore[0])
     return liste_enfants

# recuperation ligne
lignes = lire('adventOfCode/2022/input.txt')
currentDir = ""

dossiers = {}

# construction dico
for ligne in lignes:
    if ligne[0] == "$":
        if ligne[2] == "c":
             destination = ligne.strip().split(' ')[2]
             if destination == "..":
                  print("ligne",ligne, currentDir, "fin", dossiers)
                  destination = dossiers[currentDir]["parent"]
                  currentDir = destination
             else: 
                if destination not in dossiers :
                    dossiers[destination] = {}
                    dossiers[destination]["parent"] = currentDir
                    if currentDir != "":
                        dossiers[currentDir][destination] = "dir"
                currentDir = destination      
    else : 
         info, name = ligne.strip().split(' ')
         if info != "dir":
              dossiers[currentDir][name] = info

        
# calcul somme par dossier
sommeGlobale = 0

tailleDossier = {}

for cle in dossiers.keys():
     somme = 0
     for cle2 in dossiers[cle].keys():
          if cle2 != "parent" and dossiers[cle][cle2] != "dir":
               somme += int(dossiers[cle][cle2])
     if cle not in tailleDossier:
          tailleDossier[cle] = somme

# il manque que si e est dans a alors compte e dans a 
for cle in dossiers.keys():
     somme = tailleDossier[cle]
     for i in recuperer_enfants(cle):
          somme += tailleDossier[i]
     if somme < 100000:
          sommeGlobale += somme

print(sommeGlobale)
