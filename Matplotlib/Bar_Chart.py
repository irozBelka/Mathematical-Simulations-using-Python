import numpy as np
import matplotlib.pyplot as plt

# Data
PL = ["C++", "C#", "Java", "Python", "Go"]
Poll = [20, 10, 100, 140, 1]

# Bar plot
plt.bar(PL, Poll, color="lightcoral", align="center", edgecolor="darkblue", lw=2, width=0.6)

# Add a title and labels
plt.title("Poll Results for Programming Languages", fontsize=16, fontweight='bold')
plt.xlabel("Programming Languages", fontsize=14)
plt.ylabel("Votes", fontsize=14)

# Add data labels on top of the bars
for i, v in enumerate(Poll):
    plt.text(i, v + 5, str(v), ha='center', va='bottom', fontsize=12, fontweight='bold')

# Add grid for better readability
plt.grid(True, linestyle='--', alpha=0.7)

# Improve layout and display
plt.tight_layout()

plt.show()
