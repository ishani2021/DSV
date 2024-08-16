from bokeh.plotting import figure, output_file, show 

p = figure() 

x = [x for x in range(1, 11)] 
colors = ['red', 'green', 'blue', 'yellow'] 
for i in range(2, 6): 
	p.line(x, [val*i for val in x], line_width=2, color=colors[i-2], 
		alpha=0.8, legend_label='Multiples of {}'.format(i)) 

p.legend.location = "top_left"
p.legend.click_policy = "hide"
output_file("interactive_legend.html") 

show(p) 
