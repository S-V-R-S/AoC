def creer_tab():
        with open('adventOfCode/2024/input.txt', encoding="UTF-8", mode= "r") as file:  
                lignes = file.read().splitlines()
        return lignes


def correct_order(dico, liste):
       for i in range(len(liste)):
             temp = liste[:i]
             if liste[i] in dico:
                temp += dico[liste[i]]
                if len(temp) != len(set(temp)):
                    return False
       return True

lignes = creer_tab()

dico = {}

to_print = []

for line in lignes:
    if '|' in line:
           x ,y = map(int, line.split("|"))
           if x not in dico:
                dico[x] = []  
           dico[x].append(y)

    elif line != "":
           to_print.append(line)

somme = 0
for line in to_print:
       liste = list(map(int, line.split(",")))
       if correct_order(dico, liste):
              milieu = len(liste) //2 
              somme+=liste[milieu]
              

print(somme)

