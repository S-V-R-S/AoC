with open('adventOfCode/2015/input.txt', encoding="UTF-8", mode= "r") as file:  
    strings = file.readlines()
    
nice = 0

for string in strings:
    rule_1 = rule_2 = False
    
    for i in range(1,len(string)):
        
        pattern = string[i-1:i+1]
        
        if pattern in string[:i-1] or pattern in string[i+1:]:
            rule_1 = True
            

        if  i > 1 and string[i] == string[i-2]:
            rule_2 = True
                
        if rule_1 and rule_2:
            nice += 1
            break

print(nice)

