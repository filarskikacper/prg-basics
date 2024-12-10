hotels_in_Krakow = [
   {"name":"Sky","price":320.00},
   {"name":"Metropol","price":480.00},
   {"name":"New Port","price":420.00},
   {"name":"Aparthotel","price":390.00}
]

hotels_in_Sopot = [
   {"name":"Focus","price":510.00},
   {"name":"Aqua","price":345.00},
   {"name":"La Boutique","price":390.00},
   {"name":"Marina","price":410.00}
]

def hotels(dict):
    for hotel in dict:
       print(dict["name"], end=',')

avg_Krakow = 0
for hotel, price in hotels_in_Krakow:
    avg_Krakow += price
avg_Krakow /= len(hotels_in_Krakow)

avg_Sopot = 0
for hotel in hotels_in_Sopot:
    avg_Sopot += hotels_in_Sopot[hotel]
avg_Sopot /= len(hotels_in_Sopot)

hotels(hotels_in_Krakow)