import csv

fields = []
rows = []

with open('it_company.csv', 'r') as file:
    csvreader = csv.reader(file)
    fields = next(csvreader)

    for row in csvreader:
        rows.append(row)

    for info in rows:
        if info[2] == 'Graphic Designer':
            print(f"{info[0]} {info[1]}, {info[3]}")