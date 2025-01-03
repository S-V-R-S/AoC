
import time
start_time = time.time()
with open('adventOfCode/2024/input19.txt', encoding="UTF-8", mode= "r") as file:  
        lignes = file.read().splitlines()


cache = {}
def possible(motifs, serviette, taille_max, taille_min):
        if (serviette) in cache:                
            return cache[serviette]
        
        if serviette in motifs:
                return 1
        if len(serviette) == taille_min and serviette not in motifs:
                return 0
        
        portions = []
        for i in range(taille_min, taille_max+1):
                portion = serviette[:i]
                if portion in motifs:
                        portions.append(serviette[i:])
        
        somme = sum(possible(motifs, p, taille_max, taille_min) for p in portions)
        cache[serviette] = somme
        return somme
                

serviettes = []

for ligne in lignes:
        if ligne != "":
                if "," in ligne:
                        motifs = ligne.strip().split(", ")
                else:
                        serviettes.append(ligne)

taille_max = len(motifs[0])
taille_min = len(motifs[0])

for i in range(1, len(motifs)):
        if len(motifs[i]) > taille_max:
               taille_max = len(motifs[i]) 
        if len(motifs[i]) < taille_min:
                taille_min = len(motifs[i])

somme = 0

for i, s in enumerate(serviettes):
        score = possible(motifs, s, taille_max, taille_min)
        if score > 0:
                somme += 1
print(somme)
end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Le programme a dure {elapsed_time_ms:.2f} ms est la reponse est")
