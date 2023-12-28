from collections import deque
from functools import reduce
from math import gcd


def plus_petit_multiple(a, b):
    return abs(a * b) // gcd(a, b)

def ppm_pour_une_liste(zendliste):
    return reduce(plus_petit_multiple, zendliste)

f = open("adventOfCode\\2023\\input20.txt","r")
lignes = f.readlines()
f.close()

modules = {}
origine = []
for l in lignes:
    module, destinataires = l.strip().split("->")
    module = module.strip()
    destinataires =[d.strip() for d in destinataires.split(",")]
    if module == "broadcaster": start = destinataires
    else: modules[module[1:]] = {'type': module[0], "etat": False, 'destinataires': destinataires}
    
for module, valeurs in modules.items():
    destinataires = valeurs['destinataires']
    for d in destinataires:
        if d == 'rx':
            origine.append(module)
        if d not in modules:
            continue
        if modules[d]['type'] == '&':
            if modules[d]['etat'] == False: modules[d]['etat'] = {}
            modules[d]['etat'][module] = 'low'

print(origine)
temp = dict(modules[origine[0]]['etat'])
for i in temp.keys():
    temp[i] = []
print(temp)
low = hight = 0

for j in range(1,10000):
    low += 1
    pile = deque([('broadcaster', d, 'low') for d in start])
    while pile:
        emetteur, destinataire, pulse = pile.popleft()
        if pulse == "low": low += 1
        else: hight += 1

        if destinataire == origine[0] and pulse =='hight':
            temp[emetteur].append(j)

        if destinataire not in modules:
            continue

        next = modules[destinataire]

        if next['type'] == '%':
            if pulse == 'low':
                if next['etat'] == False: nextPulse = 'hight'
                else: nextPulse = 'low'

                next['etat'] = not(next['etat'])
                for d in next['destinataires']:
                    pile.append((destinataire, d, nextPulse))
        else:
            allHight = True
            modules[destinataire]['etat'][emetteur] = pulse
            for i in next['etat'].values():
                if i  == 'low': 
                    allHight = False
                    break
            if allHight:
                nextPulse = 'low'
            else: nextPulse = 'hight'

            for d in next['destinataires']:
                    pile.append((destinataire, d, nextPulse))


endliste = []
for j in temp.values():
    endliste.append(j[0])
print(ppm_pour_une_liste(endliste))
