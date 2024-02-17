# Import necessary libraries
import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt

# Generate the x and y data
x = np.linspace(-3, 3, 50)  # Generate 50 samples between -3 and 3
y = 4 * x ** 5 + 20 * x ** 2 + 12 * x

# Create a pipeline object
# This pipeline will first transform the data using a polynomial feature transformer, which adds features for the squared x terms, up to the 4th degree. The transformed data is then passed to a linear regression model for fitting.
pipeline = make_pipeline(PolynomialFeatures(degree=4), LinearRegression())

# Fit the model to the data
# This will train the linear regression model to predict the y values for the given x values.
pipeline.fit(x.reshape(-1, 1), y)

# Make predictions
# This will use the trained model to predict the y values for the given x values.
y_pred = pipeline.predict(x.reshape(-1, 1))

# Plot the results
# This will plot the actual data points (in blue) and the fitted curve (in red).
plt.plot(x, y, 'o', label='Actual data')
plt.plot(x, y_pred, '-', label='Fitted curve')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

