import time
def time_string(hour, minute, type):
    if type == '24':
        return (hour,':',minute)
    elif type == '12':
        t = str(hour) + ':' + str(minute)
        t =time.strptime(t, "%H:%M")
        return time.strftime("%I:%M%p", t)
    
hour = int(input('Enter hour: '))
minute = int(input('Enter minute: '))
format = input('Enter format: ')
print(time_string(hour, minute, format))