import plotly.graph_objects as go
import pandas as pd

# Sample data (time series)
dates = pd.date_range('2023-01-01', periods=100)
values = pd.Series(range(100))

# Create a Plotly figure
fig = go.Figure()

# Add a time series trace
fig.add_trace(go.Scatter(x=dates, y=values, mode='lines', name='Time Series'))

# Update layout
fig.update_layout(title='Time Series Plot',
                  xaxis_title='Date',
                  yaxis_title='Value',
                  template='plotly_white')  # Use a light theme

# Show plot
fig.show()
