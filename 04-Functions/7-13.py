def f(n1, n2, operator):
    if operator == '+':
        return n1+n2
    elif operator == '%':
        return n1%n2
    elif operator == '-':
        return n1-n2
    elif operator == '**':
        return n1**n2
    elif operator == '*':
        return n1*n2
    else:
        return "Wrong operator"

n1, n2 = map(int, input('Enter numbers: ').split())
operator = input('Enter operator: ')
print(f(n1,n2,operator))