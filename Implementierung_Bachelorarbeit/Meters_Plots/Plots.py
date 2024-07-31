import matplotlib.pyplot as plt 
import numpy as np

def create_activityplot(activity_list: list, title: str, color_plot: str):

    plt.figure(figsize=(6, 6))

    # X-axis: Time in discrete time steps (seconds / delta_t)
    x = range(len(activity_list))

    # Y-axis: Activity values
    y = activity_list

    # Create the Bar plot
    plt.bar(x, y, color = color_plot)

    for spine in plt.gca().spines.values():
        spine.set_visible(False)

    # Making only the left and bottom axes visible
    plt.gca().spines['left'].set_visible(True)
    plt.gca().spines['bottom'].set_visible(True)


    # Set X-axis
    plt.xlabel('Time (seconds / )', fontsize=16)

    # Set Y-axis and set the maximum
    plt.ylabel('Activity', fontsize=16)
    plt.ylim(0, max(activity_list) * 1.1)  # Increase the maximum of the Y-axis by 10%

    # Add title
    plt.title(title, color = color_plot, fontsize=20)

    # Show the plot
    plt.show()



def plot_log_histogram(data, title):
    """
    Plots a histogram with logarithmically distributed bins from 10^0 to 10^6 and normalizes the counts to probabilities.
    
    Parameters:
    data (array-like): The data to plot (event sizes).
    """
    # Define logarithmic bins from 10^0 to 10^6
    bin_edges = np.logspace(0, 6, num=50)
    
    # Compute the histogram
    counts, bin_edges = np.histogram(data, bins=bin_edges)
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
    
    # Calculate the probabilities
    bin_widths = bin_edges[1:] - bin_edges[:-1]
    probabilities = counts / counts.sum()
    
    # Filter non-zero bins
    non_zero = counts > 0
    bin_centers = bin_centers[non_zero]
    probabilities = probabilities[non_zero]
    
    # Plot the histogram on a log-log scale
    plt.figure(figsize=(6, 6))
    plt.scatter(bin_centers, probabilities, color='blue', label='Data')
    
    # Set log-log scale
    plt.xscale('log')
    plt.yscale('log')
    
    # Add reference line for s^-2/3
    ref_x = np.logspace(0, 6, num=100)
    ref_y = ref_x ** (-2/3)
    plt.plot(ref_x, ref_y, 'r--', label=r'Reference line $s^{-2/3}$')
    
    for spine in plt.gca().spines.values():
        spine.set_visible(False)

    # Making only the left and bottom axes visible
    plt.gca().spines['left'].set_visible(True)
    plt.gca().spines['bottom'].set_visible(True)

    # Labels and title
    plt.xlabel('Avalanche Size')
    plt.ylabel('Probability')
    plt.title(title)
    plt.legend()
    plt.show()