import re
with open('adventOfCode/2015/input.txt', encoding="UTF-8", mode= "r") as file:  
    gates = file.readlines()
    
wires = {}

for gate in gates:
    gate = gate.strip()
    
    if gate.startswith("NOT"):
        _,x,y = gate.replace("-> ", "").split(" ")
        if x in wires:
            wires[y] =(~wires[x] & 0xFFFF)
        else:
            gates.append(gate)
            
    elif "AND" in gate or "OR" in gate or "LSHIFT" in gate or "RSHIFT" in gate:
        x,_,y,z = gate.replace("-> ", "").split(" ")
        
        if x.isdigit(): x = int(x)
        elif x not in wires: 
            gates.append(gate)
            continue
        else: x = wires[x]
        
        if y.isdigit(): y = int(y)
        elif y not in wires: 
            gates.append(gate)
            continue
        else: y = wires[y]
        
        if "AND" in gate:
            wires[z] = x & y
        elif "OR" in gate:
            wires[z] = x | y
        elif "RSHIFT" in gate:
            wires[z] = x >> y
        elif "LSHIFT" in gate:
            wires[z] = x << y
    
    else:
        value, wire = gate.split(" -> ")
        if value.isdigit():
            wires[wire] = int(value)
        elif value not in wires:
            gates.append(gate)
            continue
        else:
            wires[wire] = wires[value]
        

print(wires['a'])   
    