import numpy as np
import matplotlib.pyplot as plt

# Generate random data
ages = np.random.normal(20, 1.5, 1000)

# Create figure
plt.figure(figsize=(12, 6))

# Plot 1 - Default histogram
plt.subplot(1, 2, 1)
plt.hist(ages, bins=30, color="skyblue", edgecolor="black", alpha=0.7)
plt.title("Distribution of Ages (Default)", fontsize=14)
plt.xlabel("Age", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.6)

# Plot 2 - Customized histogram with red color
plt.subplot(1, 2, 2)
plt.hist(ages, bins=30, color="red", edgecolor="black", alpha=0.7)
plt.title("Distribution of Ages (Red)", fontsize=14)
plt.xlabel("Age", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.6)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()
