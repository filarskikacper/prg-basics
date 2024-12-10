with open('4-11.txt', 'w') as file:
    for i in range(1,101):
        file.write(f"{i},{i*i},{i*i*i}\n")