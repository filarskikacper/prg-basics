def f(exp):
    result = int(exp[0])
    for i, char in enumerate(exp):
        if char == '+':
            result += int(exp[i+1])
        elif char == '-':
            result -= int(exp[i+1])
    return result

print(f("2+3"))