# tv.py file
# class definition
class TV:
    def __init__(self):
      self.is_on = False
      self.channel_no = 1
      self.channel_list = []
      self.volume = 0

    def turn_off(self):
      self.is_on = False

    def turn_on(self):
      self.is_on = True

    def set_channel(self, new_channel_no):
      self.channel_no = new_channel_no

    def set_channels(self, channel_list):
      self.channel_list = channel_list
    
    def show_channels(self):
      for i, channel in enumerate(self.channel_list, 1):
        print(f'{i}. {channel}')
    
    def increase_volume(self):
      if self.volume+1 <= 10:
        self.volume += 1

    def decrease_volume(self):
      if self.volume-1 >= 0:
        self.volume -= 1

    def show_status(self):
      if self.is_on: 
        print(f"TV is on, channel {self.channel_no} ({self.channel_list[self.channel_no-1]})")
        print(f"Current volume level is {self.volume}.")
      else: print("TV is off")