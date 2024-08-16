import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Generate sample data
np.random.seed(42)
data = np.random.randn(100)

# Create a basic Seaborn plot
sns.set(style="whitegrid")
sns.histplot(data, kde=True)

# Customize the plot
plt.title('Customized Seaborn Plot')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Change the aesthetics
sns.set_palette('pastel')  # Set the color palette
sns.despine(left=True)     # Remove the left spine

# Add a background color
plt.gcf().set_facecolor('lightgrey')

# Show the plot
plt.show()
