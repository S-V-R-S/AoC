import time

start_time = time.time()


with open("adventOfCode/2025/test.txt", encoding="UTF-8", mode="r") as file:
    lignes = file.read()


cadeaux = {}
compte = 0
for ligne in lignes.split("\n\n"):
    ligne = ligne.strip()
    if "." in ligne or "#" in ligne:
        cadeaux[int(ligne.split(":")[0])] = ligne.count("#")

    else:
        break

for ligne in lignes.split("\n"):
    if "x" in ligne:
        dimensions = ligne.split(": ")[0]
        dimensions = int(dimensions.split("x")[0]) * int(dimensions.split("x")[1])
        listeCadeaux = [int(i) for i in ligne.split(": ")[1].split(" ")]
        print(ligne)
        print(listeCadeaux)
        somme = 0
        for i, nbr in enumerate(listeCadeaux):
            print(nbr, cadeaux)
            somme += nbr * cadeaux[i]
        if somme <= dimensions:
            compte += 1


print(compte)
end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Le programme a dure {elapsed_time_ms:.2f} ms est la reponse est")
