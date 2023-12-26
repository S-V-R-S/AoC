import re

f = open("input.txt","r")
lignes = f.readlines()

dist = [int(t) for t in re.findall('\d+',lignes[1].split(":")[1].strip())]
temps = [int(d) for d in re.findall('\d+',lignes[0].split(":")[1].strip())]

print(dist)
print(temps)
possibilites= 1

for i in range(len(dist)):
    add = 0
    for j in range(temps[i]+1):
        hold = j
        distance = (temps[i]-j)*j
        if(distance>dist[i]):
            add += 1
    possibilites = possibilites*add

print(possibilites)
    