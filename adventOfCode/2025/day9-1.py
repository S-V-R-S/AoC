
import time
start_time = time.time()


with open('adventOfCode/2025/test.txt', encoding="UTF-8", mode= "r") as file:  
        lignes = file.read().splitlines()

points = []
for ligne in lignes:
        x,y = [int(i) for i in ligne.split(",")]
        points.append((x,y))
aire = 0
for i, p in enumerate(points):
        for j in range(i+1, len(points)):
            p2 = points[j]
            a = (abs(p[0]-p2[0])+1)*(abs(p[1]-p2[1])+1)
            if a > aire:
                   aire = a

print(aire)
end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Le programme a dure {elapsed_time_ms:.2f} ms est la reponse est")
