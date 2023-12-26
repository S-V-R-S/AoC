import re
def outil(nom: str):
    with open(nom, encoding="UTF-8", mode="r") as file:  
        somme = 0
        matrice = []
        for ligne in file: 
            # Créer une liste pour chaque ligne
            ligne_liste = []
            for caractere in ligne:
                ligne_liste.append(caractere)
            # Ajouter la liste à la matrice
            matrice.append(ligne_liste)
        with open(nom, encoding="UTF-8", mode="r") as file:  
            incre = 0   
            for ligne in file:  
                for match in re.finditer('\d+', ligne):
                        nbr = match.group()
                        indexN = match.start()
                        cote = False
                        for ch in range(len(nbr)):
                            if(incre != 0):
                                if(not(matrice[incre-1][indexN+ch].isdigit() or matrice[incre-1][indexN+ch]==".")):
                                    cote = True
                                    break
                            if(incre != (len(matrice)-1)):
                                if(not(matrice[incre+1][indexN+ch].isdigit() or matrice[incre+1][indexN+ch]==".")):
                                    cote = True
                                    break
                        #a gauche
                        if(indexN != 0):
                            if(not(matrice[incre][indexN-1].isdigit() or matrice[incre][indexN-1]==".")):
                                cote = True
                        #a droite
                        if(indexN+len(nbr)+1 != len(ligne)):
                            if(not(matrice[incre][indexN+len(nbr)].isdigit() or matrice[incre][indexN+len(nbr)]==".")):
                                cote = True
                        #diagonale haut gauche
                        if(indexN != 0 and incre!=0):
                            if(not(matrice[incre-1][indexN-1].isdigit() or matrice[incre-1][indexN-1]==".")):
                                cote = True
                                

                        #diagonale bas gauche
                        if(indexN != 0 and incre!=(len(matrice)-1)):
                            if(not(matrice[incre+1][indexN-1].isdigit() or matrice[incre+1][indexN-1]==".")):
                                cote = True
                                
                                
                        #diagonale haut droite
                        if(indexN+len(nbr)+1 != len(ligne) and incre!=0):
                            if(not(matrice[incre-1][indexN+len(nbr)].isdigit() or matrice[incre-1][indexN+len(nbr)]==".")):
                                cote = True
                                                               
                        #diagonale bas droite
                        if(indexN+len(nbr)+1 != len(ligne) and incre!=(len(matrice)-1)):
                            if(not(matrice[incre+1][indexN+len(nbr)].isdigit() or matrice[incre+1][indexN+len(nbr)]==".")):
                                cote = True
                        if(cote):    
                                               
                            somme += int(nbr)

                incre+=1
    return somme


def outil2(nom: str):
    with open(nom, encoding="UTF-8", mode="r") as file:  
        somme = 0
        matrice = []
        for ligne in file: 
            matrice.append(ligne)
        with open(nom, encoding="UTF-8", mode="r") as file:  
            incre = 0   
            for ligne in file:  
                for match in re.finditer('\*', ligne):
                        indexE = match.start()
                        liste = []
                        multi = 0
                        if(incre!=0):
                            for match in re.finditer("\d+", matrice[incre-1]):                                
                                nbr= match.group()
                                indexN = match.start()
                                if(indexE>= indexN-1 and indexE<=indexN+len(nbr)):
                                    liste.append(nbr)
                        
                        if(incre!=len(matrice)-1):
                            for match in re.finditer("\d+", matrice[incre+1]):                                
                                nbr= match.group()
                                indexN = match.start()
                                if(indexE>= indexN-1 and indexE<=indexN+len(nbr)):
                                    liste.append(nbr)
                                    
                        if(indexE!=0):
                            for match in re.finditer("\d+", matrice[incre]):                                
                                nbr= match.group()
                                indexN = match.start()
                                if(indexE==indexN+len(nbr)):
                                    liste.append(nbr)
                        if(indexE!=len(ligne)-1):
                            for match in re.finditer("\d+", matrice[incre]):                                
                                nbr= match.group()
                                indexN = match.start()
                                if(indexE==indexN-1):
                                    liste.append(nbr)
                        if(len(liste)>1):
                            multi = 1
                            for trouve in liste:
                                multi = multi*int(trouve)
                        somme += multi

                incre += 1
    return somme

print(outil2("input.txt"))