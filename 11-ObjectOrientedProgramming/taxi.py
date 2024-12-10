class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km
    
    def print_receipt(self):
        print(f'The distance was {self.distance} and rate {self.rate_per_km}, the fare is {self.fare}')


def main():
    # your progra
    rate = TaxiRide(int(input('Enter rate per km: ')))
    rate.calculate_fare(int(input('Enter distance: ')))
    rate.print_receipt()

    

if __name__ == "__main__":
    main()