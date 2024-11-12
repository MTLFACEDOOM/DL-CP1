import random
name = list(input("Input a word: "))
name_len = len(name)
def change_a(name):
    if 'a' in name:
        name[random.randint(0, name_len)] = "d"
def change_b(name):
    if 'b' in name:
        name[random.randint(0, name_len)] = "e"
def change_c(name):
    if 'c' in name:
        name[random.randint(0, name_len)] = "f"
def change_d(name):
    if 'd' in name:
        name[random.randint(0, name_len)] = "g"
def change_e(name):
    if 'e' in name:
        name[random.randint(0, name_len)] = "d"
def change_f(name):
    if 'f' in name:
        name[random.randint(0, name_len)] = "e"
def change_g(name):
    if 'g' in name:
        name[random.randint(0, name_len)] = "f"
def change_h(name):
    if 'h' in name:
        name[random.randint(0, name_len)] = "g"
def change_i(name):
    if 'i' in name:
        name[random.randint(0, name_len)] = "d"
def change_j(name):
    if 'j' in name:
        name[random.randint(0, name_len)] = "e"
def change_k(name):
    if 'k' in name:
        name[random.randint(0, name_len)] = "f"
def change_l(name):
    if 'l' in name:
        name[random.randint(0, name_len)] = "g"
def change_m(name):
    if 'm' in name:
        name[random.randint(0, name_len)] = "d"
def change_n(name):
    if 'n' in name:
        name[random.randint(0, name_len)] = "e"
def change_o(name):
    if 'o' in name:
        name[random.randint(0, name_len)] = "f"
def change_p(name):
    if 'p' in name:
        name[random.randint(0, name_len)] = "g"
def change_q(name):
    if 'q' in name:
        name[random.randint(0, name_len)] = "d"
def change_r(name):
    if 'r' in name:
        name[random.randint(0, name_len)] = "e"
def change_s(name):
    if 'c' in name:
        name[random.randint(0, name_len)] = "f"
def change_t(name):
    if 'd' in name:
        name[random.randint(0, name_len)] = "g"
def change_u(name):
    if 'a' in name:
        name[random.randint(0, name_len)] = "d"
def change_v(name):
    if 'b' in name:
        name[random.randint(0, name_len)] = "e"
def change_w(name):
    if 'c' in name:
        name[random.randint(0, name_len)] = "f"
def change_x(name):
    if 'd' in name:
        name[random.randint(0, name_len)] = "g"
def change_y(name):
    if 'c' in name:
        name[random.randint(0, name_len)] = "f"
def change_z(name):
    if 'd' in name:
        name[random.randint(0, name_len)] = "g"

def play():
    change_a(name)
    change_b(name)
    change_c(name)
    change_d(name)
    change_e(name)
    change_f(name)
    change_g(name)
    change_h(name)
    change_i(name)
    change_j(name)
    change_k(name)
    change_l(name)
    change_m(name)
    change_n(name)
    change_o(name)
    change_p(name)
    change_q(name)
    change_r(name)
    change_s(name)
    change_t(name)
    change_u(name)
    change_v(name)
    change_w(name)
    change_x(name)
    change_y(name)
    change_z(name)
"""def change_b(name):
    if 'e' in name:
        name[random.randint(1, name_len+1)] = "r"
def change_c(name):
    if 'l' in name:
        name[random.randint(1, name_len+1)] = "g"
def change_d(name):
    if 'o' in name:
        name[random.randint(1, name_len+1)] = "p"""
play()
print(name)
print (name_len)
name = "".join(name)
print(name)