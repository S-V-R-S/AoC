print("good start")

f = open("adventOfCode\\2015\\input.txt","r")
ligne = f.read().strip()
f.close()

# on commence à l'étage 0 
etage = 0
for c in ligne:
    if c =='(': etage += 1
    else: etage -= 1

print('Réponse:', etage)