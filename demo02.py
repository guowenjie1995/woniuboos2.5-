import random
str = ""
for i in range(6):
    ch = chr(random.randrange(ord('0'), ord('9') + 1))
    str += ch

print(str)