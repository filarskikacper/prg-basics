import csv

def writetofile(row):
    genre = row[2]
    filename = f'books_{genre}.txt'
    with open(filename, 'a') as file:
        file.write(f"{row}\n") 

def openfile(filename):
    with open(filename, 'r') as file:
        fields = []
        rows = []
        csvread = csv.reader(file)
        fields = next(csvread)
        for row in csvread:
            rows.append(row)
    return rows
    

filename = 'books.csv'
rows = openfile(filename)
for row in rows:
    writetofile(row)