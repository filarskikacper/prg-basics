###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
volume = a * b * c
surface_area = a * b * 2 + a * c * 2 + b * c * 2
print(f"Volume: {volume}, surface_area: {surface_area} ")