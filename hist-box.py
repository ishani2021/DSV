import matplotlib.pyplot as plt
import numpy as np

# Histogram Plot
def draw_histogram():
    # Generate sample data
    data = np.random.randn(1000)

    # Create histogram plot
    plt.figure(figsize=(8, 6))
    plt.hist(data, bins=30, alpha=0.7, color='blue', edgecolor='black')

    # Add labels and title
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Histogram Plot')

    # Display plot
    plt.show()

# Box Plot
def draw_box_plot():
    # Generate sample data
    np.random.seed(10)
    data = np.random.normal(100, 20, 200)

    fig = plt.figure(figsize =(10, 7))

    # Creating plot
    plt.boxplot(data)

    # show plot
    plt.show()

# Main function to call the plot functions
if __name__ == "__main__":
    draw_histogram()
    draw_box_plot()
