import matplotlib.pyplot as plt

# Pie Chart
def draw_pie_chart():
    # Define data
    labels = ['Category A', 'Category B', 'Category C', 'Category D']
    sizes = [15, 30, 45, 10]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
    explode = (0.1, 0, 0, 0)  # explode first slice (i.e. 'Category A')

    # Create pie chart
    plt.figure(figsize=(8, 6))
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, 
            autopct='%1.1f%%', shadow=True, startangle=140)

    # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.axis('equal')

    # Add title
    plt.title('Pie Chart Example')

    # Display plot
    plt.show()

# Main function to call the pie chart function
if __name__ == "__main__":
    draw_pie_chart()
