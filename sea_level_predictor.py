import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    data = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'])


    # Create first line of best fit

    slope, intercept, _, _, _ = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
    years_extended = range(1880, 2051)
    plt.plot(years_extended, [slope * year + intercept for year in years_extended], label='Fit line (1880-2050)')
    
    # Create second line of best fit
    data_from_2000 = data[data['Year'] >= 2000]
    slope_2000, intercept_2000, _, _, _ = linregress(data_from_2000['Year'], data_from_2000['CSIRO Adjusted Sea Level'])
    years_extended_2000 = range(2000, 2051) 
    plt.plot(years_extended_2000, [slope_2000 * year + intercept_2000 for year in years_extended_2000], label='Fit line (2000-2050)', linestyle='--')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()