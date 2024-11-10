import numpy as np
import matplotlib.pyplot as plt

# Random data
X_data = np.random.random(50) * 100
Y_data = np.random.random(50) * 100

# Years and weights data
years = [2006 + x for x in range(16)]
weights = 82 + np.random.random(16) * 10

# Ages data
ages = np.random.normal(20, 1.5, 1000)

# Poll data
PL = ["C++", "C#", "Java", "Python", "Go"]
Poll = [20, 10, 100, 140, 1]

# Create figure
plt.figure(figsize=(12, 6))

# Scatter Plot
plt.subplot(2, 2, 1)
plt.scatter(X_data, Y_data, color='b', edgecolors='k')
plt.title("Scatter Plot of X vs Y")
plt.xlabel("X Data")
plt.ylabel("Y Data")
plt.grid(True)

# Line Plot
plt.subplot(2, 2, 2)
plt.plot(years, weights, marker='o', color='r', label="Weight over Time")
plt.title("Weight vs Years")
plt.xlabel("Years")
plt.ylabel("Weight (kg)")
plt.grid(True)
plt.legend()

# Histogram
plt.subplot(2, 2, 3)
plt.hist(ages, bins=30, color='g', edgecolor='black')
plt.title("Histogram of Ages")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.grid(True)

# Bar Plot
plt.subplot(2, 2, 4)
plt.bar(PL, Poll, color='purple')
plt.title("Poll Results for Programming Languages")
plt.xlabel("Programming Language")
plt.ylabel("Votes")
plt.grid(True)

# Adjust layout
plt.tight_layout()

# Show the plots
plt.show()
