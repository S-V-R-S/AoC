
import time
start_time = time.time()

with open('adventOfCode/2025/input.txt', encoding="UTF-8", mode= "r") as file:  
# with open('adventOfCode/2025/test.txt', encoding="UTF-8", mode= "r") as file:  
        lignes = file.read().strip()
print(lignes)
count = 0
plages = lignes.split(",")
for plage in plages:
        inf = int(plage.split("-")[0])
        sup = int(plage.split("-")[1])
        for i in range(inf, sup+1):
                ids = str(i)
                # print(ids)
                taille = len(ids)
                for j in range(taille//2):
                        pattern = ids[:j+1]
                        # print("pattern",pattern)
                        if (len(ids) % len(pattern)) == 0:
                            nbr = len(ids)//len(pattern)
                            invalid = True
                            for k in range(1,nbr):
                                   groupe =ids[k*len(pattern):k*len(pattern)+len(pattern)]
                                #    print("test avec", groupe)
                                   if pattern != groupe:
                                          invalid = False
                                          break
                        if invalid:
                               break
                if i < 10:
                       continue
                if invalid:
                    count += i
print(count)
# 1227775554                    
                
end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Le programme a dure {elapsed_time_ms:.2f} ms est la reponse est")
