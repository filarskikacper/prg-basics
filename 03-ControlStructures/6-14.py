facebook = input('Do you have Facebook (y/n)?: ')
if facebook == 'y':
    facebook = bool(True)
twitter = input('Do you have Twitter (y/n)?: ')
if twitter == 'y':
    twitter = bool(True)
instagram = input('Do you have Instagram (y/n)?: ')
if instagram == 'y':
    instagram = bool(True)

if facebook == True and instagram == True:
    print("You are a good influencer!")
elif facebook == True and twitter == True:
    print("You are a good influencer!")
elif twitter == True and instagram == True:
    print("You are a good influencer!")
elif twitter == True and instagram == True and facebook == True:
    print("You are a good influencer!")
