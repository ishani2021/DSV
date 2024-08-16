import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Generate sample data
np.random.seed(0)
data = pd.DataFrame(np.random.randn(100, 5), columns=['A', 'B', 'C', 'D', 'E'])

# Compute pairwise correlation matrix
correlation_matrix = data.corr()

# Plot correlogram
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlogram (Pairwise Correlation Matrix)')
plt.show()
