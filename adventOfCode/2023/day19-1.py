import re


f = open("advent code 2023\\input.txt","r")
lignes = f.read()
f.close()
lignes= lignes.split("\n\n")

workflow_data = lignes[0].split("\n")

piece_data = lignes[1].split("\n")
 
pieces = []
for p in piece_data:
    p = p[1:-1]
    p = p.split(",")
    pieces.append({"x": int(p[0].split("=")[1]),
                   "m": int(p[1].split("=")[1]),
                   "a": int(p[2].split("=")[1]),
                   "s": int(p[3].split("=")[1])})

worflows = {}
for w in workflow_data:
    w =  w[:-1]
    key, regles = w.split("{")
    worflows[key] = regles.split(',')

score = 0
for p0 in pieces:
    nextStep = "in"
    pos = 0

    while nextStep not in "AR":
        
        
        regle = worflows[nextStep][pos]
        nombre = int(re.findall('\d+', regle)[0])
        lettre = regle[0]
        if regle[1] == "<" and p0[lettre] < nombre or regle[1] == ">" and p0[lettre] > nombre:
            nextStep = regle.split(':')[1]
            pos = 0
        else: 
            pos += 1
            regle = worflows[nextStep][pos]
            if ">" not in regle and "<" not in regle:
                nextStep = regle
                pos = 0

    if nextStep =="A": 
        for l in "xmas":
            score+=p0[l]

print(score)





