class Phone():
        def __init__(self, model, price, color):
            self.model = model
            self.price = price
            self.color = color
            self.sounds = True
            self.screen = False
            self.vibrations = True

        def turn_on(self):
              self.screen = True
        
        def turn_off(self):
              self.screen = False
        
        def sound_on(self):
              self.sounds = True

        def sound_off(self):
              self.sounds = False

        def vibrations_on(self):
              self.vibrations = True
        
        def vibrations_off(self):
              self.vibrations = False

        def properties(self):
            print(f"The model is {self.model}, price: {self.price}PLN, the color is {self.color}.")
            if self.sounds:
                    print(f"Sounds are turned on.")
            else: print(f"Sounds are turned off.")
            if self.screen:
                    print(f"Screen is turned on.")
            else: print(f"Screen is turned off.")
            if self.vibrations:
                    print(f"Vibrations are turned on.")
            else: print(f"Vibrations are turned off.")

def main():
      phone = Phone("IPhone 12", 2999, "Black")
      phone.turn_on()
      phone.vibrations_off()
      phone.sound_off()
      phone.properties()

if __name__ == "__main__":
      main()