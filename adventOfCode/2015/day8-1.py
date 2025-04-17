import re
with open('adventOfCode/2015/input.txt', encoding="UTF-8", mode= "r") as file:  
    lines = file.readlines()
 
total = 0   
for line in lines:
    line = line.strip()
    number_string_literals = len(line)
    
    
    line = line.replace(r'\"','"')
    
    asciis = re.findall(r'\\x[0-9a-fA-F]{2}', line)
    balance = 0
    for a in asciis:
        balance += len(chr(int(a[2:], 16))) - len(a)
        
    line = line.replace(r'\\','\\')
    
    total += number_string_literals - len(line) + 2 - balance
    
print(total)
