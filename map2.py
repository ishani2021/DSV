# code for creating choropleth map of USA states
# import plotly library
import plotly

# import plotly.express module
# this module is used to create entire figures at once
import plotly.express as px

# create figure
fig = px.choropleth(locationmode="USA-states", scope="usa")
#fig = px.choropleth( scope="asia")

fig.show()



