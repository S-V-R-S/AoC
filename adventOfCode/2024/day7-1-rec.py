def correct(answer, numbers):
    if answer == numbers[0] and len(numbers) == 1 : return True
    if answer != numbers[0] and len(numbers) == 1 : return False
    
    numbers1 = numbers.copy()
    numbers2 = numbers.copy()

    numbers1[0] = numbers1[0] + numbers1[1]
    del numbers1[1]
    numbers2[0] = numbers2[0] * numbers2[1]
    del numbers2[1]

    return correct(answer, numbers1) or correct(answer, numbers2)

with open('adventOfCode/2024/input.txt', encoding="UTF-8", mode= "r") as file:  
    lignes = file.read().splitlines()

resultat = 0

for l, ligne in enumerate(lignes):
    answer, numbers = ligne.strip().split(":")
    answer = int(answer)
    numbers = list(map(int, numbers.split()))
    if correct(answer, numbers):
        resultat+=answer



print(resultat)