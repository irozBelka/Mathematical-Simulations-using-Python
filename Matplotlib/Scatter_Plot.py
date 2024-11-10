import numpy as np
import matplotlib.pyplot as plt

# Data
X_data = np.random.random(50) * 100
Y_data = np.random.random(50) * 100

# Create a scatter plot with customized features
plt.figure(figsize=(8, 6))
scatter = plt.scatter(X_data, Y_data, c=Y_data, cmap='viridis', s=100, edgecolors="black", alpha=0.7)

# Add title and labels
plt.title('Scatter Plot of X and Y Data', fontsize=16)
plt.xlabel('X Data', fontsize=12)
plt.ylabel('Y Data', fontsize=12)

# Add a color bar for the color mapping
plt.colorbar(scatter, label='Y Values')

# Add gridlines for better readability
plt.grid(True, linestyle='--', alpha=0.5)

# Adjust layout for better spacing
plt.tight_layout()

# Show the plot
plt.show()
