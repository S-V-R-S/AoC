f = open("input.txt","r")
lignes = f.read()
f.close()

bloc = lignes.split("\n")

dico = {}
for c in range(len(bloc[0])):
    dico[c] = {"O": [], "#":[]}
    for l in range(len(bloc)):

        if(bloc[l][c] == "O"): dico[c]["O"].append(len(bloc)-l)
        if(bloc[l][c] == "#"): dico[c]["#"].append(len(bloc)-l)
poidsGlobal = 0
for i, valeurs in dico.items():
    decompte = len(bloc)
    place = len(valeurs['O'])
    poids = 0 
    for l in range(len(bloc)):

        if(place == 0):
            break
        elif(decompte in valeurs['#']):
            del valeurs["#"][0]
        elif(len(valeurs['#'])==0):
            poids+=decompte
            del valeurs['O'][0]
            place -= 1
        elif(valeurs['O'][0]>valeurs['#'][0]):
            poids+=decompte
            del valeurs['O'][0]
            place -= 1
        decompte -= 1


    poidsGlobal+= poids

print(poidsGlobal)

