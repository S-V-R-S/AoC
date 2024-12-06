liste = ["^",">","v","<"]
liste_coord = [[-1,0], [0, 1], [1,0], [0, -1]]

def boucle(matrice, x, y, obstacle):

    index_direction = first_direction
    curr = liste_coord[index_direction]
    dico = set()

    while True:
        key = (x,y,index_direction)

        if key in dico:
            return 1
        
        dico.add(key)

        x1 = x + curr[0]
        y1 = y + curr[1]

        if x1 >= len(matrice) or x1 <0 or y1 >= len(matrice[0]) or y1 < 0:
            return 0

        if matrice[x1][y1] != "#" and (x1,y1) != obstacle:            
                x = x1
                y = y1
                continue
        
        index_direction += 1
        index_direction = index_direction % 4
        curr = liste_coord[index_direction]



with open('adventOfCode/2024/input.txt', encoding="UTF-8", mode= "r") as file:  
        matrice = file.read().splitlines()
        for i, ligne in enumerate(matrice):
            for j, letter in enumerate(ligne):
                if letter in ["^","v",">", "<" ]:
                    x0 = i
                    y0 = j
                    first_direction = liste.index(letter)



index_direction = first_direction
current_direction = liste_coord[index_direction]

x,y = x0,y0
path = set()
while True:
     path.add((x,y))

     x1 = x + current_direction[0]
     y1 = y + current_direction[1]

     if x1 >= len(matrice) or x1 <0 or y1 >= len(matrice[0]) or y1 < 0:
          break

     if matrice[x1][y1] != "#":
          x, y = x1, y1
          continue
     
     index_direction += 1
     index_direction = index_direction % 4
     current_direction = liste_coord[index_direction]
  
print("exo 1: ",len(path))

path = list(path)
count = 0
for step in path:
    if step != (x0, y0):
        count += boucle(matrice, x0, y0, step)

print("exo 2: ",count)
