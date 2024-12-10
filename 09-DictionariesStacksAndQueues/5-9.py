import csv

with open('vehicle.txt', 'r') as file1:
    vehicles = file1.read()
    vehicle = vehicles.splitlines()
    with open('province.csv', 'r', encoding='utf-8') as file2:
        csvdict = csv.DictReader(file2)
        provinces = [row for row in csvdict]
        matches = []
        i = 0
        for province in provinces:
            count = 0
            for car in vehicle:
                if car[0] == province['Letter']:
                    count += 1
            matches.append({"Province": province['Name'], "Count": count})

print(matches)