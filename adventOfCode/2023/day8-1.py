import re 

def contient_des_lettres(ligne):
    for caractere in ligne:
        if caractere.isalpha():
            return True
    return False


f = open("adventOfCode\\2023\\input8.txt","r")
lignes = f.readlines()
f.close()

instruction = lignes[0][:-1]
del lignes[0]
dico = {} 
for ligne in lignes: 
    if(contient_des_lettres(ligne)):
        ligne = ligne.split("=")
        dico[ligne[0].strip()] = {"L": ligne[1].split(',')[0][2:], "R": ligne[1].split(',')[1][1:4]}


lieu = 'AAA'
arrivee = 'ZZZ'
step = 0
incre = 0

while(lieu != arrivee):
    lieu = dico[lieu][instruction[incre]]
    step += 1
    incre +=1
    if(incre == len(instruction)):
        incre = 0
    
print(step)