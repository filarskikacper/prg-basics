hours = int(input('Enter hours of parking: '))
if hours > 6:
    print("You have to pay 20 PLN")
elif hours >= 3:
    print("You have to pay 15 PLN")
elif hours >=1:
    print("You have to pay 5 PLN")
else:
    print("Wrong number of hours")