import plotly.graph_objects as go

# Sample data (latitude and longitude)
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
latitudes = [40.7128, 34.0522, 41.8781, 29.7604, 33.4484]
longitudes = [-74.0060, -118.2437, -87.6298, -95.3698, -112.0740]
values = [100, 200, 150, 120, 180]  # Sample values for each city (can represent any data)

# Create a Plotly figure for scatter map
fig = go.Figure(go.Scattergeo(
    lon = longitudes,
    lat = latitudes,
    text = cities,
    marker = dict(
        size = values,
        color = values,
        colorscale = 'Viridis',
        colorbar_title = 'Value Scale'
    )
))

# Update layout
fig.update_layout(
    title = 'Cities Map',
    geo_scope='usa',  # Limit map scope to USA
)

# Show plot
fig.show()
