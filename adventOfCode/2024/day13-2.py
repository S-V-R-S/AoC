
import time
import re
import sympy

start_time = time.time()


with open('adventOfCode/2024/input13.txt', encoding="UTF-8", mode= "r") as file:  
    lignes = file.read().splitlines()

games = []
game = {}
for ligne in lignes:
    if ligne[:9] == "Button A:":
        x,y = list(map(int,re.findall(r"\d+", ligne)))
        game["A"] = [x,y]
    elif ligne[:9] == "Button B:":
        x,y = list(map(int,re.findall(r"\d+", ligne)))
        game["B"] = [x,y]
    elif ligne[:9] == "Prize: X=":
        x,y = list(map(int,re.findall(r"\d+", ligne)))
        game["P"] = [x,y]
    
    else:
        games.append(game)
        game = {}
games.append(game)
total_tokens = 0


for game in games:
    a, b = sympy.symbols("a, b")
    equations = []

    equations.append(a*game["A"][0] + b*game["B"][0] - (game["P"][0]+10000000000000))
    equations.append(a*game["A"][1] + b*game["B"][1] - (game["P"][1]+10000000000000))
    reponse = sympy.solve(equations)


    tokens = []

    a = reponse[a]
    b = reponse[b]
    if(a.is_integer and b.is_integer):
        tokens.append(a*3 + b*1)

    if len(tokens) > 0:
        total_tokens += min(tokens)

end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Le programme a dure {elapsed_time_ms:.2f} ms est la reponse est", total_tokens)
# 92572057880885