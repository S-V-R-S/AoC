import re
import functools
f = open("advent code 2023\day12-input.txt","r")
# f = open("advent code 2023\\test.txt","r")
lignes = f.readlines()
f.close()

@functools.cache
def nbrCombinaison(pattern, nombre):
    # fin de la recursive
    # la combinaison est viable
    if pattern == "" and nombre == (): return 1
    # la suite est juste . ou ? si ? compter comme . 
    if nombre == () and "#" not in pattern: return 1
    # # la elle est pas viable 
    if pattern == "" and nombre != (): return 0
    if nombre == () and "#" in pattern: return 0

    
    somme = 0
# si c'est un point je poursuis 
    if pattern[0] == ".":
        somme += nbrCombinaison(pattern[1:], nombre)
# si c'est un # est que la suite de #? peut etre de la taille du nombre attendu
    elif pattern[0] in "#":
        if nombre[0] <= len(pattern) and "." not in pattern[:nombre[0]] and (nombre[0] == len(pattern) or pattern[nombre[0]] != "#"):
            somme += nbrCombinaison(pattern[nombre[0] + 1:], nombre[1:])
# si c'est un ? je test avec un . et avec un #
    else:
        somme += nbrCombinaison(pattern[1:], nombre)
        if nombre[0] <= len(pattern) and "." not in pattern[:nombre[0]] and (nombre[0] == len(pattern) or pattern[nombre[0]] != "#"):
            somme += nbrCombinaison(pattern[nombre[0] + 1:], nombre[1:])

    return somme

somme = 0
for ligne in lignes:
    pattern, nombre = ligne.split(" ")
    nombre = tuple(int(n) for n in nombre.split(","))
    somme += nbrCombinaison(pattern, nombre)

# partie1 6949
print("partie1", somme)

somme = 0
for ligne in lignes:
    pattern, nombre = ligne.split(" ")
    pattern = "?".join(pattern for i in range(5))

    nombre = [int(n) for n in nombre.split(",")]
    nbr = []
    for i in range(5):
        for n in nombre:
            nbr.append(n)
    nombre = tuple(nbr)
    somme += nbrCombinaison(pattern, nombre)

# partie2 51456609952403
print("partie2", somme)