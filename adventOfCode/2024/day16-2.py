
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

def dijkstra(matrice, start, end):
    to_explore = [(start, (1,0))]
    explored = []
    dico = {}
    dico[(start, (1,0))] = [0, None]
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

            total_cost = cost + dico[node][0]

            if point == end:
                    scoreB.append(total_cost)

            if (point, direction) in dico:
                if dico[(point, direction)][0] > total_cost:
                    dico[(point, direction)] = [total_cost, node]
                    if (point, direction) not in to_explore:
                        to_explore.append((point, direction))
            else:
                dico[(point, direction)] = [total_cost, node]
                if (point, direction) not in to_explore:
                    to_explore.append((point, direction))
    
 
    score = min(scoreB)


    to_explore = []
    for dir in dictionnaire.keys():
        if (end, dir) in dico:
            if dico[(end, dir)][0] == score:
                to_explore.append(dico[(end, dir)])

    point = end
    path = [end, start]
    
    while to_explore:
        infos = to_explore.pop()
        point = infos[1][0]
        score = infos[0]
        dir = infos[1][1]
        if point == start:
            continue
        for dir in dictionnaire.keys():
            if (point, dir) in dico:
                new_infos = dico[(point, dir)]
                npoint = new_infos[1][0]
                nscore = new_infos[0]

                if (score == (nscore+1)) or ( score == (nscore+1001)):
                    if npoint != start:
                        to_explore.append(dico[(point, dir)])
                        path.append(npoint)
                        path.append(point)


    for p in path:
        matrice[p[1]][p[0]] = "O"



    print(len(set(path)))



dijkstra(matrice, start, end)
end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Le programme a dure {elapsed_time_ms:.2f} ms")
# 559