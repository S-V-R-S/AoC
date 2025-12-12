import time

start_time = time.time()


with open("adventOfCode/2025/test.txt", encoding="UTF-8", mode="r") as file:
    lignes = file.read().splitlines()


def noIntersection(polygone, sommets):

    for i in range(len(sommets)):
        s = sommets[i]
        s2 = sommets[(i + 1) % len(sommets)]
        

        for j in range(len(polygone)):
            p = polygone[j]
            p2 = polygone[(j + 1) % len(polygone)]

            if s[0] == s2[0] and p[1] == p2[1]:
                if (
                    s[0] > min(p[0], p2[0])
                    and s[0] < max(p[0], p2[0])
                    and p[1] > min(s[1], s2[1])
                    and p[1] < max(s[1], s2[1])
                ):
                   
                    return False

            if s[1] == s2[1] and p[0] == p2[0]:
                if (
                    min(p[1], p2[1]) < s[1]
                    and max(p[1], p2[1]) > s[1]
                    and min(s[0], s2[0]) < p[0]
                    and max(s[0], s2[0]) > p[0]
                ):

                        
                        return False

    return True


def sommetsIn(polygone, sommets):
    for point in sommets:
        onEdge = False
        inside = False
        for i in range(len(polygone)):
            p = polygone[i]
            p2 = polygone[(i + 1) % len(polygone)]
            if p[0] == p2[0]:

                if (
                    p[0] > point[0]
                    and point[1] > min(p[1], p2[1])
                    and point[1] <= max(p[1], p2[1])
                ):
                    inside = not (inside)
                elif (
                    p[0] == point[0]
                    and point[1] >= min(p[1], p2[1])
                    and point[1] <= max(p[1], p2[1])
                ):
                    onEdge = True
                    break
            else:
                if (
                    point[1] == p[1]
                    and point[0] >= min(p[0], p2[0])
                    and point[0] <= max(p[0], p2[0])
                ):
                    onEdge = True
                    break

        if not (onEdge) and not (inside):
            return False

    return True


points = []
for ligne in lignes:
    x, y = [int(i) for i in ligne.split(",")]
    points.append((x, y))

aire = 0
solution = 0
for i, p in enumerate(points):
    for j in range(i + 1, len(points)):
        p2 = points[j]
        sommets = [p, (p2[0], p[1]), p2, (p[0], p2[1])]
        if sommetsIn(points, sommets) and noIntersection(points, sommets):
            a = (abs(p[0] - p2[0]) + 1) * (abs(p[1] - p2[1]) + 1)
            if a > aire:
                aire = a
                solution = [p,p2]


print(aire, solution)
end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Le programme a dure {elapsed_time_ms:.2f} ms est la reponse est")


# 2,1
# 6,1
# 6,6
# 2,6
# 2,5
# 5,5
# 5,2
# 2,2