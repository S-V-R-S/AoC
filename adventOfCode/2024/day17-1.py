
import time
start_time = time.time()
import re

with open('adventOfCode/2024/input17.txt', encoding="UTF-8", mode= "r") as file:  
    lignes = file.read().splitlines()

dico = {}
for ligne in lignes:
    if ligne[:10] == "Register A":
        dico["A"] = int(re.findall(r"-?\d+", ligne)[0])
    if ligne[:10] == "Register B":
        dico["B"] = int(re.findall(r"-?\d+", ligne)[0])
    if ligne[:10] == "Register C":
        dico["C"] = int(re.findall(r"-?\d+", ligne)[0])
    if ligne[:8] == "Program:":
        programme = list(map(int,re.findall(r"-?\d+", ligne)))

def traduire(op, dico):
    if op < 4:
        return op  
    if op == 4:
        return dico["A"]
    if op == 5:
        return dico["B"]
    if op == 6:
        return dico["C"]
    


pointer = 0
output = []

while pointer < len(programme):
    opcode = programme[pointer]
    operand = programme[pointer +1]

    if opcode == 0:
        dico['A'] = dico['A'] // 2**traduire(operand, dico)
    if opcode == 1:
        dico['B'] ^= operand
    if opcode == 2:
        dico['B'] = traduire(operand, dico) % 8
    if opcode == 3:
        if dico["A"] != 0: 
            pointer = operand
            continue
    if opcode == 4:
        dico['B'] ^= dico['C']
    if opcode == 5:
        output.append(traduire(operand, dico) % 8)
    if opcode == 6:
        dico['B'] = dico['A'] // 2**traduire(operand, dico)
    if opcode == 7:
        dico['C'] = dico['A'] // 2**traduire(operand, dico)
    pointer += 2

print(",".join(map(str, programme)))
print(",".join(map(str, output)))

end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Le programme a dure {elapsed_time_ms:.2f} ms est la reponse est")

