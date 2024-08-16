import matplotlib.pyplot as plt
import numpy as np

# Linear Plot with Line Formatting
def draw_linear_plot_with_formatting():
    # Generate sample data
    x = np.linspace(0, 10, 100)  # 100 points between 0 and 10
    y1 = 2 * x + 1  # Linear function 1: y = 2x + 1
    y2 = -3 * x + 10  # Linear function 2: y = -3x + 10

    # Create linear plot
    plt.figure(figsize=(10, 6))
    
    # Plot first line with formatting
    plt.plot(x, y1, label='y = 2x + 1', color='blue', linestyle='--', linewidth=2, marker='o')
    
    # Plot second line with different formatting
    plt.plot(x, y2, label='y = -3x + 10', color='red', linestyle='-', linewidth=2, marker='x')

    # Add labels and title
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Linear Plot with Line Formatting')

    # Add legend
    plt.legend()

    # Display grid
    plt.grid(True)

    # Display plot
    plt.show()

# Main function to call the linear plot function
if __name__ == "__main__":
    draw_linear_plot_with_formatting()
