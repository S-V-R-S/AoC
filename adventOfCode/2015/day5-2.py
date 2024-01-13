
# OUVERTURE DE L INPUT 
f = open("adventOfCode\\2015\\input5.txt","r")
lignes = f.read().split('\n')
f.close()

def gentil(ligne):
    # ENREGISTRE LES COUPLES 
    pattern = []
    # REGLE 1 
    ecartee = False
    # REGLE 2 
    repetee = False
    # PARCOURS DES LETTES 
    for i in range(len(ligne)-1):
        # POUR NE PAS ETRE OUT RANGE 
        if i <= len(ligne)-3:
            # REGARDE REGLE 1 
            if ligne[i] == ligne[i+2]:
                ecartee = True
        # REGLE 2 
        if str(ligne[i]+ligne[i+1]) in pattern:
            index = pattern.index(str(ligne[i]+ligne[i+1]))
            # VERIFIE QU IL N Y AIT PAS DE CHEVAUCHEMENT 
            if index < i - 1:
                    repetee = True
        else:
            pattern.append(str(ligne[i]+ligne[i+1]))

    # RESPECT DES DEUX REGLE ? 
    return ecartee and repetee

#  INITIALISETAION DES MOTS MOTS GENTILS
compteur_mots_gentils = 0

# POUR CHQUE MOTS 
for ligne in lignes:
        if gentil(ligne):
            compteur_mots_gentils += 1

print(compteur_mots_gentils)
