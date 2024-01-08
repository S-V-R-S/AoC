import hashlib

puzzle = "bgvyzdsv"
# INITIALISATION A 0 
i = 0
while True:
    # ON CONSTRUIT LA CHAINE DE CARACTERE PUZZLE + NBR
    test = puzzle + str(i)
    # ON REGARDE SI CA RESPECTE LA CONDITION 
    if hashlib.md5(test.encode('utf-8')).hexdigest().startswith("00000"):
        print(i)
        break
    i += 1

