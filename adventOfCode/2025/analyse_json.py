from datetime import datetime
import json

# class dict_sans_err(dict):
#     def __getitem__(self, key):
#         if key in self:
#             return super().__getitem__(key)
#         else:
#             return None
6
# https://adventofcode.com/2025/leaderboard/private/view/3280485.json

with open('adventOfCode/2025/aoc.json', 'r') as file:
    data = json.load(file)['members']


jour = input("Quel jour ? ")
etoile = input("Quel étoile (1 ou 2 ou 3 pour la diff entre 1 et 2) ? ")
liste = []
for x in data.keys():
    date = data[x]['completion_day_level']
    if jour in date and min(etoile, "2") in date[jour]:
        t1 = datetime.fromtimestamp(date[jour]['1']['get_star_ts']) if '1' in date[jour] else ""
        t2 = datetime.fromtimestamp(date[jour]['2']['get_star_ts']) if '2' in date[jour] else ""
        t3 = t2-t1 if t2 != "" else ""
        liste.append((data[x]['name'], t1, t2, t3))

liste.sort(key=lambda x: x[int(etoile)])

print("-"*(30+19+19+14))
print(f"{"Name":<30}|{" Etoile 1":<19}|{" Etoile 2":<19}| Différence")
print("-"*(30+19+19+14))
for l in liste:
    print(f"{l[0]:<30}|{str(l[1]):<19}|{str(l[2]):<19}| {str(l[3])}")