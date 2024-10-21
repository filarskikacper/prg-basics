import time
time_24h = input('Enter time (24-hour format): ')
t = time.strptime(time_24h, "%H:%M")
time_12h = time.strftime("%I:%M%p", t)
print(f'Time in 12-hour format: {time_12h}')