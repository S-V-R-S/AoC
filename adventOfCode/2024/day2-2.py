import re
import math
from heapq import heappush, heappop
from enum import Enum
                 

def creer_tab():
        with open('adventOfCode/2024/input.txt', encoding="UTF-8", mode= "r") as file:  
                lignes = file.read().splitlines()
        return lignes

       
lignes = creer_tab()

safe = 0

def verifier_ligne(ligne):
     ecart = ligne[0] - ligne[1]

     if ecart > 0:
          for i in range(0, len(ligne)-1):
               if not(0 < ligne[i] - ligne[i+1] <= 3):
                  return i + 1
     if ecart < 0:
          for i in range(0, len(ligne)-1):
               if not(-3 <= ligne[i] - ligne[i+1] < 0):
                  return i + 1
     if ecart == 0:
          return 1
     
     return True

for ligne in lignes:
     ligne = [int(v) for v in ligne.split()]

     result = verifier_ligne(ligne)

     if str(result).isdigit():
        for i in range(len(ligne)):
             lignetmp = ligne.copy()
             del lignetmp[i]
             result = verifier_ligne(lignetmp)
             if not(str(result).isdigit()):
                  break


 
     if not(str(result).isdigit()):
          safe += 1


print(safe)

