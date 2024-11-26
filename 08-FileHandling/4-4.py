with open('it_company.csv', 'r') as file:
    for i, line in enumerate(file):
        if i == 5:
            key = input("Press Enter key... ")
            if key == "":
                continue
            else: 
                break        
        print(line, end="")
        i += 1