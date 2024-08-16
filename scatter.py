import matplotlib.pyplot as plt
import numpy as np

# Scatter Plot
def draw_scatter_plot():
    x =[5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6] 
 
    y =[99, 86, 87, 88, 100, 86, 103, 87, 94, 78, 77, 85, 86]
 
    plt.scatter(x, y, c ="blue")
 
    # To show the plot
    plt.show()

# Bubble Plot
def draw_bubble_plot():
    # Generate sample data
    x_values = [1, 2, 3, 4, 5]
    y_values = [2, 3, 5, 7, 11]
    bubble_sizes = [30, 80, 150, 200, 300]

    # Create a bubble chart with customization
    plt.scatter(x_values, y_values, s=bubble_sizes, alpha=0.6, edgecolors='b', linewidths=2)

    # Add title and axis labels
    plt.title("Bubble Chart with Transparency")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")

    # Display the plot
    plt.show()

# Main function to call the plot functions
if __name__ == "__main__":
    draw_scatter_plot()
    draw_bubble_plot()
