print("good start")

# OUVERTURE DE L INPUT 
f = open("adventOfCode\\2015\\input.txt","r")
ligne = f.read().strip()
f.close()

# ON COMMENCE A L ETAGE 0 
etage = 0
# ON INIALISE LE COMPTEUR 
position = 0

# TANT QU ON N EST PAS AU -1
while etage != -1:

    # ON ACTUALISE L ETAGE 
    c = ligne[position]
    if c =='(': etage += 1
    else: etage -= 1

    # ON INCREMENTE LE COMPTEUR 
    position += 1

print('Réponse:', position)