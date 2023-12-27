

f = open("adventOfCode\\2023\\input6).txt","r")
lignes = f.readlines()

dist = int(lignes[1].split(":")[1].replace(" ", ""))
temps = int(lignes[0].split(":")[1].replace(" ", ""))
f.close()
start = False
end = False
add = 0
for i in range(temps+1):
    
    distance = (temps-i)*i
    if(distance>dist):
        add += 1
        start = True
    if(start and distance>dist):
        end = True
    if(end and not(start)):
       break

print(add)