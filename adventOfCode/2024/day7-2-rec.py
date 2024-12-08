import time

start_time = time.time()

def correct(answer, numbers):
    if answer == numbers[0] and len(numbers) == 1 : return True
    if answer != numbers[0] and len(numbers) == 1 : return False
    if answer < numbers[0] : return False

    return correct(answer, [numbers[0] + numbers[1]] + numbers[2:]) or correct(answer, [numbers[0] * numbers[1]] + numbers[2:]) or correct(answer, [int(str(numbers[0]) + str(numbers[1]))] + numbers[2:])

with open('adventOfCode/2024/input.txt', encoding="UTF-8", mode= "r") as file:  
    lignes = file.read().splitlines()

resultat = 0

for l, ligne in enumerate(lignes):
    answer, numbers = ligne.strip().split(":")
    answer = int(answer)
    numbers = list(map(int, numbers.split()))
    if correct(answer, numbers):
        resultat+=answer


# 472290821152397
end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Le programme a duré {elapsed_time_ms:.2f} ms est la réponse est", resultat)