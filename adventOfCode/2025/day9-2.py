
import time
start_time = time.time()


with open('adventOfCode/2025/test.txt', encoding="UTF-8", mode= "r") as file:  
        lignes = file.read().splitlines()

def noIntersection(polygone,sommets):
       for i in range(sommets):
              s = sommets[i]
              s2 = sommets[(i+1)%len(sommets)]

              for j in range(polygone):
                     p = polygone[i]
                     p2 = polygone[(i+1)%len(polygone)]  

                     


       return True

def sommetsIn(polygone, sommets):
        for point in sommets:
                onEdge = False
                inside = False
                for i in range(len(polygone)):
                        p = polygone[i]
                        p2 = polygone[(i+1)%len(polygone)]
                        if p[0] == p2[0]:

                                if p[0] > point[0] and point[1] > min(p[1],p2[1]) and point[1] <= max(p[1],p2[1]):
                                        inside = not(inside)
                                elif p[0] == point[0] and point[1] >= min(p[1],p2[1]) and point[1] <= max(p[1],p2[1]):
                                        onEdge = True
                                        break
                        else:
                                if point[1] == p[1] and point[0] >= min(p[0],p2[0]) and point[0] <= max(p[0],p2[0]):
                                        onEdge = True
                                        break

                if not(onEdge) and not(inside):
                        return False


        return True

points = []
for ligne in lignes:
        x,y = [int(i) for i in ligne.split(",")]
        points.append((x,y))

aire = 0

for i, p in enumerate(points):
        for j in range(i+1, len(points)):
            p2 = points[j]
            sommets = [p,p2, [p[0],p2[1]], [p2[0],p[1]]]
            if sommetsIn(points,sommets) and noIntersection(points,sommets):
                a = (abs(p[0]-p2[0])+1)*(abs(p[1]-p2[1])+1)
                if a > aire:
                        aire = a


print(aire)
end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Le programme a dure {elapsed_time_ms:.2f} ms est la reponse est")
