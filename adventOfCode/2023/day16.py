
# LECTURE DU FICHIER A RECUPERER
f = open("test.txt","r")
lignes = f.read()
f.close()

# INITIALISATION DE DEUX MATRICES
    # MATRICE DU FICHIER 
matrice = []
    # MATRICE DE LA MEME TAILLE QUI SERVIRA A ENREGISTRER OU EST PASSEE LA LUMIERE
matriceLumiere = []

# COMPTER LE NOMBRE DE CASE OU LA LUMIERE EST PASSEE
def compter(matriceLumiere):
    nbr = 0
    for y in range(len(matriceLumiere)):
        for x in range(len(matriceLumiere[0])):
            # QUAND LA LUMIERE PASSE ON A AJOUTE UN '#' A LA POSITION
            if matriceLumiere[y][x] == "#":
                nbr += 1
    return nbr


# CREATION DE LA MATRICE DE L ENONCE: matrice
# PLUS INITIALISATION DE LA MATRICE LUMIERE QUI STOCKERA LES '#' CAD LES CASES OU EST PASSEE LA LUMIERE 
for y, ligne in enumerate(lignes.split("\n")):
    matrice.append([])
    matriceLumiere.append([])
    for ch in ligne:
        matrice[y].append(ch)
        matriceLumiere[y].append('')

# ABOUGER EST UNE LISTE QUI CONTIENT LA POSITION DE LA LUMIERE A UN INSTANT T
# AU DEBUT ELLE CONTIENT LE POINT D ENTREE
ABouger = [[(0,0), (1,0)]]
# AJOUT DU '#' DANS LA METRICE LUMIERE: LA LUMIERE EST FORCEMENT PASSEE PAR LE PT D ENTREE
matriceLumiere[0][0] = "#"

# DICTIONNAIRE QUI PERMET DE CHANGER LA DIRECTION DE LA LUMIERE EN FONCTION DU CARACTERE
# LA CLE EST LA VALEUR DU CARACTERE
# POUR CHAQUE CARACTERE IL Y A AUSSI UN DICTIONNAIRE 
    # LE DEUXIEME DICTIONNAIRE CONTIENT EN CLE LA DIRECTION DE LA LUMIERE QUI ARRIVE 
    # EN VALEUR IL Y A LA NOUVELLE VALEUR DE LA DIRECTION DE LA LUMIERE 
direction = {"|": {(0,1):[(0,1)], (0,-1):[(0,-1)], (1,0):[(0,-1),(0,1)], (-1,0):[(0,-1),(0,1)]},
             "-": {(1,0):[(1,0)], (-1,0):[(-1,0)], (0,1):[(1,0),(-1,0)], (0,-1):[(1,0),(-1,0)]},
             "/": {(1,0):[(0,-1)], (-1,0):[(0,1)], (0,1):[(-1,0)], (0,-1):[(1,0)]},
             "\\": {(1,0):[(0,1)], (-1,0):[(0,-1)], (0,1):[(1,0)], (0,-1):[(-1,0)]}}

# DICTIONNAIRE QUI PERMET DE STOCKER SI ON EST DEJA PASSE PAR UN POINT AVEC LA MEME DIRECTION 
# LA CLE EST LA CONCATENATION DE LA POSITION ET DE LA DIRECTION, LA VALEUR 1 NA PAS DE SENS
dicoDejaFait = {str(ABouger[0]):1}

# TANT QUIL RESTE DES PT A BOUGER 
while(len(ABouger)!=0):
    # LISTE QUI PERMET DE STOCKER LES PT A BOUGER AU PROCHAIN TOUR
    newABouger = []
    # POUR CHAQUE POINT A BOUGER
    for p, point in enumerate(ABouger):
        # ON RECUPERE LA POSITION
        pt = point[0]
        # ON RECUPERE LA DIRECTION
        vecteur = point[1]
        # ON RECUPERE LE CARACTERE DE LA POSITION 
        pos = matrice[pt[1]][pt[0]]

        # SI LE CARACTERE NE FAIT PAS PARTIE DU DICTIONNAIRE CAD SI CEST UN "." 
        if pos not in direction:
            # LA LUMIERE CONTINUE SON CHEMIN DANS LA MEME DIRECTION 
            x = pt[0]+vecteur[0]
            y = pt[1]+vecteur[1]
            newPos = (x,y)
            # AVANT DE BOUGER ON VERIFIE QUON NE SORTE PAS DE LA matrice
            if(-1 not in newPos and x != len(matriceLumiere[0]) and y != len(matriceLumiere)):
                # ON AJOUTE LE NOUVEAU POINT DANS LA LISTE A BOUGER SI ON N A PAS ENCORE EU CE PT AVEC CETTE DIRECTION 
                if(str([(newPos), vecteur]) not in dicoDejaFait):
                    newABouger.append([(newPos), vecteur])
                    dicoDejaFait[str([(newPos), vecteur])] = 1
                # ON AJOUTE LE '#' A LA MATRICE LUMIERE POUR DIRE QUE LA LUMIERE EST PASSEE DS CETTE CASE 
                matriceLumiere[y][x] = "#"
        else:
            # MEME PRINCIPE QUAU DESSUS MAIS AU LIEU DE CONTINUER DANS LA MEME DIRECTION ON EN CHANGE SELON LE CARACTERE DE LA POSITION 
            for d in direction[pos][vecteur]:
                x=pt[0]+d[0]
                y=pt[1]+d[1]
                newPos = (x,y)
                if(-1 not in newPos and x != len(matriceLumiere[0]) and y != len(matriceLumiere)):
                    if(str([(newPos), d]) not in dicoDejaFait):
                        newABouger.append([(newPos), d])
                        dicoDejaFait[str([(newPos), d])] = 1
                    matriceLumiere[y][x] = "#"
    # ON CHANGE LA VALEUR DE ABOUGER AVEC LES NOUVEAUX POINTS A PARCOURIR
    # UTILISATION DE CES DEUX LISTES CAR COMME IL Y A ITERATION SUR LA LISTE ABOUGER ON NE PEUT PAS EN MEME TEMPS LUI AJOUTER OU SUPPRIMER DES VALEURS 
    ABouger = []
    ABouger = newABouger


# FINALEMENT ON COMPTE LE NOMBRE DE CASE OU EST PASSEE LA LUMIERE 
print(compter(matriceLumiere))


        
        


