from bokeh.plotting import figure, output_file, show 
from bokeh.models import ColumnDataSource 

p = figure(x_range=(0.5, 2.5), y_range=(0.5, 2.5)) 

source = ColumnDataSource(dict( 
	x=[1, 1, 2, 2, 1.5], 
	y=[1, 2, 1, 2, 1.5], 
	color=['red', 'red', 'red', 'red', 'blue'], 
	label=['corner', 'corner', 'corner', 'corner', 'center'] 
)) 
p.circle(x='x', y='y', radius=0.05, color='color', legend_group='label', source=source) 

output_file("AutomaticGrouping.html") 

show(p) 
