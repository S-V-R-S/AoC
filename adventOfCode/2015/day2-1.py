with open('adventOfCode/2015/input.txt', encoding="UTF-8", mode= "r") as file:  
    lines = file.readlines()
    
total = 0

for line in lines:
    l,w,h  = map(int, line.split("x"))
    
    total += 2*l*w + 2*w*h + 2*h*l + min(l*w,w*h,h*l)
    
print(total)