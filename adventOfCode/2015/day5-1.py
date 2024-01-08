
# OUVERTURE DE L INPUT 
f = open("adventOfCode\\2015\\input5.txt","r")
lignes = f.read().split('\n')
f.close()

# IL EN FAUT AU MOINS TROIS 
voyelle = 'aeiou'
# IL FAUT AU MOINS UNE LETTRE QUI APPARAIT DEUX FOIS DE SUITE 
# NE CONTIENT PAS
bad_word = ['ab', 'cd', 'pq', 'xy']

# INITIALISETAION DES MOTS MOTS GENTILS
compteur_mots_gentils = 0

# POUR CHQUE MOTS 
for ligne in lignes:
    # INITIALISATION DU COMPTEUR DE VOYELLE
    compteur_voyelle = 0
    # INITIALISATION DES DEUX BOOLEENS 
    bad = False
    meme_lettre = False

    # PARCOURS DES LETTES 
    for i in range(len(ligne)-1):
        # MAJ DU COMPTEUR DES VOYELLES 
        if ligne[i] in voyelle:
            compteur_voyelle +=1
        # REGARDE SI ON A DEUX LETTRES IDENDIQUES QUI SE SUIVENT 
        if ligne[i] == ligne[i+1]:
             meme_lettre = True
        # REGARDE SI LES DEUX LETTRES APPARTIENNENT A LA LISTE BAD WORD 
        if ligne[i] + ligne[i+1] in  bad_word:
             bad = True

    # ON REGARDE POUR LA DERNIERE LETTRE 
    if ligne[-1] in voyelle:
            compteur_voyelle +=1

    # SI LES CONDITIONS SONT RESPECTEES ON INCREMENTE LE COMPTEUR 
    if compteur_voyelle > 2 and not(bad) and meme_lettre:
         compteur_mots_gentils += 1

print(compteur_mots_gentils)