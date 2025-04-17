import re
with open('adventOfCode/2015/input.txt', encoding="UTF-8", mode= "r") as file:  
    lines = file.readlines()
 
total = 0   
for line in lines:
    line = line.strip()
    number_string_literals = len(line)
    
    print(line)
    
    line = line.replace(r'\\',r'\\\\')
    line = line.replace(r'\"',r'\\\"')
    add = len(re.findall(r'\\x[0-9a-fA-F]{2}', line))

    line = '"\\' + line[:-1] + '\\""'
    print(line)
        
    
    total +=  len(line) - number_string_literals + add
    
print(total)
