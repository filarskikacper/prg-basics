import matplotlib.pyplot as plt
import math

x = [n for n in range(0,5)]
y = [math.sin(n) for n in x]

plt.plot(x,y)
plt.show()