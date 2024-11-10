import numpy as np
import matplotlib.pyplot as plt

# Data
years = [2006 + x for x in range(16)]
weights = 82 + np.random.random(16) * 10

# Plot the data
plt.plot(years, weights, marker='o', color='b', linestyle='-', linewidth=2)

# Add title and labels
plt.title('Weight Over Years')
plt.xlabel('Year')
plt.ylabel('Weight (kg)')

# Annotate some points directly (for example, first and last points)
plt.annotate(f'{weights[0]:.2f} kg', xy=(years[0], weights[0]), xytext=(years[0] + 1, weights[0] + 1),
             arrowprops=dict(facecolor='green', arrowstyle="->"))
plt.annotate(f'{weights[-1]:.2f} kg', xy=(years[-1], weights[-1]), xytext=(years[-1] - 1, weights[-1] - 1),
             arrowprops=dict(facecolor='red', arrowstyle="->"))

# Show the plot
plt.tight_layout()
plt.show()
