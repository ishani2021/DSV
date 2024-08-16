import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Example data
np.random.seed(0)
data = pd.DataFrame({
    'Category': np.random.choice(['A', 'B', 'C'], size=100),
    'Value': np.random.randn(100)
})

# Set the style and palette using aesthetic functions
sns.set(style='whitegrid', palette='pastel')

# Example 1: Bar Plot with customized colors
plt.figure(figsize=(8, 6))
sns.barplot(x='Category', y='Value', data=data, ci=None, palette='Set2')
plt.title('Bar Plot with Customized Colors')
plt.xlabel('Category')
plt.ylabel('Value')
plt.show()

# Example 2: Scatter Plot with markers and style
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Category', y='Value', data=data, hue='Category', style='Category', s=100, palette='Set2')
plt.title('Scatter Plot with Markers and Style')
plt.xlabel('Category')
plt.ylabel('Value')
plt.legend(title='Category', loc='upper right')
plt.show()

# Example 3: Box Plot with horizontal orientation and quartile annotations
plt.figure(figsize=(8, 6))
sns.boxplot(x='Category', y='Value', data=data, palette='Set2')
sns.swarmplot(x='Category', y='Value', data=data, color='0.25')
plt.title('Box Plot with Swarm Plot Overlay')
plt.xlabel('Category')
plt.ylabel('Value')
plt.show()
