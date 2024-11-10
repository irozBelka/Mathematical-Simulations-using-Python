import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Step 1: Define the multivariable function
def f(x, y):
    return x**2 + y**2

# Step 2: Generate input ranges for x and y
x = np.linspace(-10, 10, 100)  # 100 points from -10 to 10 for x
y = np.linspace(-10, 10, 100)  # 100 points from -10 to 10 for y

# Create a meshgrid for the x and y ranges
X, Y = np.meshgrid(x, y)

# Step 3: Evaluate the function over the grid
Z = f(X, Y)

# Step 4: Visualize the function with a 3D surface plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap="viridis")

# Add labels for axes
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("f(x, y)")

# Show the plot
plt.show()
