# Import necessary libaries
import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt

# Define the function that we want to fit
def eq(xin, a, b, c, d):
    return [(a / (b+x)) * np.sin(2* np.pi * x/c) + d for x in xin]

# Generate the x and y data
x = [x/40 for x in range(400)]
y = eq(x, 1, 1, 2, 1)

# Fit the curve to the data
popt, pcov = opt.curve_fit(eq, x, y)

# Plot the results
plt.plot(x, y, 'o', label = 'Actual Data')
plt.plot(x, eq(x, *popt), '-', label = 'Fitted Data')

# Label the axes and add a legend
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Show the plot
plt.show()

