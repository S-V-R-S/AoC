
import time
start_time = time.time()

import re
import os



with open('adventOfCode/2025/input1.txt', encoding="UTF-8", mode= "r") as file:  
# with open('adventOfCode/2025/test.txt', encoding="UTF-8", mode= "r") as file:  
        lignes = file.read().splitlines()

compteur = 0
pointeur = 50 

for ligne in lignes:
        direction = ligne[0]
        nombre = int(ligne[1:])
        
        if direction == "L":
                while nombre > pointeur:
                        nombre = nombre - pointeur - 1
                        if pointeur != 0:
                                compteur +=1
                        pointeur = 99

                pointeur = pointeur - nombre
                if pointeur == 0:
                       compteur += 1
        else:
                while nombre + pointeur > 99:
                        nombre = nombre - (99 - pointeur + 1)
                        compteur +=1
                        pointeur = 0
                        
                pointeur = pointeur + nombre
        
print(compteur)       

end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Le programme a dure {elapsed_time_ms:.2f} ms est la reponse est")

                
# 5961

























end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Le programme a dure {elapsed_time_ms:.2f} ms est la reponse est")
