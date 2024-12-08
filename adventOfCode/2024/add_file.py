default_content = """
import time
start_time = time.time()




end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Le programme a dure {elapsed_time_ms:.2f} ms est la reponse est")
"""

for day in range(1,26):
    base_name = f"adventOfCode/2024/day{day}"
    for part in range(1,3):
        file_name = base_name + f"-{part}.py"
        with open(file_name, "w") as file:
            file.write(default_content)


for day in range(1,26):
    base_name = f"adventOfCode/2024/input{day}.txt"
    with open(base_name, "w") as file:
            file.write("")