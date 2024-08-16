import matplotlib.pyplot as plt
import numpy as np

# Linear Plot
def draw_linear_plot():
    # Generate sample data
    x = np.linspace(0, 10, 100)  # 100 points between 0 and 10
    y = 2 * x + 1  # Linear function: y = 2x + 1

    # Create linear plot
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label='y = 2x + 1', color='blue', linestyle='-', linewidth=2)

    # Add labels and title
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Linear Plot')

    # Add legend
    plt.legend()

    # Display plot
    plt.show()

# Main function to call the linear plot function
if __name__ == "__main__":
    draw_linear_plot()
