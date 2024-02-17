
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt
import math
import random

# Generating random number
random.seed(1500)

# Defining the damped sine wave function
def function(xin, a, b, c, gain):
    return [gain * math.sin(a * x + b) * math.exp(-c * x) for x in xin]

# Generating x values
xv = np.arange(0, 150, 0.1)

# Generating y values
yv = function(xv, 4, 1, 0.1, 1)

# Adding gaussian noise to y values
yn = [y + random.gauss(0, 0.1) for y in yv]

# Fitting the curve
popt, pcov = opt.curve_fit(function, xv, yn)

# Difference between fitted and exact y values
diff = [abs(yf - yv) for yf, yv in zip(function(xv, *popt), yv)]

# Plot showing the error in the curve fit y values compared to the normal y values
plt.plot(xv, diff)
plt.show()

# Plot comparing damped sine wave with curve fit 
plt.plot(xv, yn, 'orange', label = 'Actual Data')
plt.plot(xv, function(xv, *popt), 'green', label = 'Fitted Data')
plt.legend()
plt.show()

# Plot comparing damped sine wave with curve fit using hints
plt.plot(xv, yv, 'orange', label = 'Actual Data')
plt.scatter(xv, function(xv, *popt), alpha=0.3, s=3, c='green', label = 'Fitted Data')
plt.legend()
plt.show()
