import plotly.graph_objects as go
import numpy as np

# Generate random data
np.random.seed(0)
x = np.random.randn(100)
y = np.random.randn(100)
z = np.random.randn(100)

# Create a 3D scatter plot
fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z, mode='markers',
                                   marker=dict(size=8, color=z, colorscale='Viridis', opacity=0.8))])

# Update layout
fig.update_layout(scene=dict(xaxis_title='X-axis', yaxis_title='Y-axis', zaxis_title='Z-axis'),
                  margin=dict(l=0, r=0, b=0, t=0))

# Show plot
fig.show()
