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

def correction(liste, dico):
    # construction of a correct line 
    good = []
    # add number by number
    for i in range(len(liste)):
          index = len(good)  
          if liste[i] in dico:
            # look if none of the previous number has to be after the current number 
            for j in good:
                # if it s the case we add the current number before the element 
                if j in dico[liste[i]]:
                    if good.index(j) < index:
                         index = good.index(j)

          good.insert(index,liste[i])
    return(good)

# gather input 
lignes = creer_tab()

dico = {}
to_print = []

# read the input 
for line in lignes:
    # gather the rule 
    if '|' in line:
           x ,y = map(int, line.split("|"))
           if x not in dico:
                dico[x] = []  
           dico[x].append(y)
    # gather the lists
    elif line != "":
           to_print.append(line)

acorriger = []
for line in to_print:
       liste = list(map(int, line.split(",")))
       if not(correct_order(dico, liste)):
            #   add the list to acorriger if not correct
              acorriger.append(liste)


somme = 0
correct_l = []
for liste in acorriger:
    # correct and add the middle
    somme+= correction(liste, dico)[len(liste) //2 ]
                 
print(somme)