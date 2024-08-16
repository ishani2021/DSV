import numpy as np
import matplotlib.pyplot as plt

# Data for the radar chart
labels = np.array(['A', 'B', 'C', 'D','e'])  # Labels for each variable
stats = np.array([80, 70, 90, 85,45])       # Values for each variable

# Number of variables
num_vars = len(labels)

# Compute angle for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# The plot is circular, so close the plot loop
stats = np.concatenate((stats,[stats[0]]))
angles += angles[:1]

# Plotting
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
ax.fill(angles, stats, color='blue', alpha=0.25)
ax.plot(angles, stats, color='blue', linewidth=2)  # Plot the line around the outside

# Add labels
ax.set_yticklabels([])  # Hide radial ticks
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels, fontsize=12)

# Add a title
plt.title('Radar Chart', size=20, color='blue', y=1.1)

# Show the plot
plt.show()
