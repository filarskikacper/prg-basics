def f(detector):
    people = 0
    for char in detector:
        if char == '+':
            people += 1
            print(people)
        elif char == '-':
            people -= 1
            print(people)
        if people >= 3:
            return True
    return False

detector = input('Enter anything: ')
print(f(detector))