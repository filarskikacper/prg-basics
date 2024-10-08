###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

# Enter temperature in degrees Celsius
temp_c = float(input('Enter temperature in degrees Celsius: '))
# Calculate
temp_k = temp_c + 273.15
temp_f = temp_c * (9/5) + 32
# Print results
print(f'Temperature in degrees Kelvin: {round(temp_k, 2)}, Fahrenheit: {round(temp_f, 2)}')