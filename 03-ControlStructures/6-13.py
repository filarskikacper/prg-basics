car_speed = int(input('Enter car speed: '))
speed_limit_min = 40
speed_limit_max = 140
if car_speed >= 0 and (car_speed < speed_limit_min or car_speed > speed_limit_max):
    print("Warning: Invalid car speed!!")
elif car_speed < 0:
    print("Car speed cannot be lower than 0")