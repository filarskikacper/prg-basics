import matplotlib.pyplot as plt

x = []
y = []

# create x values
for n in range(-100,101):
   x += [n]

# create y values
for n in x:
   y += [n**2 - 3]

# print chart
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()