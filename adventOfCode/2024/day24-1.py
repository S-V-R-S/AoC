import time
start_time = time.time()

with open('adventOfCode/2024/input24.txt', encoding="UTF-8", mode= "r") as file:  
    lines = file.read().splitlines()  
    
gates = {}
wires = []

for line in lines:
    if ":" in line:
        gates[line.split(": ")[0]] = int(line.split(": ")[1])
    elif "-" in line:
        wires.append(line.replace('-> ', '').split(" "))
        
for wire in wires:
    gate1, operator, gate2, output = wire
    if not(gate1 in gates) or not(gate2 in gates):
        wires.append(wire)
        continue
    elif operator == "AND": 
        gates[output] = int(gates[gate1] and gates[gate2])
    elif operator == "OR": 
        gates[output] = int(gates[gate1] or gates[gate2])
    elif operator == "XOR": 
        gates[output] = int(gates[gate1] ^ gates[gate2])

print(int("".join(str(gates[z_gate]) for z_gate in sorted((z for z in gates if z[0] == "z"), reverse = True)) , 2))
# 51715173446832
end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"The program ran for {elapsed_time_ms:.2f} ms")


