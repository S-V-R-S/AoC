print("good start")

# OUVERTURE DE L INPUT 
f = open("adventOfCode\\2015\\input.txt","r")
ligne = f.read().strip()
f.close()

# ON COMMENCE A L ETAGE 0 
etage = 0
for c in ligne:
    # ACTUALISATION DE LA VALEUR DE L ETAGE SELON LE SENS DE LA PARENTHESE 
    if c =='(': etage += 1
    else: etage -= 1

print('Réponse:', etage)