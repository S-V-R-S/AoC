print("good start")

f = open("adventOfCode\\2015\\input.txt","r")
ligne = f.read().strip()
f.close()

# on commence à l'étage 0 
etage = 0
position = 0
while etage != -1:
    c = ligne[position]
    if c =='(': etage += 1
    else: etage -= 1
    position += 1

print('Réponse:', position)