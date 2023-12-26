import re
from collections import deque

f = open("advent code 2023\\test.txt","r")
lignes = f.read()
f.close()
lignes= lignes.split("\n")
dico = {}
dico_input_con = {}
for ligne in lignes:
    name, destination = ligne.split("->")
    dico[re.findall('[a-zA-Z]+',name)[0]] = {'type': name[0], 'etat': False, 'last': 'low', "destinations": [v.strip() for v in destination.split(", ")]}
    if name[0] == '&':
        dico_input_con[re.findall('[a-zA-Z]+',name)[0]] = []

for ligne in lignes:
    name, destination = ligne.split("->")
    destination = [v.strip() for v in destination.split(", ")]
    for d in destination:
        if d in dico_input_con:
            dico_input_con[d].append(re.findall('[a-zA-Z]+',name)[0])

print(dico_input_con)

pile = deque([['low', 'broadcaster']])

while pile:
    print(pile)
    p = pile.popleft()
    signalRecu = p[0]
    emetteur = p[1]
    typ = dico[emetteur]['type']
    destinataires = dico[emetteur]['destinations']

    if(typ == 'b'):
        for d in destinataires:
            pile.append([signalRecu, d])

    if(typ == '%'):
        dico[emetteur]['last'] = signalRecu
        if signalRecu == 'low':
            dico[emetteur]['etat'] = not(dico[emetteur]['etat'])
            if dico[emetteur]['etat']:
                signalEnvoye = 'hight'
            else: 
                signalEnvoye = 'low'
            for d in destinataires:
                pile.append([signalEnvoye, d])

    if(typ == '&'):
        allHight = True
        for d in dico_input_con[emetteur]:
            print(d, dico[d]['last'])
            if dico[d]['last'] == 'low':
                allHight = False
                break
        if allHight:
            for d in destinataires:
                pile.append(['low', d])
        else:
            for d in destinataires:
                pile.append(['hight', d])

print(dico)



