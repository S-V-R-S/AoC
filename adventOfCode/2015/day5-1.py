with open('adventOfCode/2015/input.txt', encoding="UTF-8", mode= "r") as file:  
    strings = file.readlines()
    
vowels = "aeiou"
naughty_strings = ["ab", "cd", "pq","xy"]
nice = 0

for string in strings:
    if sum(string.count(vowel) for vowel in vowels) < 3:
        continue
    if any(n_string in string for n_string in naughty_strings):
        continue
    for i in range(1,len(string)):
        if string[i] == string[i-1]:
            nice += 1
            break

print(nice)