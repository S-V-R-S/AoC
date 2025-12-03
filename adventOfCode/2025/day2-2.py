
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
                s = str(i)
                milieu = len(s) // 2

                gauche = s[:milieu]
                droite = s[milieu:]

                if gauche == droite:
                        print(s)
                        count += i
                
print(count)
# 1227775554                    
                
end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Le programme a dure {elapsed_time_ms:.2f} ms est la reponse est")
