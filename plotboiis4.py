import matplotlib.pyplot as plt

x_values = [1,2,3,4,5]
y_values = [1, 4, 9, 16, 25]
plt.xlabel("Value", fontsize=14)
plt.ylabel("square of value", fontsize=14)

plt.scatter(x_values, y_values, s=100)
plt.show()