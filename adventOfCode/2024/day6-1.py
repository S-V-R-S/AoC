with open('adventOfCode/2024/input.txt', encoding="UTF-8", mode= "r") as file:  
        matrice = file.read().splitlines()
        for i, ligne in enumerate(matrice):
            for j, letter in enumerate(ligne):
                if letter in ["^","v",">", "<" ]:
                    x = i
                    y = j
                    first_direction = letter

liste = ["^",">","v","<"]
liste_coord = [[-1,0], [0, 1], [1,0], [0, -1]]

index_direction = liste.index(first_direction)
current_direction = liste_coord[index_direction]

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
  
print(len(path))