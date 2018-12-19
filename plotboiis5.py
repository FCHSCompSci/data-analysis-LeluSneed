import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
plt.xlabel("Value", fontsize=14)
plt.ylabel("square of value", fontsize=14)

plt.scatter(x_values, y_values, s=40)

plt.axis([0, 1100, 0, 1100000])

plt.show()