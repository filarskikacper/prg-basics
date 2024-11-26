basic_data = {
   "name":"Barbara",
   "age":21
}

advanced_data = {
   "status":"student",
   "married":False,
   "interest":["reading","swimming"]
}

person = basic_data
for key in advanced_data:
    person[key] = advanced_data[key]
print(person)