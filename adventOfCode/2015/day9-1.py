import re
with open('adventOfCode/2015/input.txt', encoding="UTF-8", mode= "r") as file:  
    lines = file.readlines()
 
id = {}   
for line in lines:
   if line.startswith("je rentre"):
       if line[9:] in id:
           id[line[9:]] += 1
       else:
           id[line[9:]] = 1
           
for i in id:
    if id[i] > 1:
        print(i, id[i])
