def read_from_file(name):
   with open(name) as file:
      content = file.read()
   return content

pets = (read_from_file('pets.txt')).splitlines()
total_words = 0
for line in pets:
   total_words += len(line.split())

print(total_words)