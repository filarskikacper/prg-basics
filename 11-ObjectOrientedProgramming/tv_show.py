# tv_show.py file
# main program
import tv

def main():
   # object creation
    tv1 = tv.TV()

   # object usage
    tv1.set_channels(["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery"])
    tv1.show_status()
    tv1.turn_on()
    tv1.increase_volume()
    tv1.show_status()
    tv1.set_channel(3)
    tv1.decrease_volume()
    tv1.show_status()
    tv1.turn_off()


if __name__ == "__main__":
   main() 