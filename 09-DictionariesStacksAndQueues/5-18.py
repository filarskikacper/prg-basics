import json

with open('dogs.json', 'r', encoding='utf-8') as file:
    dogs = json.load(file)
    
for dog in dogs:
    for key, value in dog.items():
        if key == "age":
             if value < 5:
                print(dog)
