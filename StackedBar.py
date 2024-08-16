import matplotlib.pyplot as plt
import numpy as np

# Sample data
categories = ['A', 'B', 'C', 'D']
subcategories = ['W', 'X', 'Y', 'Z']
data = np.array([[10, 20, 30, 40],
                 [20, 30, 10, 20],
                 [30, 10, 20, 10],
                 [40, 20, 10, 30]])

# Create a stacked bar plot
fig, ax = plt.subplots()

# Bottom values for stacking bars
bottom = np.zeros(len(categories))

# Plot each subcategory
for i in range(len(subcategories)):
    ax.bar(categories, data[i], label=subcategories[i], bottom=bottom)
    bottom += data[i]

# Add labels and title
ax.set_xlabel('Categories')
ax.set_ylabel('Values')
ax.set_title('Stacked Bar Plot')
ax.legend(title='Subcategories')

# Display the plot
plt.show()
