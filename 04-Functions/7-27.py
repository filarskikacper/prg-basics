def f(dice):
    digits = [0] * 7
    result = 0
    for char in dice:
        digits[int(char)] += 1
    for i in range (1, 6):
        if digits[i] > digits[i+1]:
            result = i
    return result
print(f("5233165554211"))