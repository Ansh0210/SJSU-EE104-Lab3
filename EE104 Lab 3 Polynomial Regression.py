# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 16:42:36 2023

@author: Nathan Lee
"""

import numpy as np
import scipy.optimize as opt
import scipy.stats as st
import math
import matplotlib.pyplot as plt

UserDefinedCurve = "x**5 + 2*x - 14" #Curve wanted

x = np.linspace(-7, 7,) #Plot Range of X Values

y = eval(UserDefinedCurve) #Get Y Values for curve 

n = 5 #Polynomial Order
temp = np.polyfit(x, y, n) #esmtimated fit of the data
yPoly = np.polyval(temp, x) #Linear regression

# Plot desired curve and the curve fit on graph
plt.figure(figsize=(12,10))
plt.plot(x, y, label="Original curve")
plt.plot(x, yPoly, label="Curve fit")
plt.title("Original curve and curve fit plots")
plt.legend()
plt.show()

# Plot Both Graphs on separate Plots
plt.figure(figsize=(12,10))
plt.plot(x, y, label="Original curve")
plt.title("Original curve")
plt.legend()
plt.show()

plt.figure(figsize=(10,8))
plt.plot(x, yPoly, label="Curve fit")
plt.title("Curve fit")
plt.legend()
plt.show()
