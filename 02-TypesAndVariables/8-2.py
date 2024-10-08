###
# Calculation of circle area and circumference 
#

# determine radius and PI values
radius = float(input('Enter radius: '))
pi = 3.14
# calculate area 
A = pi * radius ** 2
# calculate circumference 
C = 2 * pi * radius
# print results
print(f'Area: {round(A, 2)}, Circumference: {round(C, 2)}')