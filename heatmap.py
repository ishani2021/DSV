import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Generate sample data
np.random.seed(0)
data = np.random.rand(10, 12)

# Plot heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(data, annot=True, cmap='YlGnBu', cbar=True)
plt.title('Heatmap')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
