import re

def hash(ch):
    currentValue = 0
    for c in ch:
        ascii = ord(c)
        currentValue += ascii
        currentValue = currentValue*17 % 256
    return currentValue



sequence = ""
f = open("input.txt","r")
lignes = f.readlines()
f.close()

for i, l in enumerate(lignes):
    sequence += l.strip()

sequence = sequence.split(",")

dico = {}
for s in sequence:
    if(len(re.findall("-",s))==1):
        valeur = hash(s[:-1])
        if valeur in dico:
            if s[:-1] in dico[valeur]:
                del dico[valeur][s[:-1]]
    else:
        valeur = hash(s.split("=")[0])
        if(valeur in dico):
            dico[valeur][s.split("=")[0]] = s.split("=")[1]
        else:
            dico[valeur] = {}
            dico[valeur][s.split("=")[0]] = s.split("=")[1]

total = 0

for i in range(256):
    if i in dico:
        if len(dico[i])>0:
            incre = 1
            for key, valeur in dico[i].items():
                total += (i+1)*incre*int(valeur)
                incre += 1
print(total)



