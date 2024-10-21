age = int(input("Enter your age: "))
if age >= 65:
    print("You are senior")
elif age >= 20:
    print("You are adult")
elif age >= 13:
    print("You are teen")
elif age >= 0:
    print("You are child")
else:
    print("Wrong age")