import matplotlib.pyplot as plt
import numpy as np
np.set_printoptions(edgeitems=10)
np.set_printoptions(linewidth=200)

# write a function.
# put them in arrays.
# show the graph using plt.
cards = 50
duration = 120


power_values = [0]
power_values.extend(2.5**n for n in range(0, 7))
print(power_values)
# how to round up all the values in a list?
for i in range(len(power_values)):
    power_values[i] = int(round(power_values[i], 0))
print(power_values)
print()

array = np.zeros((duration, duration))
for i in range(duration):
    for j in range(duration - i):
        if j in power_values:
            array[i][j + i] = cards
        else:
            pass
    if i % (duration / 10) == 0:
        print(f"{(i / duration) * 100:.2f}% done")

print(array)
print()
workload = np.sum(array, axis=0)
print(workload)
print()
print(f"Maximum workload on any given day, during {duration} days: {max(workload)} cards a day.")

print(len(workload))

y = workload
x = np.arange(0, duration, 1)
plt.plot(x, y)
plt.show()

