
import time
start_time = time.time()

dictionnaire = {
    (0 , -1): [(1, 0),(-1, 0)],
    (0, 1): [(1, 0),(-1, 0)],
    (1, 0): [(0, 1),(0 , -1)],
    (-1, 0): [(0, 1),(0 , -1)]
}

with open('adventOfCode/2024/input16.txt', encoding="UTF-8", mode= "r") as file:  
    lignes = file.read().splitlines()
    matrice = []
    
    for i, ligne in enumerate(lignes):
        matrice.append([])
        for j, letter in enumerate(ligne):
            matrice[i].append(letter)
            if letter == "S":
                start = (j,i)
            if letter == "E":
                end = (j,i)



def nodes_in(coor, matrice):
      nodes = []
      current_dir = coor[1]
      xd = coor[0][0]
      yd = coor[0][1]
      x0 = xd + coor[1][0]
      y0 = yd + coor[1][1]
      if 0 <= x0 < len(matrice) and 0 <= y0 < len(matrice[0]) and matrice[y0][x0] != "#":
             nodes.append([(x0,y0), 1, current_dir])

      for dir in dictionnaire[current_dir]:
        x = xd + dir[0]
        y = yd + dir[1]
        if 0 <= x < len(matrice) and 0 <= y < len(matrice[0]) and matrice[y][x] != "#":
             nodes.append([(x,y), 1001, dir])
      return nodes

def dijkstra(matrice, point_A, point_B):
    to_explore = [(point_A, (1,0))]
    explored = []
    dico = {}
    dico[(point_A, (1,0))] = 0
    scoreB = []

    while to_explore:
        node = to_explore[0]
        del to_explore[0]
        explored.append(node)

        neighbours = nodes_in(node, matrice)

        for new in neighbours:
            point = new[0]
            cost = new[1]
            direction = new[2]

            total_cost = cost + dico[node]

            if point == point_B:
                    scoreB.append(total_cost)

            if (point, direction) in dico:
                if dico[(point, direction)] > total_cost:
                    dico[(point, direction)] = total_cost
                    if (point, direction) not in to_explore:
                        to_explore.append((point, direction))
            else:
                dico[(point, direction)] = total_cost
                if (point, direction) not in to_explore:
                    to_explore.append((point, direction))
 

    return min(scoreB)

print(dijkstra(matrice, start, end))
end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Le programme a dure {elapsed_time_ms:.2f} ms ")
# 102488