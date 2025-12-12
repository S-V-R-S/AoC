import time

start_time = time.time()

with open("adventOfCode/2025/test.txt", encoding="UTF-8", mode="r") as file:
    lignes = file.read().splitlines()


cache = {}


def allerOut(porte, fft, dac):
    global dico_parent_child
    if "fft" == porte:
        fft = True
    if "dac" == porte:
        dac = True

    if porte == "out":
        return 1 if fft and dac else 0

    if (porte, fft, dac) in cache:
        return cache[(porte, fft, dac)]

    somme = 0
    for s in dico_parent_child[porte]:
        somme += allerOut(s, fft, dac)
        cache[(porte, fft, dac)] = somme
    return somme


def simplify(dico_parent_child, dico_child_parent):
    modified = True
    while modified:

        modified = False

        keys = list(dico_parent_child.keys() - {"out", "fft", "dac", "svr"})

        for k in keys:

            deleted = set()

            if k not in deleted and len(dico_parent_child[k]) == 1:

                # for parent in dico_child_parent[k]:
                # print(parent)
                # dico_parent_child[parent] += dico_parent_child[k]
                # dico_parent_child[parent].remove(k)

                # dico_child_parent[dico_parent_child[k][0]].remove(k)
                # dico_child_parent[dico_parent_child[k][0]] += dico_parent_child[
                #     parent
                # ]

                # del dico_parent_child[k]

                # enfant de k : tty
                childK = dico_parent_child[k][0]

                # on ajout l'enfant de k à tous ses parents
                for parent in dico_child_parent[k]:
                    dico_parent_child[parent].append(childK)

                # on ajoute les parents de k a son enfant
                dico_child_parent[childK] += dico_child_parent[k]

                # on supprime k de son enfant
                dico_child_parent[childK].remove(k)

                # on supprime k de tous ses parents
                for parent in dico_child_parent[k]:
                    dico_parent_child[parent].remove(k)

                modified = True

                del dico_parent_child[k]
                del dico_child_parent[k]

                deleted.add(k)
                # print(dico_parent_child)
                # print(dico_child_parent)

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

print(allerOut("svr", False, False))


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
