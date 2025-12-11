import time

start_time = time.time()

with open("adventOfCode/2025/test.txt", encoding="UTF-8", mode="r") as file:
    lignes = file.read().splitlines()


def allerOut(dico, porte, fft, dac):
    if porte == "out":
        return 1 if fft and dac else 0

    somme = 0
    for s in dico[porte]:
        if "fft" == s:
            fft = True
        if "dac" == s:
            dac = True

        somme += allerOut(dico, s, fft, dac)

    return somme


def simplify(dico_parent_child, dico_child_parent):
    modified = True
    while modified:

        modified = False

        keys = list(dico_parent_child.keys() - {"out", "fft", "dac", "svr"})

        for k in keys:

            print(k)

            if klen(dico_parent_child[k]) == 1:
                print(f"del {k}")
                for parent in dico_child_parent[k]:
                    dico_parent_child[parent].append(dico_parent_child[k])
                    dico_parent_child[parent].remove(k)
                    del dico_parent_child[k]

                    modified = True

                del dico_child_parent[k]

    return dico_parent_child


dico_parent_child = {}
dico_child_parent = {}
for ligne in lignes:
    entree, sorties = ligne.split(":")
    sortiesList = []
    for s in sorties.strip().split(" "):
        sortiesList.append(s)
        if s not in dico_child_parent:
            dico_child_parent[s] = []
        dico_child_parent[s].append(entree)
    dico_parent_child[entree] = sortiesList

dico_parent_child = simplify(dico_parent_child, dico_child_parent)
print(dico_parent_child)
print(allerOut(dico_parent_child, "svr", False, False))


end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Le programme a dure {elapsed_time_ms:.2f} ms est la reponse est")


# aaa: you hhh
# you: bbb ccc
# bbb: ddd eee
# ccc: ddd eee fff
# ddd: ggg
# eee: out
# fff: out
# ggg: out
# hhh: ccc fff iii
# iii: out
