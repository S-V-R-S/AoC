def hash(ch):
    currentValue = 0
    for c in ch:
        ascii = ord(c)
        currentValue += ascii
        currentValue = currentValue*17 % 256
    return currentValue



sequence = ""
f = open("input.txt","r")
lignes = f.readlines()
f.close()

for i, l in enumerate(lignes):
    sequence += l.strip()

sequence = sequence.split(",")
total = 0
for s in sequence:
    total += hash(s)


print(total)