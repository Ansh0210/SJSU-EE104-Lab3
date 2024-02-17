# Importing libraries
import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt

# Defining the function with 2 x values and 2 y values, then returning the arrays
def rf(x, y0, y1):
    x0, x1 = x
    return np.sin(x0 * y0) + np.sin(x1 * y1)

# Fitting the curve of initial data points
def hint(h0, h1):
    popt, _ = opt.curve_fit(rf, xv, yv, (h0, h1))

    plt.plot(rf((x0, x1), 2, 3), 'green', label='Initial Data')
    plt.plot(rf((x0, x1), *popt), 'red', label='Fitted Data')
    plt.legend()
    plt.show()

# Generate x and y values of the function
x0 = np.arange(0, 10, 0.1) 
x1 = np.sin(x0)
xv = (x0, x1)
yv = rf(xv, 2, 3)

# h0 and h1 value of plot
hint(1, 3)