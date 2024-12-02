
with open('adventOfCode/2024/input.txt', encoding="UTF-8", mode= "r") as file:  
        lignes = file.read().splitlines()

def validite_ligne(ligne):
        first = ligne[0] - ligne[1]
        if first == 0:
                return 0
        elif first > 0 :
            for i in range(len(ligne)-1):
                   if not(0 < ligne[i] - ligne[i+1] <= 3):
                          return i
        else:
            for i in range(len(ligne)-1):
                   if not(-3 <= ligne[i] - ligne[i+1] < 0):
                          return i 
                          
        return -1        
                

safe = 0

for ligne in lignes:
        ligne = [int(i) for i in ligne.split()]
        validity = validite_ligne(ligne)
        if validity == -1:
               safe += 1
        else:

            ligne0 = ligne.copy()
            ligne1 = ligne.copy()
            ligne2 = ligne.copy()
            del ligne0[validity-1]
            del ligne1[validity]
            del ligne2[validity+1]


            v0 = validite_ligne(ligne0)
            v1 = validite_ligne(ligne1)
            v2 = validite_ligne(ligne2)
            if v0 == -1 or v1 == -1 or v2 == -1 : 
                   safe += 1

print(safe)