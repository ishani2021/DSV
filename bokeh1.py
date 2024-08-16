from bokeh.plotting import figure, output_file, show 

x = [val for val in range(10)] 
y = [val for val in range(0, 20, 2)] 

output_file("basiclegend.html") 

p = figure() 

p.line(x, y, legend_label="My Red Line", line_color="red") 

show(p) 
