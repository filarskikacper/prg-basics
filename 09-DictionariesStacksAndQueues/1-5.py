countries = [
{"name":"Poland", "population":38000000},
{"name":"Germany", "population":84000000},
{"name":"USA", "population":100000000},
{"name":"Spain", "population":72500000},
{"name":"Italy", "population":45000000}
]

print("COUNTRY POPULATION")
for dict in countries:
    print(f"{dict["name"]} {dict["population"]}")
