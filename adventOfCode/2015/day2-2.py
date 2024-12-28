with open('adventOfCode/2015/input.txt', encoding="UTF-8", mode= "r") as file:  
    lines = file.readlines()
    
total = 0

for line in lines:
    l,w,h  = map(int, line.split("x"))
    
    total += h*l*w + sum(sorted([l,w,h])[:2])*2
    
print(total)