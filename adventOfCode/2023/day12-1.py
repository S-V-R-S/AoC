import re

f = open("advent code 2023\day12-input.txt","r")
lignes = f.readlines()
f.close()

def main():
    possibilites = 0
    for ligne in lignes:
        possibilite = 0
        records= ligne.strip()

        record = records.split(" ")[0]
        groupe = records.split(" ")[1]
        groupe = [int(v) for v in groupe.split(",")]

        somme = sum(groupe)

        aPlacer = somme - len(re.findall("#", record))
        nbrPtInterro = len(re.findall("\?", record))

        liste_binaire = [bin(i)[2:].zfill(nbrPtInterro) for i in range(2**nbrPtInterro)]

        for combi in liste_binaire:
            test = ""
            incre = 0
  
            for r in record:
                if(r=="#" or r == '.'):
                    test = test + r
                else:
                    if(int(combi[incre])==0):
                        test = test + "."
                    else:
                        test = test + "#"
                    
                    incre = incre + 1

            test = re.findall("#+", test)
            
            if(len(test)==len(groupe)):
                correct = True
                for p in range(len(test)):
                    if(len(test[p]) != groupe[p]):
                        correct = False
                        break
                if(correct):
                    possibilite += 1
        possibilites += possibilite

    print(possibilites)

main()