import random
name = list(input("Input a word: "))
name_len = len(name)

def change_x(name):
    if 'h' in name:
        name[random.randint(1, name_len)] = "g"
    if 'e' in name:
        name[random.randint(1, name_len)] = "f"
    if 'l' in name:
        name[random.randint(1, name_len)] = "o"
    if 'l' in name:
        name[random.randint(1, name_len)] = "p"

change_x(name)
print(name)
name = "".join(name)
print(name)
