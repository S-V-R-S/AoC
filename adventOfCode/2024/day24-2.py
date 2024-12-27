import time
start_time = time.time()

with open('adventOfCode/2024/input24.txt', encoding="UTF-8", mode= "r") as file:  
    lines = file.read().splitlines()  
    
gates = {}
wires = {}
z_gates = []

for line in lines:
    if ":" in line:
        gates[line.split(": ")[0]] = int(line.split(": ")[1])
    elif "-" in line:
        g1, operator, g2, output = line.replace('-> ', '').split(" ")
        if output.startswith("z"): z_gates.append(output)
        wires[output] = [g1, operator, g2]

wrong_outputs = set()

higher_z = "z"+str(len(list(z for z in z_gates if z[0] == "z"))-1)

for output in wires:
    g1, operator, g2 = wires[output]
    
    if output.startswith("z") and operator != 'XOR' and output != higher_z:
        wrong_outputs.add(output)
        
    elif output == higher_z and operator != 'OR':
        wrong_outputs.add(output)
        
    elif output[0] != "z" and operator == "XOR" and g1[0] not in 'yx':
        wrong_outputs.add(output)
        
    elif output[0] not in 'zyx' and operator == 'AND' and g1[1:] != '00':
        for w in wires:
            child_g1, child_operator, child_g2 = wires[w]
            if (child_g1 == output or child_g2 == output) and child_operator != "OR":
                wrong_outputs.add(output)
                
    elif operator == 'OR' and output[0] != "z":
        for w in wires:
            child_g1, child_operator, child_g2 = wires[w]
            if (child_g1 == output or child_g2 == output) and child_operator == "OR":
                wrong_outputs.add(output)
                print(output)
        
        
print(",".join(wrong_wire for wrong_wire in sorted(wrong_outputs)))

# dpg,kmb,mmf,tvp,vdk,z10,z15,z25
end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"The program ran for {elapsed_time_ms:.2f} ms")


