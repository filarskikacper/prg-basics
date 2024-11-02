def f(name):
    out = name[0]
    flag = 0
    for char in name:
        if flag == 1: 
            out += char
            flag = 0
        if char == ' ':
            flag = 1
    return out

print(f('For Your Information'))