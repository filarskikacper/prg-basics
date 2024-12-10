import csv

filename = 'clothing.csv'
fields = []
rows = []

with open(filename, 'r') as file:
    csvread = csv.reader(file)
    fields = next(csvread)

    for row in csvread:
        rows.append(row)

    for info in rows:
        if float(info[5]) < 60 and int(info[6]) < 40:
            print(info)