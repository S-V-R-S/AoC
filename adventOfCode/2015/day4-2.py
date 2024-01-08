import hashlib

puzzle = "bgvyzdsv"
i = 0
while True:
    test = puzzle + str(i)
    if hashlib.md5(test.encode('utf-8')).hexdigest().startswith("000000"):
        print(i)
        break
    i += 1

